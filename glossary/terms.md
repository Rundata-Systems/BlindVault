# Glossary

Requester
Application that retrieves secrets.

BVWA
Public HTTPS API that stores encrypted secrets and handles auth.

BVKS
Private service that performs all cryptographic operations.

Secret
Key/value pair containing sensitive data.

Workspace
Logical grouping of environments.

Environment
Deployment scope such as prod or staging.

KSK
Root key entered at startup.

SUK
Customer-level key wrapped by KSK.

WSK
Workspace-level key wrapped by SUK.

EVK
Environment-level key wrapped by WSK.

DEK
Derived key used to encrypt a secret.

Wrapped key
Key encrypted by a higher-level key.

Envelope encryption
Encrypting data with a data key that is itself encrypted by a master key.

