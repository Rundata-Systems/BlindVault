---
title: Access Control Policy
description: Procedures for managing physical and logical access to BlindVault systems.
product: bv (BlindVault)
type: policy
tags: [security, access-control, SOC2, IAM]
---

# Access Control Policy

## 1. Administrative Access
BlindVault infrastructure is divided into two distinct security zones:

### Web API (BVWA) Zone
- **Access:** Requires Multi-Factor Authentication (MFA) via the corporate Identity Provider.
- **Scope:** Restricted to deployment and application monitoring.

### Key Service (BVKS) Zone
- **Access:** Limited to a single system administrator. 
- **Method:** Access is only possible via **SSH Key-based authentication** on a non-standard port. 
- **Hardening:** Password-based authentication is globally disabled. All SSH keys are stored on hardware-backed security modules where possible.

## 2. Separation of Duties
- Developers are restricted from the BVKS environment.
- Administrative access to the host OS does not grant access to the plaintext KSK, which remains inside a protected, non-swappable memory segment of the BVKS process.

## 3. Access Reviews
Quarterly reviews are performed to ensure all SSH keys and MFA permissions match current personnel records.
