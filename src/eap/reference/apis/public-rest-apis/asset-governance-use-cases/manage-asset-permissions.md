---
guid: 60d22645-2be2-4f38-9884-ed1a9cc26f52
locale: en-us
summary: "ODC asset permissions REST API: grant an organization role to a user for a specific asset by calling the OutSystems identity API."
figma:
coverage-type:
  - apply
topic:
  - manage-asset-permissions
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Developer
  - Platform administrator
tags:
  - Authorization
  - IT Teams
  - REST
  - Roles
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---
# Manage asset permissions

When you create an asset as part of a governed creation process, you must grant access to the user or team that requested it. You can do this in the following ways:

* Assign an organization role to a user, scoped to the newly created asset.
* Add the asset to a team, so that every member of the team holds their team role on the asset.

Permissions from the organization, team, and asset scopes add up. A role at one scope doesn't remove what a role at another scope grants.

## Prerequisites

Before using the APIs to manage asset permissions, ensure that you have:

* An API client with the following permissions:
    * **User and access management > Manage member access**, to grant an organization role scoped to the asset.
    * **User and access management > Manage teams**, to add the asset to a team or change the members of a team.
  
    For more information, refer to [Edit permissions of API client](../authentication/create-api-client.md#edit-permissions-of-api-client).

* [Generated an access token](../authentication/get-access-token.md) for the API client. Include the token in the `Authorization` header.
* The asset key you want to grant access to.

* The user key of the user you want to grant access to.

* The team key of the team you want to grant access to, if you grant access through a team.

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

## Grant access through a team

To give every member of a team access to the asset, add the asset to the team. Each member holds their team role on every asset that the team owns. For more information about adding the asset to a team, refer to [Add the asset to a team](create-asset.md#add-the-asset-to-a-team). For more information about teams, refer to [Teams and asset ownership](../../../../user-management/it-users/teams.md).

To add, update, or remove the members of a team, use the [`PATCH /teams/{key}/members`](../../identity-v1.md#patch-/teams/-key-/members) endpoint.
