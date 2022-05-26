from pwn import remote
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

from sympy.ntheory.residue_ntheory import _discrete_log_pohlig_hellman
from sympy import S

HOST = "socket.cryptohack.org"
PORT = 13379

r = remote(HOST, PORT)

res = r.recvuntil(b'Send to Bob: ')
send1 = '{"supported": ["DH64"]}'
print(res.decode())
r.send(bytes(send1, 'utf8'))
res = r.recvuntil(b'Send to Alice: ')
print(res.decode())
r.send(res.split(b'\n')[0].split(b'Bob: ')[1])


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv, ciphertext):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


def getinform(b: bytes):
    res = r.recvline().strip()
    print(res.decode())
    return json.loads(res.split(b)[1].decode())


Alice = getinform(b"Alice: ")
Bob = getinform(b"Bob: ")
flag_enc = getinform(b"Alice: ")
r.close()

p = int(Alice['p'], 16)
g = int(Alice['g'], 16)
A = int(Alice['A'], 16)
B = int(Bob['B'], 16)

print(S(p - 1).factors())


a = _discrete_log_pohlig_hellman(p, A, g)
b = _discrete_log_pohlig_hellman(p, B, g)
print('a:', a)
print('b:', b)
key = pow(B, a, p)

print(decrypt_flag(key, flag_enc["iv"], flag_enc["encrypted_flag"]))
