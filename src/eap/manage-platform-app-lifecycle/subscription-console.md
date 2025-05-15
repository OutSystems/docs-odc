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

The subscription console has three main areas. 

* **Subscription information.** This displays your Edition, End-date, and Activation code.
* **Overview tab**. This gives you a birds-eye view of all relevant parameters of your subscription.
* **Add-ons tab**. This gives you information on the available add-ons and if you have subscribed them or not.

Your organization has allocated resource limits for runtime resources. These capacities, defined by your subscription, determine the maximum usage limits for each resource. For more information, refer to [Monitor ODC resource capacity](..//getting-started/capacity-limits.md).

## Overview tab

The **Overview** tab provides visibility of all your relevant consumptions, namely:

* [Application Objects](https://www.outsystems.com/tk/redirect?g=cd994c70-9dcc-46ed-b423-84099beac39a). You can see your overall application objects count, and consumption, on your Production stage. If you click in it, the detailed view will appear, where you can see information by stage and by asset.
* [Compute instances](../getting-started/capacity-limits.md#resource-limits). Here you can the total number of instances, and consumption, that are available to be used for all apps. In the detailed view you can see the number of consumed/available instances by stage, and filter by asset and by time.
* [Custom code execution duration](../getting-started/capacity-limits.md#resource-limits). This displays the amount of time, in seconds, and the consumption, that all custom code functions in a stage can execute per day. In the details you can see this information by stage and filter by Libraries and by time.
* [Database compute](../getting-started/capacity-limits.md#resource-limits). Displays the amount of compute resources allocated to the database, and consumption, that is shared across all apps. In the details you can see the information by stage and filter it by time.
* [Database storage](../getting-started/capacity-limits.md#resource-limits). Displays the amount of storage allocated to the database and consumption, that is shared across all apps. In the details you can see the information by stage and filter it by time.
* [External end users](https://www.outsystems.com/tk/redirect?g=907b0fd3-bc46-4391-aae2-673296d795d9) and [Internal end users](https://www.outsystems.com/tk/redirect?g=907b0fd3-bc46-4391-aae2-673296d795d9). Displays the number of external end users available and consumed in your Production stage. In the details you can define [your user domains](../user-management/classify-users.md) to manage your users correctly.

<div class="info" markdown="1">

To access the details page of each component, click on the corresponding panel.

</div>

## Add-ons tab

The **Add-ons** tab provides visibility of the add-ons to which the organization is subscribed and add-ons that are available for subscription.
