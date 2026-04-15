---
guid: 60d22645-2be2-4f38-9884-ed1a9cc26f52
locale: en-us
summary: Learn how to use OutSystems APIs to grant organization roles to a user for a specific asset, which gives the requesting team access to a newly created asset.
figma:
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - full stack developers
  - platform administrators
tags: asset permissions, organization roles, access management, rest api, outsystems api
outsystems-tools:
  - odc portal
helpids:
---
# Manage asset permissions

When you create an asset as part of a governed creation process, you must grant access to the user or team that requested it. You do this by assigning an organization role scoped to the newly created asset.

## Prerequisites

Before using the APIs to manage asset permissions, ensure that you have:

* An API client with the **User management > Manage organization access** permission.
  
  For more information, refer to [Edit permissions of API client](../authentication/create-api-client.md#edit-permissions-of-api-client).

* [Generated an access token](../authentication/get-access-token.md) for the API client. Include the token in the `Authorization` header.
* The asset key you want to grant access to.

* The user key of the user you want to grant access to.

## Grant access to a user for a specific asset

To grant access to a newly created asset, follow these steps:

1. Get the list of available organization roles:

    `GET /api/identity/v1/organization-roles`

    From the response, select the role you want to assign and copy its key (`roleKey`).

    For example, select a role that includes **Asset management > Change**.

1. Grant the organization role to the user for the scope of the asset:

    `POST /api/identity/v1/users/{key}/organization-roles/{roleKey}`

    Provide the user key in `{key}` and the organization role key in `{roleKey}`.

    In the request body, set `assetKeys` to an array of asset keys that the role applies to. To scope the role to a single asset, include one asset key.

    ```json
    {
      "assetKeys": ["a111a111-1aa1-1aa1-111a-a1111a1a1a11"]
    }
    ```

After this step, you have granted the user the permissions from the assigned role for that asset.
