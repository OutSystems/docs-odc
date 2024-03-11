---
summary: The article details the JSON schema for Extensibility Configurations in mobile apps, outlining how to specify plugins, preferences, icons, splash screens, and access settings
tags: 
locale: en-us
guid: ecb98e61-f07f-4204-a899-9fd1d5460fbf
app_type: mobile apps
platform-version: odc
figma:
---
# Extensibility configurations JSON schema

<div class="info" markdown="1">

Applies only to mobile apps.

</div>

The **Extensibility Configurations** field provides additional settings as a JSON string. You can change a number of settings in the user interface of the IDE, such as the name of the app. Some advanced settings are available in the **Extensibility Configurations** only (for example, adding custom mobile plugins). You can edit **Extensibility Configurations** in the properties of your home module.

## Property schema

The value of the **Extensibility Configurations** property of a mobile app module is a JSON object. What follows is the JSON schema outlining the most common options. There may be other options applicable in your use case, if the feature you're using provides them.

```javascript
{
    "plugin": {
        // Use only one the following ways to reference a plugin
        "url": "<The url to a public git repository containing your plugin>",
        // or
        "identifier": "<The identifier for your plugin>",
        // If the plugin requires additional settings
        "variables": [
            {
                "name": "<The attribute name for your plugin variable>",
                "value": "<The attribute value for your plugin variable>"
            },
            /* ...more variables, if needed... */
        ]
    },
    "preferences": {
        // Common preferences for iOS and Android, like status bar customization settings
        "global": [
            {
                "name": "<The preference name for your Android/iOS application>",
                "value": "<The preference value for your Android/iOS application>"
            },
            /* ...more global preferences... */
        ],
        // Just for Android
        "android": [
            {
                "name": "<The preference name for your Android application>",
                "value": "<The preference value for your Android application>"
            },
            /* ...more Android preferences... */
        ],
        // Just for iOS
        "ios": [
            {
                "name": "<The preference name for your iOS application>",
                "value": "<The preference value for your iOS application>"
            },
            /* ...more iOS preferences... */
        ]
    },
    "resources": {
        // Common resources for iOS and Android
         "global": {
            "<The key of the resource>": {
                "src": $settings.<any-binary-setting>,
                "target": "<The path to where the resource will be copied within the Android/iOS project>"
            },
            /* ...more global resources... */
        },
        // Just for Android
        "android": {
            "<The key of the resource>": {
                "src": $settings.<any-binary-setting>,
                "target": "<The path to where the resource will be copied within the Android project>"
            },
            /* ...more Android resources... */
        },
        // Just for iOS
        "ios": {
            "<The key of the resource>": {
                "src": $settings.<any-binary-setting>,
                "target": "<The path to where the resource will be copied within the iOS project>"
            },
            /* ...more iOS resources... */
        }
    },
    "icons": { ... },
    "splashscreens": { ... }
}
```

## Preferences

The following section provides more details about the options you can use in the `preferences` top-level property. For a comprehensive list of the available settings, see [preferences in Config.xml](https://cordova.apache.org/docs/en/dev/config_ref/index.html#preference) by Apache Cordova.

| Property                          | Platform | Default | Description |
| --------------------------------- | -------- | ------- | ----------- |
| (iOS_FEATURE)UsageDescription    | iOS        | NA       | Adds preferences that match the pattern of UsageDescription to the Info.plist file. For full list, see [Cocoa Keys](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW1) and filter by UsageDescription. For an example, see information about [iOS usage descriptions](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions/MABS_7_Release_notes#ios-usage-descriptions) in the release notes. |
| AddUploadWidgetPermissions      | Android, iOS        | true       | Set as false to skip adding permissions required by the upload widget to AndroidManifest.xml and/or Info.plist. For an example, see information about [Upload widget permissions](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions/MABS_7_Release_notes#upload-widget-permissions) in the release notes. |
| EnableRefererHeaderCustomScheme | iOS        | false       | Set to true to inject the `Referer: URL` in the requests of the native app, where `URL` is the app domain.         |
| InitLoggerSyncDelay             | Android        | 0       | Seconds to delay the logger synchronization after the initialization.         |
| RemoveUserCertificates          | Android        |true for MABS ≥ 9; <br/> false for MABS &lt; 9| Set to true to remove user certificates from the trust anchors in network_security_config.xml.         |
| FilterTouchesWhenObscured | Android |true for MABS ≥ 9<br/> false for MABS &lt; 9| Defines the value of the filterTouchesWhenObscured property of WebView on Android. Set to true to prevent the app from handling touches while obscured by other apps. Learn more about filterTouchesWhenObscured [here](https://developer.android.com/reference/android/view/View#security).|
| DisableInspectorNotification | iOS | false | Set to true to remove the notification from the [Network inspector](https://www.outsystems.com/tk/redirect?g=2bea2ff9-7655-4952-a00c-2a3f1e3316e9) plugin in iOS debug builds. |
| DeepLinksHandlerType | Android, iOS | default | Defines how the mobile app [handles deeplinks](customize-deeplink-behavior.md). This can have 4 possible values: `default`, `event`, `function` or `legacy`. |

## Resources

The following section provides more details on the `resources` top-level property. The feature translates into the `resource-file` feature on [Cordova](https://cordova.apache.org/docs/en/12.x/config_ref/#resource-file). These resources are included in the folder `www`, available for use within the project compilation. Use **OutSystems Resources** with **Deploy Action** set to **Deploy to Target Directory** in the application project.  

* The `src` property of a resource is relative to the location of `config.xml` (project root). Since the resources become available in the `www` folder, the value should start with it.
* If you add the resource `my-resource.ext` in Service Studio, the value should be `www/my-resource.ext`.
* The `target` property of a resource is relative to the Android/iOS project. If a resource with the same name already exists in the specified `target`, it is overridden.
* For Android, the path is relative to `<project_root>/platforms/android`.
* For iOS, the path is relative to `<project_root>/platforms/ios/<app_name>/Resources`

As an example of the usage of this feature on an OutSystems-supported plugin, see the [Firebase supported plugins documentation](plugins/firebase-plugin/intro.md#adding-google-services-configuration-file).

## Constraints

To ensure the platform can build your app successfully and that your app works correctly, keep in mind the following restraints for the **Extensibility Configurations** JSON.

### Generic

Generic constants, applicable to all parts of the **Extensibility Configurations** JSON.

* The JSON schema and key/value pairs must follow the structure described in this topic.

* The first-level key/value pairs are optional and their order is not relevant.

* Write the name of each name/value pair using lowercase letters because the JSON is case-sensitive.
