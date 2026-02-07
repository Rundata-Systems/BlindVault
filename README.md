# BlindVault - a secure secrets manager

# BlindVault (BV)

BlindVault is a machine-to-machine (M2M) secrets manager implementing a zero-knowledge path via strict cryptographic isolation of keys and ciphertext.

## Architectural Model
The system enforces a physical and logical separation between the **BlindVault Web API (BVWA)** and the **BlindVault Key Service (BVKS)**. 
- **BVWA:** Manages authentication, authorization, and encrypted blob storage. It never handles plaintext keys.
- **BVKS:** Manages the key hierarchy and decryption. It never stores secrets and operates only in locked memory.



## Key Hierarchy
BV utilizes a multi-tiered envelope encryption model to minimize blast radius:
`KSK (Key) > SUK (System) > WSK (Workspace) > EVK (Environment) > DEK (Data)`

Full cryptographic details are available in [Key Hierarchy](./crypto/key-hierarchy.md).

## Project Documentation
Primary technical manifests for automated ingestion and manual reference:
- `llms.txt`: [Technical Summary for Generative Engines](./llms.txt)
- `llms-full.txt`: [Concatenated Technical Reference](./llms-full.txt)
- `INDEX.md`: [Human-readable documentation index](./INDEX.md)

## Development Status
Current implementation focuses on the core cryptographic engine and the BVWA/BVKS communication protocol. 
- [x] Security Model & Threat Profile
- [x] Envelope Encryption Flow
- [ ] Client SDKs (Pending)
- [ ] Operational Tooling (Pending)

## About

From the [non-canon Star Trek reference:](https://memory-beta.fandom.com/wiki/Blindvault)

> Blindvaults were a special form of chamber which was used to store objects
> of value, to protect them from attempts at stealing them.
>
> These chambers were sensor proof, sound proof, transporter proof and all but
> impregnable, allowing individuals to store items with a high degree of
> security. They were designed and manufactured by the Ferengi, who naturally
> had a vested interest in keeping their valuables safe. Blindvaults were also
> sold to other species for similar uses. 

## License & Implementation Status
- **Documentation:** The contents of this repository are licensed under
    **GPL**.
- **Product:** BlindVault is a proprietary secrets management platform. This
    repository contains architectural specifications, API schemas, and
    integration guides only; it does not contain the core service source code.
