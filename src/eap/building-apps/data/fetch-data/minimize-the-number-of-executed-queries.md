---
summary: 
tags: 
guid: 271f4a9c-cc4e-480a-9c84-6e09646b3997
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# Enhancing performance by limiting queries 

## Description

Minimize the number of executed queries. You can often fetch all necessary data in a single query instead of multiple ones.

## Solution

Whenever possible, group several Aggregates or SQL queries into one to avoid unnecessary trips to the database. Be sure to: 

* Merge sequences of Aggregates that reference one another into a single Aggregate, [using a join](./supported-join-types.md) to retrieve all the needed data.

* Avoid executing Aggregates or SQL queries inside a For Each cycle. Instead, replace that Aggregate or SQL query with a more complex one that gets all the related information, and executes it before the cycle. In most cases where you have an Aggregate to fetch the master entity before the cycle followed by another Aggregate inside the cycle to fetch the details, you can eliminate the inner Aggregate by [adding a Join ](./supported-join-types.md)to the outer Aggregate.

* Consider enabling the cache for the Aggregate or SQL query if it’s not possible to refactor the query. Ensure thorough validation of business rules related to cache configuration and its impact.

## Importance

Even the simplest Aggregate has to pay the round-trip cost to contact the database. The higher the number of Aggregates and SQL queries, the higher the communication overhead.

For code readability reasons, it’s frequent to use a simple query to retrieve data from a master entity and then fetch the details inside a cycle using another query. However, Aggregates and SQL queries executed inside a cycle can have severe performance impact due to database communication overhead repeated at each iteration. The impact can be greatly worsened when iterating through a list with a high number of elements or when having nested cycles.

The net cost of querying and loading data is lower when executing a single query instead of multiple queries.

## Remarks

While minimizing the number of executed queries can result in large performance gains, it's usually done at the expense of code readability. Thus, the key here is to optimize only when required. Use the Service Center Analytics reports to pinpoint the bottlenecks. Remember that a single fast query doesn't appear on the queries performance report. However, if it’s executed often in a cycle, the accumulated time can influence other reports or logs, such as the screens performance report or the screen requests logs.
