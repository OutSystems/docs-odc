---
summary: Oracle connection considerations in OutSystems Developer Cloud (ODC), including DiffMinutes and DiffSeconds limits and Oracle null handling.
tags:
  - Data
  - Entities
  - External Databases
guid: 408232bd-cb7d-4fca-b856-490e047d7bfd
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
  - remember
isautopublish: true
---

# Oracle connection considerations

Review the following considerations for an Oracle connection, including known limitations in date and time functions and how Oracle handles null values. For information about creating or editing the connection, refer to [Create connections to external data sources](create-connection-external-data.md).

## Date and time interval limits

The `DiffMinutes` and `DiffSeconds` built-in functions for Oracle only allow the following maximum intervals between dates.

* Seconds: 31 years, 9 months, 9 days, 1 hour, 46 minutes, and 39 seconds
* Minutes: 1901 years, 4 months, 29 days, 10 hours, 39 minutes, and 59 seconds

## Null handling

Oracle treats empty strings as NULL values. When inserting or updating a nullable text attribute with a value, Oracle stores NULL regardless of the Null Behavior configuration.

For more information about configuring null value handling, refer to [Handle null values](handle-null-values.md).
