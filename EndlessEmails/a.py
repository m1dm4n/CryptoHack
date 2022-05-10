from itertools import combinations
from Crypto.Util.number import *
from sympy.ntheory.modular import crt
from gmpy2 import iroot
n = []
c = []
e = 3
with open("output.txt", 'r') as f:
    while True:
        s = f.readline()
        if s == "":
            break
        if s[0] == 'c':
            tmp = s.split(' ')[-1]
            c.append(int(tmp))

        if s[0] == 'n':
            tmp = s.split(' ')[-1]
            n.append(int(tmp))

print(c)
print(n)

tests = list(combinations(zip(c, n), 3))

for test in tests:
    N = 1
    for pair in test:
        N *= pair[1]
    m = 0
    for pair in test:
        m += (pair[0] * inverse(N//pair[1], pair[1]) * (N // pair[1]))
    m %= N

    flag, isTrue = iroot(m, 3)
    if isTrue:
        print(long_to_bytes(flag).decode())
