---
summary: Explore the diverse app development capabilities of OutSystems Developer Cloud (ODC), including web and mobile applications.
tags: 
locale: en-us
guid: 2c23e305-f3ca-46cc-a8c8-a29c409a9ccf
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/zohMj3VpAEA6P9J9azwqQq/Getting-started-with-ODC?type=design&node-id=2449%3A32710&t=CxwRhrJUzQXvCd96-1
platform-version: odc
---

# Types of apps you can build

You can create several types of apps in OutSystems Developer Cloud (ODC). 

From ODC Portal, navigate to the **Apps** screen and click **Create app**. ODC Studio launches and the **What would you like to create?** window displays. Click **App** to see the options.

![Screenshot of the 'What would you like to create?' window in OutSystems Developer Cloud with options to create different types of apps](images/what-would-you-like-to-create-ss.png "ODC App Creation Options")

* Select **Web app** if you want to:
    * Create an app that users run mainly in a desktop browser, .
* Select **Phone app** or **Tablet app** if you want to: 
    * Create a mobile app to submit to Apple App Store or Google Play. You can also distribute a mobile app as a downloadable package to a group of users.
    * Create a lightweight app and share it as a Progressive Web App (PWA)(*) from your website. Users can put the app icon on their mobile home screen.

<div class="info" markdown="1">

**Libraries** exist at the same level as apps and let you share code between apps. You can learn more about them in [App Architecture](../app-architecture/intro.md#libraries-in-odc).

</div>


## What's a Web app?

In ODC, a Web app has a responsive interface that runs in the browser. The user experience is excellent across many types of devices and screen sizes.

When you develop a Web app:

* You can build apps using the client-side runtime and create responsive UX.
* Your apps run on a modern stack.

![Diagram illustrating the characteristics of a Web app in OutSystems Developer Cloud, highlighting responsive interface and modern stack](images/web-app-characteristics-diag.png "Web App Characteristics")

## What's a Mobile app?

In ODC, a Mobile App is an app that compiles to a native mobile Android or iOS app. 

You can develop for Android and iOS at the same time, as the underlying code is cross-platform. The default app templates of this type are **Phone app** and **Tablet app**.

There are two ways you can distribute a Mobile app:

* **Native app package** - A dedicated OutSystems cloud service generates native mobile builds for you, to distribute your app in the app stores or internally to a group of users.

* **Progressive Web App (PWA)**(*) - PWAs are lightweight apps that have the look and feel of native mobile apps. They're quick to distribute and install directly from your website, as they don't depend on the app stores. 

## Comparison between Web apps and Mobile apps

Here is a table comparing the features of Web apps and Mobile apps.

|<br/>|**Web app** <br/>|**Mobile app**<br/>|
|:-:|:-:|:-:|
|**Code Reusability**|![Diagram showing code reusability for Web apps in OutSystems Developer Cloud with common logic for all devices and screen sizes](images/mobile-vs-web-code-reusability-web-diag.png "Web App Code Reusability")<br/>Common logic for all devices and screen sizes.|![Diagram showing code reusability for Mobile apps in OutSystems Developer Cloud with common logic for native mobile platforms and PWAs](images/mobile-vs-web-code-reusability-mobile-diag.png "Mobile App Code Reusability")<br/>Common logic for all supported native mobile platforms, and supported browsers for PWAs.|
|**Runs in**|![Diagram indicating that Web apps run in a browser without installation, highlighting ease of access](images/mobile-vs-web-runs-in-web-diag.png "Web App Runtime Environment")<br/>A browser.<br/>No installation is needed.|![Diagram indicating that Mobile apps run on Android and iOS devices and PWAs run on supported browsers](images/mobile-vs-web-runs-in-mobile-diag.png "Mobile App Runtime Environment")<br/>Native mobile apps run on Android and iOS devices. PWAs run on any device with a supported browser.|
|**User Experience**|![Diagram highlighting the responsive layout for Web apps across different screen sizes and types](images/mobile-vs-web-user-experience-web-diag.png "Web App User Experience")<br/>Responsive layout for all screen sizes and types.|![Diagram highlighting dedicated mobile UI patterns and experiences for Mobile apps](images/mobile-vs-web-user-experience-mobile-diag.png "Mobile App User Experience")<br/>Dedicated mobile UI patterns and experiences.|
|**Access to device hardware**|![Diagram showing HTML5 supported device capabilities for Web apps](images/mobile-vs-web-access-device-web-diag.png "Web App Device Hardware Access")<br/>HTML5 supported device capabilities.|![Diagram showing native mobile apps access to device capabilities through Cordova plugins and limited access for PWAs](images/mobile-vs-web-access-device-mobile-diag.png "Mobile App Device Hardware Access")<br/>Native mobile apps access a range of device capabilities through Cordova plugins. PWAs use dedicated plugins, which by design can access only hardware that the browser running the PWA is allowed to access.|
|**Offline capabilities**|![Diagram indicating no offline capabilities for Web apps](images/mobile-vs-web-offline-web-diag.png "Web App Offline Capabilities")<br/>No offline capabilities.|![Diagram showing offline data storage options for native mobile apps and PWAs](images/mobile-vs-web-offline-mobile-diag.png "Mobile App Offline Capabilities")<br/>For storing offline data, native mobile apps use local storage and PWAs use browser storage.|
|**Deployment and updates**|![Diagram explaining automatic updates for Web apps upon browser page refresh](images/mobile-vs-web-deployments-web-diag.png "Web App Deployment and Updates")<br/>Updates are automatic when users refresh the browser page.|![Diagram explaining update mechanisms for native mobile apps and automatic updates for PWAs](images/mobile-vs-web-deployments-mobile-diag.png "Mobile App Deployment and Updates")<br/>Native mobile apps can update automatically, and users need to install a new version only when you change the native shell. PWAs update automatically when the app detects a new version.|
|**Distribution**|![Diagram showing the distribution of Web apps through sharing the app link](images/mobile-vs-web-distribution-web-diag.png "Web App Distribution")<br/>Share the app link with users.|![Diagram showing distribution options for native mobile apps and direct running of PWAs from a website](images/mobile-vs-web-distribution-mobile-diag.png "Mobile App Distribution") ![Diagram showing the distribution of Web apps through sharing the app link](images/mobile-vs-web-distribution-web-diag.png "Web App Distribution")<br/>You can distribute native mobile apps in-house or through the app stores. Users can run a PWA directly from your website, and add the app icon to the device home screen.|
