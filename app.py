from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
import pymongo
import time

if __name__ == "__main__":

    benchmark = []
    for num_voters in [5, 10]: # 50, 100, 500, 1000, 5000, 10000, 50000, 100000]:
        for num_candidates in [2, 5]:
            benchmark_data = {"num_voters": num_voters, "num_candidates": num_candidates, "start_time": 0, "end_time": 0, "time_taken_sec": 0, "time_taken_min": 0}
            # Clear DB before running
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            client.drop_database("db")

            start_time = time.time()
            ## Normal Protocol Flow
            setup_manager = SetupManager({"num_voters": num_voters, "num_candidates": num_candidates})
            registration_manager = VoterRegistration()
            registration_manager.registration()
            voting_manager = Voting()
            voting_manager.voting()
            tally_manager = Tally()
            tally_manager.tally()

            end_time = time.time()
            benchmark_data["start_time"] = start_time
            benchmark_data["end_time"] = end_time
            benchmark_data["time_taken_sec"] = end_time - start_time
            benchmark_data["time_taken_min"] = (end_time - start_time)/60
            benchmark.append(benchmark_data)
    print(benchmark)

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
