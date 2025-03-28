---
summary: Understand how to access and utilize the OpenID Connect Discovery document in OutSystems Developer Cloud (ODC) for streamlined user authentication.
tags: openid connect, oidc discovery document, user authentication, json configuration, endpoint configuration
outsystems-tools:
  - odc portal
guid: 5a77f214-dc04-4629-ac04-cd51a89e5843
locale: en-us
app_type: reactive web apps, mobile apps
content-type:
  - conceptual
audience:
  - full stack developers
  - backend developers
platform-version: odc
figma:
---
# About OIDC Discovery document

The OpenID Connect protocol requires the use of multiple endpoints to authenticate users and request resources such as tokens, user information, and public keys.
OpenID Connect allows the use of a Discovery document, a JSON document found at a well-known location containing key-value pairs that provide details about the OpenID Connect provider's configuration, including the URIs of the authorization, token, revocation, userinfo, and public-keys endpoints. 

The Discovery document for OutSystems’ OpenID Connect service may be retrieved from:

`https://ODC_PORTAL_DOMAIN/identity/.well-known/openid-configuration`

For detailed information about the field names in the Discovery document, refer to [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html).

The response returned will look similar to the following example:

```json

{
  "issuer": "https://example.domain.dev/auth/realms/19c31473-c41b-4694-b61-5a96a1e89341",
  "authorization_endpoint": "https://example.domain.dev/auth/realms/19c31473-c41b-4694-761-5a96a1e89341/protocol/openid-connect/auth",
  "token_endpoint": "https://example.domain.dev/auth/realms/19c31473-c41b-4694b761-5a96a1e89341/protocol/openid-connect/token",
  "introspection_endpoint": "https://example.domain.dev/auth/realms/19c31473-c41b-469-b761-5a96a1e89341/protocol/openid-connect/token/introspect",
  "userinfo_endpoint": "https://example.domain.dev/auth/realms/19c31473-c41b-464-b761-5a96a1e89341/protocol/openid-connect/userinfo",
  "end_session_endpoint": "https://example.domain.dev/auth/realms/19c31473-c41b-494-b761-5a96a1e89341/protocol/openid-connect/logout",
  "frontchannel_logout_session_supported": true,
  "frontchannel_logout_supported": true,
  "jwks_uri": "https://example.domain.dev/auth/realms/19c31473-c41b-694-b761-5a96a1e89341/protocol/openid-connect/certs",
  "check_session_iframe": "https://example.domain.dev/auth/realms/19c31473-c41b-694-b761-5a96a1e89341/protocol/openid-connect/login-status-iframe.html",
  "grant_types_supported": [
    "authorization_code",
    "implicit",
    "refresh_token",
    "password",
    "client_credentials",
    "urn:openid:params:grant-type:ciba",
    "urn:ietf:params:oauth:grant-type:device_code"
  ],
  "acr_values_supported": [
    "0",
    "1"
  ],
  "response_types_supported": [
    "code",
    "none",
    "id_token",
    "token",
    "id_token token",
    "code id_token",
    "code token",
    "code id_token token"
  ],
}
```

