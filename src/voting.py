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
    def __init__(self):
        pass

    def voting(self):
        voters = BullitinBoard.get_voters()
        votes_made = BullitinBoard.get_votes()
        elgamal = BullitinBoard.get_elgamal()
        for voter in voters:
            for vote in votes_made:
                for i in range(0, random.randint(1, 2)):
                    self.null_votes(elgamal["prime"],elgamal["group"], elgamal["public_key"])
                if voter == vote["voterId"] :
                    self.vote(voter, voters[voter]["t_id"], voters[voter]["cr_id"], elgamal["public_key"], vote["vote"],elgamal["prime"],elgamal["group"])
                    break
        # self.change_vote(voters[0]["id"], self.generateSK_id(7, voters[0]["cr_id"]), elgamal["public_key"], 3,elgamal["prime"],elgamal["group"],1)


    def vote(self, id, t_id, cr_id, pk_T, v_id, p, g):
        ballot = BullitinBoard.get_empty_ballot()
        for candidate, empty_value in ballot.items():
            r = random.randint(1, p-2)
            if candidate == v_id:
                vote = 1
            else :
                vote = 0
            e_v = Utility.encrypt(vote,r, g, p, pk_T)
            ballot[candidate]["vote"] = e_v
            ballot[candidate]["zk_proof"] = self.zk_snark(id, vote, cr_id, t_id, e_v, r, g, pk_T)
            
        
        BullitinBoard.set_ballot(ballot, cr_id)
    
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
    
    def null_votes(self, p, g, pk_T):
        random.seed() 
        cr_ids = []

        voters = BullitinBoard.get_voters()
        for id in voters:
            cr_ids.append(voters[id]["cr_id"])
        selected_cr_id = random.choice(cr_ids)

        
        ballot = BullitinBoard.get_empty_ballot()
        for candidate, empty_value in ballot.items():
            r = random.randint(1, p-2)
            e_v = Utility.encrypt(0,r, g, p, pk_T)
            ballot[candidate]["vote"] = e_v
            ballot[candidate]["zk_proof"] = self.zk_snark(0, 0, selected_cr_id, 0, e_v, r, g, pk_T)
        BullitinBoard.set_ballot(ballot, selected_cr_id)


    def zk_snark(self, id, v, cr_id, t_id, encrypt_vote, r, g, pk_T):
        zkey_file_name = BullitinBoard.get_zkey_file_name()
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circuits/FullCircuit/"
        js_dir = working_dir+"circuit_js/"
        circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir, r1cs=None, js_dir=js_dir,
        wasm=js_dir+"circuit.wasm",
        witness=working_dir+"witness.wtns",
        zkey= zkey_file_name,
        vkey= working_dir+"vkey.json")
        
        list_L = BullitinBoard.get_list_id_commitment()
        if(id!=0):
            for tuple in list_L:
                if tuple[0] == id:
                    c_id = tuple[1]
                    break
            (path_indices, siblings) = self.get_path_indices_and_siblings(MerklyTree(list(map(lambda x: x[1], list_L))),c_id)
        else:
            tuple = random.choice(list_L)
            (path_indices, siblings) = self.get_path_indices_and_siblings(MerklyTree(list(map(lambda x: x[1], list_L))),tuple[1])
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
                    "root": str(BullitinBoard.get_merkletree_root()),
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
