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

# Adapt Cordova plugin for compatibility with Capacitor

Existing plugins rely on [Cordova](https://cordova.apache.org/) to access native functionalities. With [MABS 12](../../building-apps/mobile/mabs-overview.md), you can build both Capacitor and Cordova apps. This means you can update your MABS version and continue using the Cordova framework and your existing plugins without any changes. However, OutSystems recommends switching to the Capacitor cross-platform native runtime to leverage its modern capabilities.

If you are building a Capacitor app and you already have an ODC library that references the Cordova plugin, you can make that library work with Capacitor apps. In some cases, the Cordova plugin itself doesn’t require any code changes. You only need to update the extensibility configurations in your ODC library so that it correctly references the plugin for Capacitor compatibility. However, if your plugin relies on Cordova-specific functionalities that are not supported by Capacitor, you must adapt the plugin. By adapting the plugin, you can integrate and use your existing plugin within your Capacitor-based app.

If adapting requires significant changes to core functionality, consider building a [dual-stack plugin](capacitor-plugins/dual-stack-plugin.md) for better performance and long-term maintenance.

This article explains how you can adapt your existing Cordova plugin for use with [Capacitor](https://capacitorjs.com/) apps.

## Approaches for Cordova plugin compatibility

While Capacitor provides [built-in support for Cordova Plugins](https://capacitorjs.com/docs/plugins/cordova), certain Cordova-specific features don't apply directly to the Capacitor environment. To bridge this gap, MABS 12 introduces capabilities such as including [universal extensibility configurations](../../building-apps/mobile/extensibility-configurations.md) and [build actions](../../building-apps/mobile/build-actions.md). These capabilities enable you to create plugins that work across both Cordova and Capacitor.

Here are the two main approaches to ensure Cordova plugins work with Capacitor:

Approach 1: Modify the [extensibility of OutSystems](#changes-in-extensibility-configurations-for-all-plugins-changes-in-extensibility) plugin and if needed adapt the Cordova plugin for Capacitor compatibility.
  
Approach 2: Create a Capacitor plugin with the same functionality as the existing Cordova Plugin. Then, update the OutSystems plugin to use either of the implementations based on the available native mobile framework. For detailed information, refer to [Implement a dual-stack plugin](capacitor-plugins/dual-stack-plugin.md)

Approach 1 is quicker and requires less effort, while approach 2 allows you to leverage Capacitor-specific functionalities directly in your plugin. You can also adopt a phased migration, starting with Approach 1 and later progressing to Approach 2.

## Changes in extensibility configurations for all plugins {#changes-in-extensibility}

With MABS 12, extensibility configurations follow [universal extensibility schema](../../building-apps/mobile/extensibility-configurations.md). You must update your OutSystems plugin, even if you only use Cordova.

For example, if your mobile plugin is offered as a library on ODC, and your extensibility configurations are:

```json
{
    "plugin": {
        "url":"{url_to_cordova_plugin}",
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
                "npm": "{url_to_cordova_plugin}"
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

* The `plugin` block is under `buildConfigurations` > `cordova`.
* Cordova preferences, previously under `plugin` > `variables` are now in `buildConfigurations` > `cordova` >  `preferences`.

The Cordova-based extensibility configurations remain to ensure the  plugin works in MABS 11.

If you choose to support Capacitor, additional changes may be required in your library’s extensibility. For detailed information refer to [Library (plugin) extensibility configuration JSON schema](../../building-apps/mobile/extensibility-configurations/extensibility-lib-reference.md).

## Use Cordova plugins in Capacitor

Capacitor supports Cordova Plugins. Depending on your plugin, you may not require changes, excluding changes in extensibility configurations.

This section first describes scenarios where no changes are needed, followed by required changes to ensure full compatibility with MABS 12 and Capacitor.

### Evaluate plugin.xml compatibility with Capacitor

In most cases, the source code of the Cordova plugin—whether JavaScript, TypeScript, Java, Kotlin, Swift, or Objective-C—doesn't require changes to be compatible with Capacitor. One exception is if it uses [Cordova-specific functionalities](#adapt-cordova-specific-references-adapt-cordova-specific-references).

The main file you need to analyze to determine if a Cordova Plugin is fully compatible with Capacitor is the `plugin.xml` file.

Capacitor in OutSystems processes some elements in a Cordova `plugin.xml` file:

* The `js-module` block, where you define your clobbers to access Cordova plugin methods in OutSystems JavaScript blocks.
  
* Tags for defining native source code and native dependencies—`source-file`, `header-file`, `resource-file`, `lib-file` `framework`, `podspec`.
  
* The `features` inside the `config-file` block.
  
* Dependencies on other Cordova plugins using the `dependency` tag. However, you must ensure those dependencies are compatible with Capacitor as well.
  
* Limited support for `config-file` and `edit-config`—changes for the Android platform, and exclusively for `AndroidManifest.xml`.

For example, if you have an OutSystems supported Cordova plugin for accessing the phone’s contacts, and the Cordova `plugin.xml` file looks like this:

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

Then the plugin should be compatible with Capacitor out of the box, apart from the [extensibility configuration changes](#changes-in-extensibility-configurations-for-all-plugins-changes-in-extensibility). Regardless, you should test your plugin on an app built with MABS 12 and Capacitor to confirm everything works as expected.

### Changes required for Capacitor compatibility {#changes-required-for-capacitor-compatbility}

The following Cordova functionalities in `plugin.xml` are not supported by Capacitor directly:

* `preference` -  setting plugin variables, be it globally or per platform.
* `hooks`  running scripts at different points of the Cordova lifecycle.
* Most changes that use `config-file` or `edit-config`. For instance, changes to `Info.plist` on iOS in `plugin.xml` are not directly supported by Capacitor.

If your OutSystems plugin uses any of the above mentioned functionalities from Cordova, you must do the following to ensure compatibility:

* [Migrate Cordova preferences](#migrate-cordova-preferences-migrate-cordova-preferences)

* [Use build actions for Cordova hooks](#use-build-actions-for-cordova-hooks-use-build-actions-for-cordova-hooks)

* [Migrate config file changes](#migrate-config-file-changes-migrate-config-file-changes)

* [Adapt Cordova-specific references](#adapt-cordova-specific-references-adapt-cordova-specific-references)

#### Migrate Cordova preferences {#migrate-cordova-preferences}

Cordova preferences allow for the creation of variables that can be customized by plugin users. These preferences can then be used elsewhere in `plugin.xml`.
Here is an example of an Android-specific preference:

```xml
<preference name="MY_CUSTOM_STRING" default="default-value" />
<config-file target="./res/values/strings.xml" parent="/resources">
    <string name="custom">$MY_CUSTOM_STRING</string>
</config-file>
```

You can set the preference values in both ODC library and app extensibility configurations (compatible with MABS 11).

In Capacitor builds, the preference value cannot be changed - the default value is always used. To allow for easier customization of these variables, OutSystems recommends using [extensibility settings](../../building-apps/mobile/configuring-mobile-apps.md#configure-extensibility-settings-configure-extensibility-settings).

#### Use build actions for Cordova hooks {#use-build-actions-for-cordova-hooks}

Cordova hooks provide a mechanism for plugin developers to perform advanced configuration tasks during the build process that cannot be achieved through standard `plugin.xml` declarations alone.

With MABS 12, you can use [build actions](../../building-apps/mobile/build-actions.md) to perform native project modifications such as modifying **Android Manifest file**, **Info.plist** or **build.gradle** files in a structured and repeatable way with minimal code.

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

In the library’s extensibility, add the reference to the .json file, and pass the `APP_NAME` parameter.  You can specify an [extensibility setting](../../building-apps/mobile/configuring-mobile-apps.md#configure-extensibility-settings) so that users can customize the value on their app via ODC Portal:

```json
{
   "buildConfigurations": {
        "buildAction": {
            "config": $resources.setAppName.json,
            "parameters": {
                "APP_NAME": $extensibilitySettings.AppName
            }
        }
    },
}
```

OutSystems recommends always using build actions. However, there may be specific uses that cannot be accomplished with build actions. In such scenarios, you can use [Capacitor Hooks](https://capacitorjs.com/docs/cli/hooks), which allow you to run scripts in different phases of the Capacitor build process.

#### Migrate `config-file` changes {#migrate-config-file-changes}

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
            "value": $extensibilitySettings.CameraUsageDescription
        }]
    }
    "pluginConfigurations": {
        "permissions": {
            "android": [
                "android.permission.CAMERA"
            ]
            "ios": {
                "NSCameraUsageDescription": {
                    "description": $extensibilitySettings.CameraUsageDescription
                }
            }
        }
    }
}
```

Here the extensibility setting name is `CameraUsageDescription`. In the example, `plugin variables` block is added in case you want to use the setting to set a [Cordova preference](#migrate-cordova-preferences) for MABS 11.

The `android` block explicitly declares the camera permission your plugin requires. While Capacitor can automatically handle permissions through Cordova's `plugin.xml`, declaring them in your ODC library extensibility provides better transparency. This makes it immediately clear to other developers what permissions your plugin needs and how it will affect their app's permission requirements.

For other changes in `Info.plist` files, as well as changes in other Android files, you must use [build actions](../../building-apps/mobile/build-actions.md).

Here’s an example for a change in Android’s `strings.xml` via Cordova `plugin.xml`:

```xml
<config-file target="./res/values/strings.xml" parent="/resources">
    <string name="custom">Custom String</string>
</config-file>
```

Here's how you can convert it to a build actions .json file:

```json
{
    "platforms": {
        "android": {
            "xml": [
                {
                    "resFile": "values/strings.xml",
                    "target": "resources",
                    "merge": "&lt;string name='custom'&gt;Custom String&lt;/string&gt;"
                }
            ]
        }
    }
}
```

#### Adapt Cordova-specific references {#adapt-cordova-specific-references}

When you build your Capacitor mobile package with MABS 12, refactor any Cordova-specific APIs your plugin uses to ensure it works in Capacitor.

You must analyse the JavaScript blocks in your OutSystems plugin, and, if possible, the JavaScript code of the Cordova plugin for Cordova framework API access.

Here are some common examples:

| Context | Cordova-specific code | Migration to Capacitor |
| :---- | :---- | :---- |
| Checking if Cordova exists. | _typeof(cordova) \!== “undefined”_ | _typeof(Capacitor) \!== “undefined”_ You should have both checks for the plugin to be compatible with Cordova and Capacitor. |
| Checking if Cordova plugin is defined. | _typeof(\<cordova\_plugin\_clobber) \!== “undefined”_ | No changes needed. |
| Get the platform. To run code depending on which platform the app is running on. | _let platform \= cordova.platformId_ | _let platform \= Capacitor.getPlatform(); if (\!platform) {     platform \= cordova.platformId; }_ |

For some of the checks in the table above, you can use the official [Common Plugin in ODC](common-plugin/intro.md) (version 1.1.0 is compatible with both Cordova and Capacitor):

* `GetNativeMobileFramework` - Returns `Capacitor`, `Cordova`, or `None`
  
* `GetOperatingSystem` - Returns `Android`, `iOS`, or `Other`

## Related resources

Explore these resources to learn more about plugin integration

* [Implement dual-stack plugin](capacitor-plugins/dual-stack-plugin.md)

* [Build a Capacitor plugin from scratch](capacitor-plugins/build-capacitor-plugin.md)

Explore these resources to learn more about the capabilities introduced from MABS 12:

* [Universal extensibility configuration JSON schema](../../building-apps/mobile/extensibility-configurations.md)

* [Build actions](../../building-apps/mobile/build-actions.md)

* [Extensibility settings](../../building-apps/mobile/configuring-mobile-apps.md#)
