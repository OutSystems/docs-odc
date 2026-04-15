---
summary: Learn about common data synchronization patterns for mobile apps with OutSystems Developer Cloud (ODC), including sample modules for implementation.
tags: data synchronization, local storage, server database, sample modules, forge components
locale: en-us
guid: f5bd8377-7e81-4ae7-a75f-f5a2dca688de
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - odc studio
  - forge
coverage-type:
  - none
topic:
  - data-synchronization
  - offline-synch
---

# Offline data sync patterns

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

This article describes common data synchronization patterns between local storage (mobile device) and the server database. These patterns are provided as samples you can use to create an implementation for your use case.

For each synchronization pattern, a working sample module is provided. You can use these modules to explore how the synchronization mechanism is implemented. [Download an application from the Forge](http://www.outsystems.com/forge/component/1638/Offline+Data+Sync+Patterns/) that contains all sample modules.

Here are the patterns:

* [Read-only data](read-only-data.md)
* [Read-only data optimized](read-only-data-optimized.md)
* [Read/write data last write wins](read-write-data-last-write-wins.md)
* [Read/write data with conflict detection](read-write-data-with-conflict-detection.md)
* [Read/write data one-to-many](read-write-data-one-to-many.md)
