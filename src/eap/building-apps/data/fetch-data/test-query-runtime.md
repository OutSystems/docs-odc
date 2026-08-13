---
summary: Learn how Test Query in ODC Studio relates to the runtime behavior of Aggregates and SQL nodes.
tags:
  - Aggregates
  - Best Practices
  - Data
  - Performance
  - SQL
guid: 27423808-d804-47e2-b238-3421126ef15d
locale: en-us
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
audience:
  - Developer
  - Front-end developer
  - Tech lead
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - unblock
isautopublish: true
---

# Understand test query results

Aggregates and SQL nodes let you validate a query's logic in ODC Studio with **Test Query**, before you use the query in your app's logic. Test Query and your published app run a query through different paths, so the results you see in Test Query and the results your app produces at runtime can differ. This article describes where each difference comes from.

## Data volume differs across environments

Aggregates and mashup queries estimate an execution plan cost based on the number of records in each entity involved. The Development stage typically holds fewer records than QA or Production. A query that stays under the cost limit in Development can exceed it in QA or Production, where the same tables hold more records.

Refer to [writing better queries in data mashup](queries.md) for the record-limit behavior, and to [troubleshooting aggregates that use data mashup](data-mashup-errors.md) for the resulting error and how to resolve it.

## Transactions on external entities

For SQL nodes that query external entities, `INSERT`, `UPDATE`, `DELETE`, and `CALL` statements commit immediately when you run Test Query. Refer to [query data using SQL](sql/use-sql.md) for this behavior and how internal entities differ.

## Different query paths

Test Query runs a query through a separate path in ODC Studio, distinct from the path your published app uses at runtime. For most queries, the two paths produce identical results. For some SQL constructs, the query that Test Query runs and the query that your app runs at runtime differ.

Use Test Query to validate a query's logic. For a complex or performance-sensitive query, also validate it in the target environment with representative data. Test Query results reflect the query's logic, not the exact rows or behavior your app produces at runtime.

## Related resources

* [Writing better queries in data mashup](queries.md)
* [Query data using SQL](sql/use-sql.md)
* [Troubleshooting aggregates that use data mashup](data-mashup-errors.md)
