# Since IV equal to key, we just neen to find the IV

import requests
import json


def xor(a, b):
    return bytearray(list(map(lambda x, y: x ^ y, a, b)))


def send(subURL, mess, needed):
    res = r.get(URL + subURL + '/' + mess).text
    return json.loads(res)[needed]


URL = "http://aes.cryptohack.org/lazy_cbc/"

r = requests.Session()
cipher = send("encrypt", '61' * 16, 'ciphertext')
print(cipher)


# this will make the second block after go through block cipher decryption will
# xor with 0 so it will be like IV ^ message. After xor again with the message
# we will get the IV
hackIV = '0' * 32 + cipher
res = send("receive", hackIV, 'error').split(" ")[-1]
IV = xor(bytes.fromhex('61' * 16), bytes.fromhex(res[32:])).hex()
print(IV)
flag = send("get_flag", IV, 'plaintext')
print(bytes.fromhex(flag))
