---
summary: This article explains how to suspend and resume access to an API client.
tags: api client management, suspend api access, resume api access, outsystems, odc portal
outsystems-tools:
  - odc portal
guid: 45df5a2d-a458-4597-a7e4-a1457ee065fd
locale: en-us
app_type: reactive web apps, mobile apps
content-type:
  - procedure
audience:
  - platform administrators
platform-version: odc
figma:
---
# Suspend and resume access to API Client

You can suspend and resume access to an API client at any time. Once you suspend access to an API client, the access token associated with the API client immediately becomes invalid and can no longer be used to access the APIs. For continued API access, you must resume access to the API client. This article is intended for administrators who govern and manage who can access to OutSystems APIs and data. 

## Prerequisites

Before suspending and resuming access to the API client, ensure you have:

* Access to the ODC portal with **Manage API Client** permissions.

## Suspend and resume access

To suspend and resume access to the API client, follow these steps:

1. Log into the ODC portal.

1. Under **Manage**, click **API clients**. A list of API Clients is displayed.

1. From the API Client list, click the API Client to be suspended. The API Client details page is displayed.

1. Click **Suspend access**.

A dialog box pops up to check if you want to suspend access to the API client.

1. Click **Suspend access**

When you suspend an API client:

* all secrets and access tokens become invalid immediately,

* you cannot access the API using the access token, and 

* the status of the API client changes to **Suspended**.

To resume access to the API client, from the API Client details page, click **Resume access.**

When you resume access to the suspended API client:

* If the secret has not expired, the secret and access token become valid, and you can use the same token to access the APIs. The status of the API client changes to **Available**.

* If the secret has expired, the access token remains valid up to 12 hrs from the time it was generated regardless of the secret's expiration, and the status of the API client changes to **Expired**. For continued API access, you must now [generate a new client secret](generate-new-secret.md) and use the new credentials to generate an access token.

<div class="info" markdown="1">

To delete the suspended API client, on the API Client details page, click the ellipsis menu and select **Delete API Client**. 

</div>

## Next steps

* [Generate a new client secret](generate-new-secret.md)

* [Get access token using client credentials flow](get-access-token.md)

