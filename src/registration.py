from src.bulletinboard import BullitinBoard
from src.merkly import MerklyTree
from src.utility import Utility
from Crypto.PublicKey import ECC
from Crypto.Signature import eddsa
import uuid

class VoterRegistration:

    bb: BullitinBoard = None

    def __init__(self, bb: BullitinBoard):
        self.bb = bb

    def registration(self):
        eligible_voters = self.bb.get_eligible_voters()

        for eligible_voter in eligible_voters:
            (c_id, cr_id, t_id) = self.register_voter(eligible_voter["id"], eligible_voter["name"])
            self.register(eligible_voter["id"],c_id)

        self.publish_merkletree()

    def register_voter(self, id, name):
        cr_id = Utility.get_pseudo_id(int(self.bb.get_public_params("CR_from")), int(self.bb.get_public_params("CR_to")))
        (c_id,t_id) = Utility.commit(cr_id, int(self.bb.get_public_params("T_from")), int(self.bb.get_public_params("T_to")))

        c_id = int(c_id, 16)
        self.bb.set_cr_ids(cr_id)
        self.bb.set_voter(name, cr_id,id,t_id) # just for testing purposes
        return (c_id, cr_id, t_id)

    def register(self, id, c_id):
        self.bb.set_list_id_commitment((str(id), str(c_id)))

    def publish_merkletree(self):
        tuple_list = []
        for i in range(pow(2,Utility.MTREE_DEPTH)-Utility.MAX_NUMBER_OF_VOTERS):
            tuple_list.append({"tuple":("-1", "0")})
        if tuple_list:
            self.bb.set_many_list_id_commitment(tuple_list)
        L = self.bb.get_list_id_commitment()
        rt_L = MerklyTree(list(map(lambda x: int(x[1]), L)))
        signing_key = ECC.import_key(self.bb.get_private_param("signing_key"))
        signer = eddsa.new(signing_key, 'rfc8032')
        sigma = signer.sign(str(rt_L.root).encode())

        self.bb.set_merkletree_root(str(rt_L.root))
        self.bb.set_merkletree_sigma(str(sigma))

    def verify(self,rt_L, proof, c_id, L):
        return rt_L.verify(proof,c_id) and rt_L.verify_correctly_build(list(map(lambda x: int(x[1]), L)), self.bb.get_merkletree_root())
