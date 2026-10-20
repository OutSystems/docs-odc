---
summary: PostgreSQL connections in OutSystems Developer Cloud (ODC) explain empty text values and default-value overwrites for nulls.
tags:
  - Data
  - Data Integrity
  - External Databases
guid: 5ca273e2-2a90-40ac-b99b-a04644352198
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
  - apply
  - unblock
topic:
  - postgresql-empty-text
isautopublish: true
---

# PostgreSQL connection considerations

Review the following consideration for a PostgreSQL connection, which covers null handling for empty text values and the data types it affects. For information about creating or editing the connection, refer to [Create connections to external data sources](create-connection-external-data.md).

## Null handling for empty text values

For PostgreSQL connections, you may encounter issues in Text data type columns when inserting an empty value, and the connection is configured to overwrite null values with default values. OutSystems recommends you set a different default value to columns of these data types, such as for Time: 00:00:00 or for Float: 0.

For more information about configuring null value handling, refer to [Handle null values](handle-null-values.md).

### Impacted data types

The following data types are impacted.

* Time
* Numeric (Any, >8)
* Numeric (>28, Any)
* Decimal (Any, >8)
* Decimal (>28, Any)
* Float4
* Float8
* Float8_range
* Real
* Double precision
* XML
* JSON
* UUID
* Pg_lsn
* Enum
