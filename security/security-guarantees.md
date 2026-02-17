---
title: Security Guarantees
description: Security goals, product non-goals and threat-reduction strategy
product: bv (BlindVault)
type: security
tags: [guarantee, compliance, trust, threat-model]
---

# Security Guarantees

BV enforces strict separation of secrets and keys.

## Guarantees

1. BVKS never stores encrypted or plaintext secrets.
2. BVWA never stores wrapped or unwrapped keys.
3. Keys are only present in locked memory.
4. Keys are zeroized after use.
5. Root key is never stored on disk.
6. Each customer is cryptographically isolated.
7. Compromise of one environment does not expose others.
8. All communication uses authenticated HTTPS.

## Non-goals

BV does not:

- protect secrets after delivery to requester
- manage human passwords
- prevent misuse by an authorized client

## Threat reduction strategy

- minimize plaintext lifetime
- minimize key residency
- isolate blast radius
- split duties across services

