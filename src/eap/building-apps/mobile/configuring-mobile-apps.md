---
guid: c7ec5c23-c83f-4bd7-ae95-c33d04f49a44
locale: en-us
summary: Configure mobile apps using OutSystems Developer Cloud (ODC) with low-code and advanced extensibility options, including syncing mobile tab settings and resolving script errors.
figma:
coverage-type:
  - evaluate
  - remember
topic:
  - customize-mobile-apps
app_type: mobile apps
platform-version: odc
audience:
  - frontend developers
  - full stack developers
  - mobile developers
  - tech leads
tags: mobile app configuration, extensibility scripts, mobile tab settings, outsystems developer cloud, mobile development
outsystems-tools:
  - mobile plugins
  - odc studio
helpids:
---
# Configuring mobile apps

OutSystems provides various ways to configure your mobile app, including low-code options and advanced extensibility configurations.

## Mobile tab settings for quick setting

To access the dialog, click the app name and then select the **Mobile** tab. The mobile properties connect to extensibility configuration, so once you configure a property in the **Mobile** tab, this same property changes in the extensibility configuration script. The same applies in the opposite way. If you change the script, the change also takes place in the **Mobile** tab properties.

Since these properties connect to extensibility configuration, they function correctly only if your extensibility scripts are error-free. ODC Studio shows the warning message in case of errors.

The extensibility script can have errors in specific properties. In this case, the same property in the **Mobile** tab informs you of the issue when you hover over the warning icon beside the property title. The same behavior occurs when a property uses a placeholder variable in the extensibility script.

## Extensibility configurations for advances settings

While the **Mobile** tab syncs with the underlying configuration files, advanced use cases may require editing these files directly for more complex requirements. [Extensibility configurations](extensibility-configurations-json-schema.md) offer granular control over your mobile app's build process, enabling custom adjustments.
