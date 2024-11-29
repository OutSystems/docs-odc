---
summary: In this article, you will learn about generating new secret for an API client.
tags: 
outsystems-tools: 
guid: cb9abd38-9a1e-4524-a7ec-c154eb710d83
locale: en-us
app_type: reactive web apps, mobile apps
content-type: 
    - procedure
audience:  
platform-version: odc
figma: https://www.figma.com/design/eFzsh8ZIP5AIbRUyjeTV26/Reference?node-id=3504-23&t=Ee0vNUQza7lfj7Sy-1
---

# Generate client secret

You can generate a new client secret for an API client if:

* You didn’t copy the client secret initially.

* The current secret is nearing expiration or has expired.

The client ID however, remains unchanged.

Once a new client secret is generated:

1. You must update the ODC app with the new secret.

1. Use the new credentials to generate a fresh access token.

The old access token remains valid for only up to 72 hrs after it was issued, regardless of the client secret’s expiration date.

Each API client can have only one client secret at a time.

##  Prerequisites

Before generating a new secret for a client ID, ensure the API client has already been created in the ODC portal.

## Generate secret

To generate a new secret, follow these steps:

1. Select the API client for which you need to generate a new secret.

1. Under Credentials, click **Generate new secret**.

1. Click **Generate new secret** on the pop-up.

    ![Pop-up window for generating a new client secret, warning that it will deactivate the current one and cut off API access for the app. It includes options to set expiration, reminders, and buttons to cancel or generate the new secret.](images/generate-new-secret-pl.png "Generate New Client Secret Pop-up")

Now, [copy the client secret](./create-api-client.md#copy-client-credentials) immediately and store it securely, as you won't be able to retrieve it once you leave the client credentials page.

## Next step

[Get access token using client credentials flow](get-access-token.md)
