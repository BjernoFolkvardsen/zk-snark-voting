from Crypto.Math.Numbers import Integer
from Crypto.Util.number import inverse
from Crypto.Random import get_random_bytes
import random

class ElgamalTest():

    p: Integer = None
    g: Integer = None
    x: Integer = None
    y: Integer = None

    def __init__(self):
        self.p = Integer(21888242871839275222246405745257275088548364400416034343698204186575808495617)
        self.g = Integer(14838620077630144943153316308768573559412592218749391403448395293294316333073)
        self.x = Integer(11291533944448431386060436621554679012591433578867632192713483442606182456262)
        self.y = Integer(9691526149856253739956789831891759414095231188027135341546631343194170947826)

    def homomorphic_addition(self, e1, e2):
        (x1, x2) = e1
        (y1, y2) = e2
        c1 = (x1 * y1) % self.p
        c2 = (x2 * y2) % self.p
        return c1, c2

    def encrypt(self, m:int, r:Integer):
        m = Integer(m)
        r = Integer(r)
        c1 = pow(self.g, r, self.p)
        c2 = (pow(self.g, m, self.p) * pow(self.y, r, self.p)) % self.p
        return c1, c2

    def decrypt(self,c1:Integer, c2:Integer):
        positive_range = self.decrypt_dlog_loop(1,100, c1, c2)
        negative_range = self.decrypt_dlog_loop(int(self.p)-100,int(self.p)-1, c1, c2)
        if positive_range:
            return positive_range
        elif negative_range:
            return negative_range
        raise Exception("Decryption of message failed! Message not in allowed massage space.")

    def decrypt_dlog_loop(self, range_from, range_to, c1, c2):
        for i in range(range_from, range_to):
            dlog = pow(self.g,i,self.p)
            c1_pow = pow(c1,self.x,self.p)
            inverse_pow = inverse(int(c1_pow),int(self.p))
            # if pow(self.g,i,self.p) == (c2 * pow(c1, -1*self.x, self.p)) % self.p :
            if dlog == (c2 * Integer(inverse_pow)) % self.p :
                return i
        return False

if __name__ == "__main__":
    print()

    ## Elgamal testing flow
    elgamal = ElgamalTest()
    q = (int(elgamal.p) - 1) >> 1
    print("q: ", q)
    p_minus_1 = int(elgamal.p)-2
    m = Integer(p_minus_1)
    r = Integer.random_range(min_inclusive=2, max_exclusive=int(elgamal.p)-1, randfunc=get_random_bytes)
    e1 = elgamal.encrypt(m, r, True)
    print("Encrypted message: ", e1)
    print()
    m = Integer(p_minus_1)
    r = Integer.random_range(min_inclusive=2, max_exclusive=int(elgamal.p)-1, randfunc=get_random_bytes)
    e2 = elgamal.encrypt(m, r,True)
    print("Encrypted message: ", e2)
    print()
    e3 = elgamal.homomorphic_addition(e1, e2)
    print("Homomorphic addition: ", e3)
    print()
    m = Integer(6)
    r = Integer.random_range(min_inclusive=2, max_exclusive=int(elgamal.p)-1, randfunc=get_random_bytes)
    e4 = elgamal.encrypt(m, r,True)
    print("Encrypted message: ", e4)
    print()
    e5 = elgamal.homomorphic_addition(e3, e4)
    print("Homomorphic addition: ", e5)
    print()
    m = elgamal.decrypt(e5[0], e5[1],True)
    print("Decrypted message: ",m)
    print()
