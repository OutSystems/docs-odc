---
summary: OutSystems Developer Cloud (ODC) considerations for connecting to SQL Server, including the database permissions the connection user needs.
tags:
  - External Databases
  - Optimization
  - Performance
  - SQL
  - Security
guid: 99281097-4322-4282-ac59-be6ba532600d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - odc portal
content-type:
  - reference
audience:
  - Developer
  - Platform administrator
coverage-type:
  - understand
topic:
  - sql-server-connections
isautopublish: true
---

# SQL Server connection considerations

Review the following consideration for a SQL Server connection. For information about creating or editing the connection, refer to [Create connections to external data sources](create-connection-external-data.md).

## Database user permissions

The database user of a SQL Server connection must have the following permissions on the connected database. ODC uses them to read the approximate row count of each table and optimize queries.

* **SQL Server 2019 and earlier:** `VIEW DATABASE STATE` and `VIEW DEFINITION`
* **SQL Server 2022 and later:** `VIEW DATABASE PERFORMANCE STATE` and `VIEW SECURITY DEFINITION`
