---
summary: Execute stored procedures from external entities using SQL nodes in OutSystems Developer Cloud (ODC) by obtaining a connectionId from Portal and using the CALL statement.
tags: stored procedures, external entities, sql nodes, odc, database integration
guid: d125e70b-1ef0-4f4e-a7df-070a396ddfad
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7307-1657
audience:
  - backend developers
  - full stack developers
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Call stored procedures from external entities

You can use the [CALL](call.md) statement of ANSI-92 syntax in SQL nodes to execute stored procedures. This is supported when you're using external entities from [connections](../../../../integration-with-systems/external-databases/create-connection-external-data.md)

* Microsoft SQL Server  
* Oracle  
* PostgreSQL

Stored procedures let you reuse logic defined in your external database. They're useful for encapsulating business rules, performing updates, or returning result sets that can be used in your OutSystems logic.

Stored procedures can’t be created or called for internal entities (the entities created in ODC Studio).

The `CALL` statement requires a `connectionId` that identifies the [connection to the data source done in Portal](../../../../integration-with-systems/external-databases/create-connection-external-data.md). 

Follow these steps to retrieve the connectionId from Portal:

1. Under **Integrate** \> **Connections** click on the connection that you’ll use to call the stored procedure. You’ll reach the connection detail:

    ![OutSystems Data Cloud interface showing the connection detail page for Northwind DB.](images/connection-id-pl.png "Connection Detail Page")

1. Click **…** and **Copy connection ID**. The connectionId is now copied to your clipboard.

    ![OutSystems Data Cloud interface showing the option to copy the connection ID for Northwind DB.](images/copy-connection-id-pl.png "Copy Connection ID")

1. Use the connectionId in your query to call stored procedures. For more details see [CALL](call.md).
