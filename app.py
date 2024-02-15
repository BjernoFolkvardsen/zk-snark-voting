from src.bulletinboard import BullitinBoard
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
from Crypto.PublicKey import ElGamal
from src.utility import Utility
import random


if __name__ == "__main__":
    BullitinBoard.setup_bulletin_board()
    setup_manager = SetupManager()
    setup_manager.setup()
    registration_manager = VoterRegistration()
    registration_manager.registration()
    voting_manager = Voting()
    voting_manager.voting()
    tally_manager = Tally()
    tally_manager.tally()

    # print()
    # print()
    # print()
    # (y,x,p,g) = setup_manager.setup_elgamal(256)
    # ElgamalKeyObject = ElGamal.construct((p,g,pk,sk))
    # (x1,x2) = encrypt(g,p,2,random.randint(1, p-2),pk)
    # print("e_v1: ", (x1,x2))
    # (y1,y2) = encrypt(g,p,3,random.randint(1, p-2),pk)
    # print("e_v2: ", (y1,y2))
    # (z1,z2) = (((x1.__int__() * y1.__int__()) % p.__int__()), ((x2.__int__() * y2.__int__()) % p.__int__()))
    # print("e_v: ", (z1,z2))
    # v = decrypt(z1.__int__(),z2.__int__(),sk.__int__(), p.__int__())
    # print("v: ", v)


    # print(x, y)
    # print("p: ", p,p.__int__())
    # print()

    # additive homomorphic
    # m1 = 2
    # m2 = 3
    # r1 = random.randint(1, p-1)
    # r2 = random.randint(1, p-1)
    # m1_encrypted = Utility.encrypt(m1, r1, g,p,y)
    # m2_encrypted = Utility.encrypt(m2, r2,g,p,y)

    # z1, z2 = Utility.encrypt(m1, r1, g,p,y)
    # m1_decrypted = Utility.decrypt(z1,z2,g,p,x)
    # print("m1_decrypted: ", m1_decrypted)
    # print()

    # h1,h2 = Utility.encrypt(m1+m2, r1+r2, g, p, y)
    # h3, h4 = m1_encrypted[0]*m2_encrypted[0] % p.__int__(), m1_encrypted[1]*m2_encrypted[1] % p.__int__()

    # print("(h1,h2),(h3,h4): ",(h1,h2),(h3,h4))
    # print()
    # decrypted1 = Utility.decrypt(h1,h2,g,p,x)
    # decrypted2 = Utility.decrypt(h3,h4,g,p,x)
    # print("decrypted 1 and 2: ",decrypted1,decrypted2)

