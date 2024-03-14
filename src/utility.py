from Crypto.Random.random import getrandbits
from Crypto.Hash import SHA256
from Crypto.PublicKey import ElGamal
from Crypto.Math.Numbers import Integer
from Crypto.Math._IntegerCustom import IntegerCustom
from Crypto.Hash import SHA224
from math import log
from pyseidon.posiedon import Poseidon
import inspect


# Used to allow use of circom. See: https://docs.circom.io/circom-language/basic-operators/#field-elements
GLOBAL_FIELD_P = 21888242871839275222246405745257275088548364400416034343698204186575808495617 # BN128
# GLOBAL_FIELD_P = 115792089210356248762697446949407573530086143415290314195533631308867097853951 # SECQ256R1

class CouldNotDecrypt(Exception):
    """Raise for fai decryption"""


class Utility :
    @staticmethod
    def encrypt(m, r, g,p,y):
        c1 = pow(g.__int__(), r, p.__int__())
        c2 = (pow(g.__int__(), m, p.__int__()) * pow(y.__int__(), r, p.__int__())) % p.__int__()
        return c1, c2
    
    @staticmethod
    def decrypt(c1, c2,g,p,x):
        for i in range(500):
            if pow(g.__int__(),i,p.__int__()) == (c2 * pow(c1, -1*x.__int__(), p.__int__())) % p.__int__() :
                return i
        raise CouldNotDecrypt("Decryption of message failed! Message not in allowed massage space.")

    @staticmethod
    def homomorphic_addition(x, y, p):
        (x1, x2) = x
        (y1, y2) = y
        return ((x1.__int__() * y1.__int__()) % p.__int__(), (x2.__int__() * y2.__int__()) % p.__int__())

    @staticmethod
    def commit(m):
        random = getrandbits(253) # OBS choose random length another way than "its shorter than the prime"
        commitment = Poseidon().hash([int(m),random])
        # Found commit within prime field GLOBAL_FIELD_P
        return (hex(commitment),random)

    @staticmethod
    def commit_verify(com,m,key):
        return com == hex(Poseidon().hash([m,key])) 

    @staticmethod
    def generateElGamalKey(bits, randfunc):
        """Randomly generate a fresh, new ElGamal key.

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

    @staticmethod
    def poseidon_hash(byte_val1: bytes, byte_val2: bytes) -> bytes:
        #(byte_val1,byte_val2) = inputs
        int_val1 = int.from_bytes(byte_val1, 'big')
        int_val2 = int.from_bytes(byte_val2, 'big')
        int_hash = Poseidon().hash([int_val1,int_val2])
        return int_hash.to_bytes(Utility.bytes_needed(int_hash), "big")
    

    @staticmethod
    def bytes_needed(n: int) -> int:
        if n == 0:
            return 1
        return int(log(n, 256)) + 1