---
summary: MySQL connection considerations in OutSystems Developer Cloud (ODC) explain Timestamp null handling and the 1970-01-01 00:00:01 minimum.
tags:
  - Data
  - Data Integrity
  - External Databases
guid: d5912694-9622-4631-8431-bdaf4ff6c44a
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
isautopublish: true
---

# MySQL connection considerations

Review the following consideration for a MySQL connection, which covers how MySQL's Timestamp data type interacts with null value handling. For information about creating or editing the connection, refer to [Create connections to external data sources](create-connection-external-data.md).

## Timestamp null handling

MySQL's Timestamp data type starts at `1970-01-01 00:00:01`. To prevent conflicts when converting MySQL's Timestamp attributes to DateTime in OutSystems, enable the **Overwrite database NULL values** option in the Null behavior configuration. This way, all OutSystems DateTime attributes default to the same minimum value of `1970-01-01 00:00:01`.

For more information about configuring null value handling, refer to [Handle null values](handle-null-values.md).
