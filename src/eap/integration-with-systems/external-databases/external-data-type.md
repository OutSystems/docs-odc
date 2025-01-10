---
summary: Data type mapping for external data source in OutSystems Developer Cloud (ODC).
tags: database integration, data security, data fabric, private gateways, configuration management
guid: 55d87c11-7a11-4448-ad61-72e6baad60b6
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - platform administrators
  - full stack developers
  - mobile developers
  - frontend developers
outsystems-tools:
  - odc studio
  - odc portal
content-type:
  - reference
---

# External data type mapping

| SQL Server and Azure SQL | Oracle | SAP OData | SAP BAPI | Salesforce | PostgreSQL |OutSystems data type |
|--|--|--|--|--|--|--|
Char<br/>Varchar<br/>Text<br/>Nchar<br/>Nvarchar<br/>Ntext<br/>Xml<br/>Numeric(Any, >8)<br/>Decimal(Any, >8)<br/>Real<br/>Float<br/>UniqueIdentifier<br/>Time<br/>Datetimeoffset | Char<br/>Varchar<br/>Varchar2<br/>Clob<br/>Long<br/>Nchar<br/>NVarchar2<br/>Nclob<br/>Number(Any, >8)<br/>Float<br/>RowId<br/>URowId | Varchar<br/>UUID<br/>Time<br/>Decimal(Any, >8)<br/>Decimal(>28, Any)|SSTRING<br/>STRING<br/>CHAR<br/>LANG<br/>UNIT<br/>NUMC<br/>DEC (Any, >8)<br/>DEC (>28, Any)<br/>CURR (Any, >8)<br/>CURR (>28, Any)<br/>QUAN (Any, >8)<br/>QUAN (>28, Any)<br/>CLNT<br/>CUKY <br/>LCHR<br/>LRAW<br/>FLTP<br/>RAW<br/>RAWSTRING<br/>GEOM_EWKB| UUID<br/>VARCHAR<br/>FLOAT<br/>Time| Varchar<br/>NVarchar<br/>Text<br/>Varbit<br/>Character<br/>Char<br/>Bpchar<br/>Time<br/>Numeric(Any, >8)<br/>Numeric(>28, Any)<br/>Decimal(Any, >8)<br/>Decimal(>28, Any)<br/>Float4<br/>Float8<br/>Float8_range<br/>Real<br/>Double precision<br/>XML<br/>JSON<br/>UUID<br/>Pg_lsn<br/>Enum |Text|
Tinyint<br/>Smallint<br/>Int<br/>Numeric(2-9, 0)<br/>Decimal(2-9, 0) | Number(2-9, 0) | Int<br/>Decimal(2-9, 0) | INT1<br/>INT2<br/>INT4<br/>ACCP<br/>PREC<br/>DEC (1-9, 0)<br/>CURR (1-9, 0)<br/>QUAN (1-9, 0)<br/>NUMC | Int | Smallint<br/>Integer<br/>Int<br/>Int2<br/>Int4<br/>Numeric<br/>Numeric(2-9, 0)<br/>Decimal(2-9, 0)<br/>Smallserial<br/>Serial<br/>Serial4 |Integer |
Bigint<br/>Numeric(10-18, 0)<br/>Decimal(10-18, 0) | Number(10-18, 0) | Decimal(10-18, 0) | DEC (10-18, 0)<br/>CURR (10-18, 0)<br/>QUAN (10-18, 0)<br/>NUMC | | Bigint<br/>Int8<br/>Bigserial<br/>Serial8<br/>Numeric(10-18, 0)<br/>Decimal(10-18, 0) |Long Integer |
Numeric(19-28, 0-8)<br/>Numeric(1-18, >1-8)<br/>Decimal(19-28, 0-8)<br/>Decimal(1-18, >1-8)<br/>Money<br/>Smallmoney | Number(19-28, 0-8)<br/>Number(1-18, 1-8) | Decimal(1-28, 1-8)<br/>Decimal(19-28, 0) | DEC (19-28, 0-8)<br/>DEC (1-18, 1-8)<br/>CURR (19-28, 0-8)<br/>CURR (1-18, 1-8)<br/>QUAN (19-28, 0-8)<br/>QUAN (1-18, 1-8) | Decimal | Numeric(1-28, 1-8)<br/>Numeric(19-28, 0)<br/>Decimal(1-28, 1-8)<br/>Decimal(19-28, 0)<br/>Money | Decimal |
Bit<br/>Numeric(1, 0)<br/>Decimal(1, 0) | Number(1, 0) | Bit<br/>Decimal(1, 0) | | Bit | Bit<br/>Boolean<br/>Bool<br/>Numeric(1, 0)<br/>Decimal(1, 0) |Boolean |
Date | | Date | DATN<br/>DATS | Date | Date |Date|
Datetime<br/>DateTime2<br/>Smalldatetime | Date<br/>Timestamp | Timestamp |  | DateTime | Timestamp | DateTime |
| | | | TIMN<br/>TIMS | | | Time |
Image<br/>Binary<br/>Varbinary | Blob<br/>Raw<br/>Long Raw | | | | Bytea |Binary Data |
Sql_variant<br/>Geometry<br/>HierarchyId<br/>Geography<br/>Rowversion<br/>Timestamp | Interval day to second<br/>Interval year to month<br/>Bfile<br/>Binary_float<br/>Binary_double<br/>XmlType<br/>VARRAY<br/>OBJECT (structured) | | INT8<br/>DECFLOAT16<br/>DECFLOAT3<br/>UTCLONG | | BIT VARYING<br/>BOX<br/>CIDR<br/>CIRCLE<br/>COMPOSITE (user defined types and other composite types)<br/>INET<br/>INTERVAL<br/>LINE<br/>LSEG<br/>MACADDR<br/>MACADDR8<br/>PATH<br/>POINT<br/>POLYGON<br/>TSQUERY<br/>TSVECTOR<br/>TXID_SNAPSHOT<br/>all of the ARRAY types | Currently not supported and won't appear in ODC Portal.|
Other data types | Other data types | Other data types | Other data types |Other data types | Other data types |No official support; attributes may not appear in the ODC Portal or may exhibit unexpected behavior. |

# Salesforce custom columns mapping

Although Salesforce supports multiple data types in the built-in tables, the following mapping are for the custom columns:

| Salesforce data type| OutSystems data type |
|--|--|
TINYINT<br/>SMALLINT<br/>INT<br/>BIGINT<br/>FLOAT<br/>DECIMAL<br/>DOUBLE<br/>NUMERIC<br/>VARCHAR<br/>BIT<br/>BINARY<br/>UUID<br/>Time | Text |
Boolean |Boolean |
Date | Date |
