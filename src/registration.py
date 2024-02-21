import uuid
from src.bulletinboard import BullitinBoard
from merkly.mtree import MerkleTree
from Crypto.Hash import SHA256, SHA512
from Crypto.Signature import eddsa
from Crypto.PublicKey import ECC
from src.utility import Utility

class VoterRegistration:
    def __init__(self):
        pass

    def registration(self):
        eligible_voters = BullitinBoard.get_eligible_voters()

        for eligible_voter in eligible_voters:
            (c_id, cr_id, t_id) = self.register_voter(eligible_voter["id"])
            self.register(eligible_voter["id"],c_id)
        
        # register_voter('frederik')
        # register_voter('isabella')
        # register_voter('fink')
        # register_voter(343)
        # (c_id, cr_id, t_id) = self.register_voter('Frederik')
        # (L, rt_L, sigma) = self.register('Frederik', c_id, [])
        # (c_id, cr_id, t_id) = self.register_voter('Isabella')
        # (L, rt_L, sigma) = self.register('Isabella', c_id, L)
        # (c_id, cr_id, t_id) = self.register_voter('Louise')
        # (L, rt_L, sigma) = self.register('Louise', c_id, L)
        # (c_id, cr_id, t_id) = self.register_voter('Alberte')
        # self.register('Alberte', c_id, L)
        

    def register_voter(self, id):
        cr_id = self.get_pseudonym(id)
        (c_id,t_id) = Utility.SHA_commit(cr_id.encode())
        # print("id", id)
        # print("c_id", c_id)
        # print("cr_id", cr_id)
        # print("t_id", t_id.hex())
        # print()

        BullitinBoard.set_voter_commitments(c_id)
        return (c_id, cr_id, t_id)

    def get_pseudonym(self, value):
        # pseudonyms = {}
        # Pseudonymize the data
        pseudonym = str(uuid.uuid4())
        # pseudonyms.setdefault(name, str(uuid.uuid4()))
        # pseudonymized_data = [
        #     pseudonyms.setdefault(name, str(uuid.uuid4())) for name in data
        # ]
        BullitinBoard.set_voter_pseudonym(value, pseudonym)
        return pseudonym

    def register(self, id, c_id):
        L = BullitinBoard.get_list_id_commitment()
        L.insert(0, id + "|" + c_id)

        # If length of list L is less than 3 don't make merkle tree
        if len(L) > 2 :
            rt_L = MerkleTree(L)
            signing_key = ECC.import_key(BullitinBoard.get_private_param("signing_key"))

            # Creating byte array for list l and merkle tree root combined
            l_rt_L_bytes = bytearray()
            # Add all elements of l to byte array
            for elem in L:
                l_rt_L_bytes.extend(bytearray(elem.encode()))
            # Add all leaves from merkle tree root to byte array
            for elem in rt_L.leaves:
                l_rt_L_bytes.extend(bytearray(elem))
            
            # message = SHA512.new(l_rt_L_bytes)
            signer = eddsa.new(signing_key, 'rfc8032')
            sigma = signer.sign(bytes(l_rt_L_bytes))
            # for value in L:
            #     # print()
            #     # print(idx)
            #     proof = rt_L.proof(value)
            #     print("proof: ", proof)
            #     print("verify: ", self.verify(rt_L,proof,idx,c_idx, L))
            # print()
            # print()
            # print()
        else :
            rt_L = None
            sigma = None
        # print(rt_L)

        # print('σ signature: ', sigma)
        
        BullitinBoard.set_voters(id)
        BullitinBoard.set_list_id_commitment(L)
        return(L, rt_L, sigma)

    def verify(self,rt_L, proof, id, c_id, L):
        return (rt_L.verify(proof,SHA256.new(id.encode()+c_id.encode()).hexdigest()) == True) and ((id, c_id) in L)

# if __name__ == "__main__":
#     registration_manager = VoterRegistration()
#     registration_manager.registration()