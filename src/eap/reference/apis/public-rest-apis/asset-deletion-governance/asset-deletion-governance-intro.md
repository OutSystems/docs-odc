---
guid: cde1c2dd-df56-4c0b-923d-f1fb26c2a3f9
locale: en-us
summary: Learn how to implement a safe, governed process for deleting assets in OutSystems Developer Cloud (ODC) by using deletion analysis and controlled approval.
figma:
coverage-type:
  - understand
topic:
  - deployments-api-automation
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Architect
  - Tech lead
  - Platform administrator
  - Developer
tags: asset governance, asset deletion, dependency analysis, risk management, rest api, outsystems api
outsystems-tools:
  - odc portal
  - odc studio
helpids:
isautopublish: true
---

# Asset deletion governance

You can use ODC REST APIs to implement a safe and governed process for deleting assets in your organization. The APIs automate the deletion analysis and the deletion itself, reducing the risk of broken dependencies and unintended impact on apps, libraries, agents, and workflows.

In this governance model:

* If you are a developer, you submit a request to delete an asset that is no longer needed.
* If you are an approver, such as an IT architect, you review and approve the request.

## Example governance flow

To implement governed asset deletion, follow these steps:

1. Remove the **Asset management > Delete** permission from developer roles.

1. Provide a request and approval process for deleting assets, such as an OutSystems app, workflow, or third-party tool.

1. For each delete request, run your approval automation to analyze the impact and review the results before approving and deleting the asset.

## Proactive governance - identify obsolete assets

In addition to handling manual deletion requests, you can automate technical debt discovery by identifying unmaintained assets.

A common governance practice is to flag assets with no activity for more than 180 days. Then, submit the flagged assets as deletion candidates and run them through the same deletion analysis workflow before approval.

## Next steps

To implement the approval automation, follow these API procedures:

1. [Perform a deletion analysis](perform-deletion-analysis.md) — Trigger an analysis and copy the `analysisKey`.

1. [Review the deletion analysis results](review-deletion-analysis-results.md) — Poll analysis status and evaluate conflicts.

1. [Delete the asset](delete-asset.md) — Delete the asset when analysis indicates no unresolved risks.

## Related resources

* [Using OAuth 2.0 to access public REST APIs](../authentication/using-oauth-access-api.md)

* [Asset Repository API reference](../../asset-v1.md)

* [Dependency Management API reference](../../dependency-v1.md)

* [Apply the principle of least privilege](../../../../user-management/best-practices-user-management.md#apply-the-principle-of-least-privilege)
