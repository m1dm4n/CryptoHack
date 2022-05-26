from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{Le_Khac_Trung_Nam}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


ciphertext = encrypt_flag(FLAG)
print(ciphertext)
print(len(ciphertext))
e = 1
arr =[]
while 1:
    n = pow(a, e, p)
    if n not in arr:
        arr.append(n)
    else:
        break
    e += 1
print(arr)

def encrypt_flag(flag):
    text = ''

'''from random import randint
a = 43
p = 97
for i in range (1,100):
    print(i,'   ', (a**i) % p,'   ' , -(a**i) % p)

arr = [71, 38, 44, 12, 41, 1, 3, 57, 94, 26, 38, 87, 16, 7, 81, 81, 34, 52, 12, 28, 89, 36, 83, 46, 44, 84, 59, 51, 54, 44, 46, 9, 79, 76, 89, 7, 49, 41, 76, 2, 5, 81, 16, 83, 88, 75, 23, 14, 62, 15, 80, 34, 8, 32, 31, 24]
flag = b'crypto{'
plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
print(plaintext)
print(len(plaintext))
print(arr)
print(len(arr))

ciphertext = []
for c in range(len(plaintext)):
    n = pow(a, arr[c], p)
    if plaintext[c] == '1':
        ciphertext.append(n)
    else:
        n = -n % p
        ciphertext.append(n)
print(ciphertext)'''