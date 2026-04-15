---
summary: Explore mobile plugin functionalities and their support in PWAs with OutSystems Developer Cloud (ODC).
tags: mobile plugins, progressive web apps, native mobile features, security, firebase
locale: en-us
guid: 55ef1d73-dac8-48e6-8b15-dc6990779660
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=3202-7454
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - forge
coverage-type:
  - understand
  - apply
topic:
  - using-cordova-plugins
---

# Use mobile plugins

 Plugins provide essential functionality to native mobile apps, enabling access to device hardware capabilities such as notifications, the camera, GPS, QR code reading, and more.

From [Mobile Apps Build Service (MABS 12)](../../building-apps/mobile/mabs-overview.md) onward, ODC supports the Capacitor cross-platform native runtime alongside Cordova, providing you with a modern and flexible way to build mobile apps. When [building](../../building-apps/mobile/creating-mobile-package.md) your mobile apps with MABS 12, you can choose between the Cordova and Capacitor.

## Using plugins in Capacitor apps {#use-plugins-capacitor-apps}

When building a Capacitor-based mobile app, you have several options for integrating plugins depending on your specific needs and available resources.

Here's the decision flow for plugin integration in Capacitor apps:

![Flowchart showing the decision process for integrating plugins in Capacitor apps, including options for using Forge plugins, custom Cordova plugins, community-supported plugins, or building plugins from scratch.](images/decision-flow-plugin-integration-diag.png "Decision Flow for Plugin Integration in Capacitor Apps")

### Check Forge for Capacitor-supported plugins

Search [Forge](https://www.outsystems.com/forge/) for Capacitor-supported plugins that meet your requirements. If available, download and integrate the plugin into your app. For detailed information, refer to [Install a plugin and use it in your app](os-supported-plugins.md#install-a-plugin-and-use-it-in-your-app).

All OutSystems-supported plugins can be used in both Cordova and Capacitor apps.

### Use existing custom Cordova plugins

If no Forge plugin exists but you already have an ODC library that references the Cordova plugin, you can make that library work with Capacitor apps. In some cases, the Cordova plugin itself doesn’t require any code changes. You only need to update the extensibility configurations in your ODC library so that it correctly references the plugin for Capacitor compatibility.

However, if your plugin relies on Cordova-specific functionalities such as preferences, hooks, or certain config-file changes, you may need to adapt the plugin. For detailed information about making Cordova plugins compatible with Capacitor, refer to [Adapt Cordova plugin for compatibility with Capacitor](migrate-cordova-plugin.md).

For maximum compatibility and performance optimization, consider making your existing ODC library that references the Cordova plugin dual-stack. In this scenario, you must implement a separate Capacitor plugin alongside your existing Cordova implementation. A dual-stack plugin provides separate implementations for each framework. You can reference both plugin implementations in the extensibility configuration of the ODC library. For detailed information, refer to [Building a dual-stack plugin](capacitor-plugins/dual-stack-plugin.md). This approach allows you to leverage Capacitor-specific features while maintaining full Cordova support.

### Use an official or community-supported Capacitor plugin

If you don't have an existing Cordova plugin, check if the functionality you need already exists as an [official or community-supported](https://capacitorjs.com/docs/plugins) Capacitor plugin. If yes, create a [wrapper ODC library](capacitor-plugins/integrate-plugin-in-app.md) to integrate the Capacitor plugin into your app.

### Build a Capacitor plugin from scratch

When no existing solution meets your needs, build a custom Capacitor plugin. Then, develop a corresponding [wrapper ODC library](capacitor-plugins/integrate-plugin-in-app.md) to expose the plugin's functionality in your app. For detailed information about building Capacitor plugins, refer to [Build a Capacitor plugin from scratch](capacitor-plugins/build-capacitor-plugin.md).

## Accessing plugins

During the build process, all Capacitor plugins are automatically bundled and made available globally through `window.CapacitorPlugins`. This includes:

* Official Capacitor plugins
* Third-party plugins from npm
* Your custom-built plugins

You reference plugins in your library's extensibility configuration.

For detailed information, refer to [Integrate Capacitor plugin into mobile app](capacitor-plugins/integrate-plugin-in-app.md).

## Important considerations when using plugins

When working with the plugins:

* Only install plugins from trusted sources. For detailed information, refer to [Security considerations](capacitor-plugins/integrate-plugin-in-app.md#plugin-security).
* Use the plugin that supports iOS or Android, depending on your target platform. The app creation fails if you use a plugin that isn't supported on the target platform. For more information on app generation errors check the [list of MABS errors](https://success.outsystems.com/support/errors/mabs_errors/).
* Each time you add, remove, or modify the plugin in an app, OutSystems creates a mobile package which you then have to distribute to the users for installation.
* Include the plugin license in your app to respect the license agreements of that plugin. These license agreements are usually placed in the About page of the app that uses them.

## Related resources

* [OutSystems supported mobile plugins](os-supported-plugins.md)

* [Integrate Capacitor plugin into mobile app](capacitor-plugins/integrate-plugin-in-app.md)

* [Adapt Cordova plugin for compatibility with Capacitor](migrate-cordova-plugin.md)

* [Build a Capacitor plugin from scratch](capacitor-plugins/build-capacitor-plugin.md)
