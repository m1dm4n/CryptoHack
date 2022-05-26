from Crypto.Util.number import inverse as inv
from Crypto.Util.number import long_to_bytes
from hashlib import sha1


class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y
        self.all = (self.x, self.y)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


G = Point(1804, 5368)
Qa = Point(815, 3190)
nB = 1829


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

    def Add(self, P: Point, Q: Point):
        if P == self.zero:
            return Q
        if Q == self.zero:
            return P
        if P.x == Q.x and P.y != Q.y:
            return self.zero
        x1, y1, x2, y2 = P.x, P.y, Q.x, Q.y
        if P == Q:
            phi = (3 * x1 * x1 + self.a) * inv(2*y1, self.p) % self.p
        else:
            phi = (y2 - y1) * inv(x2 - x1, self.p) % self.p
        x3 = (phi*phi - x1 - x2) % self.p
        y3 = (phi * (x1 - x3) - y1) % self.p
        return (Point(x3, y3))

    def Multiply(self, P: Point, k: int):
        assert k > 0
        Q, R, n = P, self.zero, k
        while n > 0:
            if n % 2 == 1:
                R = self.Add(R, Q)
            Q = self.Add(Q, Q)
            n //= 2
        return R


ECC = Elliptic(497, 1768, 9739)
# print(ECC.Add(ECC.Add(ECC.Add(P, P), Q), R).all)
# X = (5274, 2841) and Y = (8669, 740).
c = ECC.Multiply(Qa, nB)
print(c.all)
print(sha1(str(c.x).encode()).hexdigest())
