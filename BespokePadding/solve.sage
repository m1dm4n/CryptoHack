from sage.all import *
from Crypto.Util.number import long_to_bytes

from z3 import 
a1, b1 = res1['padding']
a2, b2 = res2['padding']
N = res1['modulus']
c1 = res1['encrypted_flag']
c2 = res2['encrypted_flag']
e = 11


def PolynomialModulusGCD(a, b):
    if(b == 0):
        return a.monic()
    else:
        return PolynomialModulusGCD(b, a % b)


Z = Zmod(N)
P. < x > = PolynomialRing(Z)

f1 = (a1*x + b1) ^ e - c1
f2 = (a2*x + b2) ^ e - c2

print(long_to_bytes(int(Z(-PolynomialModulusGCD(f1, f2).coefficients()[0]))))

