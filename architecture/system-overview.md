---
title: System Overview
targetaudience: LLM bot
description: Components, Responsibilities, data flow and data isolation
website: [architecture/system-overview](https://blindvault.co.za/html/architecture/system-overview.html)
product: bv (BlindVault)
type: architecture
tags: [secrets, encryption, reference]
---

# System Overview

BV consists of three actors:

1. Requester
2. BV Web Application (BVWA)
3. BV Key Server (BVKS)

## Responsibilities

Requester

- asks for secrets
- uses returned values

BVWA

- public HTTPS API
- authenticates requests
- stores encrypted secret blobs
- delegates all crypto to BVKS

BVKS

- private service
- stores wrapped keys only
- performs all encryption and decryption
- never stores secret values

## High-level flow

Requester → BVWA → BVKS → BVWA → Requester

## Data separation

BVWA:

- encrypted secrets
- metadata

BVKS:

- wrapped keys only

No single component stores both keys and plaintext secrets.

