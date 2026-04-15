---
guid: d185cdff-480f-479b-b2e2-2a93b24bf92b
locale: en-us
summary: This article explains how to generate and reuse OAuth access token when you consume an external API that use OAuth 2.0 authorization.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7721-1015
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - mobile developers
tags: oauth 2.0, access token, api authentication, rest api, authorization grant
outsystems-tools:
  - odc studio
helpids:
---
# Generate and reuse OAuth access token

To consume an external API with OAuth 2.0, you must obtain an access token. You can get this token by obtaining the authorization grant details, such as the client credentials—client ID and client secret and exchanging the grant for an access token. This access token can then be used to make authenticated API calls. For detailed information about the different authorization grant types and OAuth authorization flow, refer to the [OAuth 2.0 Authorization Framework.](https://datatracker.ietf.org/doc/html/rfc6749)

The authorization grant type depends on the authorization flow implemented by the external API.

This article is intended for developers who know how to build apps and consume REST APIs in ODC.

OutSystems recommends that you encapsulate the logic for generating access tokens in a separate server action in a library so that it can be reused across all apps. To explore a sample library, refer to OpenID Connector in [ODC User Management Forge](https://www.outsystems.com/forge/component-overview/21016/users-management-odc) component.  

This diagram represents a detailed client credentials grant flow for an authenticating a REST API. It illustrates the entire lifecycle of an access token, from its initial generation and storage to its use in API calls.

![Diagram showing the OAuth 2.0 client credentials grant flow for generating and reusing access tokens in API calls.](images/access-token-flow-diag.png "OAuth 2.0 Client Credentials Grant Flow Diagram")

Here’s the development pattern that you can use to consume external REST APIs that use OAuth 2.0 client credentials grant flow authorization.

## Get authorization grant details

Obtain the OAuth 2.0 authorization grant details from the external API provider. This includes:

Client ID: Your app's unique identifier.

Client Secret: A confidential key used to authenticate your app.

Authorization Grant Type: Name of the authorization grant type such as **client credentials** or **authorization code**

For detailed information about obtaining the authorization grant details, always refer to the API documentation of the external API.

**Example:**

Let's assume you're consuming a hypothetical "SuperService API" and have obtained the following:

Client ID: client_id_123

Client Secret: client_secret_xyz

Grant Type: client_credentials

## Get token endpoint

Retrieve the API token endpoint (`/token`). The token endpoint is required for securely exchanging the authorization grant for access tokens and optionally refreshing tokens. For detailed information about how to retrieve the token endpoint, refer to the external API documentation of the external API.

**Example:**

For the example SuperService API the token endpoint might be:

`https://api.superservice.com/v1/oauth/token`

## Generate access token

To generate the access token, make a POST request to the token endpoint and pass the authorization grant credentials and name of the authorization grant.

**Example:**

If the API uses the `client_credentials` grant type, you must send the `client_id`, `client_secret`, and `grant_type` in the request body.

```curl

curl -X POST \
  https://api.superservice.com/oauth/token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=client_credentials&client_id=client_id_123&client_secret=client_secret_xyz'

```

**Expected Response:**

A successful response returns a JSON object containing the access_token, token_type, expires_in (the token's lifetime in seconds), and sometimes a refresh_token.

```json

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "read write",
  "refresh_token": "some_long_refresh_token_string"
}

```

## Encrypt and store the access token

To prevent unauthorized access and enable token reuse, store the access token in an encrypted format in a secure storage and reuse it as long as it has not expired. If the access token expires, use the refresh token to obtain a new one or generate a new one.

OutSystems recommends that you store the access token in an entity in an encrypted format.

## Reuse of token

For each subsequent API call:

1. Retrieve the stored access token from the entity and its expiry time.

1. Check token validity by comparing the `expires_in` timestamp with the current time.

   * If the token has expired:
     * Mark the existing token as invalid.
     * Generate a new access token.
       * Using Refresh Token: If the API provided a `refresh_token`, use it to obtain a new access token without requiring user re-authentication.
       * Initiate new flow: If no refresh token is available, initiate a new access token flow.

   * If the token is still valid:
     * Decrypt the stored access token.

1. Use the decrypted token in your API request.

### Pass the token in the API call

Once you have the token, you can include it as a **Bearer** token in the **Authorization** header of your API request.

Use the **OnBeforeRequest** callback to dynamically add or update the token to the HTTP request header before sending the request. For detailed information, refer to [Example use case: Adding a header for token-based authentication](simple-customizations.md#example-use-case-adding-a-header-for-token-based-authentication).

## Related resources

### ODC REST API access token generation

* [Get access token](../../reference/apis/public-rest-apis/authentication/get-access-token.md)

### Add token to the header and consume the API

* [Customize API request and response headers](simple-customizations.md)

* [Use API in your app](consume-a-rest-api.md#use-a-rest-api-method-in-your-app--use-)

### Online training

* [Consuming REST APIs ODC Online training](https://learn.outsystems.com/training/journeys/consuming-rest-api-207) online course
