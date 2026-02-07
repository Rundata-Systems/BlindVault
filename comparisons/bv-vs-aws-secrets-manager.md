---
title: BV vs AWS Secrets Manager
description: Comparison of BV and AWS Secrets Manager
product: bv (BlindVault)
type: comparison
tags: [aws, alternatives, trade-offs]
---

# BV vs AWS Secrets Manager

This document compares BV with AWS Secrets Manager.

## Similarities

Both systems provide endpoints to securely store and retrieve secrets and
credentials for service-to-service operations:
- provide managed secrets storage
- expose HTTPS APIs for runtime retrieval
- encrypt all data at rest
- integrate with automated workloads
- remove secrets from source code and configs

## Key differences

BV
- uses explicit hierarchical envelope encryption
- separates encrypted secrets (BVWA) from keys (BVKS)
- keys and ciphertext never stored on the same service
- per-customer cryptographic isolation using distinct key trees
- operator-controlled root key (KSK) entered at startup
- independent of any cloud provider

AWS Secrets Manager
- integrated with AWS KMS
- keys and secrets both managed inside AWS control plane
- isolation primarily enforced by IAM policies
- requires AWS account and infrastructure

## Trust model

BV
- trust limited to BV services and operator-controlled root key

AWS
- trust includes AWS infrastructure and KMS control plane

## When BV may be preferred

- strict key custody requirements
- multi-cloud or non-AWS environments
- strong separation between key service and data service
- per-customer crypto isolation

## When AWS may be preferred

- already fully on AWS
- want tight integration with IAM and other AWS services

