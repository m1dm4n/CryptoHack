from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib


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


g = 2
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff

A = 0x9c7791dc328bf00f3dffbabf09297a598da21b7951ffd7709a6942a5b8fc85079b21a799b2e11f4ef28f3f0ba0b4ed0df328bc5e739d3ec20a339bcea248219ac77b09d60e79decd2c55e2e29540707b2d3566fd00d598cfd4cb94223219513c71694bcbcddc49d491d9a54f57ff4503fcd9330053d59992153ad5e2da345aff514d694d094ab128f825f20b3d639976c498ac14eabb7e5effe6fec284a818596a170cc23b0986e8e4d4ab5e2e000f1ce69560e16e3cb4931a9bcbbd5329f387

b = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944


def findsecret(A: int, b: int, p: int) -> int:
    return pow(A, b, p)


shared_secret = findsecret(A, b, p)

iv = "77094e1832f2361a06e985c82c60e0f1"
ciphertext = "98ce7148140242b33479e5f25c4dfe7b6b2ed2241524e9aefa010ee4c881fdae"

print(decrypt_flag(shared_secret, iv, ciphertext))
