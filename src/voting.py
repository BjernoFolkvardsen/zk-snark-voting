# from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import ElGamal
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.bulletinboard import BullitinBoard
import random
class Voting:
    def __init__(self):
        self.setup = SetupManager()
        self.register = VoterRegistration()
        self.bulletinboard = BullitinBoard()

    def voting(self):
        eligible_voters = self.bulletinboard.get_eligible_voters()
        votes_made = self.bulletinboard.get_votes()
        elgamal = self.bulletinboard.get_elgamal()
        for eligible_voter in eligible_voters:
            for vote in votes_made:
                self.null_votes(elgamal["prime"],elgamal["group"], elgamal["public_key"])
                if eligible_voter["id"] == vote["voterId"] :
                    (sk_id) = self.generateSK_id(7, eligible_voter["cr_id"])
                    (e_v, cr_id) = self.vote(eligible_voter["id"], sk_id, elgamal["public_key"], vote["vote"],elgamal["prime"],elgamal["group"])
                    break
        self.change_vote(eligible_voters[0]["id"], self.generateSK_id(7, eligible_voters[0]["cr_id"]), elgamal["public_key"], 4,elgamal["prime"],elgamal["group"],2)

    def generateSK_id(self, t_id, cr_id):
        sk_id = (t_id, cr_id)
        return sk_id

    def vote(self, id, sk_id, pk_T, v, p, g):
        (t_id, cr_id) = sk_id
        # Encrypt the session key with the public RSA key
        ElgamalKeyObject = ElGamal.construct((p,g,pk_T))
        # cipher_elgamal = PKCS1_OAEP.new(pk_T)
        ballot = self.bulletinboard.get_empty_ballot()
        # ballot[v] = 1
        for candidate, vote in ballot.items():
            if candidate == v:
                ballot[candidate] = ElgamalKeyObject._encrypt(pow(g,1),random.randint(1, p-2))
            else:
                ballot[candidate] = ElgamalKeyObject._encrypt(pow(g,0),random.randint(1, p-2))
        # Decrypt the session key with the private RSA key
        #DecElgamalKeyObject = ElGamal.construct((p,g,pk_T,sk_T))
        # cipher_elgamal = PKCS1_OAEP.new(private_key)
        #v_new = DecElgamalKeyObject._decrypt(e_v)
        # print('Encrypted vote:' , e_v)
        #print('Decrypted vote:' , v_new)
        
        print('Ballot:', ballot)
        self.bulletinboard.set_ballot(ballot, cr_id)
        return (ballot, cr_id)
    
    def change_vote(self, id, sk_id, pk_T, v_new, p, g, v_pre):
        (t_id, cr_id) = sk_id
        ElgamalKeyObject = ElGamal.construct((p,g,pk_T))
        ballot = self.bulletinboard.get_empty_ballot()
        for candidate, vote in ballot.items():
            if candidate == v_new:
                ballot[candidate] = ElgamalKeyObject._encrypt(pow(g,1),random.randint(1, p-2))
            elif candidate == v_pre:
                ballot[candidate] = ElgamalKeyObject._encrypt(pow(g,-1),random.randint(1, p-2))
            else:
                ballot[candidate] = ElgamalKeyObject._encrypt(pow(g,0),random.randint(1, p-2))
        self.bulletinboard.set_ballot(ballot, cr_id)
        return (ballot, cr_id)
    
    def null_votes(self, p, g, pk_T):
        cr_ids = []
        ElgamalKeyObject = ElGamal.construct((p,g,pk_T))

        eligible_voters = self.bulletinboard.get_eligible_voters()
        for eligible_voter in eligible_voters:
            cr_ids.append(eligible_voter["cr_id"])
        selected_cr_id = random.choice(cr_ids)
        
        ballot = self.bulletinboard.get_empty_ballot()
    
        for candidate, vote in ballot.items():
            ballot[candidate] = ElgamalKeyObject._encrypt(pow(g,0), random.randint(1, p-2))
        self.bulletinboard.set_ballot(ballot, selected_cr_id)
        return (ballot, selected_cr_id)


