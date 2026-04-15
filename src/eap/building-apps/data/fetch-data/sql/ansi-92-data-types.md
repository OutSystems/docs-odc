---
guid: 9d6173ce-58d4-4682-80f1-972f848456a2
locale: en-us
summary: OutSystems Developer Cloud (ODC) maps internal SQL types to external systems and supports type conversion with CAST expressions.
figma: 
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - platform administrators
tags: sql types,data mapping,type conversion,null handling
outsystems-tools:
  - odc portal
  - odc studio
---

# Data types in SQL with external entities

ODC has an internal SQL type system with mappings to/from attribute data types in external systems.

ODC will automatically map value and attribute types as outlined in [External data type mapping](../../../../integration-with-systems/external-databases/external-data-type.md) however it is also possible to `CAST` expressions and attributes to convert them to a different type, refer to [Type conversion](ansi-92-operators.md#type-conversion) for more information.

Null value handling can be configured in ODC Portal as explained [here](../../../../integration-with-systems/external-databases/handle-null-values.md).

## SQL types { #sql-types }

| Type in SQL queries | Description                      | Range                                            | Example Literals                | Example Cast                             |
|---------------------|----------------------------------|--------------------------------------------------|---------------------------------|------------------------------------------|
| BOOLEAN             | Logical values                   |                                                  | TRUE, FALSE                     | CAST(1 AS BOOLEAN)                       |
| TINYINT             | 1 byte signed integer            | [-128, 127]                                      |                                 | CAST(100 AS TINYINT)                     |
| SMALLINT            | 2 byte signed integer            | [-32768, 32767]                                  |                                 | CAST(1234 AS SMALLINT)                   |
| INTEGER             | 4 byte signed integer            | [-2147483648, 2147483647]                        | 100                             | CAST('100' AS INTEGER)                   |
| BIGINT              | 8 byte signed integer            | [-9223372036854775808, 9223372036854775807]      | 2147483648                      | CAST(100 AS BIGINT)                      |
| DECIMAL(p, s)       | Fixed point                      | precision of `p`, scale of `s`                   | 123.45                          | CAST('123.45' AS DECIMAL(5, 2))          |
| NUMERIC(p, s)       | Fixed point                      | precision of `p`, scale of `s`                   |                                 | CAST(123.45 AS NUMERIC(5, 2))            |
| FLOAT<br/>REAL      | 4 byte floating point            | 6 decimal digits precision                       |                                 | CAST(1.123E6 AS REAL)                    |
| DOUBLE              | 8 byte floating point            | 15 decimal digits precision                      | 1.123E6                         | CAST('1.123E6' AS DOUBLE)                |
| CHAR(n)             | Fixed-width character string     | `n` characters (padded with spaces on the right) | 'Hello', '' (empty string)      | CAST('abc' AS CHAR(3))                   |
| VARCHAR             | Variable-length character string |                                                  |                                 | CAST('Hello' AS VARCHAR)                 |
| BINARY(n)           | Fixed-width binary string        | `n` bytes (padded with zeros on the right)       |                                 |                                          |
| VARBINARY           | Variable-length binary string    |                                                  |                                 |                                          |
| DATE                | Date                             |                                                  | DATE '1969-07-20'               | CAST('1969-07-20' AS DATE)               |
| TIME                | Time of day                      |                                                  | TIME '20:17:40'                 | CAST('20:17:40' AS TIME)                 |
| TIMESTAMP           | Date and time                    |                                                  | TIMESTAMP '1969-07-20 20:17:40' | CAST('1969-07-20 20:17:40' AS TIMESTAMP) |
