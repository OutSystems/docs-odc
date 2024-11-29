---
summary: In this article, you will learn how to get an access token using the client credentials.
tags: 
outsystems-tools: 
guid: dae4f96f-cc24-45ef-bec7-26d483c779d2
locale: en-us
app_type: reactive web apps, mobile apps
content-type: 
    - procedure
audience: 
platform-version: odc
figma: 
---
# Get access token 

Once you have the client credentials, you can use the client ID and client secret to generate an access token from the authorization server. This article explains how to get the access token to access the public REST APIs. It is intended for developers who want to access the OutSystems' public APIs.

## Prerequisites

Before requesting an access token, ensure you obtain the client ID and client secret. For more information, refer to [Copy client credentials](create-api-client.md#copy-client-credentials).

## Get access token

To get an access token, follow these steps,

1. Obtain the [Discovery](about-oidc-discovery-document.md) document and the information that it contains by calling the `.well-known` endpoint.

```curl

curl -X GET "https://ODC_PORTAL_DOMAIN/identity/.well-known/openid-configuration" \
-H "accept: application/json"

```
Where

`ODC_PORTAL_DOMAIN` is the domain of your organization

1. Retrieve the `token_endpoint` metadata value from the Discovery document. 

1. Send a POST request to the `token_endpoint` retrieved from Step 2.

<div class="info" markdown="1">

While calling the API from the ODC app, you must manually encode the client secret using the **EncodeURL()** function.

</div>

```curl

curl -ssl -X POST
TOKEN_ENDPOINT \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "grant_type=client_credentials&client_id=CLIENT_ID&client_secret=CLIENT_SECRET" 

```
Where

`TOKEN_ENDPOINT` is the `token_endpoint` retrieved from the Discovery document.

`CLIENT_ID` is the client ID configured in the ODC app.

`CLIENT_SECRET` is the client secret configured in the ODC app.

**Sample Response**

```json

{
  "access_token": "ACCESS_TOKEN",
  "expires_in": 259200,
  "token_type": "Bearer"
}

```

2. The authorization server validates the client credentials received in the request.

If the validation is successful, the authorization server returns an access token. If not, an error message is returned.

<div class="info" markdown="1">

The validity of the access token is 12 hours, irrespective of the expiration date of the client credentials. You can use the access token to access the APIs only until the end of the expiry of the access token. You must ensure that you request a new token before or after the previous token's expiration, as needed.

You are responsible for the keeping the access token safe while it is still valid.

</div>

You can now [call APIs](call-api.md) from the ODC app with a valid access token.

## Next step

[Call API using the access token](call-api.md).
