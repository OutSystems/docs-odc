---
summary: How to find and use the subscription console in ODC.
locale: en-us
guid: 504cdfa5-68d4-46ce-8363-e08aa05e4514
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
tags: subscription management, application management, user management, permission control, licensing
audience:
  - platform administrators
  - full stack developers
outsystems-tools:
  - odc portal
coverage-type:
  - remember
---

# Subscription console

The subscription console is a centralized hub for viewing application objects (AOs), end-users, and add-ons. To access the subscription console, sign in the ODC Portal, click the **Organization** dropdown, and select **Manage Subscriptions**.

<div class="info" markdown="1">

The subscription console is only accessible to users with the **View subscription** permission in ODC Portal.

</div>

## Overview tab

The **Overview** tab provides visibility of the total usage of AOs and the number of internal and external end-users. 

## Application Objects tab

The [Application Objects](https://success.outsystems.com/support/licensing/application_objects/) tab provides a detailed breakdown of AOs per stage within a tenant. When you click on a specific stage, you can view the number of AOs consumed by each app within that stage. This feature aids in better managing AO usage and more effectively planning deployments.

## End-users tab

The **End-users** tab has a form for maintaining internal end-user domains and provides visibility of the number of internal and external users. 

## Add-ons tab

The **Add-ons** tab provides visibility of the add-ons to which the organization is subscribed and add-ons that are available for subscription.
