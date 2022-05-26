from pwn import xor
import requests

URL = "http://aes.cryptohack.org/flipping_cookie/"
r = requests.Session()
res = r.get(URL + "get_cookie/").json()["cookie"]

iv = bytearray.fromhex(res[:32])
cookie = res[32:]

iv[6:11] = xor(xor(b"True;", b"False"), iv[6:11])

a = r.get(URL + "check_admin/" + cookie + '/' + iv.hex())

print(a.text)
