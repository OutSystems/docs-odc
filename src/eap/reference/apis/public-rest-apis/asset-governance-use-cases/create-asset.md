---
guid: 85322991-4747-4dbc-b7c1-dd297c35f090
locale: en-us
summary: Learn how to use OutSystems APIs to create a new asset in OutSystems Developer Cloud (ODC), either empty or based on a template.
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
tags: asset creation, asset repository, templates, rest api, outsystems api
outsystems-tools:
  - odc portal
helpids:
---
# Create an asset from scratch or from a template

You can use OutSystems APIs to programmatically create a new asset in your development stage. You create the new asset as an [empty asset](#create-an-empty-asset) or [based on a template](#create-an-asset-based-on-a-template).

## Prerequisites

Before using the APIs to create a new asset, ensure that you have:

* An API client with the **Asset management > Create** permission.
  
  For more information, refer to [Edit permissions of API client](../authentication/create-api-client.md#edit-permissions-of-api-client).

* [Generated an access token](../authentication/get-access-token.md) for the API client. Include the token in the `Authorization` header.

## Create a new asset

To create a new asset, follow one of these procedures:

* [Create an empty asset](#create-an-empty-asset)

* [Create an asset based on a template](#create-an-asset-based-on-a-template)

### Create an empty asset

To create an empty asset, follow these steps:

1. Call:

    `POST /api/asset-repository/v1/assets`

1. In the request body, send `assetCreationDetails` with:

    * `assetName`.
    * `assetType`, set to one of these recognized values: `WebApplication`, `MobileApplication`, `MobileLibrary`, `LowCodeLibrary`, `Agent`, or `Workflow`.
    * `description`.
    * `iconBase64`, if you want to set an icon for the asset.

    ```json
    {
      "assetCreationDetails": {
        "assetName": "MyAssetName",
        "assetType": "LowCodeLibrary",
        "description": "New asset created from scratch"
      }
    }
    ```

1. Copy the `applicationKey` from the response.

    Use the `applicationKey` value to [manage asset permissions](manage-asset-permissions.md).

### Create an asset based on a template

To create an asset based on a template, follow these steps:

1. Get the template key you want to use.

    For more information about retrieving templates, refer to [Get a list of available templates](list-templates.md).

1. Call:

    `POST /api/asset-repository/v1/assets`

1. In the request body, send `assetCreationDetails` with:

    * `assetName`.
    * `assetType`, set to one of these recognized values: `WebApplication`, `MobileApplication`, `MobileLibrary`, `LowCodeLibrary`, `Agent`, or `Workflow`.
    * `templateKey`, set to the template key you selected.
    * `description`.
    * `iconBase64`, if you want to set an icon for the asset.

    ```json
    {
      "assetCreationDetails": {
        "assetName": "MyAssetName",
        "assetType": "Agent",
        "templateKey": "c111c111-1cc1-1cc1-111c-c1111c1c1c11",
        "description": "New asset created from a template"
      }
    }
    ```

1. Copy the `applicationKey` from the response.

    Use the `applicationKey` value to [manage asset permissions](manage-asset-permissions.md).

## Next steps

* [Manage asset permissions](manage-asset-permissions.md)
