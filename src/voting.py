from Crypto.PublicKey import ElGamal
from src.bulletinboard import BullitinBoard
from src.utility import Utility
import random
class Voting:
    def __init__(self):
        pass

    def voting(self):
        eligible_voters = BullitinBoard.get_eligible_voters()
        votes_made = BullitinBoard.get_votes()
        elgamal = BullitinBoard.get_elgamal()
        for eligible_voter in eligible_voters:
            for vote in votes_made:
                self.null_votes(elgamal["prime"],elgamal["group"], elgamal["public_key"])
                if eligible_voter["id"] == vote["voterId"] :
                    (sk_id) = self.generateSK_id(7, eligible_voter["cr_id"])
                    (e_v, cr_id) = self.vote(eligible_voter["id"], sk_id, elgamal["public_key"], vote["vote"],elgamal["prime"],elgamal["group"])
                    break
        self.change_vote(eligible_voters[0]["id"], self.generateSK_id(7, eligible_voters[0]["cr_id"]), elgamal["public_key"], 3,elgamal["prime"],elgamal["group"],1)

    def generateSK_id(self, t_id, cr_id):
        sk_id = (t_id, cr_id)
        return sk_id

    def vote(self, id, sk_id, pk_T, v, p, g):
        (t_id, cr_id) = sk_id
        ballot = BullitinBoard.get_empty_ballot()
        # ballot[v] = 1
        for candidate, vote in ballot.items():
            if candidate == v:
                ballot[candidate] = Utility.encrypt(1,random.randint(1, p-2), g, p, pk_T)
            else:
                ballot[candidate] = Utility.encrypt(0,random.randint(1, p-2), g, p, pk_T)
        
        # print('Ballot:', ballot)
        BullitinBoard.set_ballot(ballot, cr_id)
        return (ballot, cr_id)
    
    def change_vote(self, id, sk_id, pk_T, v_new, p, g, v_pre):
        (t_id, cr_id) = sk_id
        ballot = BullitinBoard.get_empty_ballot()
        for candidate, vote in ballot.items():
            if candidate == v_new:
                ballot[candidate] = Utility.encrypt(1,random.randint(1, p-2), g, p, pk_T)
            elif candidate == v_pre:
                ballot[candidate] = Utility.encrypt(-1,random.randint(1, p-2), g, p, pk_T)
            else:
                ballot[candidate] = Utility.encrypt(0,random.randint(1, p-2), g, p, pk_T)
        BullitinBoard.set_ballot(ballot, cr_id)
        return (ballot, cr_id)
    
    def null_votes(self, p, g, pk_T):
        cr_ids = []

        eligible_voters = BullitinBoard.get_eligible_voters()
        for eligible_voter in eligible_voters:
            cr_ids.append(eligible_voter["cr_id"])
        selected_cr_id = random.choice(cr_ids)
        
        ballot = BullitinBoard.get_empty_ballot()
    
        for candidate, vote in ballot.items():
            ballot[candidate] = Utility.encrypt(0,random.randint(1, p-2), g, p, pk_T)
        BullitinBoard.set_ballot(ballot, selected_cr_id)
        return (ballot, selected_cr_id)


