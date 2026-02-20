---
guid: 941955cc-75d6-46d7-ba71-5fe9f89da4de
locale: en-us
summary: Learn a development pattern for securing exposed REST APIs in OutSystems Developer Cloud (ODC) using JWT-based token authentication.
coverage-type:
  - understand
  - evaluate
topic:
  - rest-webservice-data
  - authentication-mechanisms
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - architects
tags: rest apis,security,authentication,jwt,token-based authentication
outsystems-tools:
  - odc studio
helpids: 
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8972-210
---

# Token-based authentication for exposed REST APIs

When you expose business logic through REST APIs in OutSystems Developer Cloud (ODC), you should protect your endpoints against unauthorized access. **Token-based authentication with JSON Web Tokens (JWT)** gives you a flexible way to authenticate callers and enforce authorization on every request.

This article describes a **development pattern** for securing exposed REST APIs in ODC with JWT-based tokens. It focuses on what you need to design and validate rather than on a specific implementation in ODC Studio.

<div class="info" markdown="1">

For interoperability between ODC and O11, see also the [development pattern for consuming REST APIs in O11 that use token-based authentication with JWTs](https://www.outsystems.com/tk/redirect?g=e475d7de-23dc-40ff-9308-0c64c3ae6c87).

To start from an accelerator for ODC-to-O11 scenarios, use the [**ODC Service Account Manager – Secure Token Auth for O11**](https://www.outsystems.com/forge/component-overview/23311/odc-service-account-manager-odc) (ODC, server-side) Forge component.

This Forge component is a community-provided accelerator and **isn't officially supported by OutSystems**. Review the source code, perform a security assessment, and validate that it meets your organization's requirements before using it in production.

O11 provides built-in support for [OAuth 2.0 client flow authorization](https://www.outsystems.com/tk/redirect?g=beb761a2-ef08-44e6-aa0c-ee11bada5baa) and handles the client ID and client secret.

</div>

## When to use this pattern

Use this pattern when:

* You expose REST APIs from ODC that are consumed by:
    * Other internal systems that require strong authentication and authorization.
    * External partners that mustn't access your APIs with long-lived credentials.
* Your security architecture team requires:
    * Short-lived tokens instead of long-lived passwords or API keys.
    * Centralized authentication and authorization policies.
    * Clear separation between the component that issues tokens and the APIs that validate and enforce them.

## Choosing the right token flow

There are different ways to obtain tokens depending on whether you identify a user or an application:

| Scenario | Recommended flow | What it validates |
| :--- | :--- | :--- |
| **Only applications** access your API (machine-to-machine) | **Service account** | App identity |
| **Users** access your API via an application | **Credentials + service account** | User credentials + app identity |
| **Users** access your API directly | **Credentials only** | User credentials only |

### Service account token flow

The service account token flow is the following:

![Diagram showing a service account token flow where an application obtains a token and calls the exposed REST API.](images/token-app-diag.png "Service Account Token Flow for Exposed REST APIs")

1. **Request token**: The user requests a token for the app from the Auth Service Backoffice.
1. **Create token**: The Auth Service Backoffice creates an app token.
1. **Configure app**: The user configures the token in the client application's service account settings. This ensures the app can authenticate itself.
1. **Request data**: The user interacts with the app to request data (for example, clicking a "View Report" button).
1. **Call API**: The app retrieves the service account token and sends it in the `Authorization` header to the REST API.
1. **Validate request**: The REST API sends the `Authorization` header to the Auth Service for validation.
1. **Verify token**: The Auth Service validates the token.
1. **Return validation**: The Auth Service returns the validation result to the REST API.
1. **Process request**: The REST API verifies the token signature to detect tampering. It uses a JWK the issuer provides or retrieves the public JWK from the issuer’s JWKS endpoint. Then the REST API processes the request.
1. **Return response**: The REST API returns the response to the app.
1. **Show data**: The app returns the response to the user.

### Credential-based token flow

In a credential-based flow, the client application authenticates on behalf of the user:

![Diagram showing a credential-based token flow between the client, token issuer, and exposed REST API.](images/token-credentials-diag.png "Credential-based Token Flow for Exposed REST APIs")

1. **Request login**: The app users login with username and password.
1. **Create token**: The auth provider validates and creates an access token.
1. **Return token**: The auth provider returns the access token to the app.
1. **Store token**: The app saves the token to use on next calls.
1. **Call API**: The app retrieves the service account token and sends it in the `Authorization` header to the REST API.

    ```http
    Authorization: Bearer <access_token>
    ```

1. **Validate request**: The REST API sends the `Authorization` header to the Auth Service for validation.
1. **Validate token**: The auth provider validate access token.
1. **Return validation**: The auth provider returns the token validation to the server API.
1. **Process request**: The REST API verifies the token signature to detect tampering. It uses a JWK the issuer provides or retrieves the public JWK from the issuer’s JWKS endpoint. Then the REST API processes the request.
1. **Return response**: The REST API sends the response to the app.

Different projects can implement the authentication side in different ways (externally with access tokens, or internally with JWT or custom tokens).

## JWT structure and responsibilities

This section explains how a JWT is structured and which responsibilities belong to the token issuer and to the exposed REST API.

### JWT structure {#JWT-structure}

A JWT is a compact JSON-based token that includes information the API uses to authenticate and authorize requests. The token has three base64url encoded parts, separated by dots (`Header.Payload.Signature`):

* **Header**: Identifies the signing algorithm and token type, for example:

  ```json
  {
    "alg": "HS256",
    "typ": "JWT"
  }
  ```

  In this example, `"alg": "HS256"` stands for the HMAC SHA-256 symmetric signing algorithm.

* **Payload (claims)**: Contains statements about the subject and context, for example:

  ```json
  {
    "sub": "user-or-client-id",
    "aud": "your-odc-api",
    "iss": "your-token-issuer",
    "exp": 1735689600,
    "scope": "customers.read",
    "tenant": "acme"
  }
  ```

* **Signature**: Cryptographic signature over the header and payload that protects integrity and authenticity.

  Example of a symmetric HMAC SHA-256 signature:

  ```text
  HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret
  )
  ```

### Responsibilities of the token issuer and API {#responsibilities-of-the-token-issuer-and-api}

The pattern splits responsibilities between the **token issuer** and the **ODC exposed REST API**:

* Token issuer:
    * Authenticates the user or client.
    * Assembles the claims required by your security architecture.
    * Signs the token with a private key or shared secret.
    * Applies **short token lifetimes** and rotation policies.
* ODC exposed REST API:
    * Validates the signature to detect tampering using a public key from one of these sources:
        * Receives a JWK from the token issuer (on the Token creation).
        * Retrieves the public key from the token issuer’s JWKS endpoint.
    * Verifies standard claims:
        * `iss` (issuer) is trusted.
        * `aud` (audience) matches this API or logical API group.
        * `nbf` (Not Before): Specifies the earliest point in time when the token can be accepted. Think of it as a "do not open until" stamp.
        * `exp` (Expiration Time): This claim specifies the time after which the token must not be accepted.
        * Together, `nbf` and `exp` define the valid window for the token. The token is only considered valid if the current time is on or after the `nbf` time and before the `exp` time.
    * Applies business-specific checks:
        * Scopes or roles in the token are allowed to execute the requested method.
        * Tenant or customer identifiers match the request context.

Ensure the token payload contains only the minimum claims necessary to make authorization decisions. Avoid putting sensitive data directly in the token.

Even though clients can base64-decode a JWT, ensure they don't treat the claims as trusted data unless they can validate the token signature with the appropriate key. In particular:

* Don't rely on client-side checks alone to enforce access control; always validate the token and its claims on the server side.
* Avoid putting critical or sensitive information in signed but unencrypted tokens, especially when tokens are accessible to browser or mobile code.
* If you must transmit sensitive data inside a token, use an encrypted JWT (JWE) in addition to a signature, and keep validation and decryption server side.

## Key management and JSON Web Keys (JWK)

For detailed guidance on designing and managing JWT signing keys for this pattern, refer to [Key management and JSON Web Keys (JWK)](key-management-and-json-web-keys.md).

## Applying the pattern in ODC exposed REST APIs

This pattern separates two roles, similar to a hotel where you show identity at the front desk (token issuer) to get a room key, and later only present the key at the room door (protected API):

* **Token issuer (App Auth Service)**: Authenticates the client and issues a token.
* **Protected API (exposed REST API)**: Validates the token on every request before executing any logic.

### App Auth Service: issuing tokens

The App Auth Service acts as the "front desk". It authenticates the client and issues the token.

![Diagram showing JWT generation in an app using asymmetric signing and key pairs.](images/app-jwt-token-generation-asymmetric-signing-diag.png "Example of JWT token generation with asymmetric signing")

1. **Get Organization JSON Web Key from Secrets**: Retrieve the signing key from a [secret setting](../../security/set-as-secret.md) or from an entity that stores the key in an encrypted format.
1. **Generate JWT token**: Use a JWT action to create the token payload with required claims (sub, aud, exp) and sign it using the retrieved key.
1. **Save token detail**: Store relevant token metadata (such as AppID and Status) in an entity for tracking or revocation purposes.
1. **Assign token output**: Return the generated signed token to the caller.

### Exposed REST API: validating tokens

The exposed REST API acts as the "room door". It validates the token on every request.

In ODC, exposed REST APIs support a request pipeline where you can plug in authentication logic using the **OnAuthentication** callback. For an overview of the exposed REST execution flow, refer to [Exposing REST APIs](intro.md).

The exposed REST request (OnAuthentication) logic is the following:

![Diagram showing the OnAuthentication callback flow in an exposed REST API, including getting the token from the header, validating the token, and applying authorization rules.](images/exposed-rest-onauthentication-diag.png "Exposed REST API OnAuthentication flow diagram")

1. **Get token from header**: In the `OnAuthentication` action, read the `Authorization` header from the incoming HTTP request and extract the token value (removing the `Bearer` prefix).

    **Implementation tip:** Use `GetRequestHeader` from the `HTTPRequestHandler` extension to read the Authorization header:

    ```
    HeaderValue = GetRequestHeader("Authorization")
    Token = Replace(HeaderValue, "Bearer ", "")
    ```

1. **Validate token**: Verify the token signature using the organization's public key or secret. Validate standard claims such as `iss`, `aud`, and `exp`. If validation fails, stop processing the request and return an appropriate HTTP status code. For more information, refer to [Responsibilities of the token issuer and API](#responsibilities-of-the-token-issuer-and-api).
1. (Optionally) **Apply authorization rules**: Map token claims to permissions required by the REST method.

## Error handling

When token validation fails, return an appropriate HTTP status code:

* **401 Unauthorized**: Token is missing, expired, or has an invalid signature.
* **403 Forbidden**: Token is valid but lacks required scopes or permissions.

To return a custom status code from a REST method or callback, use the HTTP library action [Response_SetStatusCode](../../reference/libraries/http.md#response_setstatuscode). For an ODC example of setting status codes and throwing errors, refer to [Throw a custom error in an exposed REST API](throw-a-custom-error-in-an-exposed-rest-api.md) and [Change the HTTP status code of a REST API](change-the-http-status-code-of-a-rest-api.md).

## Security best practices for JWT token-based APIs

When you implement this pattern, apply the following security best practices:

* **Use short token lifetimes**
    * Prefer access tokens with lifetimes measured in minutes, not hours or days.
    * Combine short-lived access tokens with refresh tokens when the identity provider supports them.
    * Avoid issuing long-lived tokens that effectively behave like passwords.

* **Limit token scope and claims**
    * Include only the information needed to authorize calls, such as user or client identifier, audience, scopes, and tenant.
    * Avoid sensitive personal or business data in the payload; tokens are usually only base64url encoded, not encrypted.

* **Plan for revocation**
    * Revoke tokens proactively when:
        * A user logs out or a session ends.
        * A password or second factor changes.
        * Suspicious activity is detected (for example, impossible travel or unusual device).
    * Consider maintaining a short-lived deny list for revoked tokens when your threat model requires it.

* **Protect tokens in transit and at rest**
    * In ODC, REST services are always exposed over HTTPS (TLS). You can't disable SSL/TLS or accept plain HTTP.
        * Use [**Code quality**](../../monitor-and-troubleshoot/manage-technical-debt/managing-tech-debt.md), powered by [Mentor](../../building-apps/ai-mentor/intro.md), to scan for [exposed REST services without authentication](../../monitor-and-troubleshoot/manage-technical-debt/security/exposed-rest-services-are-not-secured.md).
    * If you log or store tokens anywhere, mask them in logs and encrypt them before persisting to prevent leakage. In ODC, use an application-level encryption mechanism such as [AES_Encrypt](../../reference/libraries/security.md#aes_encrypt) so that you store only ciphertext in the database, and use [AES_Decrypt](../../reference/libraries/security.md#aes_decrypt) to decrypt values only inside trusted server-side logic when strictly needed.

* **Defend against replay attacks**
    * Combine short token lifetimes with server-side checks where appropriate.
    * For high-risk operations, consider additional checks based on device, IP, or context.

## Related resources

* [Expose a REST API](expose-a-rest-api.md)
* [Built-in HTTP status codes](built-in-http-status-codes.md)
* [Token-based authentication for consumed REST APIs in ODC](../consume_rest/token-based-auth-consume-dev-pattern.md)
