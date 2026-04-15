---
summary: Learn how to integrate GPS capabilities in your applications using the Location Plugin in OutSystems Developer Cloud (ODC).
tags: gps integration, plugin installation, real-time tracking, error handling, geolocation
locale: en-us
guid: f2b0feab-c558-4d7f-b507-4511ae094677
app_type: mobile apps
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=3203-7693&p=f&t=HgzpbirauijY3Jp8-0
audience:
  - mobile developers
  - frontend developers
  - full stack developers
platform-version: odc
coverage-type:
  - apply
  - remember
outsystems-tools:
  - odc studio
topic:
  - using-cordova-plugins
  - using-capacitor-plugins
---

# Location plugin

Use the location plugin to enable an application to access the GPS capabilities of the user device, like latitude, longitude, and altitude. This plugin works with native mobile apps, progressive web apps (PWAs), and web apps.

<div class="info" markdown="1">

Refer to [Use mobile plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps.

</div>

## Add necessary permissions (property list keys) for location (iOS only)

To use the location plugin on iOS, provide descriptions for two property list keys: **NSLocationWhenInUseUsageDescription** and **NSLocationAlwaysAndWhenInUseUsageDescription**.

From plugin version 2.2.0, set the **LocationWhenInUseUsageDescription** and **LocationAlwaysAndWhenInUseUsageDescription** extensibility settings in the **Mobile distribution** tab of the ODC Portal.

If you don't configure these settings, the plugin uses default values.

For plugin versions earlier than 2.2.0, add the permissions to the app extensibility configurations:

(Recommended) Using the universal extensibility configurations schema:

```json
{
  "appConfigurations": {
    "permissions": {
      "ios": {
        "NSLocationAlwaysAndWhenInUseUsageDescription": "This app accesses your location to give you the best restaurants near you.",
        "NSLocationWhenInUseUsageDescription": "This app accesses your location to give you the best restaurants near you."
      }
    }
  }
}
```

Using the Cordova-based extensibiility configurations schema (for MABS versions lower than 12):

```json
{
  "preferences": {
    "ios": [
      {
        "name": "NSLocationAlwaysAndWhenInUseUsageDescription",
        "value": "This app accesses your location to give you the best restaurants near you."
      },
      {
        "name": "NSLocationWhenInUseUsageDescription",
        "value": "This app accesses your location to give you the best restaurants near you."
      }
    ]
  }
}
```

## Using the plugin

To use the location plugin actions in **ODC Studio**, go to **Logic** > **Client Actions** > **LocationPlugin**.

<div class="info" markdown="1">

To prevent errors, check if the plugin is available with the action **CheckLocationPlugin** before calling any other client action. If the plugin isn't available, display an error to the user.

</div>

### Get device location

Use the **GetLocation** action to retrieve the current device location (latitude, longitude, altitude).

You can configure the action to:

* Enable high accuracy mode.
* Define a timeout.
* Set a maximum age (in milliseconds) to use a cached location.

Handle the **Success** output parameter to ensure the operation worked. If **True**, use the location data from the output. If **False**, handle the error.

![Flowchart showing the logic to get device location using the Location Plugin in ODC Studio](images/logic-to-get-device-location-odcs.png "Logic to Get Device Location")

### Track location in real time

To monitor the device location in real time and update your app as the position changes, follow these steps:

1. Drag the **LocationTracker** block to your screen. This block handles the **OnPositionChanged** event.

![Screenshot of the process to add the LocationTracker block on a screen in ODC Studio](images/add-location-tracker-ocds.png "Add LocationTracker Block")

1. Use the **WatchPosition** action to start monitoring the device position. Call this action in a flow that suits your use case (for example, on screen initialization).
    * This action returns a **WatchId**. Store this identifier if you need to stop monitoring later.

![Illustration of using the WatchPosition action to update device location in real time in ODC Studio](images/watch-position-action-odcs.png "WatchPosition Action")

1. Create a client action to handle the **OnPositionChanged** event from the **LocationTracker** block.
    * This event provides the new **Location** structure and the **WatchId**.

![Diagram showing the logic to handle the event of the device's position changing in ODC Studio](images/logic-handle-event-odcs.png "Logic to Handle Event of Position Changing")

1. To stop monitoring, use the **ClearWatch** action with the **WatchId** you stored earlier.

## Handling errors

Apps with the Location Plugin run on many Android or iOS devices, with different hardware and configurations. To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

The following actions help you handle errors. Use these actions with **If** nodes to check for errors and control how the app works.

| Variable    | Action              | Description                                                                    |
| :---------- | :------------------ | :----------------------------------------------------------------------------- |
| IsAvailable | CheckLocationPlugin | True if the Location Plugin is available in the app.                           |
| Success     | GetLocation         | True if there aren't errors while getting the device position.                 |
| Success     | WatchPosition       | True if there aren't errors while receiving position updates in real time.     |
| Success     | ClearWatch          | True if there aren't errors while canceling position updates in real time.     |

![Flowchart demonstrating how to handle errors when using the Location Plugin in ODC Studio](images/handling-errors-odcs.png "Handling Errors")

## Actions

The following actions are available in the plugin. The Location Plugin is dual-stack, using a Cordova plugin for Cordova apps and a Capacitor plugin for Capacitor apps. For more information, refer to [cordova-outsystems-geolocation](https://github.com/ionic-team/cordova-outsystems-geolocation) and [capacitor-geolocation](https://github.com/ionic-team/capacitor-geolocation).

| Action              | Description                                                                                 | Available in PWA |
| :------------------ | :------------------------------------------------------------------------------------------ | :--------------- |
| CheckLocationPlugin | Checks if the location plugin is available in the app.                                      | Yes              |
| GetLocation         | Gets the current GPS information if the GPS is enabled on the device.                       | Yes              |
| WatchPosition       | Tracks the device position and triggers OnPositionChanged event from LocationTracker block. | Yes              |
| ClearWatch          | Clears a previously registered position watch.                                              | Yes              |

## MABS compatibility

The table shows the compatibility of the Location Plugin with the Mobile Apps Builds Service (MABS).

| Plugin version  | Compatible with MABS version | Notes |
| :-------------- | :--------------------------- | :---- |
| 1.0.1 and later | MABS 10.0 and later.         |       |
| 0.1.0 and later | MABS 9.0 and later.          |       |
