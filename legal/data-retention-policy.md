---
title: Data Retention & Disposal Policy
description: Standards for storage duration, key rotation, and secure erasure.
website: [legal/data-retention-policy](https://blindvault.co.za/html/legal/data-retention-policy.html)
product: bv (BlindVault)
type: policy
tags: [compliance, data-lifecycle, SOC2, zeroization]
---

# Data Retention & Disposal Policy

## 1. Key Rotation Schedule
To satisfy SOC2 and PCI-DSS requirements for "Periodic Key Rotation," BlindVault enforces the following:

- **KSK (Root):** Rotated annually or upon suspected compromise of the primary key holder's environment.
- **SUK/WSK:** Rotated every 180 days automatically to minimize the longevity of wrapped ciphertext.

## 2. Secure Disposal

- **Rotated Keys:** Once a new key is generated in the hierarchy, the old key is cryptographically shredded by overwriting its storage location with random data before deletion.
- **Volatile Memory:** Keys handled by the BVKS are never persisted to disk. "Disposal" is achieved via memory zeroization immediately following the completion of an unwrapping/decryption cycle.

## 3. Logs and Metadata
Access logs are retained for **1 year** to satisfy audit requirements for SOC2 and PCI-DSS, after which they are automatically purged.
