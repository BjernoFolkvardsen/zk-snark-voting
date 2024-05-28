from src.bulletinboard import BullitinBoard
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
import pymongo
import configparser

def run_election(num_voters,num_candidates,re_vote_percent=0,null_vote_percent=0):
    db_name = "db_"+str(num_voters)+"_"+str(num_candidates)
    # Clear DB before running
    config = configparser.ConfigParser()
    config.read('config.ini')
    client = pymongo.MongoClient("mongodb://"+config['Database']['db_host']+":"+config['Database']['db_port']+"/")
    client.drop_database(db_name)

    bb = BullitinBoard(args={"db_name": db_name})
    bb.generate_data(num_voters=num_voters, num_candidates=num_candidates, re_vote_percent=re_vote_percent, null_vote_percent=null_vote_percent)

    ## Normal Protocol Flow
    setup_manager = SetupManager(bb)
    registration_manager = VoterRegistration(bb)
    registration_manager.registration()
    voting_manager = Voting(bb)
    voting_manager.voting()
    tally_manager = Tally(bb)
    tally_manager.tally()

if __name__ == "__main__":
    run_election(10, 3, 0.2, 0.2)
