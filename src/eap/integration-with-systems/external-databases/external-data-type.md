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

OutSystems Developer Cloud (ODC) uses an internal SQL type system to manage and map data types across different sources. This system ensures that data flows consistently between:

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


| Type in SQL queries | OutSystems Data Type               | Microsoft SQL Server                                                       | Oracle                                                                | PostgreSQL               | Salesforce       | SAP OData        |
|---------------------|------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------|--------------------------|------------------|------------------|
| BOOLEAN             | Boolean                            | BIT<br/>DECIMAL(1,0)<br/>NUMERIC(1,0)                                      | NUMBER(1, 0)                                                          | BIT<br/>BOOL             | BIT              |                  |
| TINYINT             | Integer                            | TINYINT                                                                    |                                                                       |                          |                  |                  |
| SMALLINT            | Integer                            | SMALLINT                                                                   |                                                                       | INT2<br/>SMALLSERIAL     |                  |                  |
| INTEGER             | Integer                            | INT                                                                        |                                                                       | INT4<br/>SERIAL          |                  | INT              |
| BIGINT              | Long Integer                       | BIGINT                                                                     |                                                                       | BIGSERIAL<br/>INT8       |                  |                  |
| DECIMAL(p, s)       | Decimal<br/>Text (p > 28 or s > 8) | DECIMAL(p, s)                                                              | NUMBER(p, s)                                                          | MONEY<br/>NUMERIC(p, s)  |                  | DECIMAL          |
| NUMERIC(p, s)       | Decimal<br/>Text (p > 28 or s > 8) | NUMERIC(p, s)                                                              | NUMBER(p, s)                                                          |                          |                  |                  |
| FLOAT<br/>REAL      | Text                               | REAL                                                                       | FLOAT<br/>REAL                                                        | FLOAT4                   |                  |                  |
| DOUBLE              | Text                               | FLOAT                                                                      |                                                                       | FLOAT8                   | FLOAT            |                  |
| CHAR                | Text                               | CHAR<br/>NCHAR                                                             | CHAR, NCHAR                                                           | BPCHAR                   |                  |                  |
| VARCHAR             | Text                               | DATETIMEOFFSET<br/>NTEXT<br/>TEXT<br/>UNIQUEIDENTIFIER<br/>VARCHAR<br/>XML | CLOB<br/>LONG<br/>NCLOB<br/>NVARCHAR<br/>ROWID<br/>UROWID<br/>VARCHAR | TEXT<br/>VARCHAR<br/>XML | UUID<br/>VARCHAR | UUID<br/>VARCHAR |
| BINARY              | Binary Data                        | BINARY                                                                     | BLOB                                                                  | BYTEA                    |                  |                  |
| VARBINARY           | Binary Data                        | IMAGE<br/>VARBINARY                                                        | RAW                                                                   |                          |                  |                  |
| DATE                | Date                               | DATE                                                                       | DATE                                                                  | DATE                     | DATE             | DATE             |
| TIME                | Text                               | TIME                                                                       |                                                                       | TIME                     | TIME             | TIME             |
| TIMESTAMP           | Timestamp                          | DATETIME<br/>DATETIME2<br/>SMALLDATETIME                                   | TIMESTAMP                                                             | TIMESTAMP                | TIMESTAMP        |                  |

## Salesforce custom columns mapping

Although Salesforce supports multiple data types in the built-in tables, the following mapping are for the custom columns:

| Salesforce data type                                                                                                                 | OutSystems data type |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------|
|TINYINT<br/>SMALLINT<br/>INT<br/>BIGINT<br/>FLOAT<br/>DECIMAL<br/>DOUBLE<br/>NUMERIC<br/>VARCHAR<br/>BIT<br/>BINARY<br/>UUID<br/>Time | Text                 |
|Boolean                                                                                                                               |Boolean               |
|Date                                                                                                                                  | Date                 |