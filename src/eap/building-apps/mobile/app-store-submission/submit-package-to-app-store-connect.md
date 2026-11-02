---
summary: Upload an iOS mobile package built in ODC to App Store Connect directly from the ODC Portal.
tags:
  - Deploy
  - iOS
  - Mobile app
  - Native App
locale: en-us
guid: 6f1c5a65-af06-40ce-9490-556cac291110
app_type: mobile apps
platform-version: odc
figma:
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - odc portal
coverage-type:
  - apply
content-type:
  - procedure
topic:
  - app-distribution
isautopublish: true
helpids: 30782
---

# Upload a mobile package to iOS App Store Connect

This article explains how to upload an iOS mobile package built in ODC to App Store Connect from the ODC Portal.

## Prerequisites {#prerequisites}

Before you upload a package to App Store Connect, ensure you have:

* A mobile package built with the **App Store** build type, visible on the app's **Mobile distribution** tab. For more information, refer to [Create mobile app package](../creating-mobile-package.md).
* An App Store Connect API key, its **Key ID**, and its **Issuer ID**. Generating the key requires an admin account in App Store Connect, and the key needs an **Admin**, **App Manager**, or **Developer** role to upload builds. For more information about generating these values, refer to Apple's [Creating API keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api).
* The remaining Apple account and App Store Connect setup listed in the [Apple App Store Connect prerequisites](submit-mobile-package-to-store.md#apple-prerequisites) checklist.
* A platform administrator with the [required ODC permissions](submit-mobile-package-to-store.md#odc-permissions) who configures the App Store Connect credentials for the app. Until a platform administrator completes this configuration, the **Upload to App Store Connect** button remains unavailable.

## Configure App Store Connect credentials {#configure-credentials}

A platform administrator configures the App Store Connect credentials for an app the first time anyone uploads a package for that app. ODC reuses these credentials for every subsequent upload.

To configure the credentials, follow these steps:

1. Open the app in the ODC Portal and select the **Mobile distribution** tab.

1. Under **Packages**, select **iOS**.

1. Click **Upload to App Store Connect**.

1. In the **Upload package to App Store Connect** window, provide the following:

    * **API key**: browse to or drag and drop the App Store Connect API key file, a `.p8` file.
    * **Key ID**: the key ID Apple generated for this API key.
    * **Issuer ID**: the issuer ID for your App Store Connect account.

1. Click **Upload to App Store Connect** in the window to start the upload.

ODC doesn't save the API key until you start this upload. If you leave the window before clicking **Upload to App Store Connect**, provide the key again.

## Upload a package to App Store Connect {#upload-package}

After a platform administrator configures the App Store Connect credentials for the app, you upload packages for that app without providing credentials again.

To upload a package, follow these steps:

1. Open your app in the ODC Portal and select the **Mobile distribution** tab.

1. Under **Packages**, select **iOS**.

1. Click **Upload to App Store Connect** to start the upload.

ODC validates and then uploads the package, showing the current stage on the package details page. When the upload finishes, App Store Connect makes the build available in TestFlight.

If the upload fails, ODC reports the failure on the package details page so you can correct the issue and retry, without repeating the earlier steps.

## Related resources {#related-resources}

For more information about uploading mobile packages to app stores, refer to the following resources:

* [Uploading apps to an app store](overview.md)
* [Upload a mobile package to a store](submit-mobile-package-to-store.md)
* [Create mobile app package](../creating-mobile-package.md)
* [Native mobile build API](../../../reference/apis/native-mobile-builds-api-v1.md)

For more information from Apple, refer to the following resources:

* Apple's [Creating API keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api)
* Apple's [App Store Connect help](https://developer.apple.com/help/app-store-connect/)
