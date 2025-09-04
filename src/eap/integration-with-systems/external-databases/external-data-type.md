---
summary: OutSystems Developer Cloud (ODC) manages data type mapping across external systems, SQL nodes, and app logic, ensuring consistent data flow and type compatibility.
tags: data mapping, type conversion, sql nodes, data mashups
guid: 55d87c11-7a11-4448-ad61-72e6baad60b6
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - platform administrators
  - full stack developers
  - backend developers
outsystems-tools:
  - odc studio
  - odc portal
content-type:
  - reference
coverage-type:
  - remember
topic:
---

# External data type mapping

When integrating external data sources, OutSystems Developer Cloud (ODC) automatically maps data types to ensure compatibility. This article provides the definitive reference tables showing how data types from SQL Server, Oracle, PostgreSQL, Salesforce, and SAP correspond to internal OutSystems types.

## SQL data type mapping

ODC uses an internal SQL type system to manage and map data types across different sources. This system ensures that data flows consistently between:

* The **data types used in external systems** (e.g., SQL Server, Oracle, PostgreSQL, Salesforce, SAP OData)
* The **types used in SQL nodes**, expressions, and aggregates
* The **OutSystems data types** used in your app logic

This mapping supports key features like aggregates, data mashups, and SQL queries. In most cases, ODC handles type compatibility for you—especially when retrieving data or binding it to widgets. However, **you may need to handle type conversion manually** in certain situations:

* In **SQL nodes**, use the [CAST operator](../../building-apps/data/fetch-data/sql/ansi-92-operators.md#type-conversion) of ANSI-92 to convert values to the expected type.
* In **expressions and aggregate filters**, use [built-in data conversion functions](../../reference/built-in-functions/data-conversion.md) like `TextToInteger()` or `DecimalToText()` to ensure type compatibility, when necessary.
* In **data mashups**, types from different sources are matched automatically when possible, but you may need conversions when combining or comparing values in logic.

The table below shows how common SQL node types map to OutSystems and external system data types.

For more on converting values, see:
* [Type conversion (SQL)](../../building-apps/data/fetch-data/sql/ansi-92-operators.md#type-conversion)
* [Convert data types (expressions)](../../building-apps/data/convert-data-types.md)

<div class="info" markdown="1">

Only the data types that have a mapping are supported. Data types not present in the following tables aren't yet supported.

</div>

| Type in SQL queries                                                                | OutSystems Data Type                                                                                              | Microsoft SQL Server                                                       | MySQL                                                       | Oracle                                                                | PostgreSQL                                                     | Salesforce       | SAP OData        |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------- | ---------------- |
| BOOLEAN                                                                            | Boolean                                                                                                           | BIT<br/>DECIMAL(1,0)<br/>NUMERIC(1,0)                                      | BIT(1)<br/>BOOL<br/>TINYINT(1)                              | NUMBER(1, 0)                                                          | BIT(1)<br/>BOOL                                                | BIT              |                  |
| TINYINT                                                                            | Integer                                                                                                           | TINYINT                                                                    | TINYINT                                                     |                                                                       |                                                                |                  |                  |
| SMALLINT                                                                           | Integer                                                                                                           | SMALLINT                                                                   | SMALLINT                                                    |                                                                       | INT2<br/>SMALLSERIAL                                           |                  |                  |
| INTEGER                                                                            | Integer                                                                                                           | INT                                                                        | INT<br/>MEDIUMINT                                           |                                                                       | INT4<br/>SERIAL                                                |                  | INT              |
| BIGINT                                                                             | Long Integer                                                                                                      | BIGINT                                                                     | BIGINT<br/>BIT(>1)                                          |                                                                       | BIGSERIAL<br/>INT8                                             |                  |                  |
| DECIMAL(p, s)                                                                      | Decimal<br/>Integer (if p < 10 and s = 0)<br/>Long Integer (if p = 10-18 and s = 0)<br/>Text (if p > 28 or s > 8) | DECIMAL(p, s)                                                              | DECIMAL(p, s)                                               | NUMBER(p, s)                                                          | MONEY<br/>NUMERIC(p, s)                                        |                  | DECIMAL          |
| NUMERIC(p, s)                                                                      | Decimal<br/>Integer (if p < 10 and s = 0)<br/>Long Integer (if p = 10-18 and s = 0)<br/>Text (if p > 28 or s > 8) | NUMERIC(p, s)                                                              | NUMERIC(p, s)                                               | NUMBER(p, s)                                                          |                                                                |                  |                  |
| FLOAT<br/>REAL                                                                     | Text                                                                                                              | REAL                                                                       | FLOAT                                                       | FLOAT<br/>REAL                                                        | FLOAT4                                                         |                  |                  |
| DOUBLE                                                                             | Text                                                                                                              | FLOAT                                                                      | REAL                                                        |                                                                       | FLOAT8                                                         | FLOAT            |                  |
| CHAR                                                                               | Text                                                                                                              | CHAR<br/>NCHAR                                                             | CHAR                                                        | CHAR<br/>NCHAR                                                        | BPCHAR                                                         |                  |                  |
| VARCHAR                                                                            | Text                                                                                                              | DATETIMEOFFSET<br/>NTEXT<br/>TEXT<br/>UNIQUEIDENTIFIER<br/>VARCHAR<br/>XML | ENUM<br/>JSON<br/>SET<br/>TINYTEXT<br/>UUID<br/>VARCHAR     | CLOB<br/>LONG<br/>NCLOB<br/>NVARCHAR<br/>ROWID<br/>UROWID<br/>VARCHAR | ENUM<br/>JSON<br/>PG_LSN<br/>TEXT<br/>UUID<br/>VARCHAR<br/>XML | UUID<br/>VARCHAR | UUID<br/>VARCHAR |
| BINARY                                                                             | Binary Data                                                                                                       | BINARY                                                                     | BINARY                                                      | BLOB                                                                  | BYTEA                                                          |                  |                  |
| VARBINARY                                                                          | Binary Data                                                                                                       | IMAGE<br/>VARBINARY                                                        | BLOB<br/>LONGBLOB<br/>MEDIUMBLOB<br/>TINYBLOB<br/>VARBINARY | RAW                                                                   |                                                                |                  |                  |
| DATE                                                                               | Date                                                                                                              | DATE                                                                       | DATE<br/>YEAR                                               | DATE                                                                  | DATE                                                           | DATE             | DATE             |
| TIME                                                                               | Text                                                                                                              | TIME                                                                       | TIME                                                        |                                                                       | TIME                                                           | TIME             | TIME             |
| TIMESTAMP                                                                          | DateTime                                                                                                         | DATETIME<br/>DATETIME2<br/>SMALLDATETIME                                   | DATETIME<br/>TIMESTAMP                                      | TIMESTAMP                                                             | TIMESTAMP                                                      | TIMESTAMP        |                  |
| No official support. Attributes may not appear or may exhibit unexpected behavior. | No official support. Attributes may not appear in the ODC Portal or may exhibit unexpected behavior.              | Other data types                                                           | Other data types                                            | Other data types                                                      | Other data types                                               | Other data types | Other data types |

## SAP BAPI mapping

| SAP BAPI                                                                                                                                                                                                                                                    | OutSystems data type                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| SSTRING<br/>STRING<br/>CHAR<br/>LANG<br/>UNIT<br/>NUMC<br/>DEC (Any, >8)<br/>DEC (>28, Any)<br/>CURR (Any, >8)<br/>CURR (>28, Any)<br/>QUAN (Any, >8)<br/>QUAN (>28, Any)<br/>CLNT<br/>CUKY <br/>LCHR<br/>LRAW<br/>FLTP<br/>RAW<br/>RAWSTRING<br/>GEOM_EWKB | Text                                                                                                 |
| INT1<br/>INT2<br/>INT4<br/>ACCP<br/>PREC<br/>DEC (1-9, 0)<br/>CURR (1-9, 0)<br/>QUAN (1-9, 0)<br/>NUMC                                                                                                                                                      | Integer                                                                                              |
| DEC (10-18, 0)<br/>CURR (10-18, 0)<br/>QUAN (10-18, 0)<br/>NUMC                                                                                                                                                                                             | Long Integer                                                                                         |
| DEC (19-28, 0-8)<br/>DEC (1-18, 1-8)<br/>CURR (19-28, 0-8)<br/>CURR (1-18, 1-8)<br/>QUAN (19-28, 0-8)<br/>QUAN (1-18, 1-8)                                                                                                                                  | Decimal                                                                                              |
| DATN<br/>DATS                                                                                                                                                                                                                                               | Date                                                                                                 |
| TIMN<br/>TIMS                                                                                                                                                                                                                                               | Time                                                                                                 |
| INT8<br/>DECFLOAT16<br/>DECFLOAT3<br/>UTCLONG                                                                                                                                                                                                               | Currently not supported and won't appear in ODC Portal.                                              |
| Other data types                                                                                                                                                                                                                                            | No official support. Attributes may not appear in the ODC Portal or may exhibit unexpected behavior. |

## Salesforce custom columns mapping

Although Salesforce supports multiple data types in the built-in tables, the following mapping are for the custom columns:

| Type in SQL queries | OutSystems data type | Salesforce data type                                                                 |
| ------------------- | -------------------- | ------------------------------------------------------------------------------------ |
| BOOLEAN             | Boolean              | BOOLEAN (must have a default value)                                                  |
| FLOAT<br/>REAL      | Text                 | TINYINT<br/>SMALLINT<br/>INT<br/>BIGINT<br/>FLOAT<br/>DECIMAL<br/>DOUBLE<br/>NUMERIC |
| VARCHAR             | Text                 | BINARY<br/>BIT<br/>UUID<br/>VARCHAR                                                  |
| DATE                | Date                 | DATE                                                                                 |
| TIME                | Text                 | TIME                                                                                 |
| TIMESTAMP           | Timestamp            | TIMESTAMP                                                                            |
