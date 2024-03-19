import json
# Help with Json see: https://www.freecodecamp.org/news/how-to-use-the-json-module-in-python/
class BullitinBoard:

    path= "src/Data/data.json"

    @staticmethod
    def get_data():
        with open(BullitinBoard.path, "r") as file:
            data = json.load(file)
        return data

    @staticmethod
    def set_data(data):
        with open(BullitinBoard.path, "w") as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def setup_bulletin_board():
         # Setup clean data.json from fakeData.json
        with open("src/Data/fakeData.json", "r") as file:
            data = json.load(file)
        BullitinBoard.set_data(data)

    # Private things
    @staticmethod
    def set_private_param(name, value):
        data = BullitinBoard.get_data()
        if "private_params" not in data:
            data["private_params"] = {}
        data["private_params"][name] = value
        BullitinBoard.set_data(data)

    @staticmethod
    def get_private_param(name):
        data = BullitinBoard.get_data()
        return data["private_params"][name]

    ## Digital Signatures
    @staticmethod
    def set_digital_signature(verification_key):
        data = BullitinBoard.get_data()
        data["public_params"]["digital_signature_verification_key"] = verification_key
        BullitinBoard.set_data(data)
    
    @staticmethod
    def get_digital_signature():
        data = BullitinBoard.get_data()
        return data["public_params"]["digital_signature_verification_key"]
    
    ## ElGamal
    @staticmethod
    def set_elgamal(public_key,prime,group):
        data = BullitinBoard.get_data()
        data["public_params"]["elgamal"] = {
            'public_key': public_key,
            'prime': prime,
            'group': group
        }
        BullitinBoard.set_data(data)
    
    @staticmethod
    def get_elgamal():
        data = BullitinBoard.get_data()
        return data["public_params"]["elgamal"]

    ## Get voters
    @staticmethod
    def get_eligible_voters():
        data = BullitinBoard.get_data()
        return data["eligible_voters"]

    ## Pseudonym
    @staticmethod
    def set_voter_pseudonym(name, cr_id):
        data = BullitinBoard.get_data()
        if "voters" not in data:
            data["voters"] = {}
        if name not in data["voters"]:
            data["voters"][name] = {}
        data["voters"][name]["cr_id"] = cr_id
        BullitinBoard.set_data(data)

    @staticmethod
    def get_voter_pseudonym(id):
        data = BullitinBoard.get_data()
        return data["voters"][id]["cr_id"]

    ## Commitment
    @staticmethod
    def set_voter_commitments(c_id):
        data = BullitinBoard.get_data()
        if "commitments" not in data:
            data["commitments"] = []
        data["commitments"].append(c_id)
        BullitinBoard.set_data(data)

    @staticmethod
    def get_voter_commitments():
        data = BullitinBoard.get_data()
        return data["commitments"]
    
    ##zk-SNARK
    @staticmethod
    def set_zkey_file_name(zkey_file_name):
        data = BullitinBoard.get_data()
        data["zkey_file_name"] = zkey_file_name
        BullitinBoard.set_data(data)

    @staticmethod
    def get_zkey_file_name():
        data = BullitinBoard.get_data()
        return data["zkey_file_name"]
    
    ## List of voters
    @staticmethod
    def set_voters(id):
        data = BullitinBoard.get_data()
        if "voters" not in data:
            data["voters"] = {}
        if id not in data["voters"]:
            data["voters"][id] = {}
        BullitinBoard.set_data(data)
        
    @staticmethod
    def set_voter_commitment_random(id,t_id):
        data = BullitinBoard.get_data()
        if "voters" not in data:
            data["voters"] = {}
        if id not in data["voters"]:
            data["voters"][id] = {}
        data["voters"][id]["t_id"] = t_id
        BullitinBoard.set_data(data)

    @staticmethod
    def get_voters():
        data = BullitinBoard.get_data()
        return data["voters"]
    
    @staticmethod
    def get_voter(id:str):
        data = BullitinBoard.get_data()
        return data["voters"][id]
    
    ## List of commitment and id (L)
    @staticmethod
    def set_list_id_commitment(L):
        data = BullitinBoard.get_data()
        data["list_L"] = L
        BullitinBoard.set_data(data)
    
    @staticmethod
    def get_list_id_commitment():
        data = BullitinBoard.get_data()
        if "list_L" in data:
            return data["list_L"]
        return []

    ## Merkle tree root
    # @staticmethod
    def set_merkletree_root(root):
        with open(BullitinBoard.path, "r") as file:
            data = json.load(file)
        data["merkletree_root"] = root
        with open(BullitinBoard.path, "w") as file:
            json.dump(data, file, indent=2)
        pass
    
    # @staticmethod
    def get_merkletree_root():
        with open(BullitinBoard.path, "r") as file:
            data = json.load(file)
        return data["merkletree_root"]
    
    ## Get voters votes
    @staticmethod
    def get_votes():
        data = BullitinBoard.get_data()
        return data["votes"]
    
    ## Ballot
    @staticmethod
    def get_candidates():
        data = BullitinBoard.get_data()
        return data["candidates"]

    @staticmethod
    def get_empty_ballot():
        candidates = BullitinBoard.get_candidates()
        ballot = {}
        for candidate in candidates:
            if candidate["id"] not in ballot:
                ballot[candidate["id"]] = {}
            if "vote" not in ballot[candidate["id"]]:
                ballot[candidate["id"]]["vote"] = 0
            if "zk_proof" not in ballot[candidate["id"]]:
                ballot[candidate["id"]]["zk_proof"] = {}
        return  ballot #{"cr_id": cr_id, "ballot": ballot}
    
    @staticmethod
    def set_ballot(ballot, cr_id):
        data = BullitinBoard.get_data()
        if "ballots" not in data:
            data["ballots"] = {}
        if str(cr_id) not in data["ballots"]:
            data["ballots"][str(cr_id)] = []
        data["ballots"][str(cr_id)].append(ballot)
        BullitinBoard.set_data(data)

    @staticmethod
    def get_ballot_by_cr_id(cr_id):
        data = BullitinBoard.get_data()
        return data["ballots"][str(cr_id)]

    ## Final ballots
    @staticmethod
    def set_final_ballots(final_ballot):
        data = BullitinBoard.get_data()
        if "final_ballots" not in data:
            data["final_ballots"] = []
        data["final_ballots"].append(final_ballot)
        BullitinBoard.set_data(data)
    
    @staticmethod
    def set_final_ballots_decrypted(final_ballot_decrypted, cr_id):
        data = BullitinBoard.get_data()
        if "final_ballots_decrypted" not in data:
            data["final_ballots_decrypted"] = {}
        data["final_ballots_decrypted"][cr_id] = final_ballot_decrypted
        BullitinBoard.set_data(data)
    
    @staticmethod
    def get_final_ballots_decrypted():
        data = BullitinBoard.get_data()
        return data["final_ballots_decrypted"]
    
    @staticmethod
    def set_winner(highest_number, winner):
        data = BullitinBoard.get_data()
        data["winner"] = ( highest_number, winner)
        BullitinBoard.set_data(data)
    