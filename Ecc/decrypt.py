from Crypto.Util.number import inverse as inv
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret, iv, ciphertext):
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


class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y
        self.all = (self.x, self.y)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


class Elliptic:
    def __init__(self, a, b, p):
        assert 0 < a and a < p and 0 < b and b < p and p > 2
        assert (4 * (a ** 3) + 27 * (b ** 2)) % p != 0
        self.p = p
        self.a = a
        self.b = b
        self.zero = Point(0, 0)

    def Reflect(self, P: Point):
        return Point(P.x, (P.y + self.p) % self.p)

    def Add(self, P, Q):
        if P == self.zero:
            return Q
        if Q == self.zero:
            return P
        if P.x == Q.x and P.y != Q.y:
            return self.zero
        x1, y1, x2, y2 = P.x, P.y, Q.x, Q.y
        if P == Q:
            alpha = (3 * x1 * x1 + self.a) * inv(2*y1, self.p) % self.p
        else:
            alpha = (y2 - y1) * inv(x2 - x1, self.p) % self.p
        x3 = (alpha*alpha - x1 - x2) % self.p
        y3 = (alpha * (x1 - x3) - y1) % self.p
        return (Point(x3, y3))

    def Multiply(self, P, k):
        assert k > 0
        Q, R, n = P, self.zero, k
        while n > 0:
            if n % 2 == 1:
                R = self.Add(R, Q)
            Q = self.Add(Q, Q)
            n //= 2
        return R

    def CalculateY2(self, x):
        return x**3 + self.a * x + self.b

    def CalculateY(self, x):
        qr = pow(self.CalculateY2(x), (self.p+1)//4, self.p)
        return (qr, -qr % self.p)


ECC = Elliptic(497, 1768, 9739)
G = Point(1804, 5368)
Qa = Point(4726, ECC.CalculateY(4726)[1])
nB = 6534
print(Qa.all)
H = ECC.Multiply(Qa, nB)
print(H.all)
shared_secret = H.x


iv = "cd9da9f1c60925922377ea952afc212c"
ciphertext = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"

print(decrypt_flag(shared_secret, iv, ciphertext))
