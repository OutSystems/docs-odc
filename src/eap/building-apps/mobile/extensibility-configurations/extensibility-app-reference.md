---
guid: fc8b0661-525c-4f75-8217-4d9aec2cd312
locale: en-us
summary: This article provide complete details on app extensibility configuration JSON schema.
figma:
coverage-type:
  - remember
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: Mobile,json extensibility,json configuration
outsystems-tools:
  - none
helpids:
---
# App extensibility configuration JSON schema

<div class="info" markdown="1">

The schema may change with every new MABS version.

</div>

[appConfigurations](#appconfigurations)

[Properties](#properties)

[cordova](#cordova)

[permissions](#permissions)

[displayName](#displayname)

[orientation](#orientation)

[orientation Constraints](#orientation-constraints)

[targetDevice](#targetdevice)

[targetDevice Constraints](#targetdevice-constraints)

[backgroundColor](#backgroundcolor)

[backgroundColor Constraints](#backgroundcolor-constraints)

[deeplinksHandler](#deeplinkshandler)

[deeplinksHandler Constraints](#deeplinkshandler-constraints)

[network](#network)

[connections](#connections)

[trustedCA](#trustedca)

[systembars](#systembars)

[style](#style)

[appendUserAgent](#appenduseragent)

[splashscreen](#splashscreen)

[duration](#duration)

[autoHide](#autohide)

[webViewUpdate](#webviewupdate)

[buildConfigurations](#buildconfigurations)

[Properties](#properties-1)

[resources](#resources)

[android](#android)

[ios](#ios)

[splashscreens](#splashscreens)

[android](#android-1)

[ios](#ios-ios-1)

[buildAction](#buildaction)

[config](#config)

[parameters](#parameters)

The extensibility configuration for the application defines a set of configurations that pertain to a specific application. At the top level, it is composed by the following properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| [appConfigurations](#appconfigurations) | `object` | Optional |
| [buildConfigurations](#buildconfigurations) | `object` | Optional |

Example:

```json
{
  "appConfigurations": {
    // ...
  },
  "buildConfigurations": {
    // ...
  }
}
```

## appConfigurations

Application configurations are a set of configurations that modify multiple runtime aspects/behaviors of the mobile application, from background color to how long the splash screen is visible on app launch.

`appConfigurations`

* Optional  
* Type: `object`

### Properties

| Property | Type | Required | Per platform override |
| :---- | :---- | :---- | :---- |
| [cordova](#cordova) | `object` | Optional | false |
| [permissions](#permissions) | `object` | Optional | false |
| [displayName](#displayname) | `string` | Optional | true |
| [orientation](#orientation) | `string` | Optional | true |
| [targetDevice](#targetdevice) | `string` | Optional | true |
| [backgroundColor](#backgroundcolor) | `string` | Optional | true |
| [deeplinksHandler](#deeplinkshandler) | `string` | Optional | true |
| [network](#network) | `object` | Optional | true |
| [systembars](#systembars) | `object` | Optional | true |
| [appendUserAgent](#appenduseragent) | `string` | Optional | true |
| [splashscreen](#splashscreen) | `object` | Optional | true |
| [webViewUpdate](#webviewupdate) | `object` | Optional | false |

Overriding property values per platform is achieved by referencing those properties inside `ios` and/or `android` property. Example:

```json
{
  "appConfigurations": {
    "android": {
      "displayName": "Travel Memories"
    },
    "displayName": "Travel Fragments"
  }
}
```

Where `displayName` value is overridden specifically for Android.

### cordova

Sets Cordova preferences for the application. Preference values can be set globally for both platforms or overridden per platform.

**Example**

```json
{
  "appConfigurations": {
    "cordova": {
      "preferences": {
        "SomePreference": 1337,
        "android": {
          "SomePreference": 0
        }
      }
    }
  }
}
```

Here, the Cordova preference `SomePreference` is being set globally with a value of `1337` but overridden with a value of `0` for Android specifically.

`cordova`

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| [preferences](#cordova-preferences) | `object` | Optional |

#### cordova preferences

Key-value pair of [Cordova preferences](https://cordova.apache.org/docs/en/12.x/config_ref/index.html#preference) to be set.

`preferences`

* Optional  
* Type: `object`

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| `android` | `object` | Optional |
| `ios` | `object` | Optional |
| Additional properties | any of the following: `string` or `boolean` or `number` or `integer` | Optional |

### permissions

Define Android permissions or iOS usage descriptions in the application.

| ❗️ Permissions/usage descriptions values set at the application level take precedence over the values defined on Libraries Extensibility Configuration. |
| :---- |

**Example**

```
{
  "appConfigurations": {
    "permissions": {
      "ios": {
        "NSCameraUsageDescription": "This app wants to help you take a selfie."
      },
      "android": ["android.permissions.CAMERA"]
    }
  }
}
```

`permissions`

* Optional  
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| android | `array` of `string` | Optional |
| ios | `object` | Optional |

### displayName

Override the user-visible name for the application

`displayName`

* Optional  
* Type: `string`  
* Defaults to the OutSystems application name

### orientation

The orientation of the app's user interface

`orientation`

* Optional  
* Type: `string`

#### Orientation Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value |
| :---- |
| `"portrait"` |
| `"landscape"` |
| `"all"` |

### targetDevice

| ❗️ iOS only |
| :---- |

The device family being targeted by application.

`targetDevice`

* Optional  
* Type: `string`

#### targetDevice constraints

**enum**: the value of this property must be equal to one of the following values:

| Value |
| :---- |
| `"phone"` |
| `"tablet"` |
| `"all"` |

### backgroundColor

The WebView and splash screen background color

`backgroundColor`

* Optional  
* Type: `string`  
* Defaults to the primary color of the OutSystems application

#### backgroundColor constraints

**pattern**: the string must match the following regular expression:

```
^#[0-9a-fA-F]{6}$
```

[try pattern](https://regexr.com/?expression=%5E%23%5B0-9a-fA-F%5D%7B6%7D%24)

### deeplinksHandler

<div class="info" markdown="1">

Applies only to Cordova apps.

</div>

Defines how the mobile app handles deeplinks. It can be the default handler, an event handler defined in the app, or a function defined at the window object

`deeplinksHandler`

* Optional  
* Type: `string`  
* Default value: `default`

#### deeplinksHandler constraints

<div class="info" markdown="1">

Applies only to Cordova apps.

</div>

**enum**: the value of this property must be equal to one of the following values:

| Value |
| :---- |
| `"default"` |
| `"event"` |
| `"function"` |

### network

Defines the supported network protocol for the app: HTTPS or both HTTPS and HTTP

`network`

* Optional  
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| [connections](#connections) | `string` | Optional |
| [trustedCA](#trustedca) | `string` | Optional |

### connections

Defines the supported network protocol for the app: HTTPS or both HTTPS and HTTP

`connections`

* Optional  
* Type: `string`

#### connections constraints

**enum**: the value of this property must be equal to one of the following values:

| Value |
| :---- |
| `"https"` |
| `"https_http"` |

### trustedCA

| ❗️Android only |
| :---- |

Sets the type of trusted certificate authorities for the app: `system`, `custom` or `both`.

`trustedCA`

* Optional  
* Type: `string`

#### trustedCA constraints

**enum**: the value of this property must be equal to one of the following values:

| Value |
| :---- |
| `"system"` |
| `"user"` |
| `"both"` |

### systembars

System bars configurations.

**Example**

```json
{
  "appConfigurations": {
    "systembars": {
      "style": "light"
    },
    "android": {
      "systembars": {
        "style": "default"
      }
    }
  }
}
```

`systembars`

* Optional  
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| [style](#style) | `string` | Optional |

### style

Sets the overall system bars style. The style is based on the device appearance. If the device is using Dark mode, the system bars text will be light. If the device is using Light mode, the system bars text will be dark

`style`

* Optional  
* Type: `string`

#### style constraints

**enum**: the value of this property must be equal to one of the following values:

| Value |
| :---- |
| `"default"` |
| `"dark"` |
| `"light"` |

### appendUserAgent

String to append to the original user agent of the app's main WebView

`appendUserAgent`

* Optional  
* Type: `string`

### splashscreen

Splash screen configurations.

**Example**

```json
{
  "appConfigurations": {
    "splashscreen": {
      "duration": 2000,
      "autoHide": true
    },
    "ios": {
      "splashscreen": {
        "duration": 0,
        "autoHide": false
      }
    }
  }
}
```

`splashscreen`

* Optional  
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| [duration](#duration) | `number` | Optional |
| [autoHide](#autohide) | `boolean` | Optional |

### duration

Control for how long, in milliseconds, the launch splash screen is visible when `autoHide` is enabled

`duration`

* Optional  
* Type: `number`

### autoHide

Whether to auto hide the splash after `duration`

`autoHide`

* Optional  
* Type: `boolean`

### webViewUpdate

Displays an alert prompting the user to update the Android System WebView via the Google Play Store. Only applies to OutSystems Capacitor Android apps, which require a minimum WebView version of 102.

**Example**

```json
{
  "appConfigurations": {
    "webViewUpdate": {
      "enabled": true,
      "title": "WebView Update Required",
      "message": "Please update to continue.",
      "updateButtonLabel": "Update"
    }
  }
}
```

`webViewUpdate`

* Optional
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| [enabled](#enabled) | `boolean` | Optional |
| [title](#title) | `string` | Optional |
| [message](#message) | `string` | Optional |
| [updateButtonLabel](#updatebuttonlabel) | `string` | Optional |

### enabled

Determines whether the alert is shown when the device’s WebView version is below the minimum required

`enabled`

* Optional
* Type: `boolean`
* Defaults to true

### title

Title text displayed in the update alert dialog

`title`

* Optional
* Type: `string`

### message

Message text displayed in the update alert dialog

`message`

* Optional
* Type: `string`

### updateButtonLabel

Label for the button that takes the user to the Google Play Store to update WebView

`updateButtonLabel`

* Optional
* Type: `string`

## buildConfigurations

Build configurations are a set of configurations used at build time such as adding build resources or configuring the assets for the splash screen

### **Properties**

| Property | Type | Required | Per platform override |
| :---- | :---- | :---- | :---- |
| [resources](#resources) | `object` | Optional | false |
| [splashscreens](#splashscreens) | `object` | Optional | false |
| [buildAction](#buildaction) | `object` | Optional | false |

### resources

Set of resources that can be copied from a specific source to a target location within the generated mobile project

**Example**

```json
{
  "buildConfigurations": {
    "resources": {
      "ios": [
        {
          "source": "$settings.GoogleServiceInfoPlist",
          "target": "GoogleService-Info.plist"
        }
      ],
      "android": [
        {
          "source": "$settings.GoogleServicesJsonBinary",
          "target": "android/app/src/main/res/google-services.json"
        }
      ]
    }
  }
}
```

`resources`

* Optional  
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| [android](#resource-item) | `array` of `object` | Optional |
| [ios](#resource-item) | `array` of `object` | Optional |

#### android

A list resources to be added to the generated Android project.

`android`

* Optional  
* Type: `array` of [resource](#resource-item) items

#### ios

A list resources to be added to the generated iOS project.

`ios`

* Optional  
* Type: `array` of [resource](#resource-item) items

#### resource item

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| source | `string` | Required |
| target | `string` | Required |

`source`

The source for the resource. One of:

* `string` representing a file path relative to the root folder of the generated project  
* Reference to a Setting that holds a `string` value representing a path relative to the root folder of the generated project. E.g. `$settings.SomeTextSetting`  
* Reference to a Binary Setting  
* Reference to an OutSystems application image via `$images`

`Target`

| ❗️For Android, the target location is relative to the android project located under `android/` For iOS, the target location is relative to the App folder inside `ios/App/App/` |
| :---- |

| Note that `resources` copying occurs before `cap sync` is executed. If a target location is affected by the result of `cap sync`, the resources might be missing |
| :---- |

The target location for the resource in the form of a file path

### splashscreens

Assets to customize the splash screen experience. By default, MABS 12 applications have a splash screen composed of a solid background color. Using `splashscreens` build configurations, the splash screen can be configured to have an image in the center of the screen.

**Example**

```json
{
  "buildConfigurations": {
    "splashscreens": {
      "android": {
        "logo": "$images.MyAppLogoFromAnotherDepartment"
      },
      "ios": {
        "logo": "appIcon"
      }
    }
  }
}
```

`splashscreens`

* Optional  
* Type: `object`

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| [android](#android-1) | `object` | Optional |
| [ios](#ios-1) | `object` | Optional |

#### android

Android specific configurations for the splash screen

`android`

* Optional  
* Type: `object`

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| [logo](#logo) | `string` | Optional |

#### ios {#ios-1}

iOS specific configurations for the splash screen

`android`

* Optional  
* Type: `object`

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| [logo](#logo) | `string` | Optional |

#### logo

Customize the logo based splash screen experience. When using `appIcon`, the application icon will be used in the center of the splash screen. Otherwise a path or reference to an image can be provided

`logo`

* Optional  
* Type: `string`

The value of this property can be:

* `string` representing a file path relative to the root folder of the generated project  
* Reference to an OutSystems application image via `$images`
* Literal value `appIcon`

### buildAction

Build actions enable developers to customize their mobile projects. It is available for MABS 12 and uses JSON files to define which customization is to be done on the mobile project. For more information about the JSON definition for each build action, refer to [Build actions](../build-actions.md).

To run multiple changes, you need to add all to the JSON file, and MABS will run each action following the order of the JSON file, top to bottom.

If you have build configurations defined at the plugin and app level, the plugin runs first.

| Property | Type | Required |
| :---- | :---- | :---- |
| config | `Object` | Required |
| parameters | `object` | Optional |

**Example**

```json
{
  "buildConfigurations": {
    "buildAction": {
        "config": "$resources.buildAction.json",
        "parameters": {
"parameter1" : "parameterValue1",
"parameter2" : "parameterValue2"
}
    }
  }
}
```

#### config

Reference to the resource uploaded on IDE, under resources. The file must have _Deploy Action_ as _Deploy to Target Directory._

| ❗️settings not supported |
| :---- |

* Required  
* Type: `object`

#### parameters

The parameters to pass values to the variables defined on the json.

* Optional  
* Type: `object`

<div class="info" markdown="1">

Extensibility configurations may be processed by OutSystems for the purposes of service improvement and troubleshooting. These configurations should not include or permit access by OutSystems to personal data or confidential or sensitive information. Customers are responsible for ensuring that no personal data or confidential or sensitive information is accessible to OutSystems through any Extensibility configurations. Where such information is included in those configurations, customers should use secret settings to prevent personal data or confidential or sensitive information from being collected by OutSystems.

</div>
