import logging
import os
import random
from operator import xor
import requests
from Crypto.Cipher import ARC4
from pwn import xor
r = requests.Session()
URL = "http://aes.cryptohack.org/oh_snap/send_cmd/"



def getct(pt: bytes, nonce: bytes):
    res = r.get(URL + '/' + pt.hex() + '/' + nonce.hex()).json()
    print(res)
    return bytes.fromhex(res["error"].split("nd: ")[-1])


def count_elements(xs):
    counts = {x: 0 for x in xs}

    for x in xs:
        counts[x] += 1

    return counts


def most_common_element(xs):
    counts = count_elements(xs)
    return max(xs, key=counts.get)


def test_key(nonce, counter, key, plaintext, expected_ciphertext):
    try:
        key_bytes = nonce + counter + key
        cipher = ARC4.new(key_bytes)
        ciphertext = cipher.encrypt(plaintext)

        return ciphertext == expected_ciphertext
    except:
        return False
def attack(num_sample = 8, nonce_size = 32, block_size = 256):
    samples = []
    test_nonce = os.urandom(nonce_size)
    test_pt = os.urandom(block_size)
    test_counter = random.randint(0, 100)
    test_ct = getct(test_pt, test_nonce)
    nonce = os.urandom(nonce_size)
    for counter in range(num_sample):
        pt = os.urandom(block_size)
        ct = getct(pt, nonce)
        keystream = b''.join([bytes([x ^ y]) for x, y in zip(pt, ct)])
        print(keystream)
        c = bytes([counter])
         
        samples.append((c, keystream))
    key = b""
    while not test_key(test_nonce, test_counter, key, test_pt, test_ct):
        candidate_key_bytes = []
        for counter, keystream in samples:
            known_bytes = nonce + counter + key
            num_known_bytes = len(known_bytes)
            # We know the first num_known_bytes of the key, so we can
            # step through the first num_known_bytes iteratons of RC4s
            # key scheduling algorithm (KSA):
            S = [i for i in range(256)]

            j = 0
            for i in range(num_known_bytes):
                j = (j + S[i] + known_bytes[i]) % 256
                S[i], S[j] = S[j], S[i]

            # Fetch the output we care about then derive S'[1] = next_S_i
            output_byte = keystream[num_known_bytes - 1]
            next_S_i = (num_known_bytes - output_byte) % 256

            # So we know S'[i] = S[j + S[i] + key[0] % 256]
            # and we have a value for S'[i], next_S_i
            # So we have next_S_i = S[j + S[i] + key[0] % 256]

            # Find whats inside the brackers of the LHS of the equation:
            pre_i = None
            for x in range(256):
                if S[x] == next_S_i:
                    pre_i = x
                    break

            # Get the unknown_key_byte by equating the indices of S
            # (the stuff in the square brackets).
            key_byte = (pre_i - j - S[num_known_bytes]) % 256
            candidate_key_bytes.append(key_byte)
        print(candidate_key_bytes)
        # So we can just pick the most common value:
        chosen_key_byte = most_common_element(candidate_key_bytes)
        key += bytes([chosen_key_byte])

        print(f"Picked {chosen_key_byte} for {len(key)} key byte: key = {key.hex()}")

    print(f"Key= {key.hex()}={key.decode('utf8')} verified working!")
    return key

print(attack(100, ))