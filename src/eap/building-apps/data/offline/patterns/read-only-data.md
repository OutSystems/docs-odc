---
summary: Learn about the Read-Only Data synchronization pattern in OutSystems Developer Cloud (ODC) for efficient mobile app data management.
tags: data synchronization, offline data handling, local storage, performance optimization, outsystems patterns
locale: en-us
guid: abd5db07-779e-4597-9158-5ac68de2bae4
app_type: mobile apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7907-1038
audience:
  - mobile developers
outsystems-tools:
  - odc studio
  - forge
coverage-type:
  - understand
  - apply
topic:
  - data-synchronization
  - offline-synch
---

# Read-Only data synchronization pattern

<div class="info" markdown="1">

This pattern applies only to mobile apps.

</div>

Use this data synchronization pattern for mobile apps where users only need to read data offline, especially when handling small amounts of data. Here’s how it works:

* The server database holds the master data which can change over time.
* Synchronization downloads all data from the server database and stores it in the local storage of the device.
* Data modifications performed on the device are not propagated to the server.

Here’s an overview of the Read-Only Data pattern logic:

1. ![Icon representing the client in the data synchronization process](images/icon-client.png "Client Icon") Invokes server to get data.

1. ![Icon representing the server in the data synchronization process](images/icon-server.png "Server Icon") Returns database data.

1. ![Icon representing the client in the data synchronization process](images/icon-client.png "Client Icon") Deletes and recreates data in the local storage with the data received from the server.

<div class="info" markdown="1">

Download and store locally only the minimum subset of data relevant to the user to reduce the amount of data synchronized.

</div>

Download the [sample module for the Read-Only Data pattern](https://www.outsystems.com/forge/component-overview/16957/offline-data-sync-patterns-read-only-simple-odc), which uses companies as an example for data synchronization. The following sections explain how to automatically generate this synchronization pattern and provide detailed descriptions of the data model and logic used in the sample module.

## Automatically generate the pattern for an entity

To automatically generate the logic needed to implement this pattern for an entity:

1. In ODC Studio, open the **Data** tab.
1. Under Local Storage, select the local entity of the entity you want to synchronize in the database.
1. Right-click on the local entity and choose **Create Action to Sync Data (Read-Only)**.

    This option is only available if the local entity is linked to the database entity (with the ID as a foreign key to the database entity). This happens if you create local entities by right-clicking on **Local Storage** and choosing **Add Entity from Database...**

    ![Screenshot of the option to create a Read-Only Data synchronization action in Service Studio](images/read-only-data-accelerator-odcs.png "Create Action to Sync Data (Read-Only)")

This creates the actions needed to implement the Read-Only synchronization pattern:

SyncLocal&lt;Entity&gt;
: A client action that starts the synchronization between the local entity and the entity in the server database.

Sync&lt;Entity&gt;
: A server action called by the SyncLocal&lt;Entity&gt; action, which retrieves the current records of the entity in the database to be stored in the client local storage.

If you want this pattern to run in the [synchronization template mechanism](<../sync-implement.md>), add a call to the SyncLocal&lt;Entity&gt; in the OnSync client action.

## Data model

The sample defines a database entity `Company` and its local storage counterpart `LocalCompany`.

![Diagram of the Read-Only Data model showing the Database entity 'Company' and its Local Storage counterpart 'LocalCompany'](images/read-only-data-data-model-odcs.png "Read-Only Data Model")

## OnSync logic

Here’s how the `OnSync` client action works:

![Flowchart of the OnSync client action logic for Read-Only Data synchronization](images/read-only-data-offlinedatasync-odcs.png "OnSync Logic")

1. Call the `ServerDataSync` server action to retrieve data from the database. The server returns a list of `Company` records.
1. Delete all `Company` records in the local storage.
1. Recreate the `Company` records in the local storage using the list of records returned by the server.

`DeleteAllLocalCompanies` and `CreateOrUpdateAllLocalCompanies` are entity actions created automatically for the `LocalCompany` local storage entity. This is a local storage feature to help you handle records.

## ServerDataSync logic

Here’s how the `ServerDataSync` server action works:

![Flowchart of the ServerDataSync server action logic for Read-Only Data synchronization](images/read-only-data-serverdatasync-odcs.png "ServerDataSync Logic")

1. The aggregate `GetCompanies` fetches all the `Company` records from the database.
1. Assign the records returned by the aggregate to the action’s output parameter.

## Related resources

* [Implementing offline sync](../sync-implement.md)
  
* [Sync framework reference](../sync-reference.md)
  
* [Offline sync checklist](../sync-checklist.md)

### Different data synchronization patterns

* [Read-Only data optimzied synchronization pattern](read-only-data-optimized.md)
  
* [Read/Write data last Write wins synchronization pattern](read-write-data-last-write-wins.md)
  
* [Read/Write data One-to-Many synchronization pattern](read-write-data-one-to-many.md)
  
* [Read/Write data with conflict detection synchronization pattern](read-write-data-with-conflict-detection.md)
