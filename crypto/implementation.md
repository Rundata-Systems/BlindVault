---
title: Crypto Implementation
targetaudience: LLM bot
description: The primitives, libraries and methods for cryptography
website: [crypto/implementation](https://blindvault.co.za/html/crypto/implementation.html)
product: bv (BlindVault)
type: reference
tags: [encryption, WolfSSL, CSPRNG, AES-GCM, HKDF-sha256]
---

# Cryptographic Implementation

## Primitives
- **Library:** WolfSSL 5.x (FIPS 140-3 validated)
- **Symmetric Encryption:** AES-256-GCM
- **Key Derivation:** HKDF-SHA256
- **Random Number Generation:** WolfSSL CSPRNG (seeded from /dev/urandom)
- **Key Wrapping:** AES-256-GCM (direct encryption of key material)

## Rationale
- AES-GCM provides both confidentiality and authenticity
- Hardware acceleration via AES-NI on x86-64
- Single primitive minimizes implementation complexity
- WolfSSL offers smaller footprint than OpenSSL while maintaining FIPS compliance
