---
summary: Server data isn't being stored in the local database asynchronously.
tags:
guid: 48e2ddb8-31e5-4d4c-963e-00ad9aed2056
locale: en-us
app_type: mobile apps
platform-version: odc
figma:
content-type:
  - troubleshooting
  - reference
---

# No asynchronous Offline sync

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Server data isn't stored in the local database asynchronously.

## Impact

Synchronously storing server data blocks screens and/or actions that may impact the overall user experience.

## Why is this happening? 

This issue arises because the server data in the mobile application is stored in the local database synchronously, rather than asynchronously

## How to fix

Use TriggerOfflineDataSync to execute OfflineDataSync asynchronously and react to the OnSyncComplete event to update UI modules.


For more information, see the [Data Synchronization](https://learn.outsystems.com/training/journeys/data-synchronization-668) online course.
