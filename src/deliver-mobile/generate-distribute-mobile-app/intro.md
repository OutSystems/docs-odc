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
