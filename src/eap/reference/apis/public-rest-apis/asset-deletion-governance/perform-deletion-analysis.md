---
guid: 8edc6991-b367-4f0d-8c84-7797285a6d13
locale: en-us
summary: Learn how to trigger an asset deletion analysis in ODC and capture the analysis key for dependency impact review.
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
tags: asset deletion, deletion analysis, dependency management, rest api, outsystems api
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---
# Perform a deletion analysis

You can use OutSystems APIs to evaluate the impact of deleting an asset before performing the deletion. This analysis helps you avoid breaking dependencies in your environment.

## Prerequisites

Before you trigger a deletion analysis, ensure that you have:

* An API client with the **Asset management > Delete** permission.

  For more information, refer to [Edit permissions of API client](../authentication/create-api-client.md#edit-permissions-of-api-client).

* [Generated an access token](../authentication/get-access-token.md) for the API client. Include the token in the `Authorization` header.

* The `assetKey` of the asset you plan to delete.

## Trigger a deletion analysis

To check dependencies and potential blockers, follow these steps:

1. Call:

    `POST /api/dependency-management/v1/deletion-analyses`

1. In the request body, provide the target `assetKey`:

    ```json
    {
      "assetKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11"
    }
    ```

1. Copy the `analysisKey` from the response.

    Use the `analysisKey` value to [review analysis results](review-deletion-analysis-results.md).

## Next steps

* [Review the analysis results](review-deletion-analysis-results.md)
