---
summary: In this article you will learn how to make your first API call.
tags: 
outsystems-tools: 
guid: 316cc17e-0e09-482e-87b1-e9e6d4f483ce
locale: en-us
app_type: reactive web apps, mobile apps
content-type: 
    - process
audience: 
platform-version: odc
figma: 
---

# Getting started

This article describes how to get started with the ODC REST APIs, including how to authenticate and make secure calls to these APIs.

## Prerequisites

Before making your first API call, ensure you have:

1. Access to ODC portal to [create an API client](authentication/create-api-client.md). The API client in the ODC portal allows you to create an API account and generate 
OAuth 2.0 client credentials that you can use in exchange for the access token. For more information, refer to [About the API client](authentication/about-api-client.md).

1. Valid [client credentials](authentication/create-api-client.md#copy-client-credentials). The OAuth 2.0 client credentials include the client ID and client secret copied from the API client.

## Get your access token

To use the ODC REST API, you need an access token. 
With the client credentials, [get a valid access token](authentication/get-access-token.md).

## Make your first API call

With the access token you are ready to make your first API call.

Here's an example:

Here’s an example of the List users API, which retrieves a list of users who have been assigned any application role.

```curl

curl -X GET "https://ODC_PORTAL_DOMAIN/api/identity/v1/users?limit=10&offset=0"
-H "Authorization: Bearer ACCESS_TOKEN"

```

Where,

ODC\_PORTAL\_DOMAIN is the domain of your organization

ACCESS\_TOKEN is the access token retrieved using the client credentials

## Next step

- Refer [User management API reference](../identity-v1.md)

## Additional resources

* [Create API client](authentication/create-api-client.md)

* [Copy client credentials](authentication/create-api-client.md#copy-client-credentials)

* [Get access token](authentication/get-access-token.md)




