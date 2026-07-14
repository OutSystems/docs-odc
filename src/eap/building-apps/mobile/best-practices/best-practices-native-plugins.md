---
guid: e9876507-c556-4e7e-984f-3a411913a26c
locale: en-us
summary: Apply these recommendations when selecting, integrating, and building Capacitor plugins in OutSystems Developer Cloud mobile apps.
figma:
coverage-type:
  - evaluate
app_type: mobile apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - Best Practices
  - Capacitor
  - Cordova
  - Forge
  - Mobile app
  - Native App
  - Plugins
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Best practices for native integrations and plugins

Plugins give mobile apps access to native device capabilities, such as geolocation or push notifications, but they also introduce native dependencies that affect your build process, release cadence, and long-term maintenance. Following these recommendations helps you make the right integration decisions and avoid common pitfalls.

## Use OutSystems-supported plugins before alternatives {#use-supported-plugins}

OutSystems-supported plugins on Forge have been tested with all supported MABS versions, are actively maintained, and are backed by OutSystems support. They also come with guaranteed Capacitor compatibility. Reaching for community or custom plugins before checking Forge increases both maintenance effort and risk.

### Recommendation

Before integrating any native capability, search [Forge](https://www.outsystems.com/forge/) for an OutSystems-supported plugin that meets your requirements. Unsupported Forge plugins are not guaranteed to have been updated for MABS 12, so using an OutSystems-supported plugin is the safest starting point.

The [OutSystems supported mobile plugins](../../../integration-with-systems/mobile-plugins/os-supported-plugins.md) page contains the full list of supported plugins plus links to available documentation.

If no supported plugin is available, follow the [plugin decision flow](#follow-decision-flow) before building from scratch.

### Benefits

Using OutSystems-supported plugins reduces the native code you own and maintain. Supported plugins receive updates as MABS and Capacitor evolve, so you spend less time on compatibility work and more time on your app.

## Follow the plugin decision flow {#follow-decision-flow}

When no OutSystems-supported plugin covers the capability you need, you still have options before building from scratch. The right choice depends on what already exists and the level of maintenance you are willing to own. Skipping steps creates unnecessary long-term maintenance burden.

### Recommendation

Follow the [decision flow for plugin integration in Capacitor apps](../../../integration-with-systems/mobile-plugins/intro.md#use-plugins-capacitor-apps): check Forge first, then an existing Cordova plugin you can adapt, then an official or community-supported Capacitor plugin on npm, and only build a plugin from scratch when none of those options meet your requirements.

Before integrating any community Forge plugin or npm package, review its source, maintenance activity, and security posture. For detailed information, refer to [Security considerations](../../../integration-with-systems/mobile-plugins/capacitor-plugins/integrate-plugin-in-app.md#plugin-security).

### Benefits

Each step down the decision flow increases the code you own and must maintain. Starting at the top minimizes that burden and keeps your project aligned with OutSystems support guarantees.

## Pin plugin versions in extensibility configurations {#pin-plugin-versions}

When you reference a plugin package in an extensibility configuration using a floating version range (for example, `^1.0.0` or `latest`), MABS resolves the version at build time. A new plugin release with breaking changes can silently alter your app's behavior or break the build the next time you generate a package, even though you made no changes to your app.

### Recommendation

Always specify an exact version when referencing a plugin in the `npm` field of an extensibility configuration:

```json
{
    "buildConfigurations": {
        "capacitor": {
            "source": {
                "npm": "@capacitor/barcode-scanner@2.0.3"
            }
        }
    }
}
```

When you decide to upgrade a plugin, review the plugin's changelog for breaking changes before updating the pinned version, test the result on a physical device, and distribute a new native package.

### Benefits

Pinning versions makes your builds reproducible. Two builds from the same source always produce the same native binary, which makes it easier to reproduce issues and reason about what changed between releases.

## Implement browser fallbacks for plugin calls {#browser-fallbacks}

ODC apps run in a browser during development and preview. ODC mobile apps can also be distributed as PWAs. Native plugins are not available in the browser or PWAs, so any plugin call that runs without a fallback will fail silently or throw an error that is harder to diagnose.

If your app targets PWA distribution, PWA support cannot rely on the Capacitor or Cordova plugin layer, as those native runtimes are not available in ODC PWAs. Implement any PWA-specific behavior using JavaScript directly in the ODC library.

### Recommendation

When calling a plugin from an ODC library client action using JavaScript, guard the call with a platform check to prevent crashes. If PWA support is not required, return a clear error in the fallback:

```javascript
if (typeof window.CapacitorPlugins !== 'undefined' && window.CapacitorPlugins.MyPlugin) {
    // Native app — call the plugin
    window.CapacitorPlugins.MyPlugin.myMethod();
} else {
    // Browser or PWA — feature not available
    $parameters.ErrorMessage = 'This feature requires a native device.';
}
```

If your app targets PWA distribution, implement the equivalent functionality using browser APIs in the `else` branch instead of returning an error. The following example shows a geolocation plugin call with a Web Geolocation API fallback for PWA:

```javascript
if (typeof window.CapacitorPlugins !== 'undefined' && window.CapacitorPlugins.Geolocation) {
    // Native app — use the Capacitor plugin
    window.CapacitorPlugins.Geolocation.getCurrentPosition()
        .then(function(result) {
            $parameters.Latitude = result.coords.latitude;
            $parameters.Longitude = result.coords.longitude;
        });
} else if (navigator.geolocation) {
    // Browser or PWA — use the Web Geolocation API
    navigator.geolocation.getCurrentPosition(function(position) {
        $parameters.Latitude = position.coords.latitude;
        $parameters.Longitude = position.coords.longitude;
    });
} else {
    $parameters.ErrorMessage = 'Geolocation is not available on this device.';
}
```

### Benefits

Browser fallbacks let you test the non-native flows of your app in the browser without needing a physical device for every iteration. They also enable PWA distribution and make the app more resilient on devices where a plugin is unavailable, producing clear error messages instead of silent failures.

## Use dual-stack plugins only when adaptation is not enough {#dual-stack}

During a migration from Cordova to Capacitor, some plugins need to work in both runtimes simultaneously.

A dual-stack plugin bundles a Cordova plugin and a Capacitor plugin in the same ODC library, selecting the correct implementation at runtime. Before going this route, check whether [adapting your Cordova plugin for Capacitor compatibility](../../../integration-with-systems/mobile-plugins/migrate-cordova-plugin.md) is sufficient. An adapted Cordova plugin works in both Cordova and Capacitor apps from a single implementation, which is simpler and requires less maintenance than dual-stack.

### Recommendation

Build a dual-stack plugin only when adapting the Cordova plugin is not enough and you still have active apps on both runtimes. For detailed information about the criteria that justify this approach and the full implementation steps, including runtime detection, refer to [Implement a dual-stack plugin](../../../integration-with-systems/mobile-plugins/capacitor-plugins/dual-stack-plugin.md).

The `cordova-plugin-migrator` AI skill accelerates the migration side of a dual-stack plugin. It analyzes an existing Cordova plugin, produces a structured migration plan, and generates a Capacitor-compatible implementation at a checkpoint you control. For detailed information, including installation, refer to [ionic-team/capacitor-skills](https://github.com/ionic-team/capacitor-skills).

### Benefits

A dual-stack plugin lets you adopt Capacitor capabilities without breaking existing Cordova apps, giving you a controlled migration path while keeping a single ODC library for consumers.

## Account for plugin changes in your release plan {#release-planning}

Not every app update requires a new native binary. OutSystems can deliver most logic and UI changes over the air (OTA). However, any change that affects the native layer requires generating and distributing a new native package, which users must install manually from the app store or your distribution channel.

Changes that require a new native package include:

* Adding or removing a plugin
* Changing the plugin version referenced in an extensibility configuration
* Modifying permissions, build actions, or other extensibility configuration properties

### Recommendation

Treat every plugin-related change as a release event that requires a new native package. When planning app updates that include plugin changes, account for the time needed to:

1. Generate the new package with MABS.
1. Test the package on real physical devices for both iOS and Android.
1. Submit the new package to the Play Store, Apple App Store, or your distribution channel. For iOS, allow time for App Store review.
1. Coordinate the rollout so that server-side changes are backward compatible with the previous native package until all users have updated.

When developing an ODC library that exposes new native plugin features, you cannot guarantee all users have updated to the latest native package before an OTA update reaches them. Use defensive feature detection in the library's JavaScript to prevent crashes on older native packages, while also providing a clear error message to the consumer:

```javascript
if (window.CapacitorPlugins.MyPlugin && typeof window.CapacitorPlugins.MyPlugin.newFeature === 'function') {
    // New native feature available
    window.CapacitorPlugins.MyPlugin.newFeature();
} else {
    // Older native package — degrade gracefully
    $parameters.ErrorMessage = 'Update the app to use this feature.';
}
```

This follows the same principle as browser fallbacks: always check before calling, so older native packages degrade gracefully instead of crashing.

### Benefits

Planning for native build requirements prevents situations where an OTA update references native code that older app versions do not have, which can cause runtime crashes. Early planning also reduces surprise delays from app store review cycles.

## Include plugin license text in the app {#license-attribution}

Most open-source plugins are distributed under permissive licenses such as MIT or Apache 2.0, which legally require attribution and preservation of the license text. Where you include that text is flexible: it can be an About page, a dedicated Licenses screen, a Settings section, or distribution documentation, as long as it is accessible.

### Recommendation

When evaluating a plugin, review its license before integrating it. Permissive licenses such as MIT and Apache 2.0 require attribution but are generally straightforward to comply with. Copyleft licenses such as GPL or LGPL carry stricter obligations, including in some cases the requirement to distribute source code, and warrant a review with your legal team before use in a commercial app.

For each plugin your app uses, locate the license file in the plugin's repository and include the license text in an accessible location in your app or its distribution. This applies to both OutSystems-supported plugins and community or custom plugins.

### Benefits

Reviewing licenses before integration prevents surprises late in the project. Including license text keeps your app compliant with open-source requirements and reduces legal risk for your organization.

## Related resources

To find and evaluate mobile plugins for your app, refer to the following:

* [Use mobile plugins](../../../integration-with-systems/mobile-plugins/intro.md)
* [OutSystems supported mobile plugins](../../../integration-with-systems/mobile-plugins/os-supported-plugins.md)

To adapt an existing Cordova plugin or build a new plugin for Capacitor, refer to the following:

* [Adapt Cordova plugin for compatibility with Capacitor](../../../integration-with-systems/mobile-plugins/migrate-cordova-plugin.md)
* [Implement a dual-stack plugin](../../../integration-with-systems/mobile-plugins/capacitor-plugins/dual-stack-plugin.md)
* [Build a Capacitor plugin from scratch](../../../integration-with-systems/mobile-plugins/capacitor-plugins/build-capacitor-plugin.md)

To integrate a plugin into your app and package it for distribution, refer to the following:

* [Integrate Capacitor plugin into a mobile app](../../../integration-with-systems/mobile-plugins/capacitor-plugins/integrate-plugin-in-app.md)
* [Create mobile app package](../creating-mobile-package.md)
