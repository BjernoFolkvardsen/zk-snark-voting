from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

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