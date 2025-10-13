---
summary: Learn how to use OutSystems Developer Cloud (ODC) to synchronize offline data in mobile apps with a structured framework.
tags: offline data synchronization, mobile ui framework, entity management, client logic, server logic
locale: en-us
guid: 06c3cb30-b81d-4d6d-8e98-aef3c11d949c
app_type: mobile apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7931-20
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - apply
topic:
  - offline-synch
---

# Implement offline sync

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

OutSystems provides a [framework for syncing data](<sync-reference.md>) between your mobile app and server. The framework includes actions and events available in **Screens**, enabling you to create business logic, trigger syncs, and respond to sync outcomes and network status changes. Use this framework to sync only the data you need, keeping the process lightweight.

This article uses the read-only sync mechanism as an example, but you can apply the process to other sync patterns. In this example, the product catalog is stored on the server, and during the sync, the app updates the local product list.

For local entities created with the **Add Entity from Database** command, you can use accelerators. Some parts of the logic can be generated automatically by right-clicking these local entities and selecting one of the **Create Action to Sync Data** commands.

## Step 1: Create client and server logic

Create the business logic for updating records for individual entities in the client OnSync folder. The complexity of the client and server logic for data sync depends on your business needs and implementation. Here are the common implementation parts:

* Create actions to update local entities during the sync in **Logic** > **Client Actions** > **OnSync** folder.
* Create actions to fetch data from the server and perform updates on the server in **Logic** > **Server Actions** > **OnSync** folder.
* Pass the sync data between the server and client actions.

In this example, the client `SyncProducts` action updates the local data through the local entities with new data from the server. Place this logic into the framework to prepare it for running in the background.

![Diagram showing the creation of client and server logic for data synchronization in a mobile app](images/step-1-offline-odcs.png "Client and Server Logic Creation")

## Step 2: Place the local entity action in the OnSync system event

Place the actions for updating local and remote storage in the flow of the `OnSync` system event. To create the system event, open **Logic**, right-click the **Client Actions** node in the tree, and select **Add System Event** > **On Sync**. This allows you to run the sync in the background without affecting other app processes.

In this example, there is only one action (`SyncProducts`), which is placed in the `OnSync` flow. You are now ready to configure the manual start of the sync.

![Flowchart demonstrating the placement of the local entity action within the OnSync action](images/step-2-offline-odcs.png "Local Entity Action Placement")

## Step 3: Configure manual start of the sync

Start the manual sync using `OnSync` from **Logic** > **Client Actions** > **OnSync**. Place the `OnSync` in the flow where the sync should start.

In this example, a button calls the action named `SyncOnClick`, and within the action's flow, the `OnSync` is dragged and dropped. After ensuring the updating logic works as expected, configure the automatic start of the sync.

![Screenshot of the process to configure manual start of data synchronization in a mobile app](images/step-3-offline-odcs.png "Manual Sync Configuration")

## Step 4: Configure automatic start of the sync

Click the app name, select the **Mobile** tab, and choose the automatic synchronization settings that best suit your app.

In this example, the sync does not start automatically under any conditions, so all values are unchecked.

![Interface showing the configuration settings for automatic start of data synchronization](images/step-4-offline-odcs.png "Automatic Sync Configuration")

## Sync Logic Flow

This is the flow of the sync execution stages. Note that they do not map to the steps used to create the sync logic.

![Illustration of the stages involved in the execution flow of data synchronization logic](images/sync-stages-diag.png "Sync Logic Execution Flow")

Stage 1
: `OnSync` runs the actions for updating local storage in the background. You can start this system event manually by placing it directly in a flow or automatically through an event configured in the **Mobile** tab.

Stage 2
: The actions initiated by `OnSync` collect locally changed records and send them to the server.

Stage 3
: The server processes the requests and returns the updated data.

Stage 4
: The actions in `OnSync` update the local storage with the data received from the server.

<div class="info" markdown="1">

Now that you know how to implement offline synchronization, check the [Offline sync checklist](sync-checklist.md) to avoid common issues in your solution.

</div>

## Related resources

* [Offline sync checklist](sync-checklist.md)

* [Sync framework reference](sync-reference.md)
  
* [Offline data sync patterns](patterns/intro.md)

* [Offline data synchronization mobile apps](intro.md)
