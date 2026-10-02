---
summary: OutSystems Developer Cloud (ODC) considerations for connecting to an external SAP OData data source.
tags:
  - Data
  - Entities
  - External Databases
  - Pagination
  - Performance
  - Sorting
guid: e0cb59e9-594f-4bcf-a5ec-d220530ecb1e
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
  - apply
  - unblock
isautopublish: true
---

# SAP OData connection considerations

Review the following considerations for a SAP OData connection, including pagination and query performance, null and empty value handling, entity actions, composite keys, and computed attributes. For information about creating or editing the connection, refer to [Create connections to external data sources](create-connection-external-data.md).

## Pagination and query performance

Consider the following when you configure pagination or query a SAP OData connection.

* Always [enable server-side pagination in SAP](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/server-side-pagination) to ensure integrations work correctly.
* SAP throws a `RAISE_SHORTDUMP` exception when requesting the row count for some VIEWS on the first request.
* Regarding SAP OData queries and performance, sorting can significantly affect performance. If you anticipate a lot of records, OutSystems recommends performing any required sorting in your app rather than in the aggregate.

## Null and empty value handling

Consider the following when SAP OData handles null and empty values.

* SAP OData APIs convert null values to empty strings when inserting or updating VARCHAR columns. To fetch null or empty strings, ODC recommends filtering VARCHAR columns using a condition like `Entity.TextAttribute = ' '` and do not rely on OutSystems null's built-in functions.
* SAP v4 entities do not support NULL values. You can override the default value at the attribute level. Users must manually delete the default value during input in the app to prevent NULL values from being written to SAP.

## Entity actions

Consider the following limitations on entity actions for a SAP OData connection.

* The CreateOrUpdate entity action is not available for any entity.
* Deep updates and deletes are not available. However, you can use the Update and Delete entity actions to update or delete records individually, as long as those actions are available for the given entities.
* Bulk insert/update entity action is unavailable for any entity due to SAP's lack of UPSERT support.  
* Some Update entity actions may fail if SAP requires the **If-Match** header.
    * For example, an error message `_The Data Service Request is required to be conditional. Try using the 'If-Match' header.`

## Composite keys

SAP entities can have composite primary keys.

* Entities and entity actions: The entity won't have a primary key if there is a composite key. ODC won't mark any key as a primary key. Hence, you don't get the Update entity action. Also, the Create entity action has no output parameter ID.
* Deep insert server action: The server action provides an output parameter for each PK. The data types and the names of these parameters are based on the original input structure.

## Computed attributes

In SAP, computed attributes are categorized as primitive or complex data types, and each type has different read and write behavior. The following table describes these behaviors.

| Data type | Read | Write |
| --- | --- | --- |
| Primitive | Supported. | Supported, though it may cause runtime errors due to conflicts with SAP business rules. |
| Complex | Not supported. | Allowed, though it may result in runtime errors caused by SAP business rules. |

For example, writing to a complex attribute might return an error such as `\[/IWBEP/CM\_V4\_COS/028] Complex property \&lt;ATTRIBUTE_NAME&gt; is computed and not changeable`. Replace `ATTRIBUTE_NAME` with the SAP attribute name.
