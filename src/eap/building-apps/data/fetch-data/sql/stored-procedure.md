---
summary: Execute stored procedures from external entities using SQL nodes in OutSystems Data Cloud (ODC) by obtaining a connectionId from Portal and using the CALL statement.
tags: stored procedures, external entities, sql nodes, outsystems data cloud, database integration
guid: d125e70b-1ef0-4f4e-a7df-070a396ddfad
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7307-1657
audience:
  - backend developers
  - full stack developers
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Call stored procedures from external entities

You can use the [CALL](call.md) statement of ANSI-92 syntax in SQL nodes to execute stored procedures. This is supported when you're using external entities from [connections](../../../../integration-with-systems/external-databases/create-connection-external-data.md)

* Microsoft SQL Server  
* Oracle  
* PostgreSQL

Stored procedures let you reuse logic defined in your external database. They're useful for encapsulating business rules, performing updates, or returning result sets that can be used in your OutSystems logic.

Stored procedures can’t be created or called for internal entities (the entities created in ODC Studio).

The `CALL` statement requires a `connectionId` that identifies the [connection to the data source done in Portal](../../../../integration-with-systems/external-databases/create-connection-external-data.md). 

Follow these steps to retrieve  the connectionId from Portal:

1. Under **Integrate** \> **Connections** click on the connection that you’ll use to call the stored procedure. You’ll reach the connection detail:

    ![OutSystems Data Cloud interface showing the connection detail page for Northwind DB.](images/connection-id-pl.png "Connection Detail Page")

1. Click **…** and **Copy connection ID**. The connectionId is now copied to your clipboard.

    ![OutSystems Data Cloud interface showing the option to copy the connection ID for Northwind DB.](images/copy-connection-id-pl.png "Copy Connection ID")

1. Use the connectionId in your query to call stored procedures. For more details see [CALL](call.md) and the examples below. 


## General rules for calling procedures

* Use the `CALL` statement followed by the connection and procedure name.  
* Procedures may return:  
  * A single return value  
  * A result set  
  * Nothing (in which case `-1` is returned)  

* You can assign parameters using:  
  * **Positional assignment:** arguments passed in order.  
  * **Named assignment:** `"param" = value`.  
  * **Mixed assignment:** positional arguments first, followed by named.  

* When mixing assignments:  
  * All positional arguments must come before any named ones.  
  * Optional parameters can be skipped.

## Limitations and unsupported features

* **OUTPUT and INPUT\_OUTPUT parameters** are generally not supported if they require variable declarations (SQL Server and Oracle).  
* **Unsupported parameter types** vary by database and will prevent the procedure from being recognized.  
* **Unsupported types in result sets** will return as `NULL`.  
* **Procedure overloading** (same name, different parameter lists) is not supported.

## Microsoft SQL Server

* Only **positional assignment** is supported. Named parameters are not allowed.  
* OUTPUT and INPUT\_OUTPUT parameters are not supported.  
* Unsupported input types: `GEOGRAPHY`, `GEOMETRY`, `HIERARCHYID`, `ROWVERSION`, `SQL_VARIANT`, `TIMESTAMP`
* Procedures using `EXECUTE` do not return result sets.

```sql
-- All positional parameters (correct)
CALL "connectionId"."df_test_procedure_all_argument_types"(1, 'test', 0);

-- Skipping optional parameters (correct, only if previous ones are passed)
CALL "connectionId"."df_test_procedure_all_argument_types"(1, 'test');

-- Named parameters (not supported in SQL Server – will fail)
CALL "connectionId"."df_test_procedure_all_argument_types"("@ColId" = 1, "@ColName" = 'test', "@ColCount" = 0);
```

## Oracle

* Procedures must not contain OUTPUT or INPUT\_OUTPUT parameters.  
* Named and positional parameter assignment is supported.  
* Input parameters can be passed as `NULL`, even if they have no default value.  
* Unsupported input types: `BFILE`, `BINARY_DOUBLE`, `BINARY_FLOAT`, `INTERVAL_DAY_TO_SECOND`, `INTERVAL_YEAR_TO_MONTH`, `OBJECT`, `VARRAY`, `XMLTYPE`

```sql
-- Named parameters (sorted)
CALL "connectionId"."df_test_procedure_all_argument_types"(
  "p_id" = 1, "p_name" = 'test', "p_count" = 0
);

-- Named parameters (unsorted)
CALL "connectionId"."df_test_procedure_all_argument_types"(
  "p_name" = 'test', "p_id" = 1, "p_count" = 0
);

-- Positional only
CALL "connectionId"."df_test_procedure_all_argument_types"(1, 'test', 0);
```

## PostgreSQL

* INPUT\_OUTPUT parameters are supported only if passed as **literals**.  

* OUTPUT parameters must be passed in the call.  

* Procedure returns:  
  * `-1` if no result set is returned  
  * A result set if it has OUTPUT or INPUT\_OUTPUT parameters  

* Procedures with unsupported input types or overloading are not recognized.  

* Parameter names may be `$1`, `$2`, etc. when unnamed.  

* Unsupported input types include:`BIT VARYING`, `BOX`, `CIDR`, `CIRCLE`, `COMPOSITE`, `INET`, `INTERVAL`, `LINE`, `LSEG`, `MACADDR`, `MACADDR8`, `PATH`, `POINT`, `POLYGON`, `TSQUERY`, `TSVECTOR`, `TXID_SNAPSHOT`, and all `ARRAY` types.

```sql
-- Named parameters (sorted)
CALL "connectionId"."df_test_procedure_all_argument_types"(
  "p_id" = 1, "p_name" = 'test', "p_count" = 0
);

-- Named parameters (unsorted)
CALL "connectionId"."df_test_procedure_all_argument_types"(
  "p_name" = 'test', "p_id" = 1, "p_count" = 0
);

-- Positional only
CALL "connectionId"."df_test_procedure_all_argument_types"(1, 'test', 0);
```
