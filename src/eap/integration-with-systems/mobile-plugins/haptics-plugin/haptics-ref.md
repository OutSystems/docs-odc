---
summary: Explore the Haptics Plugin functionalities in OutSystems Developer Cloud (ODC), including client actions and error handling.
tags: mobile development, haptics, vibration, feedback, plugin integration, mobile app development
locale: en-us
guid: 8f24f6f1-7d87-4ca1-9ec9-2b6dcfde47b1
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

# Haptics Plugin Reference

## Plugin Elements

### Client Actions

#### CheckHapticsPlugin

Checks if the plugin is ready for use by the app.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| IsAvailable | Output | Boolean | Whether the plugin is available or not. |
| Error | Output | Error | Error in case plugin is not available. |
| Parameter | Type | Data Type | Description |

#### Impact

Trigger a haptics impact feedback.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Style | Input | ImpactStyle Identifier | Impact feedback style. Must be one of the styles in the ImpactStyle static entity. |
| Success | Output | Boolean | Whether or not impact haptics was executed. |
| Error | Output | Error | Error in case impact haptics failed. |

#### Notification

Trigger a haptics notification feedback.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Type | Input | NotificationType Identifier | Notification feedback type. Must be one of the types in the NotificationType static entity. |
| Success | Output | Boolean | Whether or not notification haptics was executed. |
| Error | Output | Error | Error in case notification haptics failed. |

#### Vibrate

Vibrate the device.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Duration | Input | Integer | Duration of the vibration in milliseconds. |
| Success | Output | Boolean | Whether or not device vibration was triggered. |
| Error | Output | Error | Error in case device vibration failed to trigger. |

#### SelectionStart

Trigger a selection started haptic hint.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Success | Output | Boolean | Whether or not the selection start was set. |
| Error | Output | Error | Error in case selection start failed. |

#### SelectionChanged

Trigger a selection changed haptic hint. If a selection was started already, this causes the device to provide haptic feedback.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Success | Output | Boolean | Whether or not the selection changed haptics was triggered. |
| Error | Output | Error | Error in case selection change haptics failed. |

#### SelectionEnd

If SelectionStart was called, this client action ends the selection. For example, you can call this function when a user lifts their finger from a control.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Success | Output | Boolean | Whether or not the selection end was set. |
| Error | Output | Error | Error in case selection end failed. |

#### Enumerations

##### GetImpactStyleValues

Get a list of Impact Styles. This is useful for presenting options in an app UI.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| ImpactStyleList | Output | ImpactStyle Record List | List with the records from ImpactStyle. |

##### GetNotificationTypeValues

Get a list of notification types. This is useful for presenting options in an app UI.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| NotificationTypeList | Output | NotificationType Record List | List with the records from NotificationType. |

### Data structures and Static Entities

#### ImpactStyle Static Entity

The static entity for the **Style** parameter of the **Impact** client action. The available records are:

* Light
* Medium
* Heavy

#### NotificationType Static Entity

The static entity for the **Type** parameter of the **Notification** client action. The available records are:

* Success
* Warning
* Error

#### HapticsError data structure

The data structure for errors returned by the Haptics plugin.

| Parameter | Data Type | Description |
| - | - | - |
| ErrorCode | Text | Error code following the format OS-PLUG-HAPT-XXXX. |
| ErrorMessage | Text | Error message corresponding to ErrorCode. |

### Error codes

| Code | Platform | Message |
| - | - | - |
| OS-PLUG-HAPT-0001 | iOS, Android | Capacitor is not defined. This plugin is only available for Capacitor apps. |
| OS-PLUG-HAPT-0002 | iOS, Android | Plugin is not loaded. |
| OS-PLUG-HAPT-0003 | iOS, Android | (Any other errors that might occur) |
