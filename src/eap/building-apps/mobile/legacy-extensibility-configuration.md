---
guid: b48cee0f-0009-4515-9e87-673ba40db110
locale: en-us
summary: This artucles describes the legacy extensibility configuration JSON schema that can be used with Apache Cordova framework.
figma:
coverage-type:
  - apply
  - remember
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: json schema, apache cordova, mobile customization, legacy configuration, extensibility settings
outsystems-tools:
  - odc studio
helpids:
---
# Cordova-based extensibility configuration JSON schema

<div class="info" markdown="1">

Applies only to Cordova apps.

</div>

This article describes the Cordova-based extensibility configuration JSON schema that is used to customize mobile apps using only Apache Cordova framework.

To configure both Capacitor and Cordova apps. You must use the [Universal extensibility configurations JSON schema](extensibility-configurations-json-schema.md) 

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

The following section provides more details about the options you can use in the `preferences` top-level property. For a comprehensive list of the available settings, refer to [preferences in Config.xml](https://cordova.apache.org/docs/en/dev/config_ref/index.html#preference) by Apache Cordova.

| Property                          | Platform | Default | Description |
| --------------------------------- | -------- | ------- | ----------- |
| (iOS_FEATURE)UsageDescription    | iOS        | NA       | Adds preferences that match the pattern of UsageDescription to the Info.plist file. For the full list, refer to [Cocoa Keys](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW1) and filter by UsageDescription. For an example, refer to information about [iOS usage descriptions](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions/MABS_7_Release_notes#ios-usage-descriptions) in the release notes. |
| AddUploadWidgetPermissions      | Android, iOS        | false       | Set as false to skip adding permissions required by the upload widget to AndroidManifest.xml and/or Info.plist. For an example, refer to information about [Upload widget permissions](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions/MABS_7_Release_notes#upload-widget-permissions) in the release notes. |
| EnableRefererHeaderCustomScheme | iOS        | false       | Set to true to inject the `Referer: URL` in the requests of the native app, where `URL` is the app domain.         |
| InitLoggerSyncDelay             | Android        | 0       | Seconds to delay the logger synchronization after the initialization.         |
| RemoveUserCertificates          | Android        |true | Set to true to remove user certificates from the trust anchors in network_security_config.xml.         |
| FilterTouchesWhenObscured | Android |true| Defines the value of the filterTouchesWhenObscured property of WebView on Android. Set to true to prevent the app from handling touches while obscured by other apps. For detailed information about filterTouchesWhenObscured, refer to [Android documentation](https://developer.android.com/reference/android/view/View#security).|
| DisableInspectorNotification | iOS | false | Set to true to remove the notification from the [Network inspector](https://www.outsystems.com/tk/redirect?g=2bea2ff9-7655-4952-a00c-2a3f1e3316e9) plugin in iOS debug builds. |
| DeepLinksHandlerType | Android, iOS | default | Defines how the mobile app [handles deeplinks](extensibility-configurations.md#customize-deeplink-behavior). This can have 4 possible values: `default`, `event`, `function` or `legacy`. |

## Resources

The following section provides  details on the `resources` top-level property. The feature translates into the `resource-file` feature on [Cordova](https://cordova.apache.org/docs/en/12.x/config_ref/#resource-file). These resources are included in the folder `www`, available for use within the project compilation. Use **OutSystems Resources** with **Deploy Action** set to **Deploy to Target Directory** in the app project.  

The `src` property specifies the origin of the resource. It can be one of the following:

* **Extensibility setting reference**: A reference to a binary setting, typically used for files like configuration binaries.
Example: `$extensibilitySettings.GoogleServicesJsonBinary`
**
* Extensibility resource reference**: A reference to a resource deployed to the target directory.
Example: `$resources.MyAppResource`

*** OutSystems app image**: A reference to an image stored in the ODC app.
Example: `$images.MyAppLogo`

* **File path**: A string representing a file path relative to the root folder of the generated project.
Example: **path/to/resource.ext**

The `target` property specifies the destination path within the mobile project. It determines where the resource will be copied.

* For Android, the path is relative to **{project_root}/platforms/android**.

* For iOS, the path is relative to **{project_root}/platforms/ios/{app_name}/Resources**

```json
{
  "buildConfigurations": {
    "resources": {
      "ios": [
        {
          "source": "$extensibilitySettings.GoogleServiceInfoPlist",
          "target": "GoogleService-Info.plist"
        },
        {
          "source": "$images.MyAppLogo",
          "target": "AppIcon.png"
        }
      ],
      "android": [
        {
          "source": "$extensibilitySettings.GoogleServicesJsonBinary",
          "target": "google-services.json"
        },
        {
          "source": "path/to/local/resource.ext",
          "target": "resource.ext"
        }
      ]
    }
  }
} 
```

As an example of the usage of this feature on an OutSystems-supported plugin, see the [Firebase supported plugins documentation](../../integration-with-systems/mobile-plugins/firebase-plugin/intro.md#adding-google-services-configuration-file).

## Related resources

* [Universal extensibility configuration JSON schema](extensibility-configurations.md)

* [Troubleshooting errors](extensibility-configurations/troubleshooting-errors.md)

<div class="info" markdown="1">

Extensibility configurations may be processed by OutSystems for the purposes of service improvement and troubleshooting. These configurations should not include or permit access by OutSystems to personal data or confidential or sensitive information. Customers are responsible for ensuring that no personal data or confidential or sensitive information is accessible to OutSystems through any Extensibility configurations. Where such information is included in those configurations, customers should use secret settings to prevent personal data or confidential or sensitive information from being collected by OutSystems.

</div>
