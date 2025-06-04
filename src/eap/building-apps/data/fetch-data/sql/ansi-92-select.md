---
guid: 33a2f97a-130e-4311-913a-e7f797df9b12
locale: en-us
summary: Understand SQL SELECT statement and WITH clause in OutSystems Developer Cloud (ODC) for executing mashup queries involving internal and external entities.
figma:
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - data engineers
tags: sql, mashup queries, select statement, with clause, database queries
outsystems-tools:
  - odc studio
  - odc portal
---

# SELECT statement in ANSI-92 queries

```sql
[ WITH withItem [ , withItem ]* ]
SELECT [ DISTINCT ] { * | selectItem [, selectItem ]* }
[ FROM entityExpression ]
[ WHERE condition ]
[ GROUP BY { expression [, expression ]* } ]
[ HAVING condition ]
[ WINDOW windowName AS ( windowDefinition ) [, windowName as ( windowDefinition ) ]* ]
[ UNION [ ALL | DISTINCT ] select ]
[ ORDER BY orderItem [, orderItem ]* ]
[ LIMIT count ]

withItem:
        entityAlias [ ( attributeAlias [, attributeAlias ]* ) ] AS ( select )

selectItem:
        expression [ [ AS ] attributeAlias ]
    |   windowFunction OVER { windowName | ( windowDefinition ) } [ [ AS ] attributeAlias ]

entityExpression:
        entity [ [ AS ] entityAlias [ ( attributeAlias [ , attributeAlias ]* ) ] ]
    |   ( select ) [ [ AS ] entityAlias [ ( attributeAlias [ , attributeAlias ]* ) ] ]
    |   entityExpression [, entityExpression ]*
    |   entityExpression [ CROSS ] JOIN entityExpression
    |   entityExpression [ INNER ] JOIN  entityExpression ON condition
    |   entityExpression { LEFT | RIGHT | FULL } [ OUTER ] JOIN entityExpression ON condition

windowDefinition:
        [ existingWindowName ]
        [ PARTITION BY expression [, expression ]* ]
        [ ORDER BY orderItem [, orderItem ]* ]
        [ { RANGE | ROWS } BETWEEN windowBound AND windowBound ]

windowBound:
        CURRENT ROW
    |   { UNBOUNDED | value } { PRECEDING | FOLLOWING }

orderItem:
        expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ]
```

`SELECT` fetches records from one or more entities.

The statement must reference at least one external entity and may reference any number of internal entities.

A `SELECT` statement that contains both internal and external entities or that uses external entities from more than one external system is called a "mashup" query. There are significant differences in how mashup queries are executed compared to regular queries, for more information please refer to [Query execution](ansi-92-syntax.md#query-execution).


<div class="info" markdown="1">

* The user configured on the connection must have permission to read from the entity in the external system
* If the entity has attributes of an unsupported data type then those attributes will not appear in the result and can't be referenced in the query. `SELECT *` and `SELECT {entity}.*` will still work in this case but won't reference the unsupported attributes.
* Subqueries can't be used in expressions unless using an [Operator](ansi-92-operators.md) which accepts a subquery like `EXISTS`.

</div>

## WITH clause

```sql
[ WITH withItem [ , withItem ]* ]

withItem:
        entityAlias [ ( attributeAlias [, attributeAlias ]* ) ] AS ( select )
```

The `WITH` clause defines one or more named entity expressions based on other `SELECT` statements which can then be referenced as entities in the subsequent outer `SELECT` statement.

The query for a given `withItem` must return records with the correct number of attributes to match the `attributeAlias` list. To reference the result of this query in the outer `SELECT` statement, the `entityAlias` may be used in any place where an `entity` can be used however the syntax is not the same. Entities are referenced using `{entity}` but a `withItem` must be referenced with the `"entityAlias"` syntax. Similarly, the attributes of a `withItem` are not referenced using the usual `{entity}.[attribute]` syntax, instead you should use `"entityAlias".[attributeAlias]` or `"entityAlias"."attributeAlias"`.

### SELECT DISTINCT

```sql
SELECT [ DISTINCT ] { * | selectItem [, selectItem ]* }

selectItem:
        expression [ [ AS ] attributeAlias ]
```

If `SELECT DISTINCT` is specified, the fetched records will be deduplicated before being returned in the result.

ODC converts `SELECT DISTINCT` into `GROUP BY` for all external systems in order to provide a more consistent experience. This also means that `SELECT DISTINCT` is equivalent to using `GROUP BY` with the expressions in the [SELECT list](#select-list).

When `SELECT DISTINCT` is used with a [SELECT List](#select-list) which does not reference any attributes from an external system which requires attributes to be used in `GROUP BY`, such as Microsoft SQL Server, then ODC will push the expressions in the [SELECT List](#select-list) into a subquery and use `GROUP BY` with the result of the subquery.

### SELECT list { #select-list }

```sql
SELECT [ DISTINCT ] { * | selectItem [, selectItem ]* }

selectItem:
        expression [ [ AS ] attributeAlias ]
```

The `SELECT` list (between `SELECT` and `FROM`) specifies expressions that will be mapped to attributes in the returned records. The expressions may use [Operators](ansi-92-operators.md), [Literals](ansi-92-data-types.md#sql-types), dynamic parameters, and/or any attributes from entities or subqueries in the `FROM` clause.

There are important differences in how identifiers work in ANSI-92 syntax compared to commonly used database systems, for more information please refer to [Statements](ansi-92-syntax.md#statements).

```sql
-- Not valid, the outer SELECT expects abc but the inner SELECT returns ABC
SELECT sub.[abc] FROM ( SELECT 1 as abc ) as sub

-- All of these are valid
SELECT sub.abc FROM ( SELECT 1 as abc ) as sub
SELECT sub.[abc] FROM ( SELECT 1 as [abc] ) as sub
SELECT sub.[abc] FROM ( SELECT 1 as "abc" ) as sub
SELECT sub."abc" FROM ( SELECT 1 as "abc" ) as sub
```

Expressions in a `SELECT` list without an explicit alias will be given a name automatically depending on the type of expression. If the expression is a simple reference to an attribute from the `FROM` clause then the name of the attribute will be used as the alias. No guarantees are made about the names used for other types of expression, they may not always be the same. When an attribute is renamed in ODC Portal and not aliased in a query, the generated alias will be the original attribute name and not the new name provided in ODC Portal.

```sql
-- In this example, entity has one attribute called 'abc' in the external system which has been renamed to 'Abc' in ODC Portal

-- The implicit alias will be 'abc' and not `Abc`
SELECT {entity}.[Abc] FROM {entity}

-- Neither of these are valid because the implicit alias in the subquery is 'abc' and not 'Abc'
SELECT [Abc] FROM ( SELECT {entity}.[Abc] FROM {entity} ) sub
SELECT sub.[Abc] FROM ( SELECT {entity}.[Abc] FROM {entity} ) sub

-- The recommended way to write the query above is to use an explicit alias
-- This query is always valid even if the attribute is renamed on the entity
SELECT [Abc] FROM ( SELECT {entity}.[Abc] AS [Abc] FROM {entity} ) sub

-- No guarantees are made about the implicit alias for other expressions
-- They should be aliased if they need to be referenced by another part of the query
SELECT sub.[result] FROM (SELECT {entity}.[abc] + 3 AS [result] FROM {entity}) sub
```

It's recommended to use quoted and qualified names throughout the query to avoid unexpected issues and because it makes the query easier to understand.

The `SELECT` list may also contain one or more [window functions](ansi-92-operators.md#window-functions) used together with an inline window definition or a named window defined in the [WINDOW clause](#window-clause).

#### Known issues with SELECT list

* Attributes with the same name but from different entities/subqueries in the same `SELECT` list
  must be explicitly aliased.
    ```sql
    -- Returns error: Attribute 'name' is ambiguous
    SELECT {this}.[name], {other}.[name] FROM {this}, {other}

    -- Workaround
    SELECT {this}.[name] AS thisname, {other}.[name] AS othername FROM {this}, {other}
    ```

* The error message returned when an alias is not in scope is incorrect.

    ```sql
    -- Query is invalid because the FROM clause contains an explicit alias
    -- Returns error: 'entity' not found in any connection
    SELECT {entity}.[attribute] FROM {entity} AS renamed
    -- All of these are valid
    SELECT {entity}.[attribute] FROM {entity}
    SELECT renamed.[attribute] FROM {entity} AS renamed
    ```

### FROM clause { #from-clause }

```sql
[ FROM entityExpression ]

entityExpression:
        entity [ [ AS ] entityAlias [ ( attributeAlias [ , attributeAlias ]* ) ] ]
    |   entityExpression [, entityExpression ]*
    |   entityExpression [ CROSS ] JOIN entityExpression
    |   entityExpression [ INNER ] JOIN  entityExpression ON condition
    |   entityExpression { LEFT | RIGHT | FULL } [ OUTER ] JOIN entityExpression ON condition
    |   ( subquery ) [ [ AS ] entityAlias [ ( attributeAlias [ , attributeAlias ]* ) ] ]
```

The `FROM` clause specifies one or more entities for the `SELECT` to fetch records from. The query must have at least one `FROM` clause since it must reference at least one external entity, however this clause can be in a subquery and does not have to be in the outermost `SELECT`.

A `SELECT` without a `FROM` clause will return a single record with the values derived from the expressions in the [SELECT List](#select-list).

The `FROM` clause supports a number of different join types.

The `FROM {left}, {right}` syntax is equivalent to both a `CROSS JOIN` (cartesian product) and an `INNER JOIN` with an `ON TRUE` condition. The comma join syntax is only supported at the top level, for example `FROM ({left} CROSS JOIN {right}), {other}` is not valid. These joins will
produce a result where every record from the left entity is joined to every record in the right entity. If both entities had 5 records, the result would contain 25 records.

An inner join such as `FROM {left} INNER JOIN {right} ON condition` will only return joined records for which the condition evaluates to `TRUE`.

A one-sided outer join such as `FROM {left} LEFT OUTER JOIN {right} ON condition` will return joined records for which the condition evaluates to `TRUE` and one-sided records with values only from the outer entity (left in this example) when the condition does not evaluate to `TRUE`. The
one-sided records will have `NULL` values for the attributes from the inner entity (right, in this example).

A full outer join such as `FROM {left} FULL OUTER JOIN {right} ON condition` will return joined records for which the condition evaluates to `TRUE` and one-sided records for both sides when the condition does not evaluate to `TRUE`.

The `ON` clause is mandatory for inner and all outer joins. The `OUTER` keyword is optional.

The `FROM` clause may also source records from one or more subqueries, commonly known as derived tables. Derived tables may be used in any position where an entity reference can be used. Derived tables must be enclosed in parentheses.

Entities and subqueries used in a `FROM` clause may optionally be given an alias. Subqueries without an alias will be given a name automatically however that name is not guaranteed to always be the same. For this reason, it is recommended to always specify an alias for subqueries.

#### Known issues with FROM

* Joining more than one subquery without a `FROM` clause to an entity is not supported, for example:

    ```sql
    SELECT * FROM (
        SELECT 1
    ) "a", (
        SELECT 2
    ) "b", { entity }
    ```

* Entities with the same original name but from different connections in the `FROM` clause must be explicitly aliased.

### WHERE clause

```sql
[ WHERE condition ]
```

The `WHERE` clause is used to filter records based on a provided condition. The result will only contain records for which the condition evaluates to `TRUE`.

Like the [SELECT List](#select-list), the condition may contain any of the supported [operators](ansi-92-operators.md) as well as any attributes from entities or subqueries in the [FROM clause](#from-clause).

Aliases from the [SELECT List](#select-list) cannot be used in the `WHERE` clause for that `SELECT`.
The `WHERE` clause can however, use attributes from the [FROM clause](#from-clause).

Filtering based on an expression in the `SELECT` can usually be achieved by copying the expression into the `WHERE` clause.

### GROUP BY clause { #group-by }

```sql
[ GROUP BY { expression [, expression ]* } ]
```

The `GROUP BY` clause is used to aggregate records based on one or more expressions.

The expressions in the `GROUP BY` clause may contain any of the supported [operators](ansi-92-operators.md), any attributes from the [FROM clause](#from-clause), and/or any aliases from the [SELECT List](#select-list).

When the [SELECT List](#select-list) contains an [Aggregate Function](ansi-92-operators.md#aggregate-functions) together with non-aggregated attributes, the `GROUP BY` clause is mandatory to specify the groups of records that the aggregate function should be calculated for.

For example, `SELECT "A" / 2 AS "key", MAX( "B" ) AS "value"` must have a `GROUP BY` which groups the `"A"` attribute. In this case, either `GROUP BY "key"` or `GROUP BY "A"` can be used.

#### Known issues with GROUP BY

* Grouping by a boolean expression is not supported in Oracle and Microsoft SQL Server.

### HAVING clause

```sql
[ HAVING condition ]
```

The `HAVING` clause is used to filter records after they have been grouped and may only be used when a [GROUP BY clause](#group-by) is specified.

The condition may contain any of the supported [operators](ansi-92-operators.md) as well as any attributes from the [FROM clause](#from-clause). Aliases from the [SELECT list](#select-list) cannot be used in
the `HAVING` clause.

### WINDOW clause

```sql
[ WINDOW windowName AS ( windowDefinition ) [, windowName as ( windowDefinition ) ]* ]
windowDefinition:
        [ existingWindowName ]
        [ PARTITION BY expression [, expression ]* ]
        [ ORDER BY orderItem [, orderItem ]* ]
        [ { RANGE | ROWS } BETWEEN windowBound AND windowBound ]
windowBound:
        CURRENT ROW
    |   { UNBOUNDED | value } { PRECEDING | FOLLOWING }
```

The `WINDOW` clause is used to create one or more named windows. The windowName may be referenced in an `OVER` clause in the [SELECT List](#select-list) or by a subsquent window definition with existingWindowName.

The expressions in the `WINDOW` clause may contain [operators](ansi-92-operators.md) (excluding those which require subqueries) as well as any attributes from the [FROM clause](#from-clause). Aliases from the [SELECT list](#select-list) cannot be used in expressions in the `WINDOW` clause.

The `PARTITION BY` clause groups the records of the window frame into one or more partitions, in this case the window function is applied to each partition separately. If a `PARTITION BY` clause is not specified, then all records of the window frame will be in a single partition. This clause is not allowed when defining a new window based on another window using existingWindowName.

The `ORDER BY` clause defines the order of records in each partition of the window frame. This clause is mandatory for some [Window functions](ansi-92-operators.md#window-functions) because their result depends on the ordering of the records.

The `RANGE` or `ROWS` clause specifies the lower and upper bounds of the window frame. This clause may only be used if there is an `ORDER BY` clause in the same window or in the referenced window (existingWindowName). A window without an `ORDER BY` clause will have bounds equivalent to `RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`. A window with an `ORDER BY` but no `RANGE` or `ROWS` clause will have bounds equivalent to `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

When using `RANGE`, the `ORDER BY` must only sort on a single attribute and the bounds are specified in terms of that attribute. The values provided as bounds in this case must also match the data type of the sorted attribute. For example, `ORDER BY {entity}.[age] RANGE BETWEEN 1 PRECEDING and 2 FOLLOWING` will include records around the current record from `[age] - 1` to `[age] + 2`.

The `ROWS` clause specifies the bounds in terms of the number of records. For example, `ORDER BY {entity}.[age] ROWS BETWEEN 1 PRECEDING AND 2 FOLLOWING` will include the previous record and up to two subsequent records.

If an existingWindowName is specified, then it must refer to an earlier entry in the same `WINDOW` clause. There are some special rules that apply in this case:

* The existing window must not have a `ROWS` or `RANGE` clause
* The new window must not have a `PARTITION BY` clause
* The new window may only have an `ORDER BY` clause if the existing window does not have one

#### Known issues with WINDOW and OVER

* Microsoft SQL Server only supports `RANGE` with bounds of `CURRENT ROW` and `UNBOUNDED`, values may not be used as bounds
* Window functions are not supported with Salesforce and SAP OData

### UNION clause { #union-clause }

```sql
[ UNION [ ALL | DISTINCT ] select ]
```

The `UNION` clause implements the logical set operation of the same name.

`select1 UNION select2` collects records from the results of both `select1` and `select2`. The
records are deduplicated by default (`UNION DISTINCT` is the default behaviour). To keep the
duplicates, use the `UNION ALL` syntax.

#### Known issues with UNION

- `UNION` is not supported in mashup queries.

### ORDER BY clause

```sql
[ ORDER BY orderItem [, orderItem ]* ]

orderItem:
        expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ]
```

The `ORDER BY` clause is used to sort the result of a query by one or more expressions before it's returned. When two records are equal according to the left-most expression, they're compared according to the next expression and so on. If the records are equal according to all expressions, then the records may be returned in any order.

When an `ORDER BY` clause isn't specified, the records returned by the query may be in any order and that order is not guaranteed to always be the same. If your application requires the records to be returned in a specific order, then always use an `ORDER BY` to guarantee the records are returned in the expected order.

The `ORDER BY` expressions can reference attributes from the [SELECT list](#select-list), using either their ordinal position (`ORDER BY 1` will order by the first attribute), or by name (`ORDER BY "a"` will order by attribute `"a"`). Ordering by constants or dynamic parameters (without inline expansion) isn't supported.

The `ORDER BY` expressions may also use operators and functions from the following categories:

* [Arithmetic operators and functions](ansi-92-operators.md#arithmetic-operators-and-functions)
* [Character string operators and functions](ansi-92-operators.md#character-string-operators-and-functions)
* [Date/time functions](ansi-92-operators.md#datetime-functions)
* [Type conversion functions](ansi-92-operators.md#type-conversion)

The `ASC` and `DESC` keywords may be used to control the direction of the sort (ascending and descending). If not specified, `ASC` is assumed by default.

The `NULLS FIRST` and `NULLS LAST` keywords may be used to control how `NULL` values are sorted.
When not specified, ODC will not override the `NULL` ordering of the external system.

| External System      | Default NULL Ordering |
|----------------------|-----------------------|
| Microsoft SQL Server | LOWEST VALUE          |
| Oracle               | HIGHEST VALUE         |
| PostgreSQL           | HIGHEST VALUE         |
| Salesforce           | FIRST                 |
| SAP OData            | LOWEST VALUE          |

For mashup queries, the default `NULL` ordering can vary depending on which external system the attribute is sourced from and whether the sorting is pushed down to an external system.

In mashup queries where the sort cannot be pushed down, the default `NULL` ordering is the same as Oracle and PostgreSQL (`HIGEST VALUE`).

Note that `ORDER BY` is not supported in subqueries. A given `SELECT` statement should not have more than one `ORDER BY` and, if present, it should be on the outermost `SELECT`.

#### Known issues with ORDER BY

- Ordering by a constant or dynamic parameter based expression in the [SELECT List](#select-list) is
  not supported
- Ordering by character strings can be inconsistent depending on the collation of the attributes.
- `NULLS FIRST` and `NULLS LAST` have no effect when the sorting is pushed down to Microsoft SQL
  Server.

### LIMIT clause { #limit }

```sql
[ LIMIT count ]
```

The `LIMIT` clause is used to limit the number of records returned by a query. It's recommended as a best practice to always specify the `LIMIT` clause to ensure that a query does not return more records than intended.

The `count` may be specified using a literal of any numeric type or with a dynamic parameter.

The `LIMIT` clause is permitted in subqueries but this is only supported with PostgreSQL and won't work with other external systems.

### OFFSET clause

```sql
[ OFFSET start ]
```

The `OFFSET` clause is used to skip a number of records returned by a query so that the result starts from the position specified. This is commonly used with `LIMIT` when implementing pagination.
`OFFSET` should always be used with `ORDER BY` to ensure that the records are always sorted the same way.

The `start` may be specified using a literal of any numeric type or with a dynamic parameter.

The `OFFSET` clause is permitted in subqueries but this is only supported with PostgreSQL (when used with `LIMIT`) and will not work with other external systems.


## Examples

```sql
-- Select all attributes of an entity with a specific id
SELECT {entity}.*
FROM {entity}
WHERE {entity}.[id] = @dynamic
-- Common table expressions
WITH "temp1" ("id", "total") AS (
  SELECT
    {entity1}.[id] AS "id",
    SUM({entity1}.[value]) AS "total"
  FROM {entity1}
  GROUP BY {entity1}.[id]
  HAVING SUM({entity1}.[value]) > 100
), "temp2" ("id", "name") AS (
  SELECT
    {entity2}.[id] AS "id",
    {entity2}.[name] AS "name"
  FROM {entity2}
)
SELECT
  "temp2"."name",
  "temp1"."total"
FROM "temp1"
INNER JOIN "temp2"
ON "temp1"."id" = "temp2"."id"
ORDER BY "temp2"."name" ASC
LIMIT 10
-- Use a subquery with EXISTS in WHERE
SELECT {entity1}.*
FROM {entity1}
WHERE EXISTS (
  SELECT *
  FROM {entity2}
  WHERE {entity2}.[id] = {entity1}.[id]
)
-- Derived tables
SELECT
  "a"."name" AS "name",
  CAST(COALESCE("b"."average", 0) AS DECIMAL(9, 3)) AS "average"
FROM (
  SELECT
    {entity1}.[id] AS "id",
    {entity1}.[name] AS "name"
    FROM {entity1}
    WHERE {entity1}.[name] LIKE @dynamic
) "a" LEFT JOIN (
  SELECT
    {entity2}.[id] AS "id",
    AVG({entity2}.[value]) AS "average"
  FROM {entity2}
  WHERE {entity2}.[isDeleted] IS FALSE
  GROUP BY {entity2}.[id]
) "b"
ON "a"."id" = "b"."id"
ORDER BY "b"."average" DESC
LIMIT 10
-- Window functions
SELECT
    {entity}.[department],
    AVG({entity}.[salary]) OVER "framed",
    SUM({entity}.[salary]) OVER "by_department"
FROM {entity}
WINDOW
    "by_department" AS (PARTITION BY {entity}.[department]),
    "ordered" AS ("by_department" ORDER BY {entity}.[startDate]),
    "framed" AS ("ordered" RANGE BETWEEN INTERVAL '1' YEAR PRECEDING AND INTERVAL '1' YEAR FOLLOWING)
```
