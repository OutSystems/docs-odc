---
summary: Explore the Keyboard Plugin functionalities in OutSystems Developer Cloud (ODC), including client actions, web blocks, and error handling.
tags: mobile development, keyboard, plugin integration, mobile app development, OutSystems api, error handling
locale: en-us
guid: 20a10b22-f55c-4ffa-aa89-d19f2cbaf911
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# Keyboard plugin reference

## Plugin Elements

### Client Actions

#### CheckKeyboardPlugin

Checks if the plugin is ready for use by the app.

|Parameter|Type|Data Type|Description|
|---|---|---|---|
|IsAvailable|Output|Boolean|Whether the plugin is available or not.|
|Error|Output|Error|Error in case plugin is not available.|

#### Show (Android only)

Shows the keyboard.

|Parameter|Type|Data Type|Description|
|---|---|---|---|
|Success|Output|Boolean|Whether or not the function to show the keyboard was called.|
|Error|Output|Error|Error in case showing the keyboard fails.|

#### Hide

Hides the keyboard.

|Parameter|Type|Data Type|Description|
|---|---|---|---|
|Success|Output|Boolean|Whether or not the function to hide the keyboard was called.|
|Error|Output|Error|Error in case hiding the keyboard fails.|

#### SetAccesoryBarVisible (iOS only)

Sets whether or not the accessory bar is visible in the keyboard. This is useful in forms with multiple inputs.

|Parameter|Type|Data Type|Description|
|---|---|---|---|
|IsVisible|Input|Boolean|Boolean variable to set if the accessory bar is visible or not.|
|Success|Output|Boolean|Whether or not setting the accessory bar visibiity was successful.|
|Error|Output|Error|Error in case setting the accessory bar visibility fails.|

#### SetStyle (iOS only)

Sets the style of the keyboard.

|Parameter|Type|Data Type|Description|
|---|---|---|---|
|Style|Input|KeyboardStyle Identifier|Keyboard style to set. Must be one of the styles in the KeyboardStyle static entity. Set it to KeyboardStyle.Default to use the device's default.|
|Success|Output|Boolean|Whether or not setting the style was successful.|
|Error|Output|Error|Error in case setting the style fails.|

### Web Blocks

#### KeyboardEvents

A block that handles the **OnKeyboardWillShow**, **OnKeyboardDidShow**, **OnKeyboardWillHide**, and **OnKeyboardWillHide** events.

##### OnKeyboardWillShow

The event triggered when the keyboard is about to be shown.

|Parameter|Type|Data Type|Description|
|---|---|---|---|
|KeyboardHeight|Input|Integer|Height of the keyboard on the screen.|

##### OnKeyboardDidShow

The event triggered when the keyboard is shown.

|Parameter|Type|Data Type|Description|
|---|---|---|---|
|KeyboardHeight|Input|Integer|Height of the keyboard on the screen.|

##### OnKeyboardWillHide

The event triggered when the keyboard is about to be hidden.

##### OnKeyboardDidHide

The event triggered when the keyboard is hidden.

### Data structures and static entities

#### KeyboardStyle static entity

The static entity for the **Style** parameter of the **SetStyle** client action. Available records are:

* Light
* Dark
* Default

#### KeyboardError data structure

The data structure for errors returned by the Keyboard plugin.

|Parameter|Data Type|Description|
|---|---|---|
|ErrorCode|Text|Error code following the format OS-PLUG-KEYB-XXXX.|
|ErrorMessage|Text|Error message corresponding to ErrorCode.|

### Error Codes

|Code|Platform|Message|
|---|---|---|
|OS-PLUG-KEYB-0001|iOS, Android|Capacitor is not defined. This plugin is only available for Capacitor apps.|
|OS-PLUG-KEYB-0002|iOS, Android|Plugin is not loaded.|
|OS-PLUG-KEYB-0003|iOS, Android|(Any other errors that might occur)|
|OS-PLUG-KEYB-0004|iOS, Android|Not implemented. (For example, this will be returned when calling **Show** on iOS)|
