from src.bulletinboard import BullitinBoard
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
from src.verification import Verification
import pymongo
import time
import csv

def run_election(num_voters,num_candidates,benchmark,re_vote_percent=0,null_vote_percent=0):
    benchmark_data = {"num_voters": num_voters, "num_candidates": num_candidates, "start_time": 0, "setup_time": 0, "registration_time": 0, "voting_time": 0, "tally_time": 0, "end_time": 0, "setup_time_taken_sec": 0, "setup_time_taken_min": 0, "registration_time_taken_sec": 0, "registration_time_taken_min": 0, "voting_time_taken_sec": 0, "voting_time_taken_min": 0, "tally_time_taken_sec": 0, "tally_time_taken_min": 0, "total_time_taken_sec": 0, "total_time_taken_min": 0}
    db_name = "db_"+str(num_voters)+"_"+str(num_candidates)
    # Clear DB before running
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    client.drop_database(db_name)

    bb = BullitinBoard(env="local", args={"type": "mongo_db", "db_name": db_name})
    bb.generate_data(num_voters=num_voters, num_candidates=num_candidates, re_vote_percent=re_vote_percent, null_vote_percent=null_vote_percent)

    start_time = time.time()
    ## Normal Protocol Flow
    setup_manager = SetupManager(bb)
    setup_time = time.time()
    registration_manager = VoterRegistration(bb)
    registration_manager.registration()
    registration_time = time.time()
    voting_manager = Voting(bb)
    voting_manager.voting()
    voting_time = time.time()
    tally_manager = Tally(bb)
    tally_manager.tally()
    tally_time = time.time()
    # verfication_manager = Verification(bb)
    # verfication_manager.verify_tally()

    end_time = time.time()
    benchmark_data["start_time"] = start_time
    benchmark_data["setup_time"] = setup_time
    benchmark_data["registration_time"] = registration_time
    benchmark_data["voting_time"] = voting_time
    benchmark_data["tally_time"] = tally_time
    benchmark_data["end_time"] = end_time
    benchmark_data["setup_time_taken_sec"] = setup_time - start_time
    benchmark_data["setup_time_taken_min"] = (setup_time - start_time)/60
    benchmark_data["registration_time_taken_sec"] = registration_time - setup_time
    benchmark_data["registration_time_taken_min"] = (registration_time - setup_time)/60
    benchmark_data["voting_time_taken_sec"] = voting_time - registration_time
    benchmark_data["voting_time_taken_min"] = (voting_time - registration_time)/60
    benchmark_data["tally_time_taken_sec"] = tally_time - voting_time
    benchmark_data["tally_time_taken_min"] = (tally_time - voting_time)/60
    benchmark_data["total_time_taken_sec"] = end_time - start_time
    benchmark_data["total_time_taken_min"] = (end_time - start_time)/60
    benchmark.append(benchmark_data)
    return benchmark

if __name__ == "__main__":
    keys_list = ["num_voters", "num_candidates", "start_time", "setup_time", "registration_time", "voting_time", "tally_time", "end_time", "setup_time_taken_sec", "setup_time_taken_min", "registration_time_taken_sec", "registration_time_taken_min", "voting_time_taken_sec", "voting_time_taken_min", "tally_time_taken_sec", "tally_time_taken_min", "total_time_taken_sec", "total_time_taken_min"]

    benchmark = []
    for num_voters in [5,10]:
        for num_candidates in [20,30,40]:
            benchmark = run_election(num_voters, num_candidates, benchmark)
            with open( str(num_voters)+'_'+str(num_candidates)+'_benchmark_0_revote_and_0_nullvote.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames = keys_list)
                writer.writeheader()
                writer.writerows(benchmark)

        # Københavns Storkreds valg 2022, 549.738 voters, 131 candidates
        # benchmark = run_election(549738, 131, benchmark)

    with open('final_benchmark_0_revote_and_0_nullvote.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = keys_list)
        writer.writeheader()
        writer.writerows(benchmark)
