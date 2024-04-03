from src.bulletinboard import BullitinBoard
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
from Crypto.PublicKey import ElGamal
from src.utility import Utility
import pymongo

if __name__ == "__main__":
    # Clear DB before running
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    client.drop_database("db")
    ## Normal Protocol Flow
    setup_manager = SetupManager()
    setup_manager.use_dummy_data()
    registration_manager = VoterRegistration()
    registration_manager.registration()
    voting_manager = Voting()
    voting_manager.voting()
    tally_manager = Tally()
    tally_manager.tally()

    ## ZK-SNARK testing flow
    # setup_manager = SetupManager()
    # setup_manager.setup_zk_SNARK()
    # voting_manager = Voting()
    # voting_manager.zk_snark()

    ## Test MongoDB
    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    # db = client["database"]
    # collection = db["public_params"]
    # mydict = { "name": "John", "address": "Highway 37" }
    # x = collection.insert_one(mydict)

    # y = collection.find_one()

    # print(y)
