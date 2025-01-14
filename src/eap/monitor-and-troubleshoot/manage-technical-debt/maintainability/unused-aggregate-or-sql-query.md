---
summary: An Aggregate or SQL query isn't used.
tags: unused aggregates, sql queries, performance optimization, code maintenance, app performance
guid: f6b3dd0f-5a48-47a9-9e62-fb6b0dfc7c77
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - unblock
  - remember
audience:
  - full stack developers
  - mobile developers
  - backend developers
outsystems-tools:
  - odc studio
  - odc portal
---
# Unused Aggregate or SQL Query

An Aggregate or SQL query isn't used.

## Impact

Unused data queries (Aggregates or SQL queries) can waste resources and degrade performance, as they might run even if not referenced. Unused data queries also bloat your code base, making maintenance and debugging difficult.

## Why is this happening?

The logic defines an aggregate or SQL query, but it's not used or referenced anywhere in the app.

## How to fix

Consider deleting the aggregate or SQL query if they aren't strictly necessary.
