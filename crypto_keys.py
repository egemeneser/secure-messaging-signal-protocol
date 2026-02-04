"""
Elliptic Curve key generation and digital signatures for a
Signal-inspired secure messaging protocol.

Server-side communication code is intentionally omitted.
"""

from ecpy.curves import Curve, Point
from Crypto.Random import random
from Crypto.Hash import SHA3_512

curve = Curve.get_curve("Ed25519")
P = curve.generator
n = curve.order


def generate_ec_keypair():
    sk = random.randint(1, n - 1)
    pk = sk * P
    return sk, pk


def sign_message(sk, pk, message: bytes):
    h1 = SHA3_512.new(sk.to_bytes(32, "big")).digest()
    r = int.from_bytes(
        SHA3_512.new(h1[32:] + message).digest(), "big"
    ) % n

    R = r * P

    h2 = int.from_bytes(
        SHA3_512.new(
            R.x.to_bytes(32, "big")
            + R.y.to_bytes(32, "big")
            + pk.x.to_bytes(32, "big")
            + pk.y.to_bytes(32, "big")
            + message
        ).digest(),
        "big",
    ) % n

    s = (r + sk * h2) % n
    return R, s


def verify_signature(pk, message: bytes, R, s):
    h = int.from_bytes(
        SHA3_512.new(
            R.x.to_bytes(32, "big")
            + R.y.to_bytes(32, "big")
            + pk.x.to_bytes(32, "big")
            + pk.y.to_bytes(32, "big")
            + message
        ).digest(),
        "big",
    ) % n

    return s * P == R + h * pk