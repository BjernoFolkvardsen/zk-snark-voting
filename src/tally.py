from src.bulletinboard import BullitinBoard
from src.utility import Utility
from zkpy.circuit import Circuit, GROTH
import random
import json
import os

class Tally:
    def __init__(self):
        self.votes = {}
    
    def tally(self):
        cr_ids = []
        voters = BullitinBoard.get_voters()
        for voter in voters:
            cr_ids.append(voters[voter]["cr_id"])
     
        
        random.shuffle(cr_ids)
        for cr_id in cr_ids:
            self.add_vote_same_pseudonym(cr_id)
        
        self.calculate_results()

    def verify_ballot_votes(self, ballot):
        # ballot[candidate_id]["vote"]
        # ballot[candidate_id]["zk_proof"]
        # ballot[candidate_id]["zk_proof"]["vkey"]
        # ballot[candidate_id]["zk_proof"]["public"]
        # ballot[candidate_id]["zk_proof"]["proof"]

        #print("ballot", ballot)
        for candidate_id in ballot:
            print("candidate_vote", ballot[candidate_id])
            working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../tmp/"
            circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir)
            with open("tmp/vkey.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["vkey"], file)
            with open("tmp/public.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["public"], file)
            with open("tmp/proof.json", "w") as file:
                json.dump(ballot[candidate_id]["zk_proof"]["proof"], file)

            print("Verify ballot: ",circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json"))

            if False == circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json"):
                return False
        return True

    def add_vote_same_pseudonym(self, cr_id):
        ballots = BullitinBoard.get_ballot_by_cr_id(cr_id)
        elgamal = BullitinBoard.get_elgamal()
        x = 0
        for i in range(len(ballots)):
            if x == i:
                if self.verify_ballot_votes(ballots[i]) :
                    final_ballot = ballots[i]
                else:
                    x = x+1
            else :
                if self.verify_ballot_votes(ballots[i]):
                    for j in range(len(final_ballot)):
                        final_ballot[j.__str__()]["vote"] = Utility.homomorphic_addition(final_ballot[j.__str__()]["vote"], ballots[i][j.__str__()]["vote"], elgamal["prime"])
        
        BullitinBoard.set_final_ballots(final_ballot)

        ## for test only
        elgamal_priv_key = BullitinBoard.get_private_param("elgamal_priv_key")
        final_ballot_decrypted = {}
        for j in range(len(final_ballot)):
            final_ballot_decrypted[j.__str__()] = Utility.decrypt(final_ballot[j.__str__()]["vote"][0], final_ballot[j.__str__()]["vote"][1],elgamal["group"],elgamal["prime"],elgamal_priv_key)
        
        BullitinBoard.set_final_ballots_decrypted(final_ballot_decrypted, cr_id)
        ##***************

        return (final_ballot)
    
    def calculate_results(self):
        candidates = BullitinBoard.get_candidates()
        results = {str(candidate["id"]): 0 for candidate in candidates}
        total_entries = 0
        data = BullitinBoard.get_final_ballots_decrypted()
        

        for ballot in data.values():
            total_entries += 1
            for key, value in ballot.items():
                results[key] += value

        highest_number = max(results, key=results.get)
        winner = next((candidate for candidate in candidates if str(candidate["id"]) == highest_number), None)

        BullitinBoard.set_winner(highest_number, winner)
        return results, total_entries, highest_number, winner["candidate"] if winner else None


    

    
