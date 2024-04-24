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
    for num_voters in [3, 5]: #, 10, 25, 50]: #, 100, 500, 1000, 5000, 10000, 50000, 100000]:
        for num_candidates in [2, 3]: #, 5, 10]:
            benchmark_data = {"num_voters": num_voters, "num_candidates": num_candidates, "start_time": 0, "end_time": 0, "time_taken_sec": 0, "time_taken_min": 0}
            db_name = "db_"+str(num_voters)+"_"+str(num_candidates)
            # Clear DB before running
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            client.drop_database(db_name)

            bb = BullitinBoard(env="local", args={"type": "mongo_db", "db_name": db_name})

            start_time = time.time()
            ## Normal Protocol Flow
            setup_manager = SetupManager(bb, dummy_data={"num_voters": num_voters, "num_candidates": num_candidates})
            registration_manager = VoterRegistration(bb)
            registration_manager.registration()
            voting_manager = Voting(bb)
            voting_manager.voting()
            tally_manager = Tally(bb)
            tally_manager.tally()
            verfication_manager = Verification(bb)
            verfication_manager.verify_tally()

            end_time = time.time()
            benchmark_data["start_time"] = start_time
            benchmark_data["end_time"] = end_time
            benchmark_data["time_taken_sec"] = end_time - start_time
            benchmark_data["time_taken_min"] = (end_time - start_time)/60
            benchmark.append(benchmark_data)

    table = PrettyTable()
    table.field_names = ["Number of voters", "Number of candidates", "Time taken (sec)", "Time taken (min)"]
    table.field_names = ["Number of voters", "Number of candidates", "Time taken (sec)", "Time taken (min)"]
    for row in benchmark:
        table.add_row([row["num_voters"], row["num_candidates"], row["time_taken_sec"], row["time_taken_min"]])
    print(table)

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
