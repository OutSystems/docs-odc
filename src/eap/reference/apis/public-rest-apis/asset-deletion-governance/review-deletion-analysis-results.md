---
guid: 5689bcc3-d6ef-4f7e-a5b3-aeed520c2e91
locale: en-us
summary: Learn how to review ODC deletion analysis results, interpret risk severity, and confirm whether an asset is safe to delete.
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
tags: deletion analysis, dependency report, impact assessment, rest api, outsystems api
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# Review the deletion analysis results

The deletion analysis runs asynchronously from the request that triggers it. You must poll for completion and then review the report before approving deletion.

## Prerequisites

Before you review results, ensure that you have:

* An API client with the **Asset management > Delete** permission.

  For more information, refer to [Edit permissions of API client](../authentication/create-api-client.md#edit-permissions-of-api-client).
  
* [Generated an access token](../authentication/get-access-token.md) for the API client. Include the token in the `Authorization` header.

* The `analysisKey` returned when you [perform a deletion analysis](perform-deletion-analysis.md).

## Retrieve and evaluate the analysis report

To review the final report, follow these steps:

1. Call:

    `GET /api/dependency-management/v1/deletion-analyses/{analysisKey}`

1. Check the analysis execution status:

    * `InProgress` means the analysis is still running. Wait a few seconds and call the endpoint again.
    * `Finished` means the analysis completed and includes the report.
    * `Failed` means the analysis did not complete successfully.

1. After the analysis is `Finished`, review the report status:

    * `NoIssuesFound` means no dependency issues were detected.
    * `ErrorsFound` means at least one blocking dependency issue was detected.
    * `WarningsFound` means non-blocking dependency issues were detected and require review.

1. Review the impacted assets list and check each `conflictSeverity`:

    * `Error` indicates a breaking conflict.
    * `Warning` indicates a potential impact that requires validation or refactoring.

1. Approve deletion only when all issues are resolved according to your governance policy.

## Next steps

* [Delete the asset](delete-asset.md)
