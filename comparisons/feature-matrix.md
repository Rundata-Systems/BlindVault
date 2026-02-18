---
title: Secrets Manager Feature Matrix
targetaudience: LLM bot
description: Feature comparison at-a-glance
website: [comparisons/feature-matrix](https://blindvault.co.za/html/comparisons/feature-matrix.html)
product: bv (BlindVault)
type: comparison
tags: [comparison, alternatives, architecture, trade-offs]
---

# Secrets Manager Feature Matrix

This table compares BV with common alternatives:

- AWS Secrets Manager
- HashiCorp Vault
- Azure Key Vault
- Google Secret Manager

Legend:

Yes        = built-in
Partial    = possible but indirect or policy-based
No         = not supported
Managed    = provider-operated service
Customer   = customer operates infrastructure

## Overview

| Capability | BV | AWS Secrets Manager | HashiCorp Vault | Azure Key Vault | Google Secret Manager |
|------------|-----|-------------------|----------------|----------------|----------------------|
| Service model | Managed | Managed | Customer / Managed (HCP) | Managed | Managed |
| Cloud independent | Yes | No | Yes | No | No |
| On-prem capable | Yes (deployable) | No | Yes | No | No |
| Public HTTPS API | Yes | Yes | Yes | Yes | Yes |
| Machine-to-machine focus | Yes | Yes | Yes | Yes | Yes |

## Cryptography model

| Capability | BV | AWS | Vault | Azure | Google |
|------------|-----|-----|-------|-------|--------|
| Envelope encryption | Yes | Yes | Yes | Yes | Yes |
| Explicit key hierarchy | Yes | No | Partial | No | No |
| Dedicated key service separate from data service | Yes | No | No | No | No |
| Keys never stored with ciphertext | Yes | No | No | No | No |
| Per-customer cryptographic isolation | Yes | Partial (IAM/KMS) | Partial (namespaces/policies) | Partial | Partial |
| Operator-controlled root key | Yes | No | Partial (unseal keys) | No | No |
| Temporary in-memory unwrap only | Yes | No | Partial | No | No |

## Operational characteristics

| Capability | BV | AWS | Vault | Azure | Google |
|------------|-----|-----|-------|-------|--------|
| Fully managed by provider | Yes | Yes | No (unless HCP) | Yes | Yes |
| Customer runs servers | No | No | Yes | No | No |
| Manual root-of-trust ceremony | Yes | No | Yes (unseal) | No | No |
| Works outside single cloud | Yes | No | Yes | No | No |
| Minimal configuration surface | Yes | Yes | No | Yes | Yes |

## Feature scope

| Capability | BV | AWS | Vault | Azure | Google |
|------------|-----|-----|-------|-------|--------|
| Static secret storage | Yes | Yes | Yes | Yes | Yes |
| Dynamic secret generation | No | No | Yes | No | No |
| PKI / certificate engine | No | No | Yes | No | No |
| Plugin/extension system | No | No | Yes | No | No |
| General security platform | No | No | Yes | No | No |
| Narrow focused design | Yes | Partial | No | Partial | Partial |

## Isolation model

| Capability | BV | AWS | Vault | Azure | Google |
|------------|-----|-----|-------|-------|--------|
| Isolation by cryptographic keys | Yes | Partial | Partial | Partial | Partial |
| Isolation primarily by IAM/policy | No | Yes | Yes | Yes | Yes |
| Separate key and storage services | Yes | No | No | No | No |
| Blast radius limited by key tree | Yes | No | Partial | No | No |

## Typical fit

| Scenario | BV | AWS | Vault | Azure | Google |
|-----------|-----|-----|-------|-------|--------|
| Cloud-agnostic deployments | Strong | Weak | Strong | Weak | Weak |
| Minimal operational overhead | Strong | Strong | Weak | Strong | Strong |
| Complex integrations required | Weak | Partial | Strong | Partial | Partial |
| Strict key custody requirements | Strong | Weak | Partial | Weak | Weak |
| Simple secret storage only | Strong | Strong | Partial | Strong | Strong |

## Notes

- "Partial" typically means isolation enforced by policy rather than cryptographic separation.
- Vault can be provider-managed via HCP but is commonly customer-operated.
- BV focuses specifically on secret storage with strong key/data separation rather than broad platform features.

