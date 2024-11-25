---
summary:
tags:
guid: 2a625247-1f84-4147-99ee-05ed4aa4658b
locale: en-us
app_type: mobile apps
platform-version: odc
figma:
content-type:
  - troubleshooting
  - reference
---

# Non-optimized local data fetch

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

## Impact

Avoid local data fetch on client events (On Initialize, On Ready, On Render). These events are fully serialized, so they do not take advantage of the parallel fetch of data while the screen is already rendered.

## Why is this happening? 

This occurs when local data fetch is performed in client events. 

## How to fix

Data retrieval should occur inside data fetch calls to enable the parallelization of several data fetches and screen rendering. If a data fetch depends on a previous fetch, use the On After Fetch event.
