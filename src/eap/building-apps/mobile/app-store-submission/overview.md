---
summary: ODC app store upload uses one-time store credentials to send mobile packages from the Portal to App Store Connect and Google Play.
tags:
  - Android
  - Deploy
  - iOS
  - Mobile app
  - Native App
locale: en-us
guid: e21e90f4-4cae-4b96-b84a-6a0943da68ce
app_type: mobile apps
platform-version: odc
figma:
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - odc portal
coverage-type:
  - understand
  - apply
content-type:
  - conceptual
topic:
  - app-distribution
isautopublish: true
---

# Uploading apps to an app store

After you [create a mobile package](../creating-mobile-package.md) in ODC, you can upload it to App Store Connect or Google Play Console directly from the ODC Portal. You configure the store connection details once, and ODC uploads the compiled mobile package on your behalf. This removes a manual download, context switch, and upload cycle, along with the risk of sending the wrong build to a store.

Before you upload a package for an app, you complete the app setup each store requires, such as creating the app record and generating the credentials ODC uses to authenticate. For the full prerequisites checklist, refer to [Upload a mobile package to a store](submit-mobile-package-to-store.md#prerequisites).

Once that setup is done, ODC uploads the compiled .ipa or .aab file to App Store Connect or Google Play Console respectively. You can track the upload and validation progress from the ODC Portal. If the upload fails, ODC reports the failure in detail so you can retry the upload without leaving the platform. Everything else, including app metadata, screenshots, listing details, review submission, and promoting a build to a release or a production track, stays in the store console. You complete those steps in App Store Connect or Google Play Console.

## Configuring store credentials {#credentials}

You generate the credentials in the store itself, using an account with admin access to App Store Connect or Google Cloud. A platform administrator then configures the store connection with those credentials in the ODC Portal. Apple requires an App Store Connect API key, and Google requires a Google Cloud service account key. For the steps to generate and configure each, refer to [Configure App Store Connect credentials](submit-package-to-app-store-connect.md#configure-credentials) or [Configure Google Play credentials](submit-package-to-google-play.md#configure-credentials).

These credentials are then added once to an app in the ODC Portal. ODC reuses them for every subsequent upload for that app.

## Where your build lands {#where-your-build-lands}

When you successfully upload a package from the ODC Portal, ODC transfers the compiled build to App Store Connect or Google Play Console. From there, you can submit the build for review, provide it to testing groups, or publish it to the store, depending on whether you use TestFlight or the Google Play track.

For the prerequisites checklist required by Apple and Google, and the end-to-end steps for sending a package to a store, refer to the [process for uploading a mobile package to a store](submit-mobile-package-to-store.md).

## Related resources { #related-resources }

For more information about uploading mobile packages to app stores, refer to the following resources:

* [Create mobile app package](../creating-mobile-package.md)

* [Native mobile build API](../../../reference/apis/native-mobile-builds-api-v1.md)
