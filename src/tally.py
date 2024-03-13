from src.bulletinboard import BullitinBoard
from src.utility import Utility
import random

class Tally:
    def __init__(self):
        self.votes = {}
    
    def tally(self):
        cr_ids = []
        eligible_voters = BullitinBoard.get_eligible_voters()
        for eligible_voter in eligible_voters:
            cr_ids.append(eligible_voter["cr_id"])
     
        
        random.shuffle(cr_ids)
        for cr_id in cr_ids:
            self.add_vote_same_pseudonym(cr_id)
        
        self.calculate_results()

    def add_vote_same_pseudonym(self, cr_id):
        ballots = BullitinBoard.get_ballot_by_cr_id(cr_id)
        elgamal = BullitinBoard.get_elgamal()
        for i in range(len(ballots)):
            if 0 == i :
                final_ballot = ballots[i]
            else :
                for j in range(len(final_ballot)):
                    final_ballot[j.__str__()] = Utility.homomorphic_addition(final_ballot[j.__str__()], ballots[i][j.__str__()], elgamal["prime"])
        
        BullitinBoard.set_final_ballots(final_ballot)

        ## for test only
        elgamal_priv_key = BullitinBoard.get_private_param("elgamal_priv_key")
        final_ballot_decrypted = {}
        for j in range(len(final_ballot)):
            final_ballot_decrypted[j.__str__()] = Utility.decrypt(final_ballot[j.__str__()][0], final_ballot[j.__str__()][1],elgamal["group"],elgamal["prime"],elgamal_priv_key)
        
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


    

    
