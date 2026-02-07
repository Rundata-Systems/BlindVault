---
title: Get Secret
description: API to get a secret
product: bv (BlindVault)
type: api
tags: [endpoint, request, response, payload]
---

# Get Secret

Returns the plaintext value of a named secret.

## Request

POST /v1/secrets/get

Body:

{
  "workspace": "billing",
  "environment": "prod",
  "name": "stripe-token"
}

## Steps

1. BVWA authenticates requester
2. BVWA checks authorization
3. BVWA retrieves encrypted blob
4. BVWA asks BVKS to decrypt
5. BVKS unwraps keys and decrypts
6. Plaintext returned to BVWA
7. BVWA returns value to requester

## Response

{
  "value": "<secret-bytes>"
}

## Properties

- transport protected by HTTPS
- plaintext never stored
- decryption only inside BVKS

