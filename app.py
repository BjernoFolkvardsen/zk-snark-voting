from src.bulletinboard import BullitinBoard
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
from prettytable import PrettyTable
from src.verification import Verification
import pymongo
import time
import io
import csv

def run_election(num_voters,num_candidates,benchmark):
    benchmark_data = {"num_voters": num_voters, "num_candidates": num_candidates, "start_time": 0, "setup_time": 0, "registration_time": 0, "voting_time": 0, "tally_time": 0, "end_time": 0, "setup_time_taken_sec": 0, "setup_time_taken_min": 0, "registration_time_taken_sec": 0, "registration_time_taken_min": 0, "voting_time_taken_sec": 0, "voting_time_taken_min": 0, "tally_time_taken_sec": 0, "tally_time_taken_min": 0, "total_time_taken_sec": 0, "total_time_taken_min": 0}
    db_name = "db_"+str(num_voters)+"_"+str(num_candidates)
    # Clear DB before running
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    client.drop_database(db_name)

    bb = BullitinBoard(env="local", args={"type": "mongo_db", "db_name": db_name})

    start_time = time.time()
    ## Normal Protocol Flow
    setup_manager = SetupManager(bb, dummy_data={"num_voters": num_voters, "num_candidates": num_candidates})
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

    # benchmark = {"divider":[False,True,False,True,False,False],"num_voters": [4,'',5, '',6, ''],"num_candidates": [2,3, 2,3, 2,3], "time_taken_sec": [10, 20, 30, 40, 50, 60], "time_taken_min": [0.1666667, 0.3333333, 0.5, 0.6666667, 0.8333333, 1]}
    # # benchmark_headers = ["Number of voters", "Number of candidates", "Time (sec)", "Time (min)"]
    # table = PrettyTable()
    # table.title = "Benchmark Results"
    # table.field_names = ["Number of voters", "Number of candidates"]
    # table.add_row([4, 2])
    # table.add_row(['', 3], divider=True)
    # table.add_row([5, 2])
    # table.add_row(['', 3], divider=True)
    # table.add_row([10, 2])
    # table.add_row(['', 3])

    # table_full = PrettyTable()
    # table_full.title = "Full"
    # table_full.field_names = ["sec.", "min."]
    # table_full.add_row([10, 0.1666667])
    # table_full.add_row([60, 1], divider=True)
    # table_full.add_row([10, 0.1666667])
    # table_full.add_row([60, 1], divider=True)
    # table_full.add_row([10, 0.1666667])
    # table_full.add_row([60, 1])

    # table_setup = PrettyTable()
    # table_setup.title = "Setup"
    # table_setup.field_names = ["sec.", "min."]
    # table_setup.add_row([10, 0.1666667])
    # table_setup.add_row([60, 1], divider=True)
    # table_setup.add_row([10, 0.1666667])
    # table_setup.add_row([60, 1], divider=True)
    # table_setup.add_row([10, 0.1666667])
    # table_setup.add_row([60, 1])


    # table_registration = PrettyTable()
    # table_registration.title = "Registration"
    # table_registration.field_names = ["sec.", "min."]
    # table_registration.add_row([10, 0.1666667])
    # table_registration.add_row([60, 1], divider=True)
    # table_registration.add_row([10, 0.1666667])
    # table_registration.add_row([60, 1], divider=True)
    # table_registration.add_row([10, 0.1666667])
    # table_registration.add_row([60, 1])

    # table_voting = PrettyTable()
    # table_voting.title = "Voting"
    # table_voting.field_names = ["sec.", "min."]
    # table_voting.add_row([10, 0.1666667])
    # table_voting.add_row([60, 1], divider=True)
    # table_voting.add_row([10, 0.1666667])
    # table_voting.add_row([60, 1], divider=True)
    # table_voting.add_row([10, 0.1666667])
    # table_voting.add_row([60, 1])

    # table_tally = PrettyTable()
    # table_tally.title = "Tally"
    # table_tally.field_names = ["sec.", "min."]
    # table_tally.add_row([10, 0.1666667])
    # table_tally.add_row([60, 1], divider=True)
    # table_tally.add_row([10, 0.1666667])
    # table_tally.add_row([60, 1], divider=True)
    # table_tally.add_row([10, 0.1666667])
    # table_tally.add_row([60, 1])

    # o1 = io.StringIO(table.get_string())
    # o2 = io.StringIO(table_full.get_string())
    # o3 = io.StringIO(table_setup.get_string())
    # o4 = io.StringIO(table_registration.get_string())
    # o5 = io.StringIO(table_voting.get_string())
    # o6 = io.StringIO(table_tally.get_string())

    # for s1,s2,s3,s4,s5,s6 in zip(o1,o2,o3,o4,o5,o6):
    #     print(s1.strip()[:-1] + s2.strip()[:-1] + s3.strip()[:-1] + s4.strip()[:-1] + s5.strip()[:-1] + s6.strip() + "\n")


    # table1.add_row(['','',"sec.", "min.","sec.", "min.","sec.", "min.","sec.", "min.","sec.", "min.","sec.", "min."], divider=True)
    # for i in range(len(benchmark["num_voters"])):
    #     table.add_row([benchmark["num_voters"][i], benchmark["num_candidates"][i], benchmark["time_taken_sec"][i], benchmark["time_taken_min"][i]], divider=benchmark["divider"][i])
    # table.add_column("Number of voters", [4,'',5, '',6, ''])
    # table.add_column("Number of candidates", [2,3, 2,3, 2,3])
    # table.add_column("Time (sec)", [10, 20, 30, 40, 50, 60])
    # table.add_column("Time (min)", [0.1666667, 0.3333333, 0.5, 0.6666667, 0.8333333, 1])
    # print(table, table_full, table_setup, table_registration, table_voting, table_tally)
    # raise Exception("Please run the code in the following order: python3 app.py")
    benchmark = []
    for num_voters in [5, 10, 100, 1000, 10000, 100000, 1000000]:
        for num_candidates in [2, 5, 10, 50, 100, 150 ]:
           benchmark = run_election(num_voters, num_candidates, benchmark)

    # Københavns Storkreds valg 2022, 549.738 voters, 131 candidates
    benchmark = run_election(549738, 131, benchmark)

    # table = PrettyTable()
    # table.field_names = ["Number of voters", "Number of candidates", "Time taken (sec)", "Time taken (min)"]
    # table.field_names = ["Number of voters", "Number of candidates", "Time taken (sec)", "Time taken (min)"]
    # for row in benchmark:
    #     table.add_row([row["num_voters"], row["num_candidates"], row["time_taken_sec"], row["time_taken_min"]])
    # print(table)

    keys_list = ["num_voters", "num_candidates", "start_time", "setup_time", "registration_time", "voting_time", "tally_time", "end_time", "setup_time_taken_sec", "setup_time_taken_min", "registration_time_taken_sec", "registration_time_taken_min", "voting_time_taken_sec", "voting_time_taken_min", "tally_time_taken_sec", "tally_time_taken_min", "total_time_taken_sec", "total_time_taken_min"]
    with open('benchmark_0_revote_and_0_nullvote.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = keys_list)

        writer.writeheader()
        writer.writerows(benchmark)

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
