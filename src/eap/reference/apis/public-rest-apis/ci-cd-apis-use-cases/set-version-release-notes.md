---
guid: d4bc5676-5fc9-4729-94c1-519b07daa7e8
locale: en-us
summary: Learn how to use OutSystems APIs to programmatically set the release version and the release notes before deploying your asset to production.
figma: https://www.figma.com/design/eFzsh8ZIP5AIbRUyjeTV26/Reference?node-id=4766-2&t=Y641MIoDIVqm9IxN-1
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: release version, release notes, api usage, deployment automation, outsystems apis
outsystems-tools:
  - odc portal
helpids:
---
# Setting the release version and release notes

This article explains how to use OutSystems APIs to programmatically set the release version and the release notes before deploying your asset to production. By locking the exact revision, enabling reliable rollbacks, and clearly communicating what changes were made between releases, you make each deployment traceable and auditable.

## Prerequisites

Before using the APIs to set the release version and release notes, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) with these [permissions](../authentication/create-api-client.md#edit-permissions-of-api-client):
    * [Asset management > Change](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/asset_repository_api/#patch-/assets/-assetKey-/revisions/-revisionNumber-)
    * [Release management > Release](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/asset_repository_api/#patch-/assets/-assetKey-/revisions/-revisionNumber-)  
* The [revision number](select-revision-build.md#select) you want to deploy  
* The key of the asset to be deployed

    <div class="info" markdown="1">

    To get the asset key, go to **Portal** > **Apps**, and select the asset you want to deploy. In the URL, copy the asset key after "application?id=", as shown in this example:

    ![Screenshot of the ODC Portal showing how to retrieve the asset key from the asset URL](images/asset-key-pl.png "Get the asset key")

    You can also retrieve the asset key programmatically, using `GET /api/asset-repository/v1/assets` with the necessary filters.

    </div>

## Set the release version and release notes

Before deploying to production, define a release version and release notes, and tag the revision you want to deploy with that version and those release notes. Follow these steps:

1. The next version to tag needs to be higher than the current one. To check the current version, look up the highest version tagged:

    `GET /api/asset-repository/v1/assets/{assetKey}/highest-tag-revision`

1. To define the next version, calculate it automatically or prompt the user to define it. Also define the release notes, and then patch the revision:

    `PATCH /api/asset-repository/v1/assets/{assetKey}/revisions/{revisionNumber}`

    In the body, pass the release version and the release notes:

        {
        "tag": "<release version>",
        "releaseNotes": "<release notes>"
        }

## Next steps

* [Reviewing asset configurations](asset-configurations.md)
* [Deploying your asset to the target stage](deploy-asset.md)
