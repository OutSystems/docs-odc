---
guid: 5fcd4f00-c8d2-4413-9b00-5a1291c92923
locale: en-us
summary: Learn how to govern asset creation in OutSystems Developer Cloud (ODC) by using ODC REST APIs to list templates, create assets, and manage permissions.
figma:
coverage-type:
  - understand
topic:
  - deployments-api-automation
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - architects
  - tech leads
  - platform administrators
  - full stack developers
tags: asset governance, asset creation, templates, access management, rest api, outsystems api
outsystems-tools:
  - odc portal
  - odc studio
helpids:
---
# Governance model for asset creation

You can use ODC REST APIs to restrict who creates new assets in your development stage and automate approved creation requests. You prevent unapproved assets from accumulating, such as unused or duplicate apps, libraries, agents, and workflows. You keep visibility and control over what assets exist, who owns them, and why you created them.

In this governance model:

* If you are a developer, you submit a request for a new asset.
* If you are an approver, such as an IT architect, you review and approve the request.

## Example governance flow

To implement governed asset creation, follow these steps:

1. Remove the **Asset management > Create** permission from developer roles.

1. Provide a request and approval process for creating new assets, such as an OutSystems app, workflow, or third-party tool.

1. After you approve the request, run your approval automation to create the asset and grant access to the requesting user or team.

## Next steps

To implement the approval automation, follow these API procedures:

1. [Get a list of available templates](list-templates.md) — Identify the template asset key, `templateKey`. Skip this procedure when you create an empty asset.

1. [Create an asset from scratch or from a template](create-asset.md) — Create the asset and copy the asset key, `applicationKey`, from the response.

1. [Manage asset permissions](manage-asset-permissions.md) — Grant an organization role to the requesting user and scope it to the new asset key, `applicationKey`.

## Related resources

* [Using OAuth 2.0 to access public REST APIs](../authentication/using-oauth-access-api.md)

* [Asset Repository API reference](../../asset-v1.md)

* [User and Access Management API reference](../../identity-v1.md)

* [Apply the principle of least privilege](../../../../user-management/best-practices-user-management.md#apply-the-principle-of-least-privilege)
