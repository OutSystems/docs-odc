---
summary: This article provides conceptual information about ODC REST API authentication and authorization.
tags: 
outsystems-tools: 
guid: 3a2b2308-eb3f-42f5-ac92-ab287e3e6af4
locale: en-us
app_type: reactive web apps, mobile apps
content-type: 
    - conceptual
audience: 
platform-version: odc
figma: 
---

# API authentication and authorization

Authentication ensures the identity of the user or system accessing the API. 

The ODC REST APIs uses the [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) protocol for authorization and authentication, which is based on the [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) framework.  OIDC enables user authentication via token-based mechanisms, ensuring a secure and standardized way to verify users' identities.

Authorization determines the level of access granted to an authenticated user or system. 

The ODC REST APIs uses [OAuth 2.0](#about-oauth-20-and-oidc) framework to manage and enforce access controls via access tokens. These tokens dictate what ODC APIs and data you are authorized to access. 

For detailed information, refer to [Using OAuth 2.0 to access APIs](using-oauth-access-api.md).

## About Oauth 2.0 and OIDC

[OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749), which stands for **Open Authorization 2.0**, is a framework that allows apps to securely access resources on behalf of a user or another service. It facilitates secure data sharing between applications without the need for users to share their credentials. Instead of sharing passwords, OAuth 2.0 uses access tokens to grant access to the requested resources, ensuring better security and user control over their data.

OIDC is built on top of OAuth 2.0 that adds **authentication** to confirm the identity of a user or system accessing an API. It uses JSON web tokens (JWTs) to verify user identity and obtain basic profile information.

### OAuth 2.0 grants

In OAuth 2.0, grants are the different ways a client (a system that requires access to the protected resources) can get [authorization](https://datatracker.ietf.org/doc/html/rfc6749#section-4) to access a protected resource. To access the resource, the client must have the access token.

OAuth 2.0 defines different grant types, which specify the steps the client needs to follow to receive an access token. The different grant types are:

- Authorization Code Grant

- Implicit Grant

- Client Credentials Grant

- Resource Owner Password Credentials (ROPC) Grant

- Authorization Code with PKCE (Proof Key for Code Exchange)

The [Client Credentials Grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4) is designed for server-to-server communication. It allows a client to directly authenticate with the authorization server to obtain an access token using the client credentials (client ID and secret). This grant type is ideal for API access from the backend systems.

To access the OutSystems APIs and data, you must use the **Client Credentials Grant** and generate the client ID and client secret using the [API Client](create-api-client.md) in the ODC portal.

You can  then use the client credentials to generate an access token which you can use to access the public APIs.

## Further reading

- [Using OAuth 2.0 to access APIs](using-oauth-access-api.md)

- [Configure API access using an API Client](create-api-client.md)
