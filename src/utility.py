from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.PublicKey import ElGamal
from Crypto.Math.Numbers import Integer
from Crypto.Math._IntegerCustom import IntegerCustom


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
    def SHA_commit(m):
        random = get_random_bytes(256)
        commitment = SHA256.new(random+m)
        return (commitment.hexdigest(),random)

    @staticmethod
    def SHA_commit_verify(com,m,key):
        return com == SHA256.new(key+m).hexdigest()

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

        # Prime set after circom prime: https://docs.circom.io/circom-language/basic-operators/#field-elements
        primeInt = 21888242871839275222246405745257275088548364400416034343698204186575808495617
        obj.p = IntegerCustom.from_bytes(primeInt.to_bytes((primeInt.bit_length() + 7) // 8, 'big'),byteorder="big")
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