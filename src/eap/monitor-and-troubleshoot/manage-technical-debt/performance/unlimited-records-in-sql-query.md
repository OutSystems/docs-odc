---
summary: The number of records fetched from the database is not set in the SQL query.
tags: 
guid: d6d8dc05-4263-4561-923c-31e9598f20fc
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3525-270&t=iZQsHW2YE3rUNFK0-1
---

# Unlimited records in SQL query

The number of records fetched from the database isn't set in the SQL query.

## Impact

More records are fetched from the database than are used by the application, resulting in useless I/O and memory consumption.

## Why is this happening?

The issue occurs because the SQL queries fetch all records by default, leading to unnecessary data retrieval and potential performance problems.

![A SQL query without a limit to the number of records fetched.](images/odcs-max-records-sql.png "Unlimited records in a SQL query")

## How to fix

Use `ROWNUM` (for Oracle) or `TOP` (for MS SQL Server) in the SQL query to limit the number of records to the required amount. Note that in SQL queries, the Max. Records parameter only limits the number of records displayed and not the number of records fetched.
