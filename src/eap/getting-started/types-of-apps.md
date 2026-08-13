---
summary: "OutSystems Developer Cloud (ODC) app types: Web, Mobile, Agentic, libraries, and workflows — and how to choose the right one for your use case."
tags:
  - Agentic
  - Libraries
  - Mentor Studio
  - Mentor Web
  - Mobile app
  - Web
  - Workflows
locale: en-us
guid: 2c23e305-f3ca-46cc-a8c8-a29c409a9ccf
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/zohMj3VpAEA6P9J9azwqQq/Getting-started-with-ODC?type=design&node-id=2449%3A32710&t=CxwRhrJUzQXvCd96-1
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
  - evaluate
topic:
  - choose-app-type
  - basic-architecture
isautopublish: true
---

# Types of apps you can build

OutSystems Developer Cloud (ODC) supports several top-level asset types: Web apps, Mobile apps, Agentic apps, libraries, and workflows. You select the type when you create the asset. **Agentic development** through Mentor Web and Mentor Studio is the default build path for Web apps, and Mentor Studio extends to libraries and Agentic apps. The visual editor in ODC Studio is available for every type. For the full list of assets each AI tool supports, refer to [Agentic development](../agentic-development/intro.md).

![Screenshot of the 'What would you like to create?' window in OutSystems Developer Cloud with options to create different types of apps](images/types-of-apps-odcs.png "ODC App Creation Options")

* Select **Web app** if you want to create an app that users run mainly in a desktop browser.
* Select **Mobile app** if you want to create an app to submit to Apple App Store or Google Play. You can also distribute a mobile app as a downloadable package to a group of users or as a Progressive Web App (PWA).
* Select **Agentic app** if you want to build an app that uses AI at runtime to perform tasks, automate workflows, or handle complex, multi-step interactions.

The runtime type and the build approach are independent choices. An **Agentic app** is the runtime type: an app that calls AI when users run it. **Agentic development** is how you build apps with AI assistance from Mentor Web or Mentor Studio. The two are independent. You can build an Agentic app manually, or use agentic development to produce a Web app.

## What's a Web app?

In ODC, a Web app has a responsive interface that runs in the browser. The user experience is excellent across many types of devices and screen sizes.

When you develop a Web app:

* You can build apps using the client-side runtime and create responsive UX.
* Your apps run on a modern stack.

  ![Diagram illustrating the characteristics of a Web app in OutSystems Developer Cloud, highlighting responsive interface and modern stack](images/web-app-characteristics-diag.png "Web App Characteristics")

## What's a Mobile app?

In ODC, a Mobile app compiles to a native Android or iOS app. The same app adjusts to the device form factor at runtime, so you build once and ship to phone and tablet from a single source.

You can distribute a Mobile app in two ways:

* **Native app package.** A dedicated OutSystems cloud service generates native mobile builds for you to distribute in the app stores or internally to a group of users.
* **Progressive Web App (PWA).** Lightweight apps with the look and feel of native mobile apps. They're quick to distribute and install directly from your website, and they don't depend on the app stores.

## What's an agentic app?

In ODC, an Agentic app is a type of app that uses AI to act autonomously. These apps perform background operations and lack a user interface. Instead, Web or Mobile apps consume their capabilities to create intelligent, automated experiences.

## Comparison between Web, Mobile, and Agentic apps

Here is a table comparing the features of Web, Mobile, and Agentic apps.

|<br/>|**Web app** <br/>|**Mobile app**<br/>|**Agentic app**<br/>|
|:-:|:-:|:-:|:-:|
|**Code Reusability**|![Diagram showing code reusability for Web apps in OutSystems Developer Cloud with common logic for all devices and screen sizes](images/mobile-vs-web-code-reusability-web-diag.png "Web App Code Reusability")<br/>Common logic for all devices and screen sizes.|![Diagram showing code reusability for Mobile apps in OutSystems Developer Cloud with common logic for native mobile platforms and PWAs](images/mobile-vs-web-code-reusability-mobile-diag.png "Mobile App Code Reusability")<br/>Common logic for all supported native mobile platforms, and supported browsers for PWAs.|![Diagram showing that Web and Mobile apps can consume reusable logic from Agentic apps](images/agentic-reusable-logic-diag.png "Agentic App Reusable Logic")<br/>Web and Mobile apps can consume reusable logic.|
|**Runs in**|![Diagram indicating that Web apps run in a browser without installation, highlighting ease of access](images/mobile-vs-web-runs-in-web-diag.png "Web App Runtime Environment")<br/>A browser.<br/>No installation is needed.|![Diagram indicating that Mobile apps run on Android and iOS devices and PWAs run on supported browsers](images/mobile-vs-web-runs-in-mobile-diag.png "Mobile App Runtime Environment")<br/>Native mobile apps run on Android and iOS devices. PWAs run on any device with a supported browser.|![Diagram showing that Agentic apps run on the server and do not have a user interface](images/agentic-run-on-server-diag.png "Agentic App Runtime Environment")<br/>Runs on the server. Doesn't have a user interface.|
|**User Experience**|![Diagram highlighting the responsive layout for Web apps across different screen sizes and types](images/mobile-vs-web-user-experience-web-diag.png "Web App User Experience")<br/>Responsive layout for all screen sizes and types.|![Diagram highlighting dedicated mobile UI patterns and experiences for Mobile apps](images/mobile-vs-web-user-experience-mobile-diag.png "Mobile App User Experience")<br/>Dedicated mobile UI patterns and experiences.|![Diagram showing that Agentic apps provide capabilities to other apps without a direct user experience](images/agentic-capabilities-apps.png "Agentic App Capabilities")<br/>No direct user experience; provides capabilities to other apps.|
|**Access to device hardware**|![Diagram showing HTML5 supported device capabilities for Web apps](images/mobile-vs-web-access-device-web-diag.png "Web App Device Hardware Access")<br/>HTML5 supported device capabilities.|![Diagram showing native mobile apps access to device capabilities through Cordova plugins and limited access for PWAs](images/mobile-vs-web-access-device-mobile-diag.png "Mobile App Device Hardware Access")<br/>Native mobile apps access a range of device capabilities through Cordova plugins. PWAs use dedicated plugins, which by design can access only hardware that the browser running the PWA allows.|![Diagram showing that Agentic apps provide capabilities to other apps without a direct user experience](images/agentic-not-applicable-diag.png "Agentic App Capabilities")<br/>Not applicable. Operates on the server-side.|
|**Offline capabilities**|![Diagram indicating no offline capabilities for Web apps](images/mobile-vs-web-offline-web-diag.png "Web App Offline Capabilities")<br/>No offline capabilities.|![Diagram showing offline data storage options for native mobile apps and PWAs](images/mobile-vs-web-offline-mobile-diag.png "Mobile App Offline Capabilities")<br/>For storing offline data, native mobile apps use local storage and PWAs use browser storage.|![Diagram indicating no offline capabilities for Web apps](images/mobile-vs-web-offline-web-diag.png "Web App Offline Capabilities")<br/>No offline capabilities.|
|**Deployment and updates**|![Diagram explaining automatic updates for Web apps upon browser page refresh](images/mobile-vs-web-deployments-web-diag.png "Web App Deployment and Updates")<br/>Updates are automatic when users refresh the browser page.|![Diagram explaining update mechanisms for native mobile apps and automatic updates for PWAs](images/mobile-vs-web-deployments-mobile-diag.png "Mobile App Deployment and Updates")<br/>Native mobile apps can update automatically, and users need to install a new version only when you change the native shell. PWAs update automatically when the app detects a new version.|![Diagram showing that the server deploys updates for Agentic apps, making them immediately available to consuming apps](images/agentic-updates-diag.png "Agentic App Updates")<br/>The server deploys updates, making them immediately available to consuming apps.|
|**Distribution**|![Diagram showing the distribution of Web apps through sharing the app link](images/mobile-vs-web-distribution-web-diag.png "Web App Distribution")<br/>Share the app link with users.|![Diagram showing distribution options for native mobile apps and direct running of PWAs from a website](images/mobile-vs-web-distribution-mobile-diag.png "Mobile App Distribution")<br/>You can distribute native mobile apps in-house or through the app stores. Users can run a PWA directly from your website, and add the app icon to the device home screen.|![Diagram showing that Agentic apps are exposed and consumed as a Service Action by other apps within the ODC environment](images/agentic-consumed-exposed-diag.png "Agentic App Consumption")<br/>Exposed and consumed as a Service Action by other apps within the ODC environment.|

## What's a library?

A library is a reusable top-level asset that other apps consume for UI components, logic, or themes. Libraries are stateless by design: they provide functionality without persisting data, which keeps apps modular and reduces duplication. ODC supports general-purpose libraries for web and mobile apps, and mobile libraries for native mobile capabilities. For details, refer to [Libraries](../building-apps/libraries/libraries.md).

## What's a workflow?

A workflow automates a business process: a repeatable sequence of activities, decisions, and human approvals that runs in response to events from your apps. You design workflows in the workflow editor, a visual web-based tool in ODC Portal. Workflows are a top-level asset type with their own independent lifecycle, alongside apps and libraries. For details, refer to [Workflows in ODC](../building-apps/workflows/workflows-in-odc.md).

## Related resources

* [Intro to OutSystems Development (ODC)](https://learn.outsystems.com/training/journeys/intro-to-outsystems-development-570) online course
