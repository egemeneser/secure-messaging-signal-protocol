# Secure Messaging with Signal Protocol (X3DH & PQXDH)

This repository contains a cryptography-focused implementation of a secure messaging protocol
inspired by the Signal Protocol. The project demonstrates end-to-end encryption, forward secrecy,
and a hybrid post-quantum key exchange design.

## Implemented Components
- Identity Key (IK), Signed Pre-Key (SPK), and One-Time Pre-Key (OTK) generation using Ed25519
- End-to-end encrypted messaging with forward secrecy via X3DH-style key agreement
- AES-256-CTR encryption with HMAC-SHA256 authentication
- Key Derivation Function (KDF) chains for per-message encryption and MAC keys
- Post-quantum extension using Kyber-based key encapsulation (PQOTKs) and hybrid session key derivation

## Scope & Limitations
- The implementation focuses on cryptographic key management and session establishment.
- Post-quantum message exchange can be extended using the same message flow as the classical X3DH-based implementation.
- Server-side logic and credentials are intentionally omitted.

## Notes
- This project was implemented for educational and demonstrative purposes.
- No private keys, credentials, or instructor-provided code are included.

## Technologies
Python · Ed25519 · SHA3 · AES-CTR · HMAC · Kyber (Post-Quantum Cryptography)
