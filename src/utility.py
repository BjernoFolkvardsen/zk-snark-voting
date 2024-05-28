from Crypto.Random import get_random_bytes
from Crypto.Math.Numbers import Integer
from Crypto.Math.Primality import ( test_probable_prime, COMPOSITE )
from pyseidon.posiedon import Poseidon
import math

class CouldNotDecrypt(Exception):
    """Raise for fail decryption"""

class Utility :

    # Used to allow use of circom. See: https://docs.circom.io/circom-language/basic-operators/#field-elements
    GLOBAL_FIELD_P = 21888242871839275222246405745257275088548364400416034343698204186575808495617 # BN128
    MAX_NUMBER_OF_VOTERS = 0
    MTREE_DEPTH = 0

    @staticmethod
    def commit(m):
        random = Integer.random_range(min_inclusive=2, max_exclusive=Utility.GLOBAL_FIELD_P-1, randfunc=get_random_bytes)
        commitment = Poseidon().hash([int(m),random])
        return (hex(commitment),random)

    @staticmethod
    def commit_verify(com,m,key):
        return com == hex(Poseidon().hash([m,key])) 
    
    @staticmethod
    def set_max_voters_and_mtree_depth(num_voters):
        Utility.MAX_NUMBER_OF_VOTERS = num_voters
        Utility.MTREE_DEPTH = math.ceil(math.log(num_voters,2))

    # Generate an ElGamal key with N bits
    @staticmethod
    def generateElGamal(randfunc=get_random_bytes, p:int=None):
        """Taken from https://github.com/Legrandin/pycryptodome/blob/master/lib/Crypto/PublicKey/ElGamal.py#L34-L94
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

        obj=ElGamal(randfunc)

        # Generate a safe prime p
        # See Algorithm 4.86 in Handbook of Applied Cryptography
        if p is None:
            obj.p = Integer(Utility.GLOBAL_FIELD_P)
        else:
            obj.p = Integer(p)

        # Generate generator g
        while 1:
            # Choose a square residue; it will generate a cyclic group of order q.
            obj.g = pow(Integer.random_range(min_inclusive=2, max_exclusive=obj.p-1, randfunc=randfunc), 2, obj.p)

            # We must avoid g=2 because of Bleichenbacher's attack described
            # in "Generating ElGamal signatures without knowning the secret key",
            # 1996
            if obj.g in (1, 2):
                continue

            # Discard g if it divides p-1 because of the attack described
            # in Note 11.67 (iii) in HAC
            if (obj.p - Integer(1)) % obj.g == Integer(0):
                continue

            # g^{-1} must not divide p-1 because of Khadir's attack
            # described in "Conditions of the generator for forging ElGamal
            # signature", 2011
            ginv = obj.g.inverse(obj.p)
            if (obj.p - Integer(1)) % ginv == Integer(0):
                continue

            # Found
            break

        # Generate private key x
        obj.x = Integer.random_range(min_inclusive=2, max_exclusive=obj.p-1, randfunc=randfunc)

        # Generate public key y
        obj.y = pow(obj.g, obj.x, obj.p)
        return obj

    @staticmethod
    def constructElGamal(tup, randfunc=get_random_bytes):
        """Taken from https://github.com/Legrandin/pycryptodome/blob/master/lib/Crypto/PublicKey/ElGamal.py
        Construct an ElGamal from a tuple of valid ElGamal components.

        The modulus *p* must be a prime.
        The following conditions must apply:

        .. math::

            \begin{align}
            &1 < g < p-1 \\
            &g^{p-1} = 1 \text{ mod } 1 \\
            &1 < x < p-1 \\
            &g^x = y \text{ mod } p
            \end{align}

        Args:
        tup (tuple):
            A tuple with either 3 or 4 integers,
            in the following order:

            1. Modulus (*p*).
            2. Generator (*g*).
            3. Public key (*y*).
            4. Private key (*x*). Optional.

        Raises:
            ValueError: when the key being imported fails the most basic ElGamal validity checks.

        Returns:
            an :class:`ElGamal` object
        """

        obj=ElGamal(randfunc)
        if len(tup) not in [3,4]:
            raise ValueError('argument for construct() wrong length')
        for i in range(len(tup)):
            field = obj._keydata[i]
            setattr(obj, field, Integer(tup[i]))

        fmt_error = test_probable_prime(obj.p) == COMPOSITE
        fmt_error |= obj.g<=1 or obj.g>=obj.p
        fmt_error |= pow(obj.g, obj.p-1, obj.p)!=1
        fmt_error |= obj.y<1 or obj.y>=obj.p
        if len(tup)==4:
            fmt_error |= obj.x<=1 or obj.x>=obj.p
            fmt_error |= pow(obj.g, obj.x, obj.p)!=obj.y

        if fmt_error:
            raise ValueError("Invalid ElGamal key components")

        return obj

class ElGamal():

    p: Integer = None
    g: Integer = None
    x: Integer = None
    y: Integer = None
    randfunc:callable = None

    #: Dictionary of ElGamal parameters.
    #:
    #: A public key will only have the following entries:
    #:
    #:  - **y**, the public key.
    #:  - **g**, the generator.
    #:  - **p**, the modulus.
    #:
    #: A private key will also have:
    #:
    #:  - **x**, the private key.
    _keydata=['p', 'g', 'y', 'x']

    def __init__(self, randfunc=get_random_bytes):
        self.randfunc = randfunc

    def can_decrypt(self):
        return self.x is not None

    def homomorphic_addition(self, e1:tuple[int,int], e2:tuple[int,int]):
        (x1, x2) = e1
        (y1, y2) = e2
        c1 = (Integer(x1) * Integer(y1)) % self.p
        c2 = (Integer(x2) * Integer(y2)) % self.p
        return int(c1), int(c2)

    def encrypt(self, m:int):
        m = Integer(m)
        r = Integer.random_range(min_inclusive=2, max_exclusive=self.p-1, randfunc=self.randfunc)
        c1 = pow(self.g, r, self.p)
        c2 = (pow(self.g, m, self.p) * pow(self.y, r, self.p)) % self.p
        return int(c1), int(c2), int(r)

    def decrypt(self, c1:int, c2:int):
        if not self.can_decrypt():
            raise CouldNotDecrypt("Can not decrypt without private key")
        # Brute force decryption of possible positive messages
        for i in range(Utility.MAX_NUMBER_OF_VOTERS):
            if pow(self.g,Integer(i),self.p) == Integer(c2 * pow(c1, -1*int(self.x), int(self.p))) % self.p :
                return i
        # Brute force decryption of possible negative messages
        for i in range(int(self.p)-10,int(self.p)-1):
            if pow(self.g,Integer(i),self.p) == Integer(c2 * pow(c1, -1*int(self.x), int(self.p))) % self.p :
                return i
        raise CouldNotDecrypt("Decryption of message failed! Message not in allowed massage space.")

    def pet(self, a1:int, a2:int, m:int):
        if not self.can_decrypt():
            raise CouldNotDecrypt("Can not decrypt without private key")
        a1 = Integer(a1)
        a2 = Integer(a2)
        (b1,b2,r) = self.encrypt(m)
        b1 = Integer(b1)
        b2 = Integer(b2)
        (c1, c2) = (a1* (pow(b1,(self.p-2), self.p)) % self.p), (a2 * (pow(b2,(self.p-2), self.p)) % self.p) 
        # Math is from this paper: https://medium.com/@VitalikButerin/exploring-elliptic-curve-pairings-c73c1864e627
        # curve point division
        z = Integer.random_range(min_inclusive=2, max_exclusive=self.p-2, randfunc=self.randfunc)  # Generate a random exponent z
        (c1, c2) = (pow(c1, z, self.p), pow(c2, z, self.p))  # Blind the ciphertext
        return (int(c2) * pow(int(c1), -1*int(self.x), int(self.p))) % int(self.p) == 1

    def make_proof_of_decryption():
        pass

    def verify_proof_of_decryption():
        pass
