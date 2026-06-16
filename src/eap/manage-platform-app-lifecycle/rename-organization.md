---
summary: "Change your organization's display name in the ODC Portal."
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

# Change your organization name

Your organization's display name appears throughout the ODC Portal and in ODC Studio headers. The name is a display label and has no effect on your apps, users, domains, or configurations. It's possible to change it at any time in ODC Portal.

## Prerequisites {#prerequisites}

To change the organization name, you need the [**Manage organization** permission](../user-management/roles.md#permissions-registry).

## Change the organization name {#change-org-name}

To change your organization name, follow these steps:

1. In the ODC Portal, select **Management** > **Organization**.

1. In the **Details** section, in the **Organization name** container, click the elipsys and then **Edit organization name**.
1. Type the new name.

    ![Organization name container in edit mode with a text input field](images/rename-org-edit-pl.png "Edit organization name")

1. Click **Save**.

A toast notification confirms the change and the name updates throughout the portal.

## Organization name rules {#org-name-rules}

The organization name must meet the following requirements:

* Maximum 100 characters.
* Allowed characters: letters, accented letters, numbers, and spaces.
* Additional allowed characters: `. , : ' ( ) - _ & @ # +`

If the name violates one of these requirements, an error message displays inline.
