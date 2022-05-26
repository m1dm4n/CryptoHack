from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from itertools import combinations
from Crypto.Cipher import PKCS1_OAEP


def decryptfile(key, filename):
    msg = bytes.fromhex(open(filename, "r").read())
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(msg)
    print(plaintext)


for i in list(combinations(list(range(1, 51)), 2)):
    print(f"[+] {str(i[0])}.pem + str{i[1]}.pem: ", end="")
    data1 = open(f"{str(i[0])}.pem", "r").read()
    key1 = RSA.importKey(data1)
    data2 = open(f"{str(i[1])}.pem", "r").read()
    key2 = RSA.importKey(data2)

    if (key1.n == key2.n):
        print("Not Found")
        continue
    p = GCD(key1.n, key2.n)
    print("Found a gcd " + str(p) if p > 1 else "Not Found")
    if p > 1:
        privkey1 = RSA.construct(
            [key1.n, key1.e, inverse(key1.e, (p - 1) * ((key1.n // p) - 1))])
        decryptfile(privkey1, f"{str(i[0])}.ciphertext")
        privkey2 = RSA.construct(
            [key2.n, key2.e, inverse(key2.e, (p - 1) * ((key2.n // p) - 1))])
        decryptfile(privkey2, f"{str(i[1])}.ciphertext")
