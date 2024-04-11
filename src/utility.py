from Crypto.Random.random import getrandbits
from Crypto.PublicKey import ElGamal
from Crypto.Math.Numbers import Integer
from Crypto.Math._IntegerCustom import IntegerCustom
from pyseidon.posiedon import Poseidon
import random
import math

# Used to allow use of circom. See: https://docs.circom.io/circom-language/basic-operators/#field-elements
GLOBAL_FIELD_P = 21888242871839275222246405745257275088548364400416034343698204186575808495617 # BN128
MAX_NUMBER_OF_VOTERS = 1000

class CouldNotDecrypt(Exception):
    """Raise for fai decryption"""


class Utility :
    @staticmethod
    def encrypt(m, r:int, g:int,p:int,y:int):
        c1 = pow(g.__int__(), r, p.__int__())
        c2 = (pow(g.__int__(), m, p.__int__()) * pow(y.__int__(), r, p.__int__())) % p.__int__()
        return c1, c2
    
    @staticmethod
    def decrypt(c1:int, c2:int, g:int, p:int, x:int):
        for i in range(MAX_NUMBER_OF_VOTERS):
            if pow(g,i,p) == (c2 * pow(c1, -1*x, p)) % p :
                return i
        raise CouldNotDecrypt("Decryption of message failed! Message not in allowed massage space.")
    
    @staticmethod
    def pet(a1, a2, m, g, p, y, x):
        r = random.randint(1, p-2)
        (b1,b2) = Utility.encrypt(m, r, g, p, y)
        (c1, c2) = (a1* (pow(b1,(p-2), p)) % p), (a2 * (pow(b2,(p-2), p)) % p) 
        # Math is from this paper: https://medium.com/@VitalikButerin/exploring-elliptic-curve-pairings-c73c1864e627
        # curve point division
        z = random.randint(1, p-2)  # Generate a random exponent z
        (c1, c2) = (pow(c1, z, p), pow(c2, z, p))  # Blind the ciphertext
        print("test:", (pow(c1, -1*x, p) * c2) % p)
        return  (pow(c1, -1*x, p) * c2) % p == 1


    @staticmethod
    def homomorphic_addition(x:list[str,str], y:list[str,str], p:int):
        (x1, x2) = x
        (y1, y2) = y
        return [str((int(x1) * int(y1)) % p), str((int(x2) * int(y2)) % p)]

    @staticmethod
    def commit(m):
        random = getrandbits(253) # OBS choose random length another way than "its shorter than the prime"
        commitment = Poseidon().hash([int(m),random])
        # Found commit within prime field GLOBAL_FIELD_P
        return (hex(commitment),random)

    @staticmethod
    def commit_verify(com,m,key):
        return com == hex(Poseidon().hash([m,key])) 
    
    def calc_tree_depth(num_voters):
        return math.ceil(math.log(num_voters,2))

    @staticmethod
    def generateElGamalKey(randfunc):
        """
        Taken from https://github.com/Legrandin/pycryptodome/blob/master/lib/Crypto/PublicKey/ElGamal.py#L34-L94
        Randomly generate a fresh, new ElGamal key.

        The key will be safe for use for both encryption and signature
        (although it should be used for **only one** purpose).

        Args:
        bits (int):
            Key length, or size (in bits) of the modulus *p*.
            The recommended value is 2048.
        randfunc (callable):
            Random number generation function; it should accept
            a single integer *N* and return a string of random
            *N* random bytes.

        Return:
            an :class:`ElGamalKey` object
        """

        obj=ElGamal.ElGamalKey()
        
        obj.p = IntegerCustom.from_bytes(GLOBAL_FIELD_P.to_bytes((GLOBAL_FIELD_P.bit_length() + 7) // 8, 'big'),byteorder="big")
        q = (obj.p - 1) >> 1

        # Generate generator g
        while 1:
            # Choose a square residue; it will generate a cyclic group of order q.
            obj.g = pow(Integer.random_range(min_inclusive=2,
                                        max_exclusive=obj.p,
                                        randfunc=randfunc), 2, obj.p)

            # We must avoid g=2 because of Bleichenbacher's attack described
            # in "Generating ElGamal signatures without knowning the secret key",
            # 1996
            if obj.g in (1, 2):
                continue

            # Discard g if it divides p-1 because of the attack described
            # in Note 11.67 (iii) in HAC
            if (obj.p - 1) % obj.g == 0:
                continue

            # g^{-1} must not divide p-1 because of Khadir's attack
            # described in "Conditions of the generator for forging ElGamal
            # signature", 2011
            ginv = obj.g.inverse(obj.p)
            if (obj.p - 1) % ginv == 0:
                continue

            # Found
            break

        # Generate private key x
        obj.x = Integer.random_range(min_inclusive=2,
                                    max_exclusive=obj.p-1,
                                    randfunc=randfunc)
        # Generate public key y
        obj.y = pow(obj.g, obj.x, obj.p)
        return obj
