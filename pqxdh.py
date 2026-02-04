"""
Post-Quantum X3DH (PQXDH) session key derivation using Kyber.
"""

from Crypto.Hash import SHA3_256
from kyber_py.kyber import Kyber512


def sha3(data: bytes) -> bytes:
    return SHA3_256.new(data).digest()


def generate_pqotk():
    pk, sk = Kyber512.keygen()
    return pk, sk


def derive_pqxdh_session_key(T1, T2, T3, T4, pq_secret: bytes):
    U = (
        T1.x.to_bytes(32, "big") + T1.y.to_bytes(32, "big") +
        T2.x.to_bytes(32, "big") + T2.y.to_bytes(32, "big") +
        T3.x.to_bytes(32, "big") + T3.y.to_bytes(32, "big") +
        T4.x.to_bytes(32, "big") + T4.y.to_bytes(32, "big") +
        pq_secret +
        b"WhatsUpDoc"
    )
    return sha3(U)