---
summary: Upload an Android mobile package built in ODC to Google Play directly from the ODC Portal.
tags:
  - Android
  - Deploy
  - Mobile app
  - Native App
locale: en-us
guid: dc04751f-7a6f-47f7-846c-9f68aa3dc2a5
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
helpids: 30781
---

# Upload a mobile package to Google Play

This article explains how to use the ODC Portal to upload an Android mobile package to the Google Play Console.

## Prerequisites {#prerequisites}

Before you upload a package to the Google Play Console, ensure you have:

* A mobile package built with the **Google Play (App Bundle)** build type. For more information, refer to [Create mobile app package](../creating-mobile-package.md).

* A Google Cloud service account with access to the Google Play Developer API, and its JSON private key file. For more information about creating this service account, refer to Google's [Service accounts](https://developers.google.com/android/management/service-account). For more information about creating and downloading the JSON key for this service account, refer to Google's [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete).

* Invite the service account as a user to your Play Console account, then grant it the **Release apps to testing tracks**, **View app information and download bulk reports (read-only)**, and **View app quality information (read-only)** permissions, either at the account level or for the specific app. These permissions let the service account publish builds on your behalf. For more information, refer to Google's [Add developer account users and manage permissions](https://support.google.com/googleplay/android-developer/answer/9844686).

* The remaining Google Play Developer account and Play Console setup listed in the [Google Play prerequisites](submit-mobile-package-to-store.md#google-play-prerequisites) checklist.

* A platform administrator who configures the Google Play credentials for the app. Until a platform administrator completes the configuration you cannot upload the package to Google Play.

## Configure Google Play credentials {#configure-credentials}

A platform administrator configures the Google Play credentials for an app the first time anyone uploads a package for that app. ODC reuses these credentials for every subsequent upload.

To configure the credentials, follow these steps:

1. Open the app in the ODC Portal and select the **Mobile distribution** tab.

1. Under **Packages**, select **Android**.

1. Click **Upload to Google Play**.

1. In the **Upload package to Google Play** window, provide the **Service account key**.

1. Click **Upload to Google Play** to start the upload.

ODC doesn't save the service account key until you start this upload. If you leave the window before clicking **Upload to Google Play**, provide the key again.

## Upload a package to Google Play {#upload-package}

After a platform administrator configures the Google Play credentials for the app, you upload packages for that app without providing credentials again.

To upload a package, follow these steps:

1. Open your app in the ODC Portal and select the **Mobile distribution** tab.

1. Under **Packages**, select **Android**.

1. Click **Upload to Google Play** to start the upload.

ODC validates and then uploads the package, showing the current stage on the package details page. When the upload finishes, Google Play makes the build available in the **Internal testing** track.

If the upload fails, ODC reports the failure on the package details page. You can correct the issue and retry the upload without repeating the previous steps.

## Related resources {#related-resources}

For more information about uploading mobile packages to app stores, refer to the following resources:

* [Uploading apps to an app store](overview.md)
* [Upload a mobile package to a store](submit-mobile-package-to-store.md)
* [Create mobile app package](../creating-mobile-package.md)
* [Native mobile build API](../../../reference/apis/native-mobile-builds-api-v1.md)

For more information from Google, refer to the following resources:

* Google's [Service accounts](https://developers.google.com/android/management/service-account)
* Google's [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete)
* Google's [Play Console help](https://support.google.com/googleplay/android-developer)
