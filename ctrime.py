import requests


URL = 'http://aes.cryptohack.org/ctrime/encrypt/'
r = requests.Session()


def encrypt(plain):
    rsp = r.get(URL + plain + '/')
    return rsp.json()['ciphertext']


alphabet = "}_!?@ETOANIHSRDLUCGWYFMPBKVJXQZ01234567890etoanihsrdlucgwyfmpbkvjxqz"


def bruteforce():

    flag = b'crypto{'
    cipher = encrypt((flag * 3).hex())
    mi = len(cipher)

    while True:
        for c in alphabet:
            cipher = encrypt(((flag+c.encode()) * 3).hex())
            print(c, len(cipher))
            if mi >= len(cipher):
                flag += c.encode()
                mi = len(cipher)
                print(mi, flag)
                break

        if flag.endswith(b'}'):
            print(flag)
            break


bruteforce()
