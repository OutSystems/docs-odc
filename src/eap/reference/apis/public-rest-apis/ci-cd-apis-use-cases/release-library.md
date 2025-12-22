---
guid: 88fba3ad-12e0-41fa-9495-8693c9ec462b
locale: en-us
summary: Learn how to use OutSystems APIs to programmatically release a library.
figma:
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: library release, api usage, outsystems apis, asset management, release management
outsystems-tools:
  - odc portal
helpids:
---
# Releasing a library

This article explains how to use OutSystems APIs to programmatically release a library. To release a library, whether it is an OutSystems library or an external library, you must tag a revision of that library.

## Prerequisites

Before using APIs to release a library, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) from an API client with these [permissions](../authentication/create-api-client.md#edit-permissions-of-api-client):  
    * [Asset management > Change](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/asset_repository_api/#patch-/assets/-assetKey-/revisions/-revisionNumber-)
    * [Release management > Release](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/asset_repository_api/#patch-/assets/-assetKey-/revisions/-revisionNumber-)  
* The [revision number](select-revision-build.md#select) you want to release  
* The key of the library to be deployed

## Release your library

To release your library, you must tag the revision you want to release:

`PATCH /api/asset-repository/v1/assets/{assetKey}/revisions/{revisionNumber}`

Pass the `assetKey` and `revisionNumber`.  

In the body, pass the `tag`. Example:

    {
    "tag": "<release version>",
    "releaseNotes": "<(optional) release notes>",
    "commitMessage": "<(optional) commit message>"
    }
