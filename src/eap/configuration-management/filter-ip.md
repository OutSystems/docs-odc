---
summary: ODC Portal lets you filter incoming IP addresses.
tags:
locale: en-us
guid: 269db566-d03b-49ae-84d8-c4aa181d8a88
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/AOyPMm22N6JFaAYeejDoge/Configuration-management?type=design&node-id=3438%3A734&mode=design&t=DiHUqvfiUZQzsSzD-1
platform-version: odc
---

# Configure IP filter 

By default, all apps are publicly available. IP Filters allow you to create rules to restrict the traffic coming into your apps at the network level based on the IP address of the request. For example, you can restrict access to apps in development so that only your developers can access them.

Implementing IP filtering enhances security and reduces the risk of unauthorized access by adding a layer of protection on top of application permissions and governance. To know how ODC is secure by design, see [Security of OutSystems Developer Cloud.](../security.md)

Only users with **Manage IP Restrictions** permissions can create, edit, and delete IP filter rules.
Create an IP filter

## Create an IP filter

By creating an IP Filter, ODC will block all traffic except traffic that originates from the IP Addresses defined in the IP Filter. To create an IP filter, follow these steps:

1. Go to the ODC Portal and select **Configurations** > **IP filters** from the Navigation menu.<br/> The IP filter screen is displayed.
1. Select the stage such as Developement or Production.
1. Click **Create IP filter** to display the form.
    ![IP filters](images/ip-filter-odcs.png)
1. In the IP filter form, enter the required information in the **Name**, **Description**, and **IP address/range**.<br/> ODC validates:
    * The uniqueness of each filter name.
    * The correct IP address/range format, such as IPv4 and IPv6.
1. Click **+** to add the IP address or range of IP addresses, and then click **Save**
    * A confirmation popup is displayed.
1. Click **Create** 
    * The updated list of IP filters is displayed.

You can define up to 20 IP addresses/ranges per rule.

## Edit an IP filter

You can edit the **Name**, **Description**, and **IP address/range** of an IP filter. To edit an existing IP filter, follow these steps:

1. Go to the ODC Portal and select **Configurations** > **IP filters** from the Navigation menu.<br/> The IP filter screen is displayed.
1. In the list, select the IP filter you want to edit.
1. Click **Edit** to change the values in the form. <br/> ODC validates:
    * The uniqueness of each filter name.
    * The correct IP address/range format, such as IPv4 and IPv6.
1. Click **Save**.
1. Click **Save** again.
    * The updated list of IP filters is displayed.

## Delete an IP filter

To delete an existing IP filter, follow these steps:

1. Go to the ODC Portal and select **Configurations** > **IP filters** from the Navigation menu.<br/> The IP filter screen is displayed.
1. Find the IP filter you want to edit, and select it from the list of filters.
1. Click the ellipsis (3-dots) to the right of the IP filter name, then click the **Delete** button to display a confirmation popup.
1. Click **Delete** again to display the list of IP filters without the deleted filter.

<div class="info" markdown="1">

The feature mentioned in this article requires the subscription of an add-on to the ODC Platform edition. Please contact your OutSystems account team for more information.

</div>
