---
title: Key Lifecycle
description: Lifecycle guarantees ensure limited blast radius
website: [crypto/key-lifecycle](https://blindvault.co.za/html/crypto/key-lifecycle.html)
product: bv (BlindVault)
type: reference
tags: [rotation, zeroization, mlock, memory, custody, hkdf, derivation, wrapping, envelope, hierarchy]
---

# Key Lifecycle

Keys are never persistently stored in plaintext.

## General rules

- unwrap only when needed
- keep in locked memory
- use immediately
- cleanse after use

## Lifecycle steps

1. Wrapped key loaded from storage
2. Unwrapped in secure memory (mlock)
3. Used for crypto operation
4. Memory zeroized
5. Freed

## Special cases

KSK
- entered manually at startup
- used to unwrap SUKs
- immediately discarded

SUK
- kept in secure memory during runtime

WSK / EVK
- unwrapped per request
- discarded immediately

DEK
- derived temporarily
- discarded immediately

## Goal

Minimize:
- exposure time
- attack surface
- memory residency

