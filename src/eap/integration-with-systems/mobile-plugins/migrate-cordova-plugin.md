---
guid: 5c42a3de-543f-48f1-970a-be21fab0f28d
locale: en-us
summary: This article describes how to migrate a Cordova plugin to a Capacitor plugin
figma:
coverage-type:
  - understand
  - apply
  - unblock
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: plugin migration, cordova, capacitor, mobile development, outsystems plugins
outsystems-tools:
  - odc studio
  - odc portal
helpids:
---
# Migrate Cordova plugin to Capacitor plugin

This article explains how you can migrate OutSystems Mobile Plugins to use [Capacitor](https://capacitorjs.com/), a modern native runtime framework for mobile apps. ODC app plugins rely on [Cordova](https://cordova.apache.org/) to access native functionalities. With MABS 12, you can build both Capacitor and Cordova apps. This means you can update your MABS version and continue using the Cordova framework and your existing plugins without changes. However, we recommend switching to the Capacitor framework to leverage its modern capabilities.

Capacitor supports [Cordova Plugins](https://capacitorjs.com/docs/plugins/cordova), though with some limitations. To address these limitation, MABS 12 introduces capabilities such as universal extensibility and build actions that, when used with guidance provided in this article, allow you to make OutSystems plugins compatible with both Cordova (MABS 11) and Capacitor (MABS 12), enabling a dual-stack approach.

To achieve this, you can follow two main approaches:

Approach 1: Make an existing Cordova Plugin compatible with Capacitor for use in Capacitor apps.
  
Approach 2: Create a Capacitor Plugin with the same functionality as the existing Cordova Plugin. Then, configure the OutSystems plugin to use either one based on the available native mobile framework.

Approach 1 is quicker and requires less effort, while approach 2 allows you to leverage Capacitor-specific functionalities directly in your plugin. You can also adopt a phased migration, starting with Approach 1 and later progressing to Approach 2.

## Changes in extensibility configurations for all plugins

With MABS 12, extensibility configurations now follow a [universal extensibility schema](../../building-apps/mobile/extensibility-configurations.md). You need to update your OutSystems plugin, even if you only use Cordova.

For example, if your mobile plugin is offered as a library on ODC, and your current extensibility Configurations are:

```json
{
    "plugin": {
        "url":"<url_to_cordova_plugin>",
        "variables": [
            {
                "name": "CUSTOM_CORDOVA_PREFENCE",
                "value": "cordova_preference_value"
            }
        ]
    },
    "metadata": {
        "mabs-min": "10.0.0",
        "name": "Your Plugin",
        "version": "1.0.0"
    }
}
```

To comply with MABS 12’s universal schema, you must update your extensibility configurations to:

```json
{
    "buildConfigurations": {
        "cordova": {
            "source": {
                "npm": "<url_to_cordova_plugin>"
            },
            "preferences": {
                "CUSTOM_CORDOVA_PREFENCE": "cordova_preference_value"
            }
        }
    },
    "plugin": {
        "url":"<url_to_cordova_plugin>",
        "variables": [
            {
                "name": "CUSTOM_CORDOVA_PREFENCE",
                "value": "cordova_preference_value"
            }
        ]
    },
    "metadata": {
        "mabs-min": "10.0.0",
        "name": "Your Plugin",
        "version": "1.0.0"
    }
}
```

Key differences between the Cordova-based and Universal schema are:

1. The `plugin` block is now under `buildConfigurations` > `cordova`.
2. Cordova preferences, previously under `plugin` > `variables` are now in `buildConfigurations` > `cordova` >  `preferences`.

The Cordova-based extensibility configurations remain to ensure the OutSystems Plugin works in MABS 11.

If you choose to support Capacitor, additional changes may be required in your library’s extensibility. These are described later in this document. For detailed information refer to [Library (plugin) extensibility configuration JSON schema](../../building-apps/mobile/extensibility-configurations/extensibility-lib-reference.md).

## Use Cordova plugins in Capacitor

Capacitor supports Cordova Plugins. Depending on your plugin, you may not require changes, excluding changes in extensibility configurations.

This section first describes scenarios where no changes are needed, followed by required changes to ensure full compatibility with MABS 12 and Capacitor.

### Existing Cordova-Capacitor compatibility

In most cases, the source code of the Cordova Plugin—whether JavaScript, TypeScript, Java, Kotlin, Swift, or Objective-C—doesn’t require changes to be compatible with Capacitor. One exception is if it uses [Cordova-specific functionalities](#cordova-specific-references).

The main file you need to analyze to determine if a Cordova Plugin is fully compatible with Capacitor is the `plugin.xml` file.

Capacitor in OutSystems processes some elements in a Cordova `plugin.xml` file:

* The `js-module` block, where you define your clobbers to access Cordova plugin methods in OutSystems JavaScript blocks.
* Tags for defining native source code and native dependencies—`source-file`, `header-file`, `resource-file`, `lib-file` `framework`, `podspec`.
* The `features` inside the `config-file` block.
* Dependencies on other Cordova plugins using the “dependency” tag. However, you must ensure those dependencies are compatible with Capacitor as well.
* Limited support for `config-file` and `edit-config`—changes for the Android platform, and exclusively for `AndroidManifest.xml`.

For example, if you have an OutSystems Plugin for accessing the phone’s contacts, and the Cordova `plugin.xml` file looks like this:

```xml
<plugin>
    ...
    <js-module src="www/contacts.js" name="Contacts">
        <clobbers target="cordova.plugins.contacts" />
    </js-module>
    <platform name="android">
        <config-file target="res/xml/config.xml" parent="/*">
            <feature name="Contacts"> ... </feature>
        </config-file>
        <config-file target="AndroidManifest.xml" parent="/*">
            <uses-permission android:name="android.permission.READ_CONTACTS" />
        </config-file>
        <source-file src="src/android/ContactManager.java" />
    </platform>
    <platform name="ios">
        <config-file target="config.xml" parent="/*">
            <feature name="Contacts"> ... </feature>
        </config-file>
        <header-file src="src/ios/CDVContacts.h" />
        <source-file src="src/ios/CDVContacts.m" />
    </platform>
</plugin>
```

Then the plugin should be compatible with Capacitor out of the box, apart from the [extensibility configuration changes](#changes-in-extensibility-configurations-for-all-plugins). Regardless, you should test your plugin on an OutSystems app built with MABS 12 and Capacitor to confirm everything works as expected.

### Changes required for Capacitor compatibility

These Cordova functionalities in `plugin.xml` are not supported by Capacitor directly:

* `preference` -  setting plugin variables, be it globally or per platform.
* `hooks`  running scripts at different points of the Cordova lifecycle.
* Most changes that use `config-file` or `edit-config`. For instance, changes to `Info.plist` on iOS in `plugin.xml` are not directly supported by Capacitor.

If your OutSystems plugin uses any of the above mentioned functionalities from Cordova, there will be migration work to make the plugin compatible with Capacitor.

### Migrate Cordova preferences

Cordova preferences allow for the creation of variables that can be customized by users of a Plugin. These preferences can then be used elsewhere in `plugin.xml`.
Below is an example of an Android-specific preference:

```xml
<preference name="MY_CUSTOM_STRING" default="default-value" />
<config-file target="./res/values/strings.xml" parent="/resources">
    <string name="custom">$MY_CUSTOM_STRING</string>
</config-file>
```

You can currently set the preference values in both ODC library and app extensibility configurations (compatible with MABS 11).

In Capacitor builds, the preference value cannot be changed  the default value is always used. To allow for easier customization of these variables by OutSystems users, we recommend using Settings in ODC.
Using ODC Studio, you can add Settings to your Library by going into “Data” \-\> “Settings” \-\> Right-click \-\> “Add Setting”.
OutSystems developers are able to customize the setting value without having to change the App’s Extensibility \- in the App’s “Configuration” tab inside ODC Portal.

### Migrate Cordova hooks

Cordova hooks exist to allow plugin developers to perform custom actions and setup that is otherwise not possible when configuring the `plugin.xml`.
MABS 12 overcomes this with a new feature called [build actions](../../building-apps/mobile/build-actions.md). With Build Actions, you can do various customizations on native mobile apps, writing minimal code.

There are separate build actions for [iOS](../../building-apps/mobile/build-actions-iOS.md) and [Android](../../building-apps/mobile/build-actions-android.md) platform.

You set up build actions in a single .json file. This example changes the app’s name:

```json
{
    "variables": {
        "APP_NAME": {
            "type": "string",
            "default": "My OutSystems App"
        }
    },
    "platforms": {
        "android": {
            "appName": "$APP_NAME"
        },
        "ios": {
            "displayName": "$APP_NAME"
        }
    }
}
```

Where `APP_NAME` is a variable that you can specify when invoking the build actions.

In ODC Studio, include the json file in **Data > Resources**.

In the library’s extensibility, add the reference to the .json file, and pass the `APP_NAME` parameter.  You can specify a setting so that users can customize the value on their app via ODC Portal:

```json
{
   "buildConfigurations": {
        "buildAction": {
            "config": $resources.setAppName.json,
            "parameters": {
                "APP_NAME": $settings.AppName
            }
        }
    },
}
```

OutSystems recommends always using build action however there may be specific uses that cannot be accomplished with build actions. In such scenarios, you can use [Capacitor Hooks](https://capacitorjs.com/docs/cli/hooks), which allow you to run scripts in different phases of the Capacitor build process.

### Migrate “config-file” changes

Most `config-file` declarations in Cordova’s `plugin.xml` do not work out-of-the-box in Capacitor. Depending on the change, there are multiple ways to migrate.

If you have a usage description for the `Info.plist` file on iOS, you can use MABS 12 Extensibility Configurations. For example, if you have your `plugin.xml` with:

```xml
    <config-file target="*-Info.plist" parent="NSCameraUsageDescription">
      <string>This app requires access to camera to scan barcodes.</string>
    </config-file>
```

You add the following content to the library’s extensibility, leveraging ODC settings:

```json
{
    "plugin": {
        "variables": [{
            "name": "CAMERA_USAGE_DESCRIPTION",
            "value": $settings.CameraUsageDescription
        }]
    }
    "pluginConfigurations": {
        "permissions": {
            "android": [
                "android.permission.CAMERA"
            ]
            "ios": {
                "NSCameraUsageDescription": {
                    "description": $settings.CameraUsageDescription
                }
            }
        }
    }
}
```

Where the setting name is `CameraUsageDescription`, and `plugin variables` block is added in case you want to use the setting to set a [Cordova preference](#migrate-cordova-preferences) for MABS 11.

There’s also an `android` block for permissions. Even though Capacitor supports permission changes via Cordova `plugin.xml`, you can still declare it in your ODC library extensibility, and it can make it clearer for other OutSystems developers what permissions your plugin (and therefore, their app) requires.

For other changes in `Info.plist` files, as well as changes in other Android files, you should use [build actions](../../building-apps/mobile/build-actions.md).

Here’s an example for a change in Android’s `strings.xml` via Cordova `plugin.xml`:

```xml
<config-file target="./res/values/strings.xml" parent="/resources">
    <string name="custom">Custom String</string>
</config-file>
```

Here’s how you can convert it to a build actions .json file:

```json

platforms:
  android:
    xml:
      - resFile: values/strings.xml
        target: resources
        merge: |
          <string name="custom">Custom String</string>

```

### Cordova-specific references

In a MABS 12 build that uses Capacitor, the Cordova framework won’t be available, and any usages of Cordova-specific APIs by your plugin may need to be refactored so that your plugin works well in Capacitor.

You should analyse JavaScript blocks in your OutSystems plugin, and, if possible, the JavaScript code of the Cordova plugin for Cordova framework API accesses.
Here are some common examples:

| Context | Cordova-specific code | Migration to Capacitor |
| :---- | :---- | :---- |
| Checking if Cordova exists.  | _typeof(cordova) \!== “undefined”_ | _typeof(Capacitor) \!== “undefined”_ You should have both checks for the plugin to be compatible with Cordova and Capacitor. |
| Checking if Cordova plugin is defined. | _typeof(\<cordova\_plugin\_clobber) \!== “undefined”_ | No changes needed. |
| Get the platform. To run code depending on which platform the app is running on. | _let platform \= cordova.platformId_ | _let platform \= Capacitor.getPlatform(); if (\!platform) {     platform \= cordova.platformId; }_ |

For some of the checks in the table above, you can use the official [Common Plugin in ODC](common-plugin/intro.md) (version 1.1.0 is compatible with both Cordova and Capacitor):

* `GetNativeMobileFramework` - Returns `Capacitor`, `Cordova`, or `None`
  
* `GetOperatingSystem` - Returns `Android`, `iOS`, or `Other`

## Two plugins: Cordova and Capacitor

To fully make your OutSystems plugin dual-stack, and to be able to better leverage Capacitor, the best option is to have a Capacitor plugin that is based off of the existing Cordova Plugin.

### Building a Capacitor plugin

For detailed information about building a Capacitor plugin, refer to [How to build a Capacitor plugin](https://docs.google.com/document/d/1OtPcZy19-XqsTfNuCKtpg-G4I_XEmp-2uhHhcbpE7Cg/edit?usp=sharing).

Here's some important points to remember on building a Capacitor plugin, based on an existing Cordova plugin:

* Like Cordova plugins, you can define a JavaScript API that the OutSystems plugin will consume. Under the hood, Cordova / Capacitor will call the appropriate native implementation.
  
* Most of the native code (Java and/or Kotlin for Android, Objective-C and/or Swift for iOS) from the Cordova Plugin can be reused for Capacitor.To promote reusability, you can create a native library for each platform.
  
* OutSystems recommends to publish the Capacitor Plugin to the [npm registry](https://www.npmjs.com/). Alternatively, if you have the plugin hosted in a GitHub repository, you may use that instead.

### Use Capacitor plugin in OutSystems

You will need to make changes in your existing OutSystems Plugin to decide whether to use Capacitor or Cordova.

Let’s use an example to illustrate the changes you would do: You have a Cordova plugin to scan QR Codes **cordova.plugin.qrcode**. You created a new Capacitor plugin, published in npm with id `@my-org/qr-code-capacitor` named `QrCode`.

You should update your plugin extensibility configurations as follows:

```json
{
    "buildConfigurations": {
        "cordova": {
            "source": {
                "npm": "@my-org/cordova.plugin.qrcode@1.2.0"
            }
        },
        "capacitor": {
            "source": {
                "npm": "@my-org/qr-code-capacitor@1.0.0"
            }
        },
    },
    "plugin": {
        "identifier": "@my-org/cordova.plugin.qrcode@1.2.0"
    }
}
```

Where the `buildConfigurations` block is used for MABS 12, and `plugin` for MABS 11 and below. Note how the Cordova plugin is declared side by side with the Capacitor inside `buildConfigurations`. This is because app users may configure MABS 12 to use either Cordova or Capacitor, so both need to be declared.

If you instead have your Capacitor (or Cordova) plugin in a GitHub repository, you should create a git tag and change the extensibility:

```
               "npm":"https://github.com/<org-name>/<capacitor-plugin-repo-name>#1.0.0"
```

For the client actions of your ODC Library, you will need to update your JavaScript blocks that reference the Cordova plugin.

If you’re on a Capacitor app, use the Capacitor plugin, otherwise, you should use the Cordova plugin. If both Cordova and Capacitor plugins have a `scanQRCode` method, you should have a code block like below:

```javascript
if (typeof(Capacitor) !== 'undefined') {
    // Capacitor app - use Capacitor Plugin
    Capacitor.Plugins.QrCode.scanQRCcode();
} else {
    // otherwise - use Cordova Plugin
    cordova.plugins.qrcode.scanQRCcode();
}
```

Alternatively, you can accomplish the same logic using the [Common Plugin’s](common-plugin/intro.md) `GetNativeMobileFramework` client action, having a JavaScript block for the Cordova call and one for Capacitor.

### Additional changes

Keep in mind however that there are certain functionalities in Cordova Plugins that aren’t supported in Capacitor Plugins directly such as plugin hooks and some changes  via `plugin.xml`.

For more information on Cordova features and how to map them in MABS 12 Capacitor builds, refer to [Changes required for Capacitor compatibility](#changes-required-for-capacitor-compatibility).
