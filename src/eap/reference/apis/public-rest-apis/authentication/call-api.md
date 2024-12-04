---
summary: Discover how to call APIs in OutSystems Developer Cloud (ODC) using an access token, with step-by-step guidance for developers.
tags: 
outsystems-tools: 
guid: 850e2e06-cdab-4e45-9ea6-2964c1a3a5ce
locale: en-us
app_type: reactive web apps, mobile apps
content-type: 
    - procedure
audience: 
platform-version: odc
figma: 
---

# Call API using the access token

Once the authorization server validates the credentials and generates an access token, you can call the APIs using the access token. The access token is valid only for 12 hours from the time it was generated. Use the access token within the validity period of to access the APIs.

Once the token expires, you must generate a new access token to call the API. This article explains how to call an API using the access token. It is intended for developers who want to access the ODC REST APIs from their app.

## Prerequisites

Before calling the API using the access token, ensure you have:

* Set the client credentials in the app

* [Generated the access token](get-access-token.md) using the client credentials

## Call API

With the access token, you are ready to make your first API call.

Here’s an example of the List users API, which retrieves a list of users who have been assigned an application role.

```curl

curl -X GET "https://ODC_PORTAL_DOMAIN/api/identity/v1/users?hasApplicationRoles=true&limit=10&offset=0" -H "Authorization: Bearer ACCESS_TOKEN"

```

Where 

`ODC_PORTAL_DOMAIN` is the domain of your Organization

`ACCESS_TOKEN` is the access token retrieved using the client credentials

## Next step

[User management API reference](../../identity-v1.md)
