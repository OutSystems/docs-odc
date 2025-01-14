---
summary: The Local Storage model is not optimized.
tags: local storage optimization, mobile performance, client aggregates, data modeling, app performance improvement
guid: 3d1e42c4-4ce3-4d68-876b-7f64a4c85d7e
locale: en-us
app_type: mobile apps
platform-version: odc
figma:
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
  - full stack developers
outsystems-tools:
  - odc studio
---
# Non-optimized Local Storage

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

The Local Storage model is not optimized.

## Impact

A non-optimized Local Storage forces the use of multiple joins in client aggregates, hindering the app's performance on mobile devices.

## Why is this happening?

Local Storage is either being copied exactly from server entities or using a complex model (including too many fields, foreign keys, or complex data types).

## How to fix

Simplify local entities to the minimum number of attributes and de-normalize them as much as possible, still keeping them simple; review client aggregates for unnecessary joins.

For more information, see the [Local Storage](https://learn.outsystems.com/training/journeys/local-storage-676) online course.
