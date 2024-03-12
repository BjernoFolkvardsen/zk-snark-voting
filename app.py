from src.bulletinboard import BullitinBoard
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
from Crypto.PublicKey import ElGamal
from src.utility import Utility
import random

from pyseidon.posiedon import Poseidon

if __name__ == "__main__":
    # BullitinBoard.setup_bulletin_board()
    # setup_manager = SetupManager()
    # setup_manager.setup_zk_SNARK()
    # registration_manager = VoterRegistration()
    # registration_manager.registration()
    # voting_manager = Voting()
    # voting_manager.voting()
    # voting_manager.zk_snark()
    # tally_manager = Tally()
    # tally_manager.tally()

    hash = Poseidon().hash([5,4])
    print(hash)