---
summary: You can generate the mobile app package for your mobile app and distribute it for tests purposes or, when you have completed work on your app, generate a production-ready version of your app to distribute to a selected group of end users or to publish in mobile app stores.
tags: runtime-mobile, article-page
---

# Generate and Distribute Your Mobile App

Before generating your mobile app for the first time, you have to configure specific iOS and/or Android settings. Check the [topics listed at the end of this page](#Articles_in_this_Section) for details about different scenarios, such as development tests, distributing your app to a limited group of end users or publishing your app in Mobile App Stores.

The following sections show how to configure and generate iOS and Android app packages of your mobile apps in Service Studio or in Service Center. For additional information about generating and distributing iOS and Android app packages, see [More Information on Generating and Distributing Mobile Apps](more-information.md).

<div class="warning">

Don't tamper with the iOS or Android mobile builds once the platform generates them. For example, don't use a third-party tool to add new functionality like performance monitoring. If you modify a mobile build, you're risking having an app that doesn't run correctly and that fails to pass integrity checks. 

</div>

## Configure and generate a mobile app package in Service Studio { #config-generate-service-studio }

To configure or generate your mobile app package (iOS or Android) in Service Studio, do the following:

1. Navigate to the app detail screen of your mobile app. 

1. Select the **Distribute** tab. The native mobile settings are in the **Native Platforms** section.

1. When configuring your mobile app for the first time for a given platform (iOS or Android), click the **Generate Android app** or **Generate iOS app** button, according to the platform. Follow the configuration steps for your desired scenario, described in the [topics listed at the end of this page](#Articles_in_this_Section). If you have previously defined your mobile app's iOS or Android configuration settings, click on the cog icon for the correct platform to change your configuration. 

1. After defining or changing your mobile app iOS or Android settings, click **Generate Android app** or **Generate iOS app**. 

    ![Native app settings in Service Studio](images/native-platforms-tab-ss.png?width=600)


### Choosing the MABS version to build your mobile packages { #choose-mabs-version }

The [Mobile Apps Build Service (MABS)](<../mobile-apps-build-service/intro.md>) is a **cloud service** used by OutSystems to generate the mobile packages of your mobile apps developed in OutSystems for iOS and Android. 

MABS is continuously improved and OutSystems regularly makes available new versions of this cloud service. However, you might not want to use the latest version, since different MABS versions support different mobile stacks and therefore different ranges of devices and mobile platform versions.

You can select the MABS version used to generate the mobile packages **by mobile app** and **by mobile platform** (iOS and Android), for a given environment. You can do this in Service Center at the app level.

To choose a MABS version do the following:

1. In Service Center, click the **Applications** tab, open your mobile app from the app list and select the **Distribute** tab. The native mobile settings are in the **Native Platforms** section.

1. In the **Settings** column, click the **Configure** link for the iOS or Android entry.

    ![Mobile app settings screen](images/sc-open-mabs-version-selection.png?width=750)

1. At the end of the configuration settings page, select the MABS version you wish to use for generating the mobile app package for the mobile platform you're configuring (iOS or Android) in the current environment, either the latest available version or a specific version (see below for details).

    ![Mobile Apps Build Service (MABS) version selection)](<images/sc-select-mabs-version.png>)

    **Note:** The MABS version selection is only available for apps whose native platform settings are already configured.

1. Click **Save and Generate** and wait a few moments while OutSystems generates your mobile app package.

When choosing a MABS version you have the following options available:

* **Always use the latest version available**: Always use the most recent MABS version available to generate the mobile package of the app for the current platform and in the current environment.

* **Specific version _(select from list)_**: Generate mobile app packages (in the current environment) with the MABS version selected from the list.

Whether you selected the option of using the latest MABS version or using a specific MABS version for the app package generation, when you generate and tag a mobile app version, OutSystems records the MABS version used to generate the mobile package.

**To fully understand the impacts of this setting, be sure to check [Understanding MABS Versions](<../mobile-apps-build-service/intro.md#understanding-mabs-versions>).**

## Download mobile app build logs { #download-mobile-app-build-logs }

You can obtain the build logs of your mobile apps in Service Center. Build logs are available for both successful and unsuccessful builds, and each platform (Android and iOS) has its own build log.

To obtain a mobile app build log:

1. Access the Service Center of the environment (`https://<environmentdomain>/ServiceCenter`).
1. Go to **Factory** and click the **Applications** tab.
1. Click your mobile app name to navigate to the mobile app detail page.
1. In the **Distribute** tab, under the **Native Platforms** section, click the log icon for the desired platform to download the build log.

![](<images/sc-download-build-logs.png>)

## Updating your mobile app package

Users usually don't have to update the app manually after installing it, since OutSystems automatically pushes the updates to user devices when you publish a new version of the mobile app.

However, in some specific situations, the users must install a new mobile app package. For more information check [Mobile App Update Scenarios](<../mobile-app-update-scenarios.md>).

## Distribute your app as PWA { #distribute-your-app-as-pwa }

You can use the settings in Service Center to configure your app as progressive web app (PWA). PWAs run from your server and don't require distribution though the app stores.

For more information check out [Distribute as a progressive web app (PWA)](../distribute-pwa/intro.md).

To set an app for the PWA distribution in Service Center, do the following:

1. Open the Service Center console of the environment (`https://<environmentdomain>/ServiceCenter`) and navigate to **Factory**.

1. Click the **Applications** tab, open your mobile app from the app list, then select the **Distribute** tab. The PWA settings are in the **Progressive Web Application (PWA)** section.

    ![PWA settings in Service Center](images/sc-pwa-settings.png?width=750)

1. Select the checkbox **Distribute as PWA**, then click **Apply**.