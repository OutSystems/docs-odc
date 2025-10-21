---
summary: OutSystems Developer Cloud (ODC) enables rapid development of mobile apps, including native apps, PWAs, and mobile backends.
tags: mobile app development, native apps, progressive web apps, mobile backend
locale: en-us
guid: 8e81892f-5deb-4b08-b3d7-e12459619f76
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - none
coverage-type:
  - none
helpids: 30625
---

# Mobile apps

OutSystems Developer Cloud (ODC) enables you to create powerful, cross-platform mobile apps using low-code development. These apps leverage native device capabilities, providing seamless user experiences across both iOS and Android platforms.

ODC enables you to develop the following mobile assets:

* A mobile app: These are apps that users install on their phones, have access to the device sensors, can work offline, and have a UX designed for a native experience.
  
* A Progressive Web App (PWA): These are apps that users can access from their mobile browsers without installation.
  
* Mobile backend: Use OutSystems as the backend for your native mobile app, without using the traditional programming tools.

## Capacitor framework support in mobile apps

With [MABS 12](mabs-overview.md), you can build mobile apps using both Apache Cordova and [Capacitor](https://capacitorjs.com/) framework. Capacitor is modern hybrid app framework that allows you to build cross-platform native mobile apps using web technologies like HTML, CSS, and JavaScript.

Capacitor provides a flexible and scalable solution for integrating native features and plugins, enabling you to customize and extend mobile app functionality efficiently. You also have access to a highly active developer community with a growing library of [plugins](https://capacitorjs.com/docs/plugins) ready to use.

While creating your mobile package using MABS 12, you can [select the framework](creating-mobile-package.md) that best suits your app's requirements.

With MABS 12, you can:

* Build mobile apps using the modern Capacitor framework.

* Continue using the Cordova framework for existing apps while preparing for a gradual transition to Capacitor.

### Changes from Cordova to Capacitor apps

The transition from an OutSystems Cordova app to a Capacitor app brings several significant updates focusing on adopting the Capacitor framework and modernizing the build process and extensibility.

| Feature                        | Cordova app                                      | Capacitor app                                   |
|--------------------------------|--------------------------------------------------|-------------------------------------------------|
| **Hybrid framework**           | Apache Cordova                                   | Capacitor                                 |
| **Native shell plugins**            | Cordova plugins                                 | Updated Capacitor plugins for core mobile services    |
| **Forge supported plugins** | Cordova plugins                                 | Dual-stack or Capacitor compatible plugins      |
| **Extensibility**              | [Cordova-based extensibility](legacy-extensibility-configuration.md)                  | [Universal extensibility](extensibility-configurations.md) with auto-complete and syntactical validation |
| **Mobile configuration**       | Standard configurations                         | [Mobile configuration](configuring-mobile-apps.md) tab with Capacitor-specific settings |
| **Native project customization** | Limited via config files                        | [Build actions](build-actions.md) to customize native mobile projects |

## Related resources

* [Capacitor and Cordova support in MABS 12](mabs-overview.md)

* [Universal extensibility configurations JSON schema](extensibility-configurations.md)

