import random
from faker import Faker
import pymongo
import configparser

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
            config = configparser.ConfigParser()
            config.read('config.ini')
            client = pymongo.MongoClient("mongodb://"+config['Database']['db_host']+":"+config['Database']['db_port']+"/")
            if "db_name" in args:
                self.db = client[str(args["db_name"])]
            else:
                self.db = client["db"]

    def get_data(self, collection_name:str, key:str=None, query:dict=None, many:bool=False):
        collection = self.db[collection_name]
        if key is not None:
            dict = collection.find_one({"key":key})
            if dict is not None:
                return dict.get("data")
            else:
                return None
        elif query is not None:
            if many:
                return list(collection.find(query,{'_id': False}))
            else:
                return collection.find_one(query,{'_id': False})
        else:
            return list(collection.find({},{'_id': False}))

    def set_data(self, data, collection_name:str, key:str=None, many:bool=False):
        collection = self.db[collection_name]
        if key is not None:
            collection.insert_one({"key":key, "data":data})
        elif many:
            collection.insert_many(data)
        else:
            collection.insert_one(data)

    # Private things
    def set_private_param(self, name, value):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config['Private.params'][name] = value
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def get_private_param(self, name):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['Private.params'][name]

    # Public parameters
    def set_public_params(self, name, value ):
        self.set_data(value, collection_name="public_params", key=name)

    def get_public_params(self, name):
        return self.get_data(collection_name="public_params", key=name)

    ## Get voters
    def get_eligible_voters(self):
        return self.get_data(collection_name="eligible_voters")

    def set_cr_ids(self, cr_id):
        data = {"cr_id": str(cr_id)}
        self.set_data(data, collection_name="pseudo_ids")

    def get_cr_ids(self):
        data = self.get_data(collection_name="pseudo_ids")
        cr_ids = []
        for x in data:
            cr_ids.append(x["cr_id"])
        return cr_ids

    ##zk-SNARK
    def set_zkey_file_name(self, zkey_file_name):
        self.set_data(zkey_file_name, collection_name="public_params", key="zkey_file_name")

    def get_zkey_file_name(self):
        return self.get_data(collection_name="public_params", key="zkey_file_name")

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

    def does_ballot_already_exist(self, cr_id:str, cand_id:str, e_v:tuple[str,str]):
        result = self.get_data(collection_name="ballots", query = {"key": cr_id, "data."+cand_id+".vote.1":e_v[1]}, many=True)
        return len(result) != 0

    ## Final ballots
    def set_final_ballots(self,final_ballot):
        self.set_data(final_ballot,collection_name="final_ballots")

    def get_final_ballots(self):
        return self.get_data(collection_name="final_ballots")

    def set_pet_ballots(self, final_ballot):
        self.set_data(final_ballot,collection_name="final_results", key="final_pet_ballots")

    def get_pet_ballots(self):
        return self.get_data(collection_name="final_results", key="final_pet_ballots")

    ## Tally results
    def set_winner(self, highest_number, winner):
        self.set_data((highest_number, winner),collection_name="final_results", key="winner")

    def set_result(self, result):
        self.set_data(result,collection_name="final_results", key="result")

    def get_result(self):
        return self.get_data(collection_name="final_results", key="decrypted_results")

    def publish_decrypted_results(self, results_ballot_decrypted):
        self.set_data(results_ballot_decrypted,collection_name="final_results", key="decrypted_results")

    ## Functions for testing purposes
    # Get voters with their commitment randoms
    def get_voters(self):
        return self.get_data(collection_name="voters")

     ## Get voters votes
    def get_votes(self):
        return self.get_data(collection_name="votes")

    # Set voter with their commitment randoms
    def set_voter(self, name, cr_id, id, t_id):
        data = {"name": str(name), "cr_id": str(cr_id), "id": str(id), "t_id": str(t_id)}
        self.set_data(data, collection_name="voters")

    # Generate data for testing
    def generate_data(self, num_voters=4, num_candidates=2, re_vote_percent=1, null_vote_percent=1):
        fake = Faker()

        eligible_voters = [{"id": str(i), "name": fake.first_name()} for i in range(num_voters)]

        candidates = [{"id": str(i), "candidate": fake.name()} for i in range(num_candidates)]

        votes = []
        for i in range(num_voters):
            vote = {"voterId": str(i), "vote": random.choice(candidates)["id"]}
            votes.append(vote)

        num_re_votes = round(num_voters * re_vote_percent)

        for i in range(num_re_votes):
            re_vote_candidate = random.choice(candidates)["id"]
            while re_vote_candidate == votes[i]["vote"]:
                re_vote_candidate = random.choice(candidates)["id"]
            re_vote = {"voterId": str(i), "re-vote": re_vote_candidate}
            votes[i].update(re_vote)

        num_null_votes = round(num_voters * null_vote_percent)
        for i in range(num_null_votes):
            null_vote = {"voterId": str(i), "null-vote": 1}
            votes[i].update(null_vote)

        self.set_data(eligible_voters, collection_name="eligible_voters", many=True)
        self.set_data(candidates, collection_name="candidates", many=True)
        self.set_data(votes, collection_name="votes", many=True)