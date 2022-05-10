from Crypto.Cipher import DES3
from pwn import xor
key = b'\x00' * 8 + b'\xff' * 8
ptext = b'TrungNam'
cipher = DES3.new(key, DES3.MODE_ECB)
IV = b'\xc5=\x8e\x8e\xedi\xf9\x95'

ctextxorIV = bytes.fromhex("911278c8ca6af417")


def encrypt(p):
    tmp = xor(IV, p)
    c = cipher.encrypt(tmp)
    c = xor(c, IV)
    return c


ctext1 = encrypt(ptext)
ctext2 = encrypt(ctext1)

print(ctext2)
