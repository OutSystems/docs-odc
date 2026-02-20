---
summary: Learn how to design and manage JWT signing keys and JSON Web Keys (JWK) for securing exposed REST APIs in OutSystems Developer Cloud (ODC).
tags: jwt, json web keys, api security, key management, token-based authentication
locale: en-us
guid: 63f8b0fe-24f6-48bd-a3a8-90c372949aad
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - architects
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - evaluate
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8791-2
topic:
  - rest-webservice-data
  - document-apis
  - authentication-mechanisms
helpids:
---

# Key management and JSON Web Keys (JWK)

To validate [JWT signatures](token-based-auth-expose-dev-pattern.md#JWT-structure), exposed REST APIs in OutSystems Developer Cloud (ODC) need access to the appropriate cryptographic keys. Use **JSON Web Keys (JWK)** to represent these keys in a standard JSON format that tools and libraries can process consistently.

When you design key management for token-based authentication with JWTs, choose between symmetric and asymmetric signing.

## Symmetric (HMAC)

This method uses a single shared secret:

![Diagram showing a symmetric JWT signature where the same key is used to sign and validate the token.](images/symmetric-signature-diag.png "Symmetric JWT Signature Diagram")

* The same secret key signs and validates tokens.
* Simpler to set up but requires sharing the secret with every API that validates tokens.
* Best suited for peer-to-peer scenarios where there are only a few trusted components.
* Typically used when only trusted server-side components validate tokens. The shared secret must never leave secure server-side storage.

## Asymmetric (RSA or EC)

This method uses a public/private key pair:

![Diagram showing an asymmetric JWT signature with a private signing key and a public verification key.](images/asymmetric-signature-diag.png "Asymmetric JWT Signature Diagram")

* The token issuer signs with a private key.
* APIs validate signatures with the corresponding public key.
* Better for multi-tenant or multi-consumer environments and for rotating keys without redeploying all APIs.
* Recommended when untrusted clients (such as browser or mobile apps) need to verify that a token hasn't been tampered with. Expose only the public verification key to those clients.

## JWK best practices

When you use JWKs to represent keys, follow these additional practices.

* **Use JWKs for key representation and rotation**
    * Store keys using the JWK format, either locally or exposed through a JWK endpoint.
    * Plan for **key rotation**:
        * Publish new keys alongside existing ones.
        * Allow APIs to accept tokens signed with both old and new keys during a transition period.

* **Separate keys for tokens and claims**
    * Use different JWKs for:
        * **Signing tokens** used for authentication and authorization.
        * Any keys you might use to encrypt or sign additional claims or payloads.
    * Never expose token-signing keys inside token claims or other user-visible structures. This separation reduces the blast radius if one key is compromised.

The exact storage mechanism for keys in ODC depends on your architecture. Common options include the following approaches.

* **Secret settings**: Store keys securely in [secret settings](../../security/set-as-secret.md) in ODC Studio.
* **Configuration libraries**: Store keys in a secret setting or encrypt keys before storing them in entities. If you use an entity, encrypt the key by using [AES_Encrypt](../../reference/libraries/security.md#aes_encrypt) before you store it and decrypt it by using [AES_Decrypt](../../reference/libraries/security.md#aes_decrypt) when you retrieve it.
* **External identity provider integration**: Retrieve keys from your identity provider's JWK endpoint.
* **Forge components**: Use community-supported components that abstract JWK parsing and validation logic.
