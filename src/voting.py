# from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import ElGamal
from setup import SetupManager
from registration import VoterRegistration
class Voting:
    def __init__(self):
        self.setup = SetupManager()
        self.register = VoterRegistration()

    def voting(self):
        (c_id, cr_id, t_id) = self.register.register_voter('id')
        (sk_id) = self.generateSK_id(t_id, cr_id)
        (pk_T,sk_T,p,g) = self.setup.setup_elgamal(256)
        self.vote('id', sk_id, pk_T, 6,p,g,sk_T)

    def generateSK_id(self, cr_id, t_id):
        sk_id = (t_id, cr_id)
        return sk_id

    def vote(self, id, sk_id, pk_T, v,p,g,sk_T):
        # Encrypt the session key with the public RSA key
        ElgamalKeyObject = ElGamal.construct((p,g,pk_T))
        # cipher_elgamal = PKCS1_OAEP.new(pk_T)
        e_v = ElgamalKeyObject._encrypt(v,pk_T)

        # Decrypt the session key with the private RSA key
        #DecElgamalKeyObject = ElGamal.construct((p,g,pk_T,sk_T))
        # cipher_elgamal = PKCS1_OAEP.new(private_key)
        #v_new = DecElgamalKeyObject._decrypt(e_v)
        print('Encrypted vote:' , e_v)
        #print('Decrypted vote:' , v_new)
        (t_id, cr_id) = sk_id
        return (e_v, cr_id)

if __name__ == "__main__":
    voting_manager = Voting()
    voting_manager.voting()    