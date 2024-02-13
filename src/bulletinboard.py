import json
# Help with Json see: https://www.freecodecamp.org/news/how-to-use-the-json-module-in-python/
class BullitinBoard:
    def __init__(self):
        pass

    def setup_bulletin_board(self):
         # Setup clean data.json from fakeData.json
        with open("Data/fakeData.json", "r") as file:
            data = json.load(file)
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)
        pass

    # Setup Phase
    ## Digital Signatures
    def set_digital_signature(self,verification_key):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        data["public_params"]["digital_signature_verification_key"] = verification_key
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)
        pass
    
    def get_digital_signature(self):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        return data["public_params"]["digital_signature_verification_key"]
    
    ## ElGamal
    def set_elgamal(self,public_key,prime,group):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        data["public_params"]["elgamal"] = {
            'public_key': public_key,
            'prime': prime,
            'group': group
        }
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)
        pass
    
    def get_elgamal(self):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        return data["public_params"]["elgamal"]

    # Registration Phase
    ## Pseudonym
    def set_voter_pseudonym(self, id, cr_id):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        for voter in data["eligble_voters"]:
            if voter["id"] == id:
                voter['cr_id'] = cr_id
                break
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)
        pass

    def get_voter_pseudonym(self):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        return data["eligble_voters"]["cr_id"]

    ## Commitment
    def set_voter_commitments(self, c_id):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        data["commitments"].append(c_id)
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)
        pass

    def get_voter_commitments(self):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        return data["commitments"]
    
    ## List of voters
    def set_voters(self, id):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        if "voters" not in data:
            data["voters"] = []
        data["voters"].append(id)
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)

    def get_voters(self):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        return data["voters"]
    
    ## List of commitment and id
    def set_list_id_commitment(self, merkle_tree):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        data["list-L"] = [list(item) for item in merkle_tree]
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)
    
    def get_list_id_commitment(self):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        return data["list_L"]

    ## Merkle tree root
    def set_merkletree_root(self,rt_L):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        data["merkletree_root"] = rt_L
        with open("Data/data.json", "w") as file:
            json.dump(data, file, indent=2)
        pass
    
    def get_merkletree_root(self):
        with open("Data/data.json", "r") as file:
            data = json.load(file)
        return data["merkletree_root"]
    



if __name__ == "__main__":
    bullitin_board = BullitinBoard()
    bullitin_board.setup_bulletin_board()
    bullitin_board.set_elgamal("test",7,42)
    bullitin_board.set_digital_signature("digital_signature_verification_key_test")
    bullitin_board.set_voter_pseudonym(1, "3345678765")
    bullitin_board.set_voter_commitments(34567890)
    bullitin_board.set_voter_commitments("hej")
    bullitin_board.set_voters(1)
    bullitin_board.set_list_id_commitment([(1, "a"), (2, "b"), (3, "c")])
    bullitin_board.set_merkletree_root(34567898765)
    print(bullitin_board.get_elgamal())
    print(bullitin_board.get_digital_signature())
    