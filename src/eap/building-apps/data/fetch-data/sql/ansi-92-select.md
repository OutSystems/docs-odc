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
# title

```sql
[ WITH withItem [ , withItem ]* ]
SELECT [ DISTINCT ] { * | selectItem [, selectItem ]* }
[ FROM entityExpression ]
[ WHERE condition ]
[ GROUP BY { expression [, expression ]* } ]
[ HAVING condition ]
[ UNION [ ALL | DISTINCT ] select ]
[ ORDER BY orderItem [, orderItem ]* ]
[ LIMIT count ]
[ OFFSET start ]

withItem:
        entityAlias [ ( attributeAlias [, attributeAlias ]* ) ] AS ( select )

selectItem:
        expression [ [ AS ] attributeAlias ]

entityExpression:
        entity [ [ AS ] entityAlias [ ( attributeAlias [ , attributeAlias ]* ) ] ]
    |   entityExpression [, entityExpression ]*
    |   entityExpression [ CROSS ] JOIN entityExpression
    |   entityExpression [ INNER ] JOIN  entityExpression ON condition
    |   entityExpression { LEFT | RIGHT | FULL } [ OUTER ] JOIN entityExpression ON condition
    |   ( select )

orderItem:
        expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ]
```


`SELECT` fetches records from one or more entities.

The statement must reference at least one external entity and may reference any number of internal entities.

A `SELECT` statement that contains both internal and external entities or that uses external entities from more than one external system is called a "mashup" query. There are significant differences in how mashup queries are executed compared to regular queries, for more information please refer to [Query execution](ansi-92-syntax.md#query-execution).

## WITH clause

```sql
[ WITH withItem [ , withItem ]* ]

withItem:
        entityAlias [ ( attributeAlias [, attributeAlias ]* ) ] AS ( select )
```

The `WITH` clause defines one or more named entity expressions based on other `SELECT` statements which can then be referenced as entities in the subsequent outer `SELECT` statement.

The query for a given `withItem` must return records with the correct number of attributes to match the `attributeAlias` list. To reference the result of this query in the outer `SELECT` statement, the `entityAlias` may be used in any place where an `entity` can be used however the syntax is not the same. Entities are referenced using `{entity}` however a `withItem` must be referenced with the `"entityAlias"` syntax. 
Similarly, the attributes of a `withItem` are not referenced using the usual`{entity}.[attribute]` syntax, instead you should use `"entityAlias"."attributeAlias"`.

### SELECT DISTINCT

```sql
SELECT [ DISTINCT ] { * | selectItem [, selectItem ]* }

selectItem:
        expression [ [ AS ] attributeAlias ]
```

If `SELECT DISTINCT` is specified, the fetched records will be deduplicated before being returned in the result.

ODC converts `SELECT DISTINCT` into `GROUP BY` for all external systems in order to provide a more consistent experience. This also means that `SELECT DISTINCT` is equivalent to using `GROUP BY` with the expressions in the [SELECT List](#select-list).

When `SELECT DISTINCT` is used with a [SELECT List](#select-list) which does not reference any attributes from an external system which requires attributes to be used in `GROUP BY`, such as Microsoft SQL Server, then ODC will push the expressions in the [SELECT List](#select-list) into a subquery and use `GROUP BY` with the result of the subquery.

### SELECT List { #select-list }

```sql
SELECT [ DISTINCT ] { * | selectItem [, selectItem ]* }

selectItem:
        expression [ [ AS ] attributeAlias ]
```

The `SELECT` list (between `SELECT` and `FROM`) specifies expressions that will be mapped to attributes in the returned records. The expressions may use [Operators](ansi-92-operators.md) as well as any attributes from entities or subqueries in the `FROM` clause.

It's recommended to always use qualified names in the `SELECT` list when referencing attributes. This avoids potential conflicts when working with multiple entities and makes the query easier to understand.

For attributes which originate from an entity, use the `{entity}.[attribute]` syntax.
For attributes which are derived in a subquery, use the `"alias"."attribute"` syntax.

### FROM clause { #from-clause }

```sql
[ FROM entityExpression ]

entityExpression:
        entity [ [ AS ] entityAlias [ ( attributeAlias [ , attributeAlias ]* ) ] ]
    |   entityExpression [, entityExpression ]*
    |   entityExpression [ CROSS ] JOIN entityExpression
    |   entityExpression [ INNER ] JOIN  entityExpression ON condition
    |   entityExpression { LEFT | RIGHT | FULL } [ OUTER ] JOIN entityExpression ON condition
    |   ( subquery )
```

The `FROM` clause specifies one or more entities for the `SELECT` to fetch records from. The query must have at least one `FROM` clause since it must reference at least one external entity, however this clause can be in a subquery and does not have to be in the outermost `SELECT`.

A `SELECT` without a `FROM` clause will return a single record with the values derived from the expressions in the [SELECT List](#select-list).

The `FROM` clause supports a number of different join types.

The `FROM {left}, {right}` syntax is equivalent to both a `CROSS JOIN` (cartesian product) and an `INNER JOIN` with an `ON TRUE` condition. These joins will produce a result where every record from the left entity is joined to every record in the right entity. If both entities had 5 records, the result would contain 25 records.

An inner join such as `FROM {left} INNER JOIN {right} ON condition` will only return joined records for which the condition evaluates to `TRUE`.

A one-sided outer join such as `FROM {left} LEFT OUTER JOIN {right} ON condition` will return joined records for which the condition evaluates to `TRUE` and one-sided records with values only from the outer entity (left in this example) when the condition does not evaluate to `TRUE`. The one-sided records will have `NULL` values for the attributes from the inner entity (right in this example).

A full outer join such as `FROM {left} FULL OUTER JOIN {right} ON condition` will return joined records for which the condition evaluates to `TRUE` and one-sided records for both sides when the condition does not evaluate to `TRUE`.

The `ON` clause is mandatory for inner and all outer joins. The `OUTER` keyword is optional.

The `FROM` clause may also source records from one or more subqueries, commonly known as derived tables. Derived tables may be used in any position where an entity reference can be used. Derived tables must be enclosed in parentheses and should always be named with an alias.

#### Known issues

- Joining more than one subquery without a `FROM` clause to a table is not supported, for example:
    ```sql
    SELECT * FROM (
        SELECT 1
    ) "a", (
        SELECT 2
    ) "b", { entity }
    ```

### WHERE Clause

```sql
[ WHERE condition ]
```

The `WHERE` clause is used to filter records based on a provided condition. The result will only contain records for which the condition evaluates to `TRUE`.

Like the [SELECT List](#select-list), the condition may contain any of the supported [Operators](ansi-92-operators.md) as well as any attributes from entities or subqueries in [FROM clause](#from-clause)

Aliases from the [SELECT List](#select-list) cannot be used in the `WHERE` clause for that `SELECT`. The `WHERE` clause can however, use attributes from the [FROM clause](#from-clause).

Filtering based on an expression in the `SELECT` can usually be achieved by copying the expression into the `WHERE` clause.

### GROUP BY Clause

```sql
[ GROUP BY { expression [, expression ]* } ]
```

The `GROUP BY` clause is used to aggregate records based on one or more expressions.

The expressions in the `GROUP BY` clause may contain any of the supported [Operators](ansi-92-operators.md), any attributes from the [FROM clause](#from-clause) and/or any aliases from the [SELECT List](#select-list).

When the [SELECT List](#select-list) contains an [Aggregate Function](ansi-92-operators.md#aggregate-functions) together with non-aggregated attributes, the `GROUP BY` clause is mandatory to specify the groups of records that the aggregate function should
be calculated for.

For example, `SELECT "A" / 2 AS "key", MAX( "B" ) AS "value"` must have a `GROUP BY` which groups the `"A"` attribute. In this case, either `GROUP BY "key"` or `GROUP BY "A"` can be used.

#### Known Issues

- Grouping by a boolean expression is not supported in Oracle and Microsoft SQL Server.

### HAVING Clause

```sql
[ HAVING condition ]
```

The `HAVING` clause is used to filter records after they have been grouped and may only be used when a [GROUP BY Clause](#group-by-clause) is specified.

The condition may contain any of the supported [Operators](ansi-92-operators.md) as well as any attributes from the [FROM Clause](#from-clause).
Aliases from the [SELECT List](#select-list) cannot be used in the `HAVING` clause.


### UNION Clause

```sql
[ UNION [ ALL | DISTINCT ] select ]
```

The `UNION` clause implements the logical set operation of the same name.

`select1 UNION select2` collects records from the results of both `select1` and `select2`. The
records are deduplicated by default (`UNION DISTINCT` is the default behaviour). To keep the
duplicates, use the `UNION ALL` syntax.

#### Known Issues

- `UNION` is not supported in mashup queries.

### ORDER BY clause

```sql
[ ORDER BY orderItem [, orderItem ]* ]

orderItem:
        expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ]
```

The `ORDER BY` clause is used to sort the result of a query by one or more expressions before it is returned. When two records are equal according to the left-most expression, they are compared
according to the next expression and so on. If the records are equal according to all expressions, then the records may be returned in any order.

When an `ORDER BY` clause is not specified, the records returned by the query may be in any order and that order is not guaranteed to always be the same. If your application requires the records to be returned in a specific order, then always use an `ORDER BY` to guarantee the records are returned in the expected order.

The `ORDER BY` expressions can reference attributes from the [SELECT List](#select-list), using either their ordinal position (`ORDER BY 1` will order by the first attribute), or by name (`ORDER BY "a"` will order by attribute `"a"`). Ordering by constants or dynamic parameters (without inline expansion) is not supported.

The `ORDER BY` expressions may also use operators and functions from the following categories:

- [Arithmetic Operators and Functions](ansi-92-operators.md#arithmetic-operators-and-functions)
- [Character String Operators and Functions](ansi-92-operators.md#character-string-operators-and-functions)
- [Date/Time Functions](ansi-92-operators.md#datetime-functions)
- [Type Conversion Functions](ansi-92-operators.md#type-conversion-functions)

The `ASC` and `DESC` keywords may be used to control the direction of the sort (ascending and descending). If not specified, `ASC` is assumed by default.

The `NULLS FIRST` and `NULLS LAST` keywords may be used to control how `NULL` values are sorted.
When not specified, ODC will not override the `NULL` ordering of the external system.

| External System      | Default NULL Ordering |
|:---------------------|:----------------------|
| Microsoft SQL Server | LOWEST VALUE          |
| Oracle               | HIGHEST VALUE         |
| PostgreSQL           | HIGHEST VALUE         |
| Salesforce           | FIRST                 |
| SAP OData            | LOWEST VALUE          |

For mashup queries, the default `NULL` ordering can vary depending on which external system the attribute is sourced from and whether the sorting is pushed down to an external system.

In mashup queries where the sort cannot be pushed down, the default `NULL` ordering is the same as Oracle and PostgreSQL (`HIGEST VALUE`).

Note that `ORDER BY` is not supported in subqueries.

#### Known Issues

* Ordering by a constant or dynamic parameter based expression in the [SELECT List](#select-list) is not supported.
* Ordering by character strings can be inconsistent depending on the collation of the attributes.
* `NULLS FIRST` and `NULLS LAST` have no effect when the sorting is pushed down to Microsoft SQL Server.

### LIMIT clause

```sql
[ LIMIT count ]
```

The `LIMIT` clause is used to limit the number of records returned by a query. It is recommended as
a best practice to always specify the `LIMIT` clause to ensure that a query does not return more
records than intended.

The `count` may be specified using a literal of any numeric type or with a dynamic parameter.

The `LIMIT` clause is permitted in subqueries but this is only supported with PostgreSQL and will
not work with other external systems.

### OFFSET clause

```sql
[ OFFSET start ]
```

The `OFFSET` clause is used to skip a number of records returned by a query so that the result starts from the position specified. This is commonly used with `LIMIT` when implementing pagination.
`OFFSET` should always be used with `ORDER BY` to ensure that the records are always sorted the same way.

The `start` may be specified using a literal of any numeric type or with a dynamic parameter.

The `OFFSET` clause is permitted in subqueries but this is only supported with PostgreSQL (when used with `LIMIT`) and will not work with other external systems.

## Notes

* The user configured on the connection must have permission to read from the entity in the external system.
* If the entity has attributes of an unsupported data type then those attributes will not appear in the result and cannot be referenced in the query. `SELECT *` and `SELECT {entity}.*` will still work in this case but will not reference the unsupported attributes.
* Subqueries cannot be used in expressions unless using an [Operator](ansi-92-operators.md) which accepts a subquery like `EXISTS`.

