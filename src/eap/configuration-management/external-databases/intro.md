---
summary: This article explains how to integrate external databases with OutSystems Developer Cloud and how to manage connections and select entities for use in apps.
tags:
locale: en-us
guid: 67608c14-0b83-4e69-bf46-ba023ed730f4
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Integrate with external databases 

OutSystems Developer Cloud (ODC) enables you to integrate external data into your apps. From the ODC Portal, you create connections to the supported databases and use the data in your apps through ODC Studio for selected entities.

<div class="info" markdown="1">

ODC currently supports SQL Server, from version 2016 or later.

</div>

Before you can access data from your external database, you must have the correct access information to create a connection from ODC Portal to your external database. Contact your database administrator to get access information. The apps in ODC can be in several stages, such as Development, QA, and Production. If you want your app to use different databases depending on the stage, you should set up a connection for each stage.

Here is an overview of how to use an external database in ODC:

1. In ODC Portal, **admins** create and test connections to an external database.
2. In ODC Portal, **admins** select the entities and attributes you want developers to use in ODC apps.
3. In ODC Studio, **developers** add the entities as public elements and develop the app.

## Allow developers to manage connections to an external database

By default, only users with the administrator role can manage connections and select entities. If you want to give your developers the same, you need to grant developers the following permissions:

* Edit connection entities
* Manage connections

For more information about users and custom roles, see [User management](../../user-management/intro.md)

## Create and test a new connection

From ODC Portal, select **Configurations** > **Connections** > then click **Create connection** and then select a database provider. After selecting the provider, enter the information about the connection. Testing the connection is required to continue. Click **Test connection** to test the connection. 

* To use the same connection for all stages, enter information about the connection in any stage. Click **Apply to all stages**.
* To use a different database for each stage, click the stage name and enter information about the connection.

![New external database connection](images/new-external-connection-odcs.png)

<div class="info" markdown="1">

Developers can write to your external database if the database user in the connection you created has the write permissions. External database permissions take priority over permissions in ODC. For example, developers can only read data from your database if you have read permission on your external database and read-write permission in ODC.

</div>

### Additional parameters

Use the **Additional parameters** field if you need to include additional parameters for your database connection. For example, you can add `trustServerCertificate=true;`. Separate these values with `;` in the additional parameters field.

## View and edit an existing connection

From the ODC Portal, you can view all connections to the external databases by selecting **Configurations** > **Connections**. 

To edit a connection to an external database, select the connection's name and click **Edit** on the screen that opens.

<div class="info" markdown="1">

You don't have to test your connection again if you modify the name or description in the configuration.

</div>

## Select entities for use in an app

After you create a connection to an external database, you need to select the entity names and attributes you want to be visible in ODC Studio. You can also rename entities. From ODC Portal, select **Configurations** > **Connections** > **Select entities**. In the next screen, select entity names and attributes you want to use. Click **Save** to confirm.

The developers can now use the selected entities and attributes as [public elements](../../building-apps/use-public-elements.md) in their apps.   

## Current limitations

During the tech preview, the following limitations will be addressed:

* CreateOrUpdateSome (Bulk Inserts/Updates) entity action is not supported
* Some data types are not supported in Oracle - BINARY_FLOAT, BINARY_DOUBLE, BFILE, ROWID, UROWID, and XMLTYPE
* When reading from a SQL Server database, images aren't being fetched
* Some OutSystems built-in functions are ready, such as TIMESTAMPADD and Timestamp cast
* DiffMinutes and DiffSeconds built-in functions for Oracle have a limitation regarding the date interval. The allowed max intervals between dates are:
    * Seconds: 31 years, 9 months, 9 days, 1 hour, 46 minutes, and 39 seconds;
    * Minutes: 1901 years, 4 months, 29 days, 10 hours, 39 minutes, and 59 seconds;
* External entities are not supported in Advanced SQL Nodes
* Preview data is not displaying the OS default value data type instead of the Null value
