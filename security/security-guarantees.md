# Security Guarantees

BV enforces strict separation of secrets and keys.

## Guarantees

BVKS never stores encrypted or plaintext secrets.

BVWA never stores wrapped or unwrapped keys.

Keys are only present in locked memory.

Keys are zeroized after use.

Root key is never stored on disk.

Each customer is cryptographically isolated.

Compromise of one environment does not expose others.

All communication uses authenticated HTTPS.

## Non-goals

BV does not:
- protect secrets after delivery to requester
- manage human passwords
- prevent misuse by an authorized client

## Threat reduction strategy

- minimize plaintext lifetime
- minimize key residency
- isolate blast radius
- split duties across services

