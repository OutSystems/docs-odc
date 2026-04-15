---
guid: 16289dfd-ab8f-4714-879c-d744865c094a
locale: en-us
summary: Learn how to use OutSystems APIs to retrieve a list of available application templates that you use as a starting point when creating a new asset.
figma:
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: templates, asset creation, asset repository, rest api, outsystems api
outsystems-tools:
  - odc portal
helpids:
---
# Get a list of available templates

You can use OutSystems APIs to retrieve the list of available templates you use as a starting point when creating a new asset. The list includes built-in templates and templates created in your organization.

## Prerequisites

Before using the APIs to get the list of available templates, ensure that you have:

* An API client with the **Asset management > Open** permission.
  
  For more information, refer to [Edit permissions of API client](../authentication/create-api-client.md#edit-permissions-of-api-client).

* [Generated an access token](../authentication/get-access-token.md) for the API client. Include the token in the `Authorization` header.

## Get the list of template assets

You identify templates by filtering the asset repository for assets marked as templates.

To get the list of template assets, follow these steps:

1. To list application templates, use:

    `GET /api/asset-repository/v1/assets?metadata.templateType=ApplicationTemplate`

1. To filter results by asset type, repeat the `assetTypes` query parameter. For example:

    `GET /api/asset-repository/v1/assets?metadata.templateType=ApplicationTemplate&assetTypes=WebApplication&assetTypes=Agent`

1. From the response, select the template asset you want to use as a starting point, and copy its `key` value.

    Use this value as the `templateKey` when you [create an asset from scratch or from a template](create-asset.md).

## Next steps

* [Create an asset from scratch or from a template](create-asset.md)
