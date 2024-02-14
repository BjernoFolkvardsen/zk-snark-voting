from src.bulletinboard import BullitinBoard
from src.setup import SetupManager
from src.registration import VoterRegistration
from src.voting import Voting
from src.tally import Tally
from Crypto.PublicKey import ElGamal
import random

# # encryption function
# def encrypt(m, r, exponential=False):
#     c1 = pow(g, r, p)
#     if exponential is True:
#         c2 = (pow(g, m, p) * pow(y, r, p)) % p
#     else:
#         c2 = (m * pow(y, r, p)) % p
#     return c1, c2

# # decryption function


# def decrypt(c1, c2):
#     return (c2 * pow(c1, -1*x, p)) % p

if __name__ == "__main__":
    # bulletinboard = BullitinBoard()
    # bulletinboard.setup_bulletin_board()
    # setup_manager = SetupManager()
    # setup_manager.setup()
    # registration_manager = VoterRegistration()
    # registration_manager.registration()
    # voting_manager = Voting()
    # voting_manager.voting()
    # tally_manager = Tally()
    # tally_manager.tally()

    print()
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

    # encryption function
    def encrypt(m, r, exponential=False):
        c1 = pow(g.__int__(), r, p.__int__())
        if exponential is True:
            c2 = (pow(g.__int__(), m, p.__int__()) * pow(y.__int__(), r, p.__int__())) % p.__int__()
        else:
            c2 = (m * pow(y.__int__(), r, p.__int__())) % p.__int__()
        return c1, c2

    # decryption function


    def decrypt(c1, c2):
        return (c2 / pow(c1, x.__int__(), p.__int__())) % p.__int__()

    # key generation
    p = 109506524947787965089385963978987843743802988013634808802997207213573066621303
    g = random.randint(1, p-2)

    x = 61200906519625114184228504320966203849029219953630973958644618004107006916619  # private key
    y = pow(g, x, p)                            # public key

    # print(x, y)
    print("p: ", p,p.__int__())
    print()

    # additive homomorphic
    m1 = 9
    m2 = 11
    r1 = random.randint(1, p-1)
    r2 = random.randint(1, p-1)
    m1_encrypted = encrypt(m1, r1, exponential=True)
    m2_encrypted = encrypt(m2, r2, exponential=True)

    z1, z2 = encrypt(m1, r1)
    m1_decrypted = decrypt(z1,z2)
    print("m1_decrypted: ", m1_decrypted)
    print()

    h1,h2 = encrypt(m1+m2, r1+r2, exponential=True)
    h3, h4 = m1_encrypted[0]*m2_encrypted[0] % p.__int__(), m1_encrypted[1]*m2_encrypted[1] % p.__int__()

    print("(h1,h2),(h3,h4): ",(h1,h2),(h3,h4))
    print()
    decrypted1 = decrypt(h1,h2)
    decrypted2 = decrypt(h3,h4)
    print("decrypted 1 and 2: ",decrypted1,decrypted2)

