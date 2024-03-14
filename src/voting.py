from Crypto.PublicKey import ElGamal
from src.bulletinboard import BullitinBoard
from src.registration import VoterRegistration
from src.utility import Utility
from zkpy.circuit import Circuit, GROTH
from src.merkly import MerklyTree
import random
import os
import json
from Crypto.Random import get_random_bytes
class Voting:
    def __init__(self):
        pass

    def voting(self):
        voters = BullitinBoard.get_voters()
        votes_made = BullitinBoard.get_votes()
        elgamal = BullitinBoard.get_elgamal()
        for voter in voters:
            for vote in votes_made:
                self.null_votes(elgamal["prime"],elgamal["group"], elgamal["public_key"])
                if voter == vote["voterId"] :
                    (sk_id) = self.generateSK_id(7, voters[voter]["cr_id"])
                    (e_v, cr_id) = self.vote(voter, sk_id, elgamal["public_key"], vote["vote"],elgamal["prime"],elgamal["group"])
                    break
        # self.change_vote(voters[0]["id"], self.generateSK_id(7, voters[0]["cr_id"]), elgamal["public_key"], 3,elgamal["prime"],elgamal["group"],1)

    def generateSK_id(self, t_id, cr_id):
        sk_id = (t_id, cr_id)
        return sk_id

    def vote(self, id, sk_id, pk_T, v, p, g):
        (t_id, cr_id) = sk_id
        ballot = BullitinBoard.get_empty_ballot()
        for candidate, vote in ballot.items():
            if candidate == v:
                ballot[candidate] = Utility.encrypt(1,random.randint(1, p-2), g, p, pk_T)
            else:
                ballot[candidate] = Utility.encrypt(0,random.randint(1, p-2), g, p, pk_T)
        
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

        voters = BullitinBoard.get_voters()
        for id in voters:
            cr_ids.append(voters[id]["cr_id"])
        selected_cr_id = random.choice(cr_ids)
        
        ballot = BullitinBoard.get_empty_ballot()
    
        for candidate, vote in ballot.items():
            ballot[candidate] = Utility.encrypt(0,random.randint(1, p-2), g, p, pk_T)
        BullitinBoard.set_ballot(ballot, selected_cr_id)
        return (ballot, selected_cr_id)


    def zk_snark(self):
        zkey_file_name = BullitinBoard.get_zkey_file_name()
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circuits/FullCircuit/"
        js_dir = working_dir+"circuit_js/"
        circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir, r1cs=None, js_dir=js_dir,
        wasm=js_dir+"circuit.wasm",
        witness=working_dir+"witness.wtns",
        zkey= zkey_file_name,
        vkey= working_dir+"vkey.json")

        ## VOTE INPUT
        elgamal = BullitinBoard.get_elgamal()
        r = random.randint(1, int(elgamal["prime"])-2)
        v = 0
        null_vote = Utility.encrypt(v,r, elgamal["group"], elgamal["prime"], elgamal["public_key"])
        
        id = "Alberte"
        voter = BullitinBoard.get_voter(id)
        cr_id = voter["cr_id"]
        t_id = voter["t_id"]
        list_L = BullitinBoard.get_list_id_commitment()
        for tuple in list_L:
            if tuple[0] == id:
                c_id = tuple[1]
                break

        (path_indices, siblings) = self.get_path_indices_and_siblings(MerklyTree(list(map(lambda x: x[1], list_L))),c_id)

        inputs = {
                    "pk_t":str(elgamal["public_key"]), 
                    "g":str(elgamal["group"]), 
                    "e_v":[null_vote[0],null_vote[1]], 
                    "r":str(r), 
                    "v":str(v), 
                    "cr_id":str(cr_id), 
                    "c_id":str(c_id), 
                    "t_id":str(t_id),
                    "root":BullitinBoard.get_merkletree_root(), 
                    "pathIndices": path_indices,
                    "siblings": siblings
                  }

        with open('circuits/FullCircuit/input.json', 'w') as f:
             json.dump(inputs, f)
        #print("inputs:", inputs)
        # print("zkey_file_name: ", zkey_file_name)
        # print("inputs_json:", json.dumps(inputs))
        # inputs_json = json.dumps(inputs)

        ## COMMIT INPUT
        # registration_manager = VoterRegistration()
        # (c_id, cr_id, t_id) = registration_manager.register_voter('Frederik')
        # inputs = { "c_id":c_id, "cr_id":cr_id, "t_id":t_id }
        # print("inputs:", inputs)

        circuit.gen_witness(working_dir+"input.json")
        circuit.prove(GROTH)
        circuit.export_vkey(output_file=working_dir+"vkey.json")
        circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json")
    
    def get_path_indices_and_siblings(self, tree, leaf_value):
        path_indices = []
        siblings = []

        proof = tree.proof(leaf_value)
        for i, proof_node in enumerate(proof):     
            siblings.append(proof_node.data)
            path_indices.append(1 - proof_node.side.value)

        # print("leaf_value: ", leaf_value)
        # print("root: ", tree.root)
        # print("path indeces: ", path_indices)
        # print("siblings: ", siblings)

        return (path_indices, siblings)
