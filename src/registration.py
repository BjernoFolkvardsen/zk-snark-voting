import uuid
from src.setup import SetupManager
#from src.bulletinboard import BullitinBoard
from merkly.mtree import MerkleTree
from Crypto.Hash import SHA256, SHA512
from Crypto.Signature import eddsa

class VoterRegistration:
    def __init__(self):
        self.setup = SetupManager()
        #self.bulletinboard = BullitinBoard()
        pass

    def registration(self):
        # register_voter('frederik')
        # register_voter('isabella')
        # register_voter('fink')
        # register_voter(343)
        (c_id, cr_id, t_id) = self.register_voter('frederik')
        (L, rt_L, sigma) = self.register('frederik', c_id, [])
        (c_id, cr_id, t_id) = self.register_voter('isabella')
        (L, rt_L, sigma) = self.register('isabella', c_id, L)
        (c_id, cr_id, t_id) = self.register_voter('bob')
        (L, rt_L, sigma) = self.register('bob', c_id, L)
        (c_id, cr_id, t_id) = self.register_voter('alice')
        (L, rt_L, sigma) = self.register('alice', c_id, L)
        (c_id, cr_id, t_id) = self.register_voter('charlie')
        self.register('charlie', c_id, L)
        

    def register_voter(self, id):
        cr_id = self.get_pseudonym(id)
        (c_id,t_id) = self.setup.SHA_commit(cr_id.encode())
        # print("id", id)
        # print("c_id", c_id)
        # print("cr_id", cr_id)
        # print("t_id", t_id.hex())
        # print()

        #self.bulletinboard.set_voter_commitments(c_id)
        return (c_id, cr_id, t_id)

    def get_pseudonym(self, value):
        # pseudonyms = {}
        # Pseudonymize the data
        pseudonym = str(uuid.uuid4())
        # pseudonyms.setdefault(name, str(uuid.uuid4()))
        # pseudonymized_data = [
        #     pseudonyms.setdefault(name, str(uuid.uuid4())) for name in data
        # ]
        # print("cr_id ",pseudonym)
        
        #self.bulletinboard.set_voter_pseudonym(id, pseudonym)
        return pseudonym

    def register(self, id, c_id, L ):
        tuple = (id, c_id)
        L.insert(0, tuple)
        # print('The list after adding: ', str(L) )
        if len(L) > 2 :
            l = []
            for (idx,c_idx) in L:
                l.insert(0,SHA256.new(idx.encode()+c_idx.encode()).hexdigest())
            rt_L = MerkleTree(l)
            (signing_key, verification_key) = self.setup.setup_digital_signature()
            # Creating byte array for list l and merkle tree root combined
            l_rt_L_bytes = bytearray()
            # Add all elements of l to byte array
            for elem in l:
                l_rt_L_bytes.extend(bytearray(elem.encode()))
            # Add all leaves from merkle tree root to byte array
            for elem in rt_L.leaves:
                l_rt_L_bytes.extend(bytearray(elem))
                
            message = SHA512.new(l_rt_L_bytes)
            signer = eddsa.new(signing_key, 'rfc8032')
            sigma = signer.sign(message)
            for (idx,c_idx) in L:
                print()
                print(idx)
                proof = rt_L.proof(SHA256.new(idx.encode()+c_idx.encode()).hexdigest())
                print("proof: ", proof)
                print("verify: ", self.verify(rt_L,proof,idx,c_idx, L))
            print()
            print()
            print()
        else :
            rt_L = None
            sigma = None
        print(rt_L)

        # print('σ signature: ', sigma)
        
        #self.bulletinboard.set_voters(id)
        #self.bulletinboard.set_merkletree(L)
        return(L, rt_L, sigma)

    def verify(self,rt_L, proof, id, c_id, L):
        #self.bulletinboard.get_list_id_commitment(id)
        return (rt_L.verify(proof,SHA256.new(id.encode()+c_id.encode()).hexdigest()) == True) and ((id, c_id) in L)

if __name__ == "__main__":
    registration_manager = VoterRegistration()
    registration_manager.registration()