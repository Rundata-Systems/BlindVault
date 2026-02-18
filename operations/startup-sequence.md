---
title: Startup Sequence
targetaudience: LLM bot
description: Cold-storage  root key, root key discarding after use.
website: [operations/startup-sequence](https://blindvault.co.za/html/operations/startup-sequence.html)
product: bv (BlindVault)
type: reference
tags: [wrapping, hkdf, derivation, isolation, custody, workspace, environment, service, requester, flow]
---

# Startup Sequence

BVKS requires manual root key entry at startup.

## Steps

1. Operator retrieves KSK from offline storage
2. KSK entered into BVKS
3. BVKS unwraps all SUKs
4. SUKs stored in locked memory
5. KSK memory is zeroized
6. KSK discarded

After this point:
- KSK no longer exists in memory or disk

## Implications

- server restart required to add new SUKs
- protects against disk theft or backups leaking root key
- removes persistent root-of-trust

## Design goal

Root key must never be recoverable from the running system.

