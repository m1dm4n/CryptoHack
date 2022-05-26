import requests
from pwn import xor
BLOCK = 16
URL = "http://aes.cryptohack.org/bean_counter/"
r = requests.Session()

res = r.get(URL + "encrypt").json()["encrypted"]

png_head = bytes.fromhex("89504E470D0A1A0A0000000D49484452")
cipher = bytes.fromhex(res)
print(png_head)

key = xor(cipher[:BLOCK], png_head)

png = [0]*len(cipher)
for i in range(len(cipher)):
    png[i] = cipher[i] ^ key[i % len(key)]

with open('bean_counter.png', 'wb') as f:
    f.write(bytes(png))
