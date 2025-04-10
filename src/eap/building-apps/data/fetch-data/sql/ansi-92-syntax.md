---
guid: 4d569b71-1430-4801-96da-cce2e9984174
locale: en-us
summary: Learn ANSI-92 SQL syntax in OutSystems Developer Cloud (ODC) for querying external entities with supported operations.
figma:
coverage-type:
  - understand
  - remember
topic:
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - mobile developers
tags: sql syntax, ansi-92, external entities, sql queries
outsystems-tools:
  - odc studio
helpids: 30583
---

# Understand ANSI-92 syntax in SQL nodes

[SQL nodes](use-sql.md) in OutSystems Developer Cloud (ODC) use a syntax based on ANSI-92 when working with external entities or when combining internal and external entities.

ANSI-92 is a syntax that helps you write portable, consistent SQL designed to work with all the [external systems connected via Data Fabric](../../../../integration-with-systems/external-databases/intro.md). 

Use this article as a starting point to learn how ANSI-92 queries work in ODC.

<div class="warning" markdown="1">

Support for querying data using SQL with Salesforce and SAP systems is still experimental.

</div>

## Statements { #statements }

SQL statements define the actions your query performs. Each statement type serves a specific purpose, such as retrieving or modifying data.

<div class="info" markdown="1">

The user assigned to the [connection](../../../../integration-with-systems/external-databases/create-connection-external-data.md) must have permission to perform all the [operations](#supported-operations) in the statement.

</div>

Entity names must be enclosed in `{ }` and attributes must be enclosed in `[ ]`. For example, entity `{Customers}` and attribute `[Id]`. Attributes should always be qualified using the `{Customers}.[Id]` syntax to ensure that attributes which are renamed in ODC Portal have the correct name in the query to the external system.

An important difference to note in ANSI-92 SQL compared to some commonly used database systems is that unquoted identifiers are automatically uppercased. For example, `subquery.id` is converted to `SUBQUERY.ID`. To preserve the original letter casing of identifiers, they must be enclosed in `[ ]` or `" "`. Identifiers are case-sensitive and so care must be taken when working with a combination of quoted and unquoted identifiers. For example, `subquery.[id]` isn't a valid reference to `subquery.id` because `id` isn't considered to be the same as `ID`.

### Multiple statements { #multiple-statements }

Multiple statements delimited by `;` can be executed on an external system in a single SQL Node.

All statements in a multiple statement SQL Node will be executed in a single transaction with an isolation level of `READ COMMITTED` provided that the external system supports transactions. If an error occurs in the execution of any statement, the transaction will be rolled back automatically. The transaction is committed as soon as the last statement executes successfully and before results are returned. If an error occurs while fetching results, the transaction will not be rolled back.

When executing multiple statements in an SQL Node, the result will be that of the last statement. The results of earlier statements will not be returned.

<div class="info" markdown="1">

All statements in a multiple statement SQL Node must use entities and actions from the same [connection](../../../../integration-with-systems/external-databases/create-connection-external-data.md).

</div>

The following table lists the compatibility of multiple statements with each data source as well as whether or not the statements will be executed in a transaction.

| Data source          | Multiple statements | Executed in transaction |
| -------------------- | ------------------- | ----------------------- |
| Microsoft SQL Server | Yes                 | Yes                     |
| Oracle               | Yes                 | Yes                     |
| PostgreSQL           | Yes                 | Yes                     |
| Salesforce           | Yes                 | No                      |
| SAP OData            | Yes                 | No                      |

#### Syntax for multiple statements { #syntax-multiple-statements }

`statement ; statement;`

The following is an example of using multiple statements:

```sql
\-- comments can be included like this

CALL "connectionId"."actionName" ("param1" = 'test', "param2" = @dynamic1);

DELETE FROM {entity1};

INSERT INTO {entity2} ({entity2}.[attribute1], {entity2}.[attribute2]) VALUES ('abc', @dynamic2);

SELECT {entity2}.* FROM {entity2};

```

## Supported operations { #supported-operations }

ANSI-92 operations define what each SQL statement does. The following operations are supported:

* [**SELECT**](ansi-92-select.md): Retrieves data from one or more entities.

* [**WITH**](ansi-92-select.md): Defines temporary result sets (common table expressions) used within a query.

* [**INSERT**](ansi-92-insert.md): Adds new records to an external entity.

* [**UPDATE**](ansi-92-update.md): Changes existing records from external entities based on a condition.

* [**UPSERT**](ansi-92-insert.md): Creates or updates one or more records in an external entity.

* [**DELETE**](ansi-92-delete.md): Deletes records in an external entity.

* [**CALL**](call.md): Executes stored procedures or functions on the external system.


## Operators { #operators }

Operators let you compare values, filter results, and build logic into your SQL statements. 

ANSI-92 supports standard comparison, logical, and pattern-matching operators.

For examples and usage guidance, see the article on [ANSI-92 operators and functions](ansi-92-operators.md).

## Data types { #data-types }

SQL data types define the kind of data you can store and work with in your queries. ANSI-92 uses common types that are supported by most systems.
ODC has an internal SQL type system with mappings to/from attribute data types in external systems. 
ODC will automatically map value and attribute types as outlined in [External data type mapping](../../../../integration-with-systems/external-databases/external-data-type.md) however. it's also possible to `CAST`expressions and attributes to convert them to a different type, refer to [Type conversion](ansi-92-operators.md#type-conversion) for more information. 

<div class="info" markdown="1">

Only the data types that have a mapping at [External data type mapping](../../../../integration-with-systems/external-databases/external-data-type.md) are supported. 

</div>


Null value handling can be configured in ODC Portal as explained [here](../../../../integration-with-systems/external-databases/handle-null-values.md).

For details on supported types and platform-specific differences, see the [data types reference](ansi-92-data-types.md).

## Query execution { #query-execution }

In ODC, queries on external entities aren't sent directly to external systems. ODC parses your SQL, normalizes it, and then generates SQL in the dialect of each external system in order to execute your query. This allows queries to be written in a common language for all external systems and also makes it possible to build mashup queries which can reference entities in multiple external systems.

### Querying one external system

Queries that use entities from a single external system will be fully pushed down to that external system provided it is capable of executing the query. ODC will still normalize the query and generate equivalent SQL in the dialect of the external system.

For trivial queries, the generated SQL is usually similar to the original SQL. For more complex use cases which involve subqueries and common table expressions, the generated SQL may appear quite different from the original query due to how ODC normalizes queries. While ODC may adjust the syntax
of your query, the changes have no impact on the meaning or result of the query and minimal to no impact on the performance of the query.

### Querying multiple external systems (mashup)

Queries that use both internal and external entities or that use entities from more than one external system are called "mashup" queries.

When a mashup query is executed, ODC normalizes the query and pushes down as much of it as possible to the involved external systems. Operations that are usually pushed down include filtering, sorting, calculation of expressions, aggregate functions, and joins when they are between entities on the same external system. Operations which cannot be pushed down will be executed in ODC.

Writing a performant mashup query isn't as easy as writing a performant query to a single external system. In particular, it is critical to use filters, limits, and the right join types to minimize the amount of data that needs to be retrieved by ODC in order to process joins between external
entities.

ODC estimates the computational cost of mashup queries based on the potential number of records that would need to be processed in order for the query to produce a result. When your query exceeds this limit, you will receive an error message explaining which operations in the query are contributing
the most to the expected cost.

We recommend reviewing the following [documentation](../queries.md) for an overview of how to write better mashup queries.
