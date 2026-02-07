---
title: Incident Response Plan (IRP)
description: Protocol for detection, containment, and recovery from security incidents.
product: bv (BlindVault)
type: policy
tags: [security, incident-response, SOC2, containment]
---

# Incident Response Plan

## 1. Overview
This plan defines the procedures for responding to security incidents involving the BVWA (Web API) or the BVKS (Key Service).

## 2. Incident Classification
- **Level 1 (Low):** Isolated unauthorized access attempts to BVWA (blocked).
- **Level 2 (Medium):** Suspected compromise of a Workspace Key (WSK). Impact is limited to a single customer/tenant.
- **Level 3 (High):** Suspected compromise of a System User Key (SUK) or the Master Key Service Key (KSK), or unauthorized SSH access to the BVKS host.

## 3. Response Phases
### Detection & Analysis
Monitoring systems alert on:
- Unauthorized SSH attempts to BVKS on non-standard ports.
- BVKS memory integrity violations or unexpected process restarts.
- High-frequency calls to `POST /v1/secrets/get` suggesting token scraping.

### Containment Strategy
- **BVKS Memory Zeroization:** In the event of Level 3 compromise, the BVKS process is signaled to perform immediate `memset` zeroization of all unwrapped keys in memory.
- **Credential Revocation:** Immediate rotation of SSH keys for the affected infrastructure.

### Recovery
- **Hierarchy Re-initiation:** Execution of the [Startup Sequence](../operations/startup-sequence.md).
- **Mandatory Rotation:** Forced rotation of the KSK and SUK layers to invalidate any potentially exfiltrated wrapped keys.
