---
summary: Use the OutSystems Developer Cloud (ODC) checklist to improve offline data synchronization in mobile apps, enhancing performance and user experience.
tags: offline data synchronization, performance optimization, best practices, mobile sync patterns, data management
locale: en-us
guid: d3fe3f23-f7bf-443b-b37e-8e772fffe77a
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
topic:
  - data-synchronization
  - offline-synch
---

# Offline sync checklist

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Here is a checklist for implementing sync in mobile devices. If you follow the checklist you can improve synchronization of data between the mobile device and the server, as well as ensure there are no performance issues in the overall experience.

## Introduction

Understand the importance of offline synchronization and how it enhances the performance and user experience of mobile apps.

## Common pitfalls to avoid

Learn about common mistakes in offline synchronization and how to prevent them.

Have you called `OnSync` multiple times?
: Calling `OnSync` multiple times triggers several synchronizations simultaneously, which can cause your data to sync incorrectly.

Have you called the `OnSync` system event inside an `OnSyncComplete` action?
: If you use `OnSyncComplete` to trigger multiple syncs, avoid calling `OnSync` inside `OnSyncComplete`, as this creates a synchronization loop. Instead, to synchronize sequentially, call `OnSyncComplete` one after the other. These calls are queued and processed sequentially.

## Improve performance

Follow these guidelines to optimize your mobile app's performance during offline synchronization.

Are the local entities designed as lightweight versions of the server entities? Have the entity relationships been denormalized?
: Mobile devices lack the network resources and computing power of a server and can efficiently handle only small amounts of data. Ensure the local entities contain only the attributes your offline business logic requires. Avoid adding all the attributes of the server entities. Additionally, update only the records relevant to the current user of the mobile app.

Does the server logic minimize the data-set returned while keeping the logic simple?
: The application should transfer the least amount of data that is needed to successfully complete the synchronization. Also, know your users and the conditions in which the app works - this will help you determine the optimal settings, such as the timeouts.

Is `OnSync` called to initiate the sync?
: Ensure all elements used to manually start the sync, call `OnSync`, which launches the sync in the background. `OnSync` is optimized for asynchronous sync, background tasks, and triggering sync events.

Do you use the `Context` of `OnSync` to sync only the entities that need an update?
: Pass the string parameter `Context` to `OnSync` so the execution flow can branch and sync only the necessary entities.

## Application design best practices

Follow these guidelines to create maintainable mobile apps and handle data conflicts effectively.

Did you consider an app design that avoids conflicts during sync?
: Sometimes, you can improve the app to prevent conflicts between local and server data. Consider whether conflicts are essential to the use case. For example, the last-write-wins pattern may suit most needs, or editing can be locked while the device is offline.

If the business logic needs to deal with data conflicts, does the UX support conflict management?
: If data conflicts are part of your business case, ensure user data is never lost due to poor UX. End users should clearly understand the consequences of their actions and be informed of the sync status.

Do all synced local entities have their own action in the OfflineDataSync folder?
: Instead of placing all logic for synced local entities in the default OnSync action, create individual actions in the same folder to sync each local entity. This keeps the sync logic organized and enables granular, controlled syncs.

## Enhance end user experience

Follow these guidelines to provide a seamless and user-friendly experience during offline synchronization.

Is automatic sync configured?
: Set up automatic data syncs for specific conditions in the Mobile tab inside Application Properties.

Does the app provide feedback to end users about the sync status?
: End users should know the status of the data sync. Use Screen events to react to changes in the network and sync status, and update the UI to provide visual feedback. For example, display messages like "Syncing...", "Sync failed...", or "You’re offline."

## Related resources

* [Sync framework reference](sync-reference.md)
* [Offline data sync patterns](patterns/intro.md)
