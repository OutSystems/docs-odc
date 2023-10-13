---
summary: Use the Firebase-based plugins Analytics, Crashlytics, and Performance to implement common development patterns in your mobile apps.
tags: article-page; runtime-mobile; support-application_development; support-Mobile_Apps; support-Mobile_Apps-featured
locale: en-us
guid: 050c7d77-0418-4f38-9bb8-7b0275931b80
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4345%3A125&mode=design&t=OmSDtxS14Ggp4J6f-1
platform-version: odc
---

# Firebase plugins

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Firebase is a Google mobile development platform that speeds up the mobile app creation and design processes. You can use the Firebase services in the Mobile app through the following OutSystems Firebase-based plugins. On the [Forge](https://www.outsystems.com/forge/) portal, search for the following Firebase-based plugins compatible with ODC:

* Analytics Plugin (Firebase)
* Crash Reporting Plugin (Firebase)
* Dynamic Links Plugin (Firebase)
* Performance Monitoring Plugin (Firebase)
* Cloud Messaging Plugin (Firebase)


## Prerequisites

To use the Firebase plugins, you must complete the following prerequisites:

* Set up a Firebase project in the [Google Firebase console](https://console.firebase.google.com/).

* [Add an Android and an iOS app in Firebase](https://support.google.com/firebase/answer/9326094?hl=en) and download the configuration files:

    * **GoogleService-Info.plist** for iOS
    * **google-services.json** for Android

## Demo app

Install the **Firebase Mobile Sample App** from [Forge](https://www.outsystems.com/forge/) portal. Then open the app in the ODC Studio. The demo app contains logic for common use cases, which you can examine and recreate in your apps. If you want to build the app and run it, check the prerequisites on the Forge page.

## Adding and using a Firebase plugin

To add a Firebase plugin to your mobile app, complete the following steps:

1. Install the **Firebase** plugin and reference it in your mobile app. For detailed instruction, see [Installing a plugin and adding a public element to your app](../intro.md#installing-a-plugin-and-adding-a-public-element-to-your-app).

1. Add the [Google services configuration file](#adding-google-services-configuration-file) to your mobile app.

    <div class="info" markdown="1">

    You only need to add Google services configuration file for the first Firebase plugin in your mobile app. The next Firebase plugin you add uses the same configuration files.

    </div>

1. Open ODC Studio.

2. Navigate to **Logic** > **Client Actions**, then select your Firebase plugin and use the actions in your logic.

    ![Screenshot of creating and using the firebase actions in the logic tab of ODC Studio](images/create-and-use-firebase-plugin-in-logic-tab-odcs.png)

<div class="info" markdown="1">

To learn how to use the Firebase Cloud Messaging plugin, see [Firebase Cloud Messaging Plugin](../firebase-plugin/firebase-cloud-messaging-plugin.md) compatible with ODC.

</div>

## Adding Google services configuration file

You must provide the plugin configuration file as settings in the ODC Portal for an app with a Firebase Plugin. To add the Firebase configuration to your app, complete the following steps:

1. Open the ODC Portal.

1. From the left Navigation menu, select **Apps** and from the details page, select your app. Then select **Settings**.

    Complete the two Firebase settings **GoogleServicesAndroid** and **GoogleServicesIos**.

    ![Screenshot of adding Google services configuration files in the Firebase settings](images/add-google-services-config-files-in-firebase-settings-pl.png)

1. Select the context menu associated with the GoogleServicesAndroid setting, then select **Edit** and upload the **google-services.json** file.

1. In the Firebase settings, select the context menu associated with the GoogleServicesIos setting, then select **Edit** and upload the **GoogleService-Info.plist** file.

<div class="info" markdown="1">

Add the Google services configuration files only for the first Firebase plugin in your app. The next Firebase plugin you add uses the same configuration files.

</div>

### Additional setup for the Dynamic Links plugin

The Firebase Dynamic Links Plugin requires the following additional setup steps to work correctly:

* Include a global preference in the Extensibility Configurations of the application using the plugin. Ensure that the value for this preference matches the URL prefix you set in the Dynamic Links page in the Firebase console. For example:

```JSON
{
     "preferences": {
         "global": [
            {
                "name": "FIREBASE_DOMAIN_URL_PREFIX",
                "value": "outsystemsfirebase.page.link"
            },
        ]
    }
}
```

* For iOS, use a provisioning profile from Apple that contains the Associated Domains capability. For more information, see [Configuring an Associated Domain](https://developer.apple.com/documentation/xcode/configuring-an-associated-domain) by Apple. Ensure that the app is compliant with Apple’s Data Use and Sharing guidelines.

Starting with iOS 14.5, apps on the App Store must request the user’s permission to collect tracking data through the AppTrackingTransparency framework. For more information, see [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency).

To trigger the native AppTrackingTransparency framework, use the **RequestTrackingAuthorization** client action from the Firebase Analytics Plugin. Apple recommends triggering this prompt as soon as the app loads.
If you want to present an alert before the iOS tracking permission dialog, enable the parameter **ShowInformation** on the action. To provide more context to app users in the dialog, set a **Title** and **Message**.

![RequestTrackingAuthorization client action parameters on Service Studio](images/firebase-request-tracking-authorization-flow-odcs.png)

By default, the **NSUserTrackingUsageDescription** field is set to `AppName needs your attention.`. As explained by Apple [here](https://developer.apple.com/documentation/apptrackingtransparency), this property must contain "a message that informs the user why an app is requesting permission to use data for tracking the user or the device.". You can set your custom description by including an iOS-specific preference (`USER_TRACKING_DESCRIPTION_IOS`) in the Extensibility Configurations of the application, as follows:

```JSON
{
    "preferences": {
        "ios": [{
            "name": "USER_TRACKING_DESCRIPTION_IOS",
            "value": "This is an example of a description."
        }]
    }
}
```

You can use the **RequestTrackingAuthorization** action multiple times in the same app because iOS remembers a user's choice and only prompts users again after they uninstall and then reinstall the app on the device.

By default, an app using the Firebase Analytics plugin is able to trigger the native AppTrackingTransparency framework. It also contains the **NSUserTrackingUsageDescription** field in the app's **\*-Info.plist** file. If you don't want to trigger the framework and don't want to include the description field in the **.plist** file, you can disable this through the Extensibility Configurations as follows:

```JSON
{
    "preferences": {
        "ios": [{
            "name": "EnableAppTrackingTransparencyPrompt",
            "value": "false"
        }]
    }
}
```

<div class="info" markdown="1">

If your app collects user data for advertising purposes, also known as Attribution, within Firebase Analytics context, it must prompt the AppTrackingTransparency framework.

</div>
