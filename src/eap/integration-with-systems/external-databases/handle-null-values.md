---
helpids: 30499
summary: OutSystems Developer Cloud (ODC) supports seamless integration with external databases for enhanced app development.
tags: database integration, null value handling, configuration management, data types, external database connectivity
locale: en-us
guid: b29382ab-f4d3-479c-be4b-22a8319e612c
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - platform administrators
  - full stack developers
  - backend developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
topic:
  - get-data-from-external-db
---

# Handle null values

To handle null values while integrating with external systems, administrators must assign new values to represent null values in external databases. You can use the following options to handle null values.

* Overwrite database NULL values(default option):
    * When writing data, ODC stores default values instead of null values in external databases.
    * When reading data, ODC reads null values as default values.
* Keep database NULL values:
    * When writing data, ODC stores null values in external databases.
    * When reading data, ODC reads null values as default values.

Administrators can define handling null values at either connection or entity level:

* Connection level: All entities in the connection are impacted
* Entity level: Only the selected entity that defines the unique behavior of the selected entity is impacted

<div class="info" markdown="1">

An entity level configuration takes priority over the connection level.

</div>  

Null behavior doesn't apply to primary and foreign keys. They keep null values in the database.

Null behavior applies to SQL Nodes with external entities when using [SELECT](../../building-apps/data/fetch-data/sql/ansi-92-select.md) but only if the external entity is set as the output type.
When using a structure as the output type, null values will be converted to the default values configured on the structure attributes. If no default value is configured for a given structure attribute, then the default value for the OutSystems [data type](../../building-apps/data/data-types.md) applies.

Data manipulation statements such as [INSERT/UPSERT](../../building-apps/data/fetch-data/sql/ansi-92-insert.md), [UPDATE](../../building-apps/data/fetch-data/sql/ansi-92-update.md), and [CALL](../../building-apps/data/fetch-data/sql/call.md) will not convert default values to null values, they will be passed without modification to the external system. However, it is possible to implement this conversion using the `NULLIF` function or `CASE` operator, for more information please see [Conditional functions and operators](../../building-apps/data/fetch-data/sql/ansi-92-operators.md#conditional-functions-and-operators).

## Default value configuration

Administrators must configure default values. ODC suggests default values for every data type, which admins can change. Administrators can configure default values at the connection and attribute level.

* Connection level: All nullable attributes of all entities in the connection. 
* Attribute level: All selected attribute defines unique behavior for the selected attribute.

<div class="info" markdown="1">

Attribute level configuration takes priority over the connection level.

</div>  

## Non-relational databases

The null behavior configuration functions as follows:

* Null behavior: Keep the database null values. This cannot be modified.
* Default values: Add or configure or select the default values.
