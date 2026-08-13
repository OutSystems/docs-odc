---
summary: OutSystems Developer Cloud (ODC) provides a server action that invalidates server-side caches for an application, across all replicas.
tags: caching, cache invalidation, system actions
locale: en-us
guid: 61a489f4-a08e-413f-ba58-0892b2bf6746
app_type: mobile apps, reactive web apps
platform-version: odc
content-type:
  - reference
figma:
audience:
  - Developer
outsystems-tools:
  - odc studio
coverage-type:
  - remember
isautopublish: true
---

# ApplicationInvalidateCache server action

ApplicationInvalidateCache invalidates server-side caches for the calling application, across all replicas.

Aggregates, Advanced SQL queries, and server actions store their results in memory when you set their **Cache in Minutes** property. Each application replica keeps an independent copy of that cached data. For details on that property, refer to [Query data using aggregates](../../building-apps/data/fetch-data/aggregate.md#properties), [Query data using SQL](../../building-apps/data/fetch-data/sql/use-sql.md), and [Server Action](../logic-actions/server-action.md#properties).

ApplicationInvalidateCache takes no inputs and returns no outputs.
