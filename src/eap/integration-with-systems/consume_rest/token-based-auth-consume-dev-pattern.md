---
guid: 9f31b7c4-6a7a-4a43-8b45-3b0f0b7d7f22
locale: en-us
summary: Learn a development pattern for consuming REST APIs that use JWT-based token authentication in OutSystems Developer Cloud (ODC).
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8700-1097
coverage-type:
  - understand
  - apply
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - mobile developers
tags: jwt, token-based authentication, access token, rest api, api authentication
outsystems-tools:
  - odc studio
helpids:
---

# Token-based authentication for consumed REST APIs

Many external REST APIs use **[JSON Web Tokens (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token)** to authenticate and authorize requests. You can consume these APIs in OutSystems Developer Cloud (ODC) by implementing the logic to obtain, store, and attach tokens to each request.

This article describes a **technology-agnostic development pattern** for consuming REST APIs that use token-based authentication with JWTs. The pattern isn't tied to a specific library or component.

<div class="info" markdown="1">

For interoperability between O11 and ODC, see also the [development pattern for securing exposed REST APIs in O11 with JWT-based tokens](https://www.outsystems.com/tk/redirect?g=5f8c0c2b-41e0-4a0d-9b3b-2f5a6a1d9f11). If you prefer to start from a prebuilt accelerator instead of implementing the pattern from scratch, consider using these Forge components:

* [**ODC REST Connector – Secure Token Auth for O11**](https://www.outsystems.com/forge/component-overview/23091/odc-rest-connector-client-odc) (ODC, client-side)
* [**O11 Service Account Manager – Secure Token Auth for ODC**](https://www.outsystems.com/forge/component-overview/23018/o11-service-account-manager-server-o11) (O11, server-side)

These Forge components are community-provided accelerators and **aren't officially supported by OutSystems**. Review the source code, perform a security assessment, and validate that they meet your organization's requirements before using them in production.

</div>

## When to use this pattern

Use the pattern for consuming REST APIs that use token-based authentication with JWTs when:

* You consume REST APIs that:
    * Require an `Authorization: Bearer <token>` header, where the token is a JWT.
    * Follow OAuth 2.0 or a similar token-based authorization flow.
    * Implement custom token endpoints that issue JWTs after validating credentials.
* You need to:
    * Centralize token acquisition and reuse across multiple REST APIs.
    * Control how and when tokens are refreshed.
    * Ensure tokens are handled securely and not scattered across your app logic.

## Token flows for different scenarios

When you integrate with a token-based API, the API provider typically uses one of the following flows:

| Scenario | Recommended flow | What it validates |
| :--- | :--- | :--- |
| **Only applications** call the API (machine-to-machine) | **Service account** | App identity |
| **Users** call the API through an application | **Credentials + service account** | User identity + app identity |
| **Users** call the API directly | **Credentials only** | User identity only |

Your ODC app must follow the flow required by the API provider. The rest of this article applies to all three flows.

This pattern applies both when you consume:

* REST APIs exposed from other internal systems that follow the matching token-based authentication pattern.
* Third-party APIs that use JWT-based authorization.

### Service account token flow

The service account token flow is the following. In this scenario, your ODC app is the client that obtains the token and calls the external REST API.

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

In a credential-based flow, your ODC app (as the client application) authenticates on behalf of the user and calls the external REST API with the token:

![Diagram showing a credential-based token flow between the client, token issuer, and exposed REST API.](images/token-credentials-diag.png "Credential-based Token Flow for Exposed REST APIs")

1. **Request login**: The app users login with username and password.
1. **Create token**: The auth provider validates and creates an access token.
1. **Return token**: The auth provider returns the access token to the app.
1. **Store token**: The app saves the token to use on next calls.
1. **Call API**: The app retrieves the access token and sends it in the `Authorization` header to the REST API.

    ```http
    Authorization: Bearer <access_token>
    ```

1. **Validate request**: The REST API sends the `Authorization` header to the Auth Service for validation.
1. **Validate token**: The auth provider validate access token.
1. **Return validation**: The auth provider returns the token validation to the server API.
1. **Process request**: The REST API verifies the token signature to detect tampering. It uses a JWK the issuer provides or retrieves the public JWK from the issuer’s JWKS endpoint. Then the REST API processes the request.
1. **Return response**: The REST API sends the response to the app.

Different projects can implement the authentication side in different ways (externally with access tokens, or internally with JWT or custom tokens).

## Applying this pattern in your ODC app {#applying-odc-token-consume-pattern}

To apply this pattern in your ODC app, follow these steps:

1. [Design the token manager library](#design-the-token-manager-library)
1. [Attach tokens in OnBeforeRequest and handle failures](#attach-tokens-in-onbeforerequest-and-handle-failures)

### Design the token manager library {#design-the-token-manager-library}

* **Encapsulate token logic in a library**
    * Create a dedicated library that exposes server actions to:
        * Request a new token from the external token endpoint.
        * Store and retrieve the token and its metadata (for example, expiration time).
        * Decide whether to reuse or refresh the token.
    * Use this library from all apps and REST integrations that need the same token.
* **Choose a storage strategy**
    * Treat access tokens as secrets.
    * Prefer storing tokens:
        * On the server side, in an entity in an **encrypted** format or in a [secret setting](../../security/set-as-secret.md). Decrypt them only inside the token manager when they're needed for outgoing API calls.
        * Per logical context (for example, per tenant or per technical client).
    * Avoid long-lived tokens and avoid storing them in locations that are directly accessible from untrusted clients.
* **Align with the authorization flow**
    * If the API uses OAuth 2.0 with client credentials, reuse the existing pattern from [Generate and reuse OAuth access token](generate-reuse-oauth-token.md).
    * If the API uses a custom JWT flow, design an equivalent server action that:
        * Calls the token endpoint with the required credentials.
        * Parses the response and extracts the JWT access token and expiration details.

The goal is to have a single place that knows **how to get a token**, **how long it is valid**, and **how to store it securely**.

### Attach tokens in OnBeforeRequest and handle failures {#attach-tokens-in-onbeforerequest-and-handle-failures}

After your app obtains a token from the external provider, you must attach it to every REST API call that requires authentication. In ODC, you attach the token to the request in the **OnBeforeRequest** callback of the consumed REST API:

1. **Configure the OnBeforeRequest callback**
    * In ODC Studio, open the consumed REST API.
    * Set the **OnBeforeRequest** property to a server action that runs before each request.
1. **Retrieve the token**
    * In the OnBeforeRequest action, call your token manager library to get the current token.
    * If the token manager returns an expired token or an error, handle it appropriately (for example, raise an exception or attempt a refresh).
1. **Add the Authorization header**
    * Use the **AddHeader** action or equivalent logic to add the `Authorization` header to the request.
    * Format the header value as:

        ```
        Bearer <access_token>
        ```

    * Ensure there is a space between `Bearer` and the token value.
1. **Handle token refresh on failure**
    * If the API call returns HTTP 401 (Unauthorized) or 403 (Forbidden), consider:
        * Invalidating or marking the stored token as invalid.
        * Triggering a token refresh using your token manager.
        * Retrying the request once with the new token, if it's appropriate for the operation you're performing.
    * Use exception handlers around your REST calls, as described in [Handling REST errors](handling-rest-errors.md), to capture token-related errors and inspect the details (for example, error messages or response bodies).
    * Avoid infinite retries. If a refreshed token still fails, treat it as a configuration or credential issue that needs investigation.
    * In more advanced scenarios, use the **OnAfterResponse** callback to inspect error responses at a lower level before OutSystems raises an exception.

This pattern keeps token handling close to the REST integration: the consumed REST API attaches tokens in **OnBeforeRequest**, while the token manager controls how tokens are acquired, stored, and reused.

For a detailed example of adding a header to a request, refer to [Example use case: Adding a header for token-based authentication](simple-customizations.md#example-use-case-adding-a-header-for-token-based-authentication).

## Security best practices for consumers

When you design token-based consumption patterns in ODC, apply the following security guidance:

* **Protect tokens in storage and in logs**
    * Encrypt tokens at rest when you store them in entities or configuration records.
    * Never write full tokens to logs, analytics events, or error messages.

* **Limit privileges**
    * Request and use only the scopes or roles the app needs to call the API.
    * Align scopes, roles, and API method permissions with your overall security model.

* **Integrate with broader access controls**
    * Combine token-based API authentication with other controls, such as:
        * MFA and adaptive authentication in the identity provider.
        * Role-based access control in your ODC app.
    * Use token claims (for example, scopes, roles, tenant) as inputs to your app-level authorization logic where appropriate.

By following these practices, you minimize the risk associated with token leakage, replay, and misuse.

<!-- [Commented out for now—logic interoperability GA delayed, and may be documented in a separate article.]

## Pattern variations and interoperability with O11

You can apply this pattern in different contexts:

* **Consuming O11-exposed APIs**
    * When the provider is an O11 REST API that follows the **Token-based authentication pattern for exposed REST APIs**, both sides:
        * Use the same expectations for JWT structure and claims.
        * Share a common understanding of audiences and scopes.
    * This alignment simplifies configuration and troubleshooting for logic interoperability scenarios.

![Diagram showing JWT generation in an app using asymmetric signing and key pairs.](images/app-JWT-token-generation-asymmetric-signing-diag.png "Example of JWT Token Generation with Asymmetric Signing")

* **Consuming third-party APIs**
    * When the provider is an external system:
        * Adapt the token acquisition action to the provider's authorization flow.
        * Configure claim and scope handling according to the provider's documentation.
    * The rest of the pattern (centralized token manager, `OnBeforeRequest`, and error handling) remains the same.
-->

## Related resources

* [Use REST APIs in your app](intro.md)
* [Token-based authentication for exposed REST APIs in ODC](../exposing_rest/token-based-auth-expose-dev-pattern.md)
* [Token-based authentication for exposed REST APIs in OutSystems 11](https://www.outsystems.com/tk/redirect?g=5f8c0c2b-41e0-4a0d-9b3b-2f5a6a1d9f11)
