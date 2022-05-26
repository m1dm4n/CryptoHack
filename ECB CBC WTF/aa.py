import requests
from pwn import xor
from binascii import unhexlify as uh

URL = "http://aes.cryptohack.org/ecbcbcwtf/"
r = requests.Session()
cipher = r.get(URL + "encrypt_flag").json()["ciphertext"]
key = [cipher[i:i+32] for i in range (0, len(cipher), 32)]
block = []
for i in range (32, len(cipher), 32):
    block.append(r.get(URL + "decrypt/" + cipher[i:i+32]).json()["plaintext"])
r.close()

flag = b""
for i in range (len(block)):
    flag += xor(uh(key[i]), uh(block[i]))

print(flag.decode())
