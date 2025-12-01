---
summary: OutSystems Developer Cloud (ODC) supports the Keyboard Plugin for keyboard display and visibility control, and event tracking for when the keyboard shows and hides.
tags: mobile development, keyboard, plugin integration, mobile app development
locale: en-us
guid: 0bc905b8-1635-4a06-b439-4bb8059f7f9b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8273-22
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# Keyboard plugin

<div class="info" markdown="1">

Applies only to Mobile Apps.

The Keyboard Plugin available in the ODC Forge is currently only available for MABS 12 or higher, and Capacitor. It uses the [@capacitor/keyboard](https://capacitorjs.com/docs/apis/keyboard) plugin.

</div>

Use the Keyboard plugin for more control over the device's keyboard within your app.

As a best practice, always verify that the plugin is available in the app. Use the **Logic > Client Actions > KeyboardPlugin > CheckKeyboardPlugin** action to check for the plugin's availability before using other plugin actions. If the plugin isn't available to the app, display an error to your users.

<div class="info" markdown="1">

For detailed information about how to install a plugin in your app, refer to  [Adding plugins](../intro.md).

</div>

## Show the device's keyboard (Android only)

To create the logic to show the Android device's keyboard, follow these steps:

1. From the ODC Studio,  go to **Logic > Client Actions > KeyboardPlugin** and drag the **Show** action to your flow. The **Show** action has no input parameters.

![Screenshot of the Show client action being used in ODC Studio](images/show-client-action-odcs.png "Show Client Action")

1. As a best practice, you should handle the result of calling the action by checking the **Success** output parameter. If any errors occur, you can check them using the **Error** output parameters.

Here's the result of calling the **Show** client action on Android:

![Gif of the keyboard opened on an Android device](images/show-keyboard-diag.png "Show Keyboard on Android")

## Hide the device's keyboard

To create the logic to hide the device's keyboard on Android and iOS, follow these steps:

1. From the ODC Studio, go to **Logic > Client Actions > KeyboardPlugin** and drag the **Hide** action to your flow. The **Hide** action has no input parameters.

![Screenshot of the Hide client action being used in ODC Studio](images/hide-client-action-odcs.png "Hide Client Action")

1. As a best practice, you should handle the result of calling the action by checking the **Success** output parameter. If any errors occur, you can check them using the **Error** output parameters.

Here's the result of calling the **Hide** client action on Android:

![Screenshot of the keyboard hidden on an Android device](images/hide-keyboard-android-diag.png "Hide Keyboard on Android")

Here's the result of calling the **Hide** client action on iOS:

![Gif showing the keyboard being hidden on an iOS device](images/hide-keyboard-ios-diag.png "Hide Keyboard on iOS")

## Set the keyboard accessory bar visibility (iOS only)

To create the logic to set the keyboard accessory bar visibility on iOS, follow these steps:

1. From the ODC Studio, go to **Logic > Client Actions > KeyboardPlugin** and drag the **SetAccessoryBarVisible** action to your flow.

![Screenshot of the SetAccessoryBar client action being used in ODC Studio](images/accessory-bar-client-action-odcs.png "SetAccessoryBar Client Action")

1. Set the **IsVisible** input parameter to **True** or **False**, depending if you want the accessory bar to be shown when the keyboard shows or not.

1. As a best practice, you should handle the result of calling the action by checking the **Success** output parameter. If any errors occur, you can check them using the **Error** output parameters.

Here's the result of calling setting the accessory bar as visible on iOS:

![Screenshot of the keyboard on iOS with accessory bar visible](images/accessory-bar-diag.png "Show Accessory Bar on iOS")

## Setting the keyboard style (iOS only)

To create the logic to set the keyboard style on iOS, follow these steps:

1. From the ODC Studio, go to **Logic > Client Actions > KeyboardPlugin** and drag the **SetStyle** action to your flow.

![Screenshot of the SetStyle client action being used in ODC Studio](images/set-style-client-action-odcs.png "SetStyle Client Action")

1. Set the **Style** input parameter to one of the values of **KeybordStyke**, which can be: **Light**, **Dark**, or **Default**. Use **Default** to use the default set for the device.

1. As a best practice, you should handle the result of calling the action by checking the **Success** output parameter. If any errors occur, you can check them using the **Error** output parameters.

Here's the result of calling the **SetStyle** client action with **KeyboardStyle.Dark** on iOS:

![Screenshot of the keyboard with style set to Light on iOS](images/set-style-diag.png "Set Style on iOS")

## Handle keyboard events

To handle events that are triggered when the keyboard is shown and hidden in your app, use the **KeyboardEvents** block.

![Screenshot of the KeyboardEvents block in ODC Studio](images/keyboard-events-odcs.png "KeyboardEvents block in ODC Studio")

The KeyboardEvents block allows you to handle the following events:

* **OnKeyboardWillShow**: An event triggered when the keyboard is about to be shown.
* **OnKeyboardDidShow**: An event triggered when the keyboard is shown.
* **OnKeyboardWillHide**: An event triggered when the keyboard is about to be hidden.
* **OnKeyboardDidHide**: An event triggered when the keyboard is hidden.

Add the **KeyboardEvents** block to every screen where you want these events to be handled. Then, create a handler client action for each event.

## Handling errors

The app with the Keyboard plugin can run on various Android and iOS devices, with different hardware and configurations. To provide a good user experience and prevent the app from crashing, you must handle errors within the app.

See [Keyboard Reference](keyboard-ref.md) for more information about each client action.

## Known issues

* On iOS, after calling the **Hide** client action and the keyboard hides, clicking anywhere on the screen can trigger the keyboard events one more time.
* On iOS, when the accessory bar is set to visible and the keyboard is hidden, the **OnKeyboardDidHide** event can be triggered twice instead of once.
* On iOS, when the accessory bar is set to visible and there is more the once input box, navigating between input boxes with the accessory bar buttons can trigger the **OnKeyboardDidShow** event.
