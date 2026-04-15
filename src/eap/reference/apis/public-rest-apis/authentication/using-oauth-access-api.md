---
summary: Configure OAuth 2.0 to access REST APIs with OutSystems Developer Cloud (ODC), obtain client credentials, generate access tokens, and authorize API calls.
tags: oauth 2.0, api authorization, rest apis, access token, client credentials
outsystems-tools:
  - odc portal
guid: 4dcce5be-a518-4401-8261-3588e95415ba
locale: en-us
app_type: reactive web apps, mobile apps
content-type:
  - process
audience:
  - platform administrators
  - backend developers
platform-version: odc
figma: https://www.figma.com/design/eFzsh8ZIP5AIbRUyjeTV26/Reference?node-id=3492-39
---

# Using OAuth 2.0 to access the APIs

The ODC REST APIs use the [OAuth 2.0 framework](https://datatracker.ietf.org/doc/html/rfc6749) for authorization.

Before accessing the ODC REST APIs, you must obtain OAuth 2.0 [client credentials](#client-credentials): a client ID and a client secret from the [API Client](about-api-client.md) in the ODC portal. Next, use the client credentials to generate an OAuth [access token](#access-token) from the authorization server. The access token accounts for the user credentials and allows you to make API calls.

The permissions assigned to the API client control the access level to the APIs and data.
This allows the authorization server to generate an access token with relevant permissions.

Once the authorization server generates the access token, you can call the API by sending the token in the Authorization header of your request. For example, in the following request, replace ACCESS_TOKEN with the token you have received from the authorization server.

```curl

curl -X GET "https://ODC_PORTAL_DOMAIN/api/identity/v1/users?hasApplicationRoles=true&limit=10&offset=0" -H "Authorization: Bearer ACCESS_TOKEN"

```

Here’s the high-level process of authorizing and authenticating APIs:

![Diagram showing the process of authorizing and authenticating APIs using OAuth 2.0. Steps include creating an API client, generating and sharing client credentials, setting credentials in the app, requesting and validating an access token, and calling the API with the access token.](images/authentication-auth-flow-diag.png "OAuth 2.0 Authorization and Authentication Flow")

1. As an administrator in the ODC portal, [create a new API client](create-api-client.md) for the app.

   1. Set permissions for the API client to control the access level to public APIs and data.

The API client in the ODC portal validates the information and generates the client credentials.

1. [Copy the client credentials](create-api-client.md#copy-client-credentials), including the client ID and the client secret.

1. Share the client ID and client secret with the developer.

1. Configure the client credentials in the customer app.

1. From the app, using the client credentials, send a POST request to [request an access token](get-access-token.md).

1. The authorization server validates the credentials and returns an access token with a validity period.

1. Within the validity period, use the access token to [call the ODC REST API](call-api.md).

1. If the access token is valid, the requested data is returned. Else, an error is returned.

## Terminology

### Client Credentials

Unique identifiers required to access the APIs (similar to login + password used for user authentication). The client must authenticate itself with the authorization server using its client credentials (**client ID** and **client secret**)

* The client ID identifies the client accessing the API (software or an app, for example).

* The client secret is essentially a secret password.

### Access token

An access token is a long string of characters that serves as a credential to access protected resources. The access token can be issued with restrictions so that, for example, the app can read but not write or delete data on the resource server. The access token has an expiration period beyond which the token cannot be used to access the APIs.  You must request a new access token when the old token expires.
