---
guid: 4dae4042-c9fe-4c2f-af4f-9939ca189df8
locale: en-us
summary: "OutSystems Developer Cloud (ODC) native mobile builds API: start iOS and Android package builds, monitor progress, and upload to app stores via CI/CD."
figma:
coverage-type:
  - apply
topic:
  - app-distribution
app_type: mobile apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - Android
  - CI/CD
  - Deploy
  - iOS
  - Mobile app
  - Native App
  - REST
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# Automating mobile builds and uploading to app stores

This article explains how to use OutSystems APIs to automate these steps in a CI/CD pipeline:

* Start iOS and Android mobile app package builds in ODC.

* Monitor the builds until they finish, then download the mobile app packages and build logs.

* Upload the mobile app packages to App Store Connect and Google Play by using your upload tool.

A **mobile app package** is the iOS IPA or Android AAB/APK file that you upload to an app store. The API refers to the operation that generates it as a **native build**.

<div class="info" markdown="1">

This article uses endpoints under `/api/native-mobile-builds/v1/`.

ODC also provides a different **Build Operations** API under `/api/builds/v1/build-operations`, which creates asset builds for deployment. This article uses that API only to obtain the `buildKey` and `revision` required to start native mobile builds.

</div>

## Prerequisites

Before you start, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) from an API client with one or more of these [permissions](../authentication/create-api-client.md#edit-permissions-of-api-client), depending on the endpoints you call:

    * [Configuration management > View configurations](../../native-mobile-builds-api-v1.md#get-/environments/-environmentKey-/applications/-applicationKey-/configurations/ios) to call the `GET` configuration endpoints.

    * [Configuration management > Edit configurations](../../native-mobile-builds-api-v1.md#patch-/environments/-environmentKey-/applications/-applicationKey-/configurations/ios) to call the `PATCH` configuration endpoints.

    * [Release management > Deploy apps](../../native-mobile-builds-api-v1.md#post-/build-operations) to call the `POST /build-operations` endpoint.

    * [Stage > View stage](../../native-mobile-builds-api-v1.md#get-/build-operations/-operationKey-) to list and monitor build operations.

    Include the access token in the `Authorization` header as `Bearer ACCESS_TOKEN`.

* The `environmentKey` and `applicationKey` for the app you want to build.

* The `buildKey` and `revision` for the app revision you want to package.

    For more information about retrieving the build key and revision, refer to [Selecting the revision and build of your asset](select-revision-build.md).

* App Store Connect and Google Play credentials, and an upload tool for publishing packages from your CI/CD pipeline (for example, Fastlane).

## Configure mobile app package settings

Mobile app package builds depend on platform-specific configurations, such as the app identifier and signing assets.

To review or update mobile build configurations, use these endpoints:

* iOS configuration:

    * `GET /api/native-mobile-builds/v1/environments/{environmentKey}/applications/{applicationKey}/configurations/ios`

    * `PATCH /api/native-mobile-builds/v1/environments/{environmentKey}/applications/{applicationKey}/configurations/ios`

* Android configuration:

    * `GET /api/native-mobile-builds/v1/environments/{environmentKey}/applications/{applicationKey}/configurations/android`

    * `PATCH /api/native-mobile-builds/v1/environments/{environmentKey}/applications/{applicationKey}/configurations/android`

Review available native builder versions (MABS versions) by calling `GET /api/native-mobile-builds/v1/native-builder-versions`.

To upload signing assets, encode the signing files as base64 and set them in the PATCH request body:

* For iOS, base64-encode the certificate file and provisioning profile file, then set them as `certificate.value` and `provisioningProfile.value`.

* For Android, base64-encode the keystore file, then set it as `keystore.value`.

For example, to update iOS signing assets, build type, app identifier, native builder version, and mobile framework:

```json
{
  "certificate": { "value": "CERTIFICATE_BASE64" },
  "certificateName": { "value": "my-certificate.p12" },
  "certificatePassword": { "value": "CERTIFICATE_PASSWORD" },
  "provisioningProfile": { "value": "PROVISIONING_PROFILE_BASE64" },
  "provisioningProfileName": { "value": "my-profile.mobileprovision" },
  "appIdentifier": { "value": "com.example.myapp" },
  "buildType": { "value": "Development" },
  "mabsVersion": { "value": "12.0" },
  "mobileFramework": { "value": "Capacitor" }
}
```

For example, to update Android signing assets, build type, app identifier, native builder version, and mobile framework:

```json
{
  "keystore": { "value": "KEYSTORE_BASE64" },
  "keystoreName": { "value": "my-keystore.jks" },
  "keystorePassword": { "value": "KEYSTORE_PASSWORD" },
  "alias": { "value": "KEY_ALIAS" },
  "aliasPassword": { "value": "ALIAS_PASSWORD" },
  "appIdentifier": { "value": "com.example.myapp" },
  "buildType": { "value": "Bundle" },
  "mabsVersion": { "value": "12.0" },
  "mobileFramework": { "value": "Capacitor" }
}
```

<div class="info" markdown="1">

Signing assets (such as iOS certificates and provisioning profiles, or Android keystores) are secrets. Treat them as sensitive data and store them in a secure secret store in your CI/CD system.

Not all build types require you to upload signing assets. For example, iOS **Simulator** builds don’t require a certificate or provisioning profile. For more information, refer to [Mobile app build types](../../../../building-apps/mobile/mobile-build-types.md).

</div>

## Start mobile app package builds for iOS and Android

Mobile app package builds run as asynchronous operations.

To select version values for the next build, use:

`POST /api/native-mobile-builds/v1/build-operations/version-suggestions`

This endpoint returns a suggested `mobileVersionNumber` and `mobileVersionCode` for iOS, Android, or both platforms.

To validate whether a new mobile app package build is needed for a given platform, use:

`POST /api/native-mobile-builds/v1/build-operations/native-build-validation`

The response includes a `platformResults` object. Check `platformResults.Android` and `platformResults.iOS` for the platforms you want to build. For example:

```json
{
  "platformResults": {
    "Android": "NativeBuildNeeded",
    "iOS": "NativeBuildNotNeeded"
  }
}
```

* `NativeBuildNeeded`: Start a build for that platform.

* `NativeBuildNotNeeded`: Skip starting a build for that platform.

* `MissingConfiguration`: Update the platform configuration, then run the validation again.

To start a mobile app package build, use:

`POST /api/native-mobile-builds/v1/build-operations`

The request body includes the app revision (`buildKey` and `revision`), the target platform, and the stage context (`environmentKey` and `applicationKey`).

Example request body for iOS:

```json
{
  "buildKey": "b111b111-1bb1-1bb1-111b-b1111b1b1b11",
  "revision": 12,
  "mobileVersionNumber": "1.2.0",
  "mobileVersionCode": 120,
  "mobilePlatform": "iOS",
  "environmentKey": "1ee11e11-1111-1111-e1ee-1e111e11eee1",
  "applicationKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11"
}
```

Example request body for Android:

```json
{
  "buildKey": "b111b111-1bb1-1bb1-111b-b1111b1b1b11",
  "revision": 12,
  "mobileVersionNumber": "1.2.0",
  "mobileVersionCode": 120,
  "mobilePlatform": "Android",
  "environmentKey": "1ee11e11-1111-1111-e1ee-1e111e11eee1",
  "applicationKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11"
}
```

When the request succeeds, the response returns `key`. Use that value as the `{operationKey}` in the monitor endpoints to track the build and retrieve download URLs.

## Monitor the build and retrieve downloads

To monitor a build operation, use the `operationKey` returned as `key` when you start the build:

`GET /api/native-mobile-builds/v1/build-operations/{operationKey}?environmentKey={environmentKey}&applicationKey={applicationKey}`

The `status` field shows the current state. When the status is `Finished`, the response includes download URLs such as:

* `appBinaryDownloadUrl` (the mobile app package file, such as IPA or AAB).

* `mobileBuildLogUrl` (build logs).

* `appSourceDownloadUrl` (source bundle, when available).

* `appDeploymentFileDownloadUrl` (deployment file for installing the iOS app package on a device).

To retrieve progress messages during the build, use:

`GET /api/native-mobile-builds/v1/build-operations/{operationKey}/log-messages?environmentKey={environmentKey}&applicationKey={applicationKey}&limit={limit}&offset={offset}`

<div class="info" markdown="1">

The build operation endpoints have a rate limit of 100 requests per minute. Use a polling interval that stays under this limit.

</div>

If the operation finishes with an error, retrieve the build logs and progress messages. Fix the underlying issue (often a missing or invalid configuration) and start a new build.

## Upload the mobile app packages to the app stores

After you download the iOS and Android mobile app packages from `appBinaryDownloadUrl`, upload them to the app stores by using your App Store Connect and Google Play credentials and upload tool.

Some iOS builds also include `appDeploymentFileDownloadUrl`, which you use to install the app package on a device.

<div class="info" markdown="1">

The Native Mobile Build API doesn’t provide endpoints to upload mobile app packages to App Store Connect or Google Play.

</div>

Add an approval gate in your CI/CD pipeline before you upload a build to a production store track.

## Related resources

Use these resources to learn more about authentication, CI/CD prerequisites, and uploading mobile app packages to the app stores:

* **OutSystems APIs**

    * [Configure API access using an API client](../authentication/create-api-client.md)

    * [Get access token](../authentication/get-access-token.md)

    * [Selecting the revision and build of your asset](select-revision-build.md)

    * [Deploying your asset to the target stage](deploy-asset.md)

* **Official app store upload documentation**

    * [Upload builds to App Store Connect](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/)

    * [Google Play Developer API](https://developers.google.com/android-publisher)

    * [Fastlane pilot action](https://docs.fastlane.tools/actions/pilot/)

    * [Fastlane supply action](https://docs.fastlane.tools/actions/supply/)
