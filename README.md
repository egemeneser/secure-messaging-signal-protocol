# Secure Messaging with Signal Protocol (X3DH & PQXDH)

This repository contains an academic cryptography project implementing a simplified version
of the Signal Protocol, developed as part of the CS 411 / CS 507 Cryptography course at
Sabancı University.

## Features
- Identity Key (IK), Signed Pre-Key (SPK), and One-Time Pre-Key (OTK) generation using Ed25519
- End-to-end encrypted messaging with forward secrecy via X3DH
- AES-256-CTR encryption with HMAC-SHA256 authentication
- Key Derivation Function (KDF) chains for per-message keys
- Post-Quantum extension using Kyber-based PQXDH (PQOTK generation and hybrid session keys)

## Project Scope
The implementation covers the protocol up to **Phase III – Section 4.2.1**, including
post-quantum one-time key generation. Message sending using PQXDH can be extended
from the X3DH-based implementation.

## Notes
- This project was implemented for educational purposes.
- Server-side components and credentials are not included.
- No private keys or sensitive information are shared.

## Technologies
Python, Ed25519, SHA3, AES, HMAC, Kyber (Post-Quantum Cryptography)
