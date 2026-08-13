---
summary: "Change your organization's or a stage's display name in the ODC Portal."
locale: en-us
guid: a7b8d6e7-352f-4237-9d05-69e548098a42
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=5060-10
audience:
  - Platform administrator
outsystems-tools:
  - odc portal
coverage-type:
  - apply
topic:
tags:
  - Settings
isautopublish: true
---

# Change your organization or stage name

Your organization and each of your stages have a display name that appears throughout the ODC Portal and in ODC Studio headers. A display name is a label only. Changing it has no effect on your apps, users, domains, or configurations. You can change either name at any time in the ODC Portal.

You can also [change the order of the stages in the pipeline](reorder-stages.md).

## Prerequisites {#prerequisites}

| Action | Permission required |
| --- | --- |
| Change the organization name | **Manage organization** |
| Change a stage name | **Manage stage** |

Organization names must not exceed 100 characters.
Stage names must not exceed 50 characters.

## Change the organization name {#change-org-name}

To change your organization name, follow these steps:

1. In the ODC Portal, select **Management** > **Organization**.

1. In the **Details** section, in the **Organization name** container, click the elipsys and then **Edit organization name**.
1. Type the new name.

    ![Organization name container in edit mode with a text input field](images/rename-org-edit-pl.png "Edit organization name")

1. Click **Save**.

A toast notification confirms the change and the name updates throughout the portal.

## Change a stage name {#change-stage-name}

Rename a stage when its display name no longer matches your organization's naming convention or SDLC process, for example after adopting different stage names for your pipeline.

To rename a stage, follow these steps:

1. In the ODC Portal, select **Management** > **Organization**.
1. On the **Stages** section, click the ellipsis `(...)` next to the stage you want to rename and select **Edit stage name**.
1. Type the new name.
1. Click **Save**.

A toast notification confirms the change. The new name appears throughout the ODC Portal and ODC Studio immediately. Renaming a stage doesn't log out users or affect running apps.

### Stage name rules {#stage-name-rules}

<!-- TK TODO: confirm actual character limit and allowed characters for stage names; not yet confirmed in any source available this session. Don't publish a guessed limit. -->

You can also rename a stage programmatically through the [Portfolio API](../reference/apis/portfolio-v2.md). Before scripting stage changes, review the [automation and integrations considerations](reorder-stages.md#automation).
