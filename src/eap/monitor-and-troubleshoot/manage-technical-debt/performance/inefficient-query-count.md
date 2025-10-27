---
summary: Counting query results using an inefficient query.
tags: sql query optimization, performance improvement, data retrieval, database efficiency, troubleshooting
guid: 0b899e99-db9d-4840-85ae-691656b8f0d8
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3525-185&t=ZHJybqzEUX6B7aIU-1
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - unblock
  - remember
---

# Inefficient query count

Counting query results using an inefficient query.

## Impact

SQL queries are usually designed for retrieving data. They may perform joins and fetch extra data needed for processing but aren't required to count the query results. When you use the Count property of a query, the system executes the same query to count the results, which is inefficient since it uses the same query definition.

## Why is this happening?

The query retrieves and processes additional data beyond what is needed for the count operation, causing this inefficiency. The joins and conditions increase the query's complexity, resulting in higher processing time and resource usage. The database engine has to perform more operations than necessary, which impacts performance.

![An action flow with a SQL query using a join and a condition, and then a Count node.](images/odcs-inefficient-query-count.png "Inefficient query count")

## How to fix

Use a simplified SQL query to efficiently count the results, removing unneeded extra data and joins.

For more information, refer to the [best practice for optimizing record counting](../../../building-apps/ui/creating-screens/best-practices-fetch-display-data.md#record-counting).
