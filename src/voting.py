from Crypto.PublicKey import ElGamal
from src.bulletinboard import BullitinBoard
from src.registration import VoterRegistration
from src.utility import Utility
from zkpy.circuit import Circuit, GROTH
import random
import os
import json
from Crypto.Random import get_random_bytes
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

        eligible_voters = BullitinBoard.get_eligible_voters()
        for eligible_voter in eligible_voters:
            cr_ids.append(eligible_voter["cr_id"])
        selected_cr_id = random.choice(cr_ids)
        
        ballot = BullitinBoard.get_empty_ballot()
    
        for candidate, vote in ballot.items():
            ballot[candidate] = Utility.encrypt(0,random.randint(1, p-2), g, p, pk_T)
        BullitinBoard.set_ballot(ballot, selected_cr_id)
        return (ballot, selected_cr_id)


    def zk_snark(self):
        zkey_file_name = BullitinBoard.get_zkey_file_name()
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circuits/SetMembershipCircuit/"
        js_dir = working_dir+"merkleTree_js/"
        circuit = Circuit("merkleTree.circom", working_dir=working_dir,output_dir=working_dir, r1cs=None, js_dir=js_dir,
        wasm=js_dir+"merkleTree.wasm",
        witness=working_dir+"witness.wtns",
        zkey= zkey_file_name,
        vkey= working_dir+"vkey.json")

        ## VOTE INPUT
        # ElGamalKey = Utility.generateElGamalKey(256, get_random_bytes)
        # (pk,sk,p,g) = (ElGamalKey.y.__int__(), ElGamalKey.x.__int__(), ElGamalKey.p.__int__(), ElGamalKey.g.__int__())
        # print("p: ", p)
        # r = random.randint(1, p-2)
        # v = 0
        # null_vote = Utility.encrypt(v,r, g, p, pk)

        # inputs = {"pk_t":pk, "g":g, "e_v":[null_vote[0],null_vote[1]], "r":r, "v":v }
        # with open('circuits/FullCircuit/input.json', 'w') as f:
        #     json.dump(inputs, f)
        # print("inputs:", inputs)
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
