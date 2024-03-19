---
summary: Learn about integrating external databases with OutSystems Developer Cloud, managing connections, and selecting entities to use in your apps.
helpids: 30191, 30483, 30501, 30502
tags:
locale: en-us
guid: 67608c14-0b83-4e69-bf46-ba023ed730f4
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/AOyPMm22N6JFaAYeejDoge/Configuration-management?type=design&node-id=3504%3A808&mode=design&t=0qX3292WcHKssBRO-1
---

# Integrate with external databases

OutSystems Developer Cloud (ODC) enables developers to integrate external data into their apps. First, from the ODC Portal, admins create connections to the supported databases and select the entities. Then, in ODC studio, developers use the data as entities in their apps.

Admins must set up configurations for each stage, such as development, QA, and production, to connect an app to an external database.

Admins ensure the app and its connection information are in the same stage. Additionally, the database model must be the same in all the stages.

There is no limit to the number of entities you can add from the external database.

<div class="info" markdown="1">

ODC offers [private gateways](../private-gateway.md) to connect your apps to private data and services that are inaccessible through the internet. Since an external database is usually hosted in a private network, using a private gateway ensures security.

</div>

## Supported systems

OutSystems supports the following versions of systems:

* Microsoft SQL server
    * SQL Server 2014
    * SQL Server 2016
    * SQL Server 2017
    * SQL Server 2019
    * SQL Server 2022

* Oracle server
    * Oracle 19c

* SAP server
    * SAP S4
    * SAP HANA

* Salesforce

* PostgreSQL Server
    * PostgreSQL 12
    * PostgreSQL 13
    * PostgreSQL 14
    * PostgreSQL 15
    * PostgreSQL 16

OutSystems supports self-managed, Aurora, and Azure provisions for PostgreSQL.

## Permissions requirements

Before accessing data from an external database, verify that you have the correct access to the database and ODC. By default, only admins can manage connections and select entities. Managing connections requires the following permissions:

* Configure Connections
* Connection management

External database permissions take priority over permissions in ODC. For example, a developer with read permission in an external database and read-write permission in ODC can only read data in the external database. Contact the external database admin to change your access to the external database..

<div class="info" markdown="1">

Read-only external entities won't have create, update, or delete entity actions in ODC Studio. An external entity is considered read-only when all selected attributes are not updatable and not insertable on the data source.

</div>  

For more information about users, permissions, and custom roles, see [User management](../../user-management/intro.md).

## Create a new connection

To create a new database connection, go to the ODC Portal and follow these steps:

1. From the ODC Portal nav menu, select **Resource** > **Connections**, and click the **Create connection** button. <br/> The **select a provider** popup displays.
1. Select the required provider and click **Confirm**.
    * If you select SAP, then select the **SAP Service** as **SAP Service Catalog**, and click **Show available services**.<br/> All available services display.
    * If you select Salesforce, select **connect to** as **Production**, and **Authentication type** as **OAuth** authentication type, and click **Authenticate**.<br/> The Salesforce login page displays.
1. In the connection form, enter the required database connection information. To learn more, refer to the [connection parameters](#connection-parameters).

<div class="info" markdown="1">

To use private gateways to connect to your external databases, enter `secure-gateway` in the Server/Host field and the secure gateway port value in the Port field.

</div>

1. After entering the information, click the **Test connection** button at the bottom of the form. 

<div class="info" markdown="1">

If the test fails, a message displays. Make the necessary changes and test again. 

</div>

1. To apply to a stage, an admin can choose one of the following.
    * Click Apply to all stages to use the same connection information in all stages.
    * Select the stage name to use connection information for a single stage.

If you select SQL or Oracle server, you can use advanced parameters to add additional parameters for a database connection. If there is more than one parameter, separate each parameter with a semi-colon (;). Different databases may require different parameters, for example:

* For the **SQL** server to select the desired schema on the database, enter `currentSchema = <schema-name>`
* For **Oracle** to select the desired schema on the database, enter `current_schema = <schema-name>`

<div class="info" markdown="1">

To establish a connection with the SQL server and allow the client to bypass certificate validation, add the `trustServerCertificate=true` parameter to the additional parameters.

</div>  

## Select entities for use in an app

After connecting to an external database, select the entity names and attributes available in ODC Studio. To select entities, go to the ODC Portal and follow these steps:

1. From the ODC Portal nav menu, select **Resource** > **Connections**, and click **Select entities** to display the **Add entities** connection screen. <br/>The connection screen displays the available entities retrieved from the database.

    ![Screenshot showing the process of selecting entities and attributes from an external database in OutSystems Developer Cloud Portal](images/external-db-entity.png "External Database Entities Selection")

1. From the **Entity** name column, select the entities and attributes you want to use.
1. Click **Save** to confirm. 

Selected entities and attributes are now available as [public elements](../../building-apps/use-public-elements.md). In ODC Studio, developers have the flexibility to rename entities, allowing for clearer descriptions. For example, an entity initially named 'Product_id_version1' can be renamed to 'Product_id'.

## Edit an existing connection

To edit an existing database connection, go to ODC Portal and follow these steps:

1. From the ODC Portal nav menu, select **Resource** > **Connections** to display the list of connections.
1. From the list of connections, select the one to edit.

You can only change the name and description without testing your connection again.

## Handle null values

Admins must assign new values to represent null values in external databases. You can use the following options to handle null values.

* Overwrite database NULL values(default option):
    * When writing data, ODC stores default values instead of null values in external databases.
    * When reading data, ODC reads null values as default values.
* Keep database NULL values:
    * When writing data, ODC stores null values in external databases.
    * When reading data, ODC reads null values as default values.

Admins can define handling null values at either connection or entity level:

* The connection level impacts all entities in the connection. 
* The entity level impacts only the selected entity to define unique behavior for the selected entity.

<div class="info" markdown="1">

An entity level configuration takes priority over the connection level.

</div>  

Null behavior doesn't apply to Primary and Foreign Keys; they keep null values in the database.

### Default value configuration

Admins must set up a configuration for the default values. ODC suggests default values for every data type, which admins can change. This configuration is available at the connection and attribute levels.

* The connection level applies to nullable attributes of all entities in the connection. 
* The attribute level applies to the selected attribute to define unique behavior for the selected attribute.

<div class="info" markdown="1">

Attribute level configuration takes priority over the connection level.

</div>  

### Non-relational databases

The Null Behavior configuration functions differently for non-relational databases.

* For a Null behavior configuration, the available option is to keep the database null values, which developers can't modify.
* For a Default values configuration, developers can select the default values.

## Connection parameters

Admins must supply the following information to connect to the external connector.

| Parameter | Description | Needs testing connection when edited | Notes |
|--|--|--|--|
| Connection name | The name of the connection | No |  |
| Description | Information about the database connection | No | Optional |
| Username | Username to access the database | Yes |  |
| Password | Password to access the database. | Yes |  |
| Server for SQL server \ Host for Oracle server | Endpoint for your database connection | Yes | For Private Gateway, enter `secure-gateway` |
| Port | The port number to connect to the database | Yes | ODC has a default port number that an admin can change. For a private gateway, enter the port configured in the connector. |
| Database for SQL server \ Service name for Oracle server | Name of the database | Yes |  |
| Additional parameters | Additional parameters for a database connection | Yes | Different databases may require different parameters |
| SAP Server domain | SAP server/host address| Yes |  |
| SAP Client | If the SAP system has multiple clients, you must provide a client number. Leave the input blank if you connect to the default client | Yes | Optional |
| Manual entry | To manually enter the Service URL| Yes | If you select "Manual entry" for a private gateway, then the domain must be `secure-gateway:<port>/..`|
| Basic authentication type | Basic is a simpler authentication method than OAuth | Yes | |
| Sandbox connection | Sandbox enables a partial or full copy of production data to test the connector. | Yes | |

## Data type mapping

When connecting to external databases, OutSystems maps the external database data types to OutSystems data types as follows:

| SQL Server | Oracle data type| SAP Server | Salesforce | PostgreSQL |OutSystems Data Type |
|--|--|--|--|--|--|
Char<br/>Varchar<br/>Text<br/>Nchar<br/>Nvarchar<br/>Ntext<br/>Xml<br/>Decimal(Any,> 8)<br/>Numeric(Any,>8) <br/>Real<br/>Float<br/>UniqueIdentifier<br/>Time<br/>Datetimeoffset | Char<br/>Varchar<br/>Varchar2<br/>Clob<br/>Long<br/>Nchar<br/>NVarchar2<br/>Nclob<br/>Number(Any,> 8)<br/>Float<br/>RowId<br/>URowId | Varchar<br/>UUID| UUID<br/>VARCHAR<br/>FLOAT<br/>Time| Varchar<br/>NVarchar<br/>Text<br/>Varbit<br/>Character<br/>Char<br/>Bpchar<br/>Time<br/>Numeric(Any, >8)<br/>Numeric(>28, Any)<br/>Decimal(Any, >8)<br/>Decimal(>28, Any)<br/>Float4<br/>Float8<br/>Float8_range<br/>Real<br/>Double precision<br/>XML<br/>JSON<br/>UUID<br/>Pg_lsn<br/>Enum |Text|
Tinyint<br/>Smallint<br/>Int<br/>Decimal(1-9,0)<br/>Numeric(1-9,0) | Number(2-9,0) | Int | Int | Smallint<br/>Integer<br/>Int<br/>Int2<br/>Int4<br/>Numeric<br/>Numeric(1-9, 0)<br/>Decimal(1-9, 0)<br/>Smallserial<br/>Serial<br/>Serial4 |Integer |
Bigint<br/>Decimal(10-18,0)<br/>Numeric(10-18,0) | Number(10-18,0) | | | Bigint<br/>Int8<br/>Bigserial<br/>Serial8<br/>Decimal(10-18, 0)<br/>Numeric(10-18, 0) |Long Integer |
Decimal(19-28,0-8)<br/>Decimal(1-18,>1-8)<br/>Numeric(19-28,0-8)<br/>Numeric(1-18,>1-8)<br/>Money<br/>Smallmoney | Number(19-28,0-8)<br/>Number(1-18,1-8) | Decimal| Decimal | Numeric(1-28, 1-8)<br/>Decimal(1-28, 1-8)<br/>Numeric(19-28, 0)<br/>Decimal(19-28, 0)<br/>Money | Decimal |
Bit | Number(1,0) | Bit| Bit | Bit<br/>Boolean<br/>Bool |Boolean |
Date | | Date | Date | Date |Date|
Datetime<br/>DateTime2<br/>Smalldatetime | Date<br/>Timestamp | Time<br/>Timestamp  | DateTime | Timestamp | DateTime |
Image<br/>Binary<br/>Varbinary | Blob<br/>Raw<br/>Long Raw | | | Bytea |Binary Data |
Sql_variant<br/>Geometry<br/>HierarchyId<br/>Geography<br/>Rowversion<br/>Timestamp | Interval day to second<br/>Interval year to month<br/>Bfile<br/>Binary_float<br/>Binary_double<br/>XmlType<br/>VARRAY<br/>OBJECT (structured) | | | BIT VARYING<br/>BOX<br/>CIDR<br/>CIRCLE<br/>COMPOSITE (user defined types and other composite types)<br/>INET<br/>INTERVAL<br/>LINE<br/>LSEG<br/>MACADDR<br/>MACADDR8<br/>PATH<br/>POINT<br/>POLYGON<br/>TSQUERY<br/>TSVECTOR<br/>TXID_SNAPSHOT<br/>all of the ARRAY types | Currently not supported and won't appear in ODC Portal.|
Other data types | Other data types | Other data types |Other data types | Other data types |No official support; attributes may not appear in the ODC Portal or may exhibit unexpected behavior. |

## Salesforce custom columns mapping

Although Salesforce supports multiple data types in the built-in tables, the following mapping are for the custom columns:

| Salesforce data type| OutSystems Data Type |
|--|--|
TINYINT<br/>SMALLINT<br/>INT<br/>BIGINT<br/>FLOAT<br/>DECIMAL<br/>DOUBLE<br/>NUMERIC<br/>VARCHAR<br/>BIT<br/>BINARY<br/>UUID<br/>Time | Text |
Boolean |Boolean |
Date | Date |

## Considerations when integrating external database

Consider the following when integrating an external database.

* The `DiffMinutes` and `DiffSeconds` built-in functions for Oracle only allow max intervals between dates:
    * Seconds: 31 years, 9 months, 9 days, 1 hour, 46 minutes, and 39 seconds
    * Minutes: 1901 years, 4 months, 29 days, 10 hours, 39 minutes, and 59 seconds
* .NET does not support the Julian calendar for Oracle and Salesforce, and the minimum supported timestamp value is -62135596800000. 
    * To avoid .NET breaking, send the maximum value between the original timestamp and the minimum supported to convert dates like 0001-01-01 to 0001-01-03.
* Oracle treats empty strings as NULL values. When inserting or updating a nullable text attribute with a value, Oracle stores NULL regardless of the Null Behavior configuration.
* Data Preview and runtime queries with Unicode characters aren't supported.
* Advanced SQL Nodes don't support external entities.
* Build aggregator or mashup data from different sources(external and local) aren't supported.
* SAP OData APIs convert null values to empty strings when inserting or updating VARCHAR columns. To fetch null or empty strings, ODC recommends filtering VARCHAR columns using a condition like `Entity.TextAttribute = ' '` and do not rely on OutSystems null's built-in functions.
* Entities and attributes for Salesforce are displayed using their API names, such as CustomObject_c, instead of Field Labels or Field Names, such as CustomObject.
* Custom attributes and their data types in Salesforce have different mapping than the built-in attributes. For more information, see [salesforce custom columns mapping.](#salesforce-custom-columns-mapping)
* Salesforce doesn't support leading and trailing white spaces. 
    * Salesforce removes those white spaces. While inserting an empty string, Salesforce inserts NULL instead.
* Salesforce is case-insensitive, and `ToUpper`/`ToLower` built-in functions don't have the expected behavior in aggregates.
* For PostgreSQL connections, you may encounter issues in Text data type columns when inserting an empty value, and the connection is configured to overwrite null values with default values.OutSystems recommends you set a different default value to columns of these data types, such as for Time: 00:00:00 or for Float: 0. The following data types are impacted:
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