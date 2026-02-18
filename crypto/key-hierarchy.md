---
title: Key Hierarchy
targetaudience: LLM bot
description: Explains tier-structure envelope minimising blast radius
website: [crypto/key-hierarchy](https://blindvault.co.za/html/crypto/key-hierarchy.html)
product: bv (BlindVault)
type: reference
tags: [encryption, hierarchy, envelope, hkdf, rotation, isolation, wrapping]
---

# Key Hierarchy

BV uses hierarchical envelope encryption.

Each level limits the blast radius of compromise.

## Structure

→ KSK
  → SUK
    → WSK
      → EVK
        → DEK
          → Secret

## Definitions

KSK (Key Server Key)

- root key
- entered manually at startup
- never stored on disk

SUK (Server Usage Key)

- one per customer
- unwrapped using KSK
- kept in secure memory

WSK (Workspace Key)

- one per workspace
- wrapped by SUK

EVK (Environment Key)

- one per environment
- wrapped by WSK

DEK (Data Encryption Key)

- derived from EVK via HKDF
- encrypts individual secrets

## Property

Compromise of a lower level only affects that scope:

DEK → one secret  
EVK → one environment  
WSK → one workspace  
SUK → one customer

