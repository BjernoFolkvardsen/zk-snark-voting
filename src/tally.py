from src.bulletinboard import BullitinBoard
from src.utility import Utility, ElGamal
from zkpy.circuit import Circuit, GROTH
import random
import json
import os

class Tally:
    bb: BullitinBoard = None

    def __init__(self, bb: BullitinBoard):
        self.bb = bb

    def tally(self):
        cr_ids = self.bb.get_cr_ids()
        random.shuffle(cr_ids)
        for cr_id in cr_ids:
            self.add_vote_same_pseudonym(cr_id)

        final_ballots = self.check_valid_ballot()
        self.calculate_results(final_ballots)

    def verify_ballot_votes(self, ballot):
        for candidate_id in ballot:
            working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../tmp/"
            circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir)
            with open("tmp/public.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["public"], file)
            with open("tmp/proof.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["proof"], file)

            if False == circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json"):
                return False
        return True

    def add_vote_same_pseudonym(self, cr_id):
        ballots = self.bb.get_ballot_by_cr_id(cr_id)
        elgamal = self.bb.get_public_params("elgamal")
        elgamal_priv_key = self.bb.get_private_param("elgamal_priv_key")
        elGamal = Utility.constructElGamal((int(elgamal["prime"]), int(elgamal["group"]), int(elgamal["public_key"]), int(elgamal_priv_key)))
        x = 0
        final_ballot = {}
        for i in range(len(ballots)):
            if x == i:
                if self.verify_ballot_votes(ballots[i]["data"]) :
                    for j in range(len(ballots[i]["data"])):
                        final_ballot[j.__str__()] = ballots[i]["data"][j.__str__()]["vote"]
                else:
                    x = x+1
            else :
                if self.verify_ballot_votes(ballots[i]["data"]):
                    for j in range(len(final_ballot)):
                        c1,c2 = elGamal.homomorphic_addition((int(final_ballot[j.__str__()][0]),int(final_ballot[j.__str__()][1])), (int(ballots[i]["data"][j.__str__()]["vote"][0]), int(ballots[i]["data"][j.__str__()]["vote"][1])))
                        final_ballot[j.__str__()] = (str(c1), str(c2))

        self.bb.set_final_ballots(final_ballot)

        return (final_ballot)

    def check_valid_ballot(self):
        final_ballots = self.bb.get_final_ballots()
        elgamal = self.bb.get_public_params("elgamal")
        elgamal_priv_key = self.bb.get_private_param("elgamal_priv_key")
        elGamal = Utility.constructElGamal((int(elgamal["prime"]), int(elgamal["group"]), int(elgamal["public_key"]), int(elgamal_priv_key)))
        final_valid_ballots = []
        for ballot in final_ballots:
            votes_valid = False
            for candidate_id, candidate_data in ballot.items():
                if (elGamal.pet(int(candidate_data[0]), int(candidate_data[1]), 1)):
                    votes_valid = True
                elif (elGamal.pet(int(candidate_data[0]), int(candidate_data[1]), 0)):
                    votes_valid = True

            ballot_sum_encrypted = self.get_ballot_sum(ballot, elGamal)
            if (elGamal.pet(int(ballot_sum_encrypted[0]), int(ballot_sum_encrypted[1]), 1)):
                votes_valid = True
            elif (elGamal.pet(int(ballot_sum_encrypted[0]), int(ballot_sum_encrypted[1]), 0)):
                votes_valid = True

            if votes_valid:
                final_valid_ballots.append(ballot)
        return final_valid_ballots

    def calculate_results(self, valid_ballots):
        elgamal = self.bb.get_public_params("elgamal")
        elgamal_priv_key = self.bb.get_private_param("elgamal_priv_key")
        elGamal = Utility.constructElGamal((int(elgamal["prime"]), int(elgamal["group"]), int(elgamal["public_key"]), int(elgamal_priv_key)))
        candidates = self.bb.get_candidates()
        results = {str(candidate["id"]): 0 for candidate in candidates}
        id_to_name = {str(candidate["id"]): candidate["candidate"] for candidate in candidates}

        first_ballot = True
        for ballot in valid_ballots:
            if first_ballot:
                results_ballot = ballot
                first_ballot = False
            else:
                for candidate_id, candidate_data in ballot.items():
                    results_ballot[candidate_id] = elGamal.homomorphic_addition((int(results_ballot[candidate_id][0]), int(results_ballot[candidate_id][1])), (int(candidate_data[0]), int(candidate_data[1])))

        results_ballot_decrypted = {}
        results = {}
        for candidate_id, candidate_data in results_ballot.items():
            decrypted_votes_count = elGamal.decrypt(int(candidate_data[0]), int(candidate_data[1]))
            results[candidate_id] = decrypted_votes_count
            results_ballot_decrypted[candidate_id] = {}
            results_ballot_decrypted[candidate_id]['number_of_votes'] = str(decrypted_votes_count)

        results_with_names = {id_to_name[id]: result['number_of_votes'] for id, result in results_ballot_decrypted.items()}

        highest_number = max(results, key=results.get)
        winner = next((candidate for candidate in candidates if str(candidate["id"]) == highest_number), None)

        self.bb.publish_decrypted_results(results_ballot_decrypted)
        self.bb.set_winner(highest_number, winner)
        self.bb.set_result(results_with_names)
        return results_ballot_decrypted, highest_number, winner["candidate"] if winner else None

    def get_ballot_sum(self, ballot, elGamal: ElGamal):
        first_item = True
        for candidate_id, candidate_data in ballot.items():
            if first_item:
                ballot_sum_encrypted = candidate_data
                first_item = False
            else:
                ballot_sum_encrypted= elGamal.homomorphic_addition((int(ballot_sum_encrypted[0]), int(ballot_sum_encrypted[1])), (int(candidate_data[0]), int(candidate_data[1])))

        return ballot_sum_encrypted
