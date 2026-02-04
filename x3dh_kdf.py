"""
X3DH-style session key derivation and KDF chains.
"""

from Crypto.Hash import SHA3_256


def sha3(data: bytes) -> bytes:
    return SHA3_256.new(data).digest()


def derive_x3dh_session_key(T1, T2, T3, T4):
    U = (
        T1.x.to_bytes(32, "big") + T1.y.to_bytes(32, "big") +
        T2.x.to_bytes(32, "big") + T2.y.to_bytes(32, "big") +
        T3.x.to_bytes(32, "big") + T3.y.to_bytes(32, "big") +
        T4.x.to_bytes(32, "big") + T4.y.to_bytes(32, "big") +
        b"WhatsUpDoc"
    )
    return sha3(U)


def kdf_chain(kkdf: bytes):
    k_enc = sha3(kkdf + b"JustKeepSwimming")
    k_hmac = sha3(kkdf + k_enc + b"HakunaMatata")
    kkdf_next = sha3(k_enc + k_hmac + b"OhanaMeansFamily")
    return k_enc, k_hmac, kkdf_next