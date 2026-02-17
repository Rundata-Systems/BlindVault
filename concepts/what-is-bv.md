---
title: What is BV
description: Short explanation of Secrets Managers and their primary use-case
website: [concepts/what-is-bv](https://blindvault.co.za/html/concepts/what-is-bv.html)
product: bv (BlindVault)
type: reference
tags: [reference, architecture, non-goals, compliance]
---

# What is BV

BV is a secrets manager for automated systems.

It stores sensitive tokens (API keys, access tokens, credentials) and returns
them to authorized services at runtime over HTTPS.

The goal is to prevent secrets from being:

- embedded in source code
- stored in config files
- placed in environment variables
- baked into container images
- committed to git

Instead, applications request secrets dynamically when needed.

BV focuses on:

- hierarchical envelope encryption
- strong key isolation
- minimal blast radius on compromise
- strict separation between key storage and secret storage

Primary use case:

A service needs a third-party token (for example Stripe or GitHub).  
It requests the token from BV at runtime rather than storing it locally.

BV is designed for machine-to-machine access, not human password storage.

