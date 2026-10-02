---
summary: Salesforce connections in OutSystems Developer Cloud (ODC) cover API names, case-sensitive sorting, and join performance.
tags:
  - Data
  - Data Model
  - Entities
  - External Databases
  - Performance
  - Sorting
  - SQL
guid: 74f7475b-3d68-4120-8267-b9a00785a4c8
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
  - unblock
isautopublish: true
---

# Salesforce connection considerations

Review the following considerations for a Salesforce connection, including entity and attribute naming, data type mapping, null and whitespace handling, case sensitivity, and query performance. For information about creating or editing the connection, refer to [Create connections to external data sources](create-connection-external-data.md).

## Entity and attribute naming

Entities and attributes for Salesforce are displayed using their API names, such as CustomObject_c, instead of Field Labels or Field Names, such as CustomObject.

## Data type mapping

Custom attributes and their data types in Salesforce have different mapping than the built-in attributes. For more information, refer to [Salesforce custom columns mapping](external-data-type.md#salesforce-custom-columns-mapping).

## Null and whitespace handling

Salesforce doesn't support leading and trailing white spaces. Salesforce removes those white spaces. While inserting an empty string, Salesforce inserts NULL instead.

## Case sensitivity

Consider the following case-sensitivity behaviors when you work with Salesforce entities.

* Salesforce is case-insensitive, and `ToUpper`/`ToLower` built-in functions don't have the expected behavior in aggregates.
* When sorting queries by ID, the Salesforce API orders the Id attribute in a case-sensitive manner, which differs from the expected case-insensitive sorting of other attributes. While regular attributes are sorted in the standard order (A, a, B, b, C, c), the Id attribute is sorted with uppercase letters first, followed by lowercase letters (A, B, C, a, b, c).

## Query performance

Consider the following when you query or join Salesforce entities.

* Regarding Salesforce queries and performance, sorting can significantly affect performance. If you anticipate a lot of records, OutSystems recommends performing any required sorting in your app rather than in the aggregate.
* When joining Salesforce entities, it's recommended to use parent-child relationships or primary key and foreign key attributes. [Salesforce query language](external-data-type.md#salesforce-custom-columns-mapping) doesn't support relationship queries using other attributes. If this guideline is not followed, the join condition can't be pushed to Salesforce, potentially causing performance issues.
