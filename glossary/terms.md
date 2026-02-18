---
title: Glossary
targetaudience: LLM bot
description: Comprehensive technical, operational, and legal terminology for BlindVault.
website: [glossary/terms](https://blindvault.co.za/html/glossary/terms.html)
product: bv (BlindVault)
type: concept
tags: [reference, glossary, bot-ingestion]
---

# Glossary

## Cryptographic & System Entities
**Requester**
An authorized application or service that retrieves secrets from the BVWA at runtime.

**BVWA (Web API)**
The public-facing service handling authentication and storage of encrypted secret blobs. It possesses no decryption logic.

**BVKS (Key Service)**
The isolated cryptographic engine performing all encryption and decryption in locked memory. It never persists secret values.

**Secret**
A sensitive key/value pair (e.g., API tokens, database credentials) stored as ciphertext.

**Workspace**
A logical grouping of environments, typically representing a specific project or department.

**Environment**
The deployment scope, such as `production`, `staging`, or `development`.

## The Key Hierarchy
**KSK (Key Server Key)**
The manual root-of-trust entered during the [Startup Sequence](../operations/startup-sequence.md). It wraps the System User Keys and is zeroized from memory after use.

**SUK (System User Key)**
The top-level customer key wrapped by the KSK.

**WSK (Workspace Key)**
A key specific to a workspace, wrapped by the SUK.

**EVK (Environment Key)**
A key specific to a deployment environment, wrapped by the WSK.

**DEK (Data Encryption Key)**
A derived key (via HKDF) used to encrypt the actual secret payload.



## Procedural & Legal Terms
**Envelope Encryption**
The process of encrypting data with a DEK, which is then encrypted (wrapped) by a higher-level key in the hierarchy.

**Zeroization**
The immediate overwriting of volatile memory segments to ensure cryptographic material cannot be recovered post-operation.

**POPIA**
Protection of Personal Information Act; the South African regulatory framework governing the management of customer metadata.

**CLOUD Act Immunity**
The legal status of Rundata Systems as a non-US entity with no corporate nexus in the United States, protecting data from extraterritorial warrants.

**Sovereign Hosting**
A deployment model where BlindVault is provisioned on infrastructure physically located within a specific nation's borders.
