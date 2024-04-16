from src.bulletinboard import BullitinBoard
from src.utility import Utility, ElGamal
from zkpy.circuit import Circuit, GROTH
import random
import json
import os

class Tally:
    bb: BullitinBoard = None

    def __init__(self):
        self.bb = BullitinBoard(env="local", args={"type": "mongo_db"})
    
    def tally(self):
        cr_ids = []
        voters = self.bb.get_voters()
        for voter in voters:
            cr_ids.append(voter["cr_id"])
        
        random.shuffle(cr_ids)
        for cr_id in cr_ids:
            self.add_vote_same_pseudonym(cr_id)
        
        final_ballots = self.check_valid_ballot()
        self.calculate_results(final_ballots)

    def verify_ballot_votes(self, ballot):
        for candidate_id in ballot:
            working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../tmp/"
            circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir)
            with open("tmp/vkey.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["vkey"], file)
            with open("tmp/public.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["public"], file)
            with open("tmp/proof.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["proof"], file)

            if False == circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json"):
                return False
        return True

    def add_vote_same_pseudonym(self, cr_id):
        ballots = self.bb.get_ballot_by_cr_id(cr_id)
        elgamal = self.bb.get_elgamal()
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

        ## for test only
        final_ballot_decrypted = {}
        for j in range(len(final_ballot)):
            final_ballot_decrypted[j.__str__()] = str(elGamal.decrypt(int(final_ballot[j.__str__()][0]), int(final_ballot[j.__str__()][1])))
        self.bb.set_final_ballots_decrypted(final_ballot_decrypted, cr_id)
        ##***************

        self.bb.set_final_ballots(final_ballot)

        return (final_ballot)
    
    def check_valid_ballot(self):
        final_ballots = self.bb.get_final_ballots()
        elgamal = self.bb.get_elgamal()
        elgamal_priv_key = self.bb.get_private_param("elgamal_priv_key")
        elGamal = Utility.constructElGamal((int(elgamal["prime"]), int(elgamal["group"]), int(elgamal["public_key"]), int(elgamal_priv_key)))
        final_pet_ballots = []
        for ballot in final_ballots:
            total_votes = 0
            votes_valid = False
            ballot_winner = None
            for candidate_id, candidate_data in ballot.items():
                if (elGamal.pet(int(candidate_data[0]), int(candidate_data[1]), 1)):
                    votes_valid = True
                    ballot_winner = candidate_id
                    total_votes += 1
                elif (elGamal.pet(int(candidate_data[0]), int(candidate_data[1]), 0)):
                    votes_valid = True
            if votes_valid and total_votes in [0, 1]:
                final_pet_ballots.append(ballot_winner)
        self.bb.set_pet_ballots(final_pet_ballots) # for testing
        return final_pet_ballots

    def calculate_results(self, final_ballots):
        candidates = self.bb.get_candidates()
        results = {str(candidate["id"]): 0 for candidate in candidates}  
        id_to_name = {str(candidate["id"]): candidate["candidate"] for candidate in candidates}

        for candidate_id in final_ballots:
            results[str(candidate_id)] += 1

        results_with_names = {id_to_name[id]: count for id, count in results.items()}

        highest_number = max(results, key=results.get)
        winner = next((candidate for candidate in candidates if str(candidate["id"]) == highest_number), None)

        self.bb.set_winner(highest_number, winner)
        self.bb.set_result(results_with_names)
        return results, highest_number, winner["candidate"] if winner else None


    

    
