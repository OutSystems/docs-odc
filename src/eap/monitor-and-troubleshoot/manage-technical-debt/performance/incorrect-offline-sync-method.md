---
summary: Offline sync patterns are not implemented correctly.
tags: offline sync, data synchronization, mobile apps, sync performance, troubleshooting
guid: 41123945-5631-4f69-8c49-49e0dc4df83b
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
  - odc portal
---
# Incorrect offline sync method

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Offline sync patterns are not implemented correctly.

## Impact

Offline synchronization is crucial to ensure data consistency between the device and the server. It is essential for maintaining functionality when the device is not connected to the internet, allowing users to continue using the app, and ensuring that any changes made locally are reflected on the server once connectivity is restored.

## Why is this happening?

Offline synchronization is not being made or is being executed with poor performance.

## How to fix

Place the local entity synchronization actions inside the OfflineDataSync action, configure the manual and automatic start of sync, and use TrigerOfflineDataSync for background synchronizations. Use the SyncUnit parameter to prevent updating unnecessary entities.  

For more information, see the online course on [Data Synchronization](https://learn.outsystems.com/training/journeys/data-synchronization-668).
