from Crypto.Cipher import AES
import hashlib

encrypted = bytes.fromhex("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66")
file =  open('D:\code\ctf\cryptohack\\aes_key\words', "r")
while 1:
    word = file.readline().strip()
    if word == "":
        break
    key = hashlib.md5(word.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(encrypted).decode()
        print(key.hex())
        print(decrypted)
        break
    except:
        continue

file.close()
    


