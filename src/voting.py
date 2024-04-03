from Crypto.PublicKey import ElGamal
from src.bulletinboard import BullitinBoard
from src.registration import VoterRegistration
from src.utility import Utility
from zkpy.circuit import Circuit, GROTH
from src.merkly import MerklyTree
import random
import os
import json
class Voting:
    bb: BullitinBoard = None

    def __init__(self):
        self.bb = BullitinBoard(env="local", args={"type": "mongo_db"})

    def voting(self):
        voters = self.bb.get_voters()
        votes_made = self.bb.get_votes()
        elgamal = self.bb.get_elgamal()
        prime = int(elgamal["prime"])
        group = int(elgamal["group"])
        public_key = int(elgamal["public_key"])
        for voter in voters:
            for i in range(0, random.randint(1, 2)):
                    self.null_votes(prime,group, public_key)
            for vote in votes_made:
                print("vote: ", vote)
                print("voter: ", voter)
                if voter["id"] == vote["voterId"] :
                    self.vote(voter["id"], voter["t_id"], voter["cr_id"], public_key, vote["vote"], prime, group)
                    self.verify_vote_on_bb(voter["cr_id"])
                    
                    # if "re-vote" in vote:
                    #  self.vote(voter, voters[voter]["t_id"], voters[voter]["cr_id"], elgamal["public_key"], vote["re-vote"],elgamal["prime"],elgamal["group"])
                    #  break


    def vote(self, id, t_id, cr_id, pk_T, v_id, p, g):
        ballot = self.bb.get_empty_ballot()
        for candidate, empty_value in ballot.items():
            r = random.randint(1, p-2)
            print(" POW", candidate, v_id)
            if candidate == v_id:
                vote = 1
            else :
                vote = 0
            e_v = Utility.encrypt(vote,r, g, p, pk_T)
            ballot[candidate]["vote"] = [str(e_v[0]),str(e_v[1])]
            ballot[candidate]["zk_proof"] = self.zk_snark(id, vote, cr_id, t_id, e_v, r, g, pk_T)
            
        self.bb.set_ballot(ballot, cr_id)
    
    # def change_vote(self, id, t_id, cr_id, pk_T, v_new, p, g, v_pre):
    #     elgamal = BullitinBoard.get_elgamal()
    #     elgamal_priv_key = BullitinBoard.get_private_param("elgamal_priv_key")
    #     ballot = BullitinBoard.get_empty_ballot()
    #     for candidate, empty_value in ballot.items():
    #         r = random.randint(1, p-2)
    #         if candidate == v_new:
    #             print("Candidatenew: ", candidate)
    #             vote = 1
    #         elif candidate == v_pre:
    #             print("Candidatepre: ", candidate)
    #             vote = -1
    #         else:
    #             vote = 0
    #         e_v = Utility.encrypt(vote,r, g, p, pk_T)
    #         print("Vote: ", vote)
    #         print("Vote e_V: ", e_v)
    #         ballot[candidate]["vote"] = e_v
    #        # ballot[candidate]["zk_proof"] = self.zk_snark(id, vote, cr_id, t_id, e_v, r, g, pk_T)

    #     print("id", id)
    #     print("ballot", ballot)
    #     print("vote 0: ", Utility.decrypt(ballot[0]["vote"][0], ballot[0]["vote"][1],elgamal["group"],elgamal["prime"],elgamal_priv_key))
    #     print("test enc", pow(g.__int__(),-1,p.__int__()))
    #     print("test enc mod p", (pow(g.__int__(),-1,p.__int__())) % p.__int__())
    #     print("org enc", (ballot[1]["vote"][1] * pow(ballot[1]["vote"][0], -1*elgamal_priv_key.__int__(), p.__int__())))
    #     print("org enc mod p", (ballot[1]["vote"][1] * pow(ballot[1]["vote"][0], -1*elgamal_priv_key.__int__(), p.__int__())) % p.__int__())
    #     print("vote 1: ", Utility.decrypt(ballot[1]["vote"][0], ballot[1]["vote"][1],elgamal["group"],elgamal["prime"],elgamal_priv_key))
    #     BullitinBoard.set_ballot(ballot, cr_id)
    
    def null_votes(self, p, g, pk_T):
        random.seed() 
        cr_ids = []

        voters = self.bb.get_voters()
        for voter in voters:
            cr_ids.append(voter["cr_id"])
        selected_cr_id = random.choice(cr_ids)

        
        ballot = self.bb.get_empty_ballot()
        for candidate, empty_value in ballot.items():
            r = random.randint(1, p-2)
            e_v = Utility.encrypt(0,r, g, p, pk_T)
            ballot[candidate]["vote"] = [str(e_v[0]),str(e_v[1])]
            ballot[candidate]["zk_proof"] = self.zk_snark(0, 0, selected_cr_id, 0, e_v, r, g, pk_T)
        self.bb.set_ballot(ballot, selected_cr_id)


    def zk_snark(self, id, v, cr_id, t_id, encrypt_vote, r, g, pk_T):
        zkey_file_name = self.bb.get_zkey_file_name()
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circuits/FullCircuit/"
        js_dir = working_dir+"circuit_js/"
        circuit = Circuit("circuit.circom", working_dir=working_dir, output_dir=working_dir, r1cs=None, js_dir=js_dir,
        wasm=js_dir+"circuit.wasm",
        witness=working_dir+"witness.wtns",
        zkey= zkey_file_name,
        vkey= working_dir+"vkey.json")
        
        list_L = self.bb.get_list_id_commitment()
        print("list_L",list_L)
        if(id!=0):
            for tuple in list_L:
                if tuple[0] == id:
                    c_id = tuple[1]
                    break
            tree = MerklyTree(list(map(lambda x: int(x[1]), list_L)))
            print("tree raw",tree.raw_leaves)
            print()
            print("tree hashed",tree.leaves)
            print()
            print("c_id",c_id)
            print()
            (path_indices, siblings) = self.get_path_indices_and_siblings(tree,int(c_id))
            print("path_indices",path_indices)
            print()
            print("siblings",siblings)
        else:
            tuple = random.choice(list_L)
            (path_indices, siblings) = self.get_path_indices_and_siblings(MerklyTree(list(map(lambda x: int(x[1]), list_L))),int(tuple[1]))
            c_id = 0

        inputs = {
                    "pk_t":str(pk_T),
                    "g":str(g),
                    "e_v":[str(encrypt_vote[0]),str(encrypt_vote[1])],
                    "r":str(r),
                    "v":str(v),
                    "cr_id":str(cr_id),
                    "c_id":str(c_id),
                    "t_id":str(t_id),
                    "root": str(self.bb.get_merkletree_root()),
                    "pathIndices": list(map(lambda x: str(x), path_indices)),
                    "siblings": list(map(lambda x: str(x), siblings))
                  }

        with open('circuits/FullCircuit/input.json', 'w') as f:
             json.dump(inputs, f, indent=2)

        circuit.gen_witness(working_dir+"input.json")
        circuit.prove(GROTH)
        circuit.export_vkey(output_file=working_dir+"vkey.json")

        proof_data = {"vkey":{}, "public": {}, "proof": {}}
        with open("circuits/FullCircuit/vkey.json", "r") as file:
            proof_data["vkey"] = json.load(file)
        with open("circuits/FullCircuit/public.json", "r") as file:
            proof_data["public"] = json.load(file)
        with open("circuits/FullCircuit/proof.json", "r") as file:
            proof_data["proof"] = json.load(file)
        
        return proof_data
        # circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json")
    
    def get_path_indices_and_siblings(self, tree, leaf_value):
        path_indices = []
        siblings = []

        proof = tree.proof(leaf_value)
        for i, proof_node in enumerate(proof):
            siblings.append(proof_node.data)
            path_indices.append(1 - proof_node.side.value)

        return (path_indices, siblings)

    def verify_vote_on_bb(self, voter_id):
        ballot = self.bb.get_ballot_by_cr_id(voter_id)
        if ballot:
            return True
        else:
            raise ValueError(f"No ballot exists for voter {voter_id}.")
