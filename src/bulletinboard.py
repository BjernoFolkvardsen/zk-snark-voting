import json
# Help with Json see: https://www.freecodecamp.org/news/how-to-use-the-json-module-in-python/
class BullitinBoard:

    def __init__(self):
        self.path = "src/Data/data.json"
        pass

    def setup_bulletin_board(self):
         # Setup clean data.json from fakeData.json
        with open("src/Data/fakeData.json", "r") as file:
            data = json.load(file)
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)
        pass

    # Setup Phase
    ## Digital Signatures
    def set_digital_signature(self,verification_key):
        with open(self.path, "r") as file:
            data = json.load(file)
        data["public_params"]["digital_signature_verification_key"] = verification_key
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)
        pass
    
    def get_digital_signature(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["public_params"]["digital_signature_verification_key"]
    
    ## ElGamal
    def set_elgamal(self,public_key,prime,group):
        with open(self.path, "r") as file:
            data = json.load(file)
        data["public_params"]["elgamal"] = {
            'public_key': public_key,
            'prime': prime,
            'group': group
        }
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)
        pass
    
    def get_elgamal(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["public_params"]["elgamal"]

    # Registration Phase
    ## Get voters
    def get_eligible_voters(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["eligible_voters"]

    ## Pseudonym
    def set_voter_pseudonym(self, name, cr_id):
        with open(self.path, "r") as file:
            data = json.load(file)
        for voter in data["eligible_voters"]:
            if voter["id"] == name:    
                voter["cr_id"] = cr_id
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)

    def get_voter_pseudonym(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["eligible_voters"]["cr_id"]

    ## Commitment
    def set_voter_commitments(self, c_id):
        with open(self.path, "r") as file:
            data = json.load(file)
        if "commitments" not in data:
            data["commitments"] = []
        data["commitments"].append(c_id)
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)

    def get_voter_commitments(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["commitments"]
    
    
    ## List of voters
    def set_voters(self, id):
        with open(self.path, "r") as file:
            data = json.load(file)
        if "voters" not in data:
            data["voters"] = []
        data["voters"].append(id)
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)

    def get_voters(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["voters"]
    
    ## List of commitment and id (L)
    def set_list_id_commitment(self, merkle_tree):
        with open(self.path, "r") as file:
            data = json.load(file)
        data["list_L"] = [list(item) for item in merkle_tree]
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)
    
    def get_list_id_commitment(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        if "list_L" in data:
            return data["list_L"]
        return []

    ## Merkle tree root
    # def set_merkletree_root(self,rt_L):
    #     with open(self.path, "r") as file:
    #         data = json.load(file)
    #     data["merkletree_root"] = rt_L
    #     with open(self.path, "w") as file:
    #         json.dump(data, file, indent=2)
    #     pass
    
    # def get_merkletree_root(self):
    #     with open(self.path, "r") as file:
    #         data = json.load(file)
    #     return data["merkletree_root"]
    
    #Voting phase

    
    ## Get voters votes
    def get_votes(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["votes"]
    
    ## Ballot
    def get_candidates(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data["candidates"]

    def get_empty_ballot(self):
        candidates = self.get_candidates()
        ballot = {}
        for candidate in candidates:
            ballot[candidate["id"]] = 0
        return  ballot #{"cr_id": cr_id, "ballot": ballot}
    
    def set_ballot(self, ballot, cr_id):
        with open(self.path, 'r') as file:
            data = json.load(file)
        if "ballots" not in data:
            data["ballots"] = {}
        if cr_id not in data["ballots"]:
            data["ballots"][cr_id] = []
        data["ballots"][cr_id].append(ballot)
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)

    def get_ballot_by_cr_id(self, cr_id):
        with open(self.path, 'r') as file:
            data = json.load(file)
        return data["ballots"][cr_id]

    # Tally

    ## Final ballots
    def set_final_ballots(self, final_ballot):
        with open(self.path, "r") as file:
            data = json.load(file)
        if "final_ballots" not in data:
            data["final_ballots"] = []
        data["final_ballots"].append(final_ballot)
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)

# if __name__ == "__main__":
#     bullitin_board = BullitinBoard()
#     bullitin_board.setup_bulletin_board()
#     bullitin_board.set_elgamal("test",7,42)
#     bullitin_board.set_digital_signature("digital_signature_verification_key_test")
#     bullitin_board.set_voter_pseudonym(1, "3345678765")
#     bullitin_board.set_voter_commitments(34567890)
#     bullitin_board.set_voter_commitments("hej")
#     bullitin_board.set_voters(1)
#     bullitin_board.set_list_id_commitment([(1, "a"), (2, "b"), (3, "c")])
#     print(bullitin_board.get_list_id_commitment(2))
#     print(bullitin_board.get_elgamal())
#     print(bullitin_board.get_digital_signature())
    