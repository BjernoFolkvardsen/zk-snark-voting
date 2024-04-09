import json
# Help with Json see: https://www.freecodecamp.org/news/how-to-use-the-json-module-in-python/
import random
from faker import Faker
import pymongo

class BullitinBoard:

    path: str = None
    db: pymongo.MongoClient = None

    def __init__(self, env:str=None, args:dict=None):
        if env == "production":
            pass
        elif env == "staging":      
            pass
        elif env == "development":
            pass
        else: # Default to local
            self.env = "local"
            if args["type"] == "mongo_db":
                self.path = "src/Data/test.json"
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                self.db = client["db"]
                self.db_type = "local_mongo_db"
            else:
                self.db_type = "local_file"
                self.path = "src/Data/data.json"

    def generate_data(self, num_voters=4, num_candidates=2):
        fake = Faker()

        eligible_voters = [{"id": str(i), "name": fake.first_name()} for i in range(num_voters)]

        candidates = [{"id": str(i), "candidate": fake.name()} for i in range(num_candidates)]

        votes = [{"voterId": str(i), "vote": random.choice(candidates)["id"]} for i in range(num_voters)]

        self.set_data(eligible_voters, collection_name="eligible_voters", many=True)
        self.set_data(candidates, collection_name="candidates", many=True)
        self.set_data(votes, collection_name="votes", many=True)

    def get_data(self, collection_name:str, key:str=None, query:dict=None, many:bool=False):
        if self.db_type == "local_file":
            with open(BullitinBoard.path, "r") as file:
                data = json.load(file)
            if key is not None:
                return data[collection_name][key]
            elif query is not None:
                for key, value in query.items():
                    data = [x for x in data[collection_name] if x[key] == value]
                return data
            else:
                return data[collection_name]
        elif self.db_type == "local_mongo_db":
            collection = self.db[collection_name]
            if key is not None:
                dict = collection.find_one({"key":key})
                return dict.get("data")
            elif query is not None:
                if many:
                    return list(collection.find(query,{'_id': False}))
                else:
                    return collection.find_one(query,{'_id': False})
            else:
                return list(collection.find({},{'_id': False}))
        else:
            return None

    def set_data(self, data, collection_name:str, key:str=None, many:bool=False):
        if self.db_type == "local_file":
            file_data = BullitinBoard.get_data()
            if collection_name not in file_data:
                if many:
                    file_data[collection_name] = []
                else:
                    file_data[collection_name] = {}
            if key is not None:
                if key not in file_data[collection_name]:
                    file_data[collection_name][key] = {}
                file_data[collection_name][key] = data
            else:
                file_data[collection_name] = data
            with open(BullitinBoard.path, "w") as file:
                json.dump(file_data, file, indent=2)
        elif self.db_type == "local_mongo_db":
            collection = self.db[collection_name]
            if key is not None:
                collection.insert_one({"key":key, "data":data})
            elif many:
                collection.insert_many(data)
            else:
                collection.insert_one(data)
        else:
            pass

    # Private things
    def set_private_param(self, name, value):
        self.set_data(value, collection_name="private_params", key=name )

    def get_private_param(self, name):
        return self.get_data(collection_name="private_params", key=name)

    ## Digital Signatures
    def set_digital_signature(self,verification_key):
        self.set_data(verification_key, collection_name="public_params", key="digital_signature_verification_key")
    
    def get_digital_signature(self):
        return self.get_data(collection_name="public_params", key="digital_signature_verification_key")
    
    ## ElGamal
    def set_elgamal(self, public_key, prime, group):
        data = {
            'public_key': public_key,
            'prime': prime,
            'group': group
        }
        self.set_data(data, collection_name="public_params", key="elgamal")
    
    def get_elgamal(self):
        return self.get_data(collection_name="public_params", key="elgamal")

    ## Get voters
    def get_eligible_voters(self):
        return self.get_data(collection_name="eligible_voters")

    def set_voter(self, name, cr_id, id, t_id):
        data = {"name": str(name), "cr_id": str(cr_id), "id": str(id), "t_id": str(t_id)}
        self.set_data(data, collection_name="voters")

    def get_voter_pseudonym(self, id):
        data = self.get_data(collection_name="voters", query={"id": id})
        return data.get("cr_id")

    ## Commitment
    def set_voter_commitments(self, c_id):
        self.set_data({"c_id": str(c_id)}, collection_name="commitments")

    def get_voter_commitments(self):
        return self.get_data(collection_name="commitments")
    
    ##zk-SNARK
    def set_zkey_file_name(self, zkey_file_name):
        # Maybe we should store the zkey file in the database and not the file name
        self.set_data(zkey_file_name, collection_name="public_params", key="zkey_file_name")

    def get_zkey_file_name(self):
        # Maybe we should store the zkey file in the database and not the file name
        return self.get_data(collection_name="public_params", key="zkey_file_name")

    def get_voters(self):
        return self.get_data(collection_name="voters")
    
    def get_voter(self, id:str):
        return self.get_data(collection_name="voters", query={"id": id})
    
    ## List of commitment and id (L)
    def set_list_id_commitment(self, tuple: (str,str)):
        self.set_data({"tuple":tuple},collection_name="id_commitment")

    def set_many_list_id_commitment(self, tuple_list: list[dict]):
        self.set_data(data=tuple_list,collection_name="id_commitment", many=True)
    
    def get_list_id_commitment(self):
        data = self.get_data(collection_name="id_commitment")
        L = []
        for x in data:
            L.append(x["tuple"])
        return L

    ## Merkle tree root
    def set_merkletree_root(self, root:str):
        self.set_data(root,collection_name="public_params", key="merkletree_root")

    def get_merkletree_root(self):
        return self.get_data(collection_name="public_params", key="merkletree_root")
    
    def set_merkletree_sigma(self, sigma:str):
        self.set_data(sigma,collection_name="public_params", key="merkletree_sigma")
    
    ## Get voters votes
    def get_votes(self):
        return self.get_data(collection_name="votes")
    
    ## Ballot
    def get_candidates(self):
        return self.get_data(collection_name="candidates")

    def get_empty_ballot(self):
        candidates = self.get_candidates()
        ballot = {}
        for candidate in candidates:
            if candidate["id"] not in ballot:
                ballot[candidate["id"]] = {}
            if "vote" not in ballot[candidate["id"]]:
                ballot[candidate["id"]]["vote"] = 0
            if "zk_proof" not in ballot[candidate["id"]]:
                ballot[candidate["id"]]["zk_proof"] = {}
        return  ballot
    
    def set_ballot(self, ballot, cr_id:str):
        self.set_data(ballot,collection_name="ballots", key=cr_id)

    def get_ballot_by_cr_id(self, cr_id:str):
        return self.get_data(collection_name="ballots", query = {"key": cr_id}, many=True)

    ## Final ballots
    def set_final_ballots(self,final_ballot):
        self.set_data(final_ballot,collection_name="final_ballots")

    def get_final_ballots(self):
        return self.get_data(collection_name="final_ballots")
    
    def set_pet_ballots(self, final_ballot):
        self.set_data(final_ballot,collection_name="final_results", key="final_pet_ballots")
    
    def get_pet_ballots(self):
        return self.get_data(collection_name="final_results", key="final_pet_ballots")
    
    def set_final_ballots_decrypted(self, final_ballot_decrypted, cr_id):
        self.set_data(final_ballot_decrypted,collection_name="final_ballots_decrypted", key=str(cr_id))

    def get_final_ballots_decrypted(self):
        return self.get_data(collection_name="final_ballots_decrypted")

    ## Tally results
    def set_winner(self, highest_number, winner):
        self.set_data((highest_number, winner),collection_name="final_results", key="winner")

    def set_result(self, result):
        self.set_data(result,collection_name="final_results", key="result")

    def get_result(self, result):
        return self.get_data(collection_name="final_results", key="result")
    