---
summary: Using too many server requests instead of Local Storage
tags: local storage, server requests, data synchronization, offline performance, mobile app optimization
guid: 3d6eebdf-a7d5-43fc-b885-468832a87141
locale: en-us
app_type: mobile apps
platform-version: odc
figma:
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
outsystems-tools:
  - odc studio
---
# Not taking advantage of Local Storage

<div class="info" markdown="1">

Applies to **Mobile apps** only.

</div>

Using too many server requests (screen data action) instead of Local Storage.

## Impact

If the app uses too many screen data actions to gather data from the server, it indicates that Local Storage isn't properly defined or used, as all data is retrieved from the server. This hinders performance and offline requirements in mobile applications.

## Why is this happening?

The app relies too heavily on screen data actions. 

## How to fix

Implement proper synchronization mechanisms and Local Storage to ensure that most data is available in the local storage and facilitates offline scenarios.

For more information, see the [Data Synchronization](https://learn.outsystems.com/training/journeys/data-synchronization-668) online course.
