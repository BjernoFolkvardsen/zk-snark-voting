from src.bulletinboard import BullitinBoard
from src.merkly import MerklyTree
from src.utility import Utility
from Crypto.PublicKey import ECC
from Crypto.Signature import eddsa
import uuid

class VoterRegistration:
    def __init__(self):
        pass

    def registration(self):
        eligible_voters = BullitinBoard.get_eligible_voters()

        for eligible_voter in eligible_voters:
            (c_id, cr_id, t_id) = self.register_voter(eligible_voter["id"])
            self.register(eligible_voter["id"],c_id)
        
    def register_voter(self, id):
        cr_id = self.get_pseudonym(id)
        print("cr_id", cr_id)
        (c_id,t_id) = Utility.commit(cr_id)

        c_id = int(c_id, 16)
        BullitinBoard.set_voter_commitments(c_id)
        BullitinBoard.set_voter_commitment_random(id,t_id)
        return (c_id, cr_id, t_id)

    def get_pseudonym(self, value):
        pseudonym = uuid.uuid4().int
        BullitinBoard.set_voter_pseudonym(value, pseudonym)
        return pseudonym
    
    def register(self, id, c_id):
        L = BullitinBoard.get_list_id_commitment()
        tuple = (id, int(c_id))
        L.append(tuple)
        # If length of list L is less than 3 don't make merkle tree
        if len(L) > 2 :
            rt_L = MerklyTree(list(map(lambda x: x[1], L)))
            signing_key = ECC.import_key(BullitinBoard.get_private_param("signing_key"))

            # Creating byte array for list l and merkle tree root combined
            l_rt_L_bytes = bytearray()
            # Add all elements of l to byte array
            for elem in L:
                l_rt_L_bytes.extend(bytearray(str(elem[0]).encode()))
                l_rt_L_bytes.extend(bytearray(str(elem[1]).encode()))
            # Add all leaves from merkle tree root to byte array
            for elem in rt_L.leaves:
                l_rt_L_bytes.extend(bytearray(str(elem).encode()))
            
            signer = eddsa.new(signing_key, 'rfc8032')
            sigma = signer.sign(bytes(l_rt_L_bytes))
        else :
            rt_L = None
            sigma = None
        
        BullitinBoard.set_voters(id)
        BullitinBoard.set_list_id_commitment(L)
        if rt_L is not None:
            BullitinBoard.set_merkletree_root(rt_L.root)
            self.verify(rt_L,  rt_L.proof(c_id), c_id, L)
        return(L, rt_L, sigma)
    
    def verify(self,rt_L, proof, c_id, L):
        return rt_L.verify(proof,c_id) and rt_L.verify_correctly_build(list(map(lambda x: x[1], L)), BullitinBoard.get_merkletree_root())
        