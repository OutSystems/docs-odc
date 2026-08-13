---
guid: 19916f2e-8305-4386-96e7-e928173daa9e
locale: en-us
summary: Learn how to delete an asset in ODC using REST APIs after validating deletion analysis results.
figma:
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Architect
  - Tech lead
  - Platform administrator
  - Developer
tags: asset deletion, asset repository, irreversible operation, rest api, outsystems api
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# Delete the asset

After you confirm the deletion analysis results, you can permanently remove the asset from your ODC organization.

## Prerequisites

Before deleting an asset, ensure that you have:

* An API client with the **Asset management > Delete** permission.

  For more information, refer to [Edit permissions of API client](../authentication/create-api-client.md#edit-permissions-of-api-client).

* [Generated an access token](../authentication/get-access-token.md) for the API client. Include the token in the `Authorization` header.

* The `assetKey` of the target asset.

* A completed deletion analysis with no unresolved risks according to your governance policy.

## Delete the target asset

<div class="warning" markdown="1">

Deleting an asset is irreversible. This action permanently removes the asset, including its revisions and related data.

</div>

To delete the asset, follow these steps:

1. Call:

    `DELETE /api/asset-repository/v1/assets/{assetKey}`

1. Replace `{assetKey}` with the identifier of the asset you approved for deletion.

1. Confirm a successful response with status code `204 No Content`.

After this step, the asset and its historical data are permanently removed from your ODC organization.
