---
guid: 9bc78152-dbc3-45e0-9a0f-6fe25601ea69
locale: en-us
summary: This article enables developers to troubleshoot common extensibility conifguration errors
figma:
coverage-type:
  - unblock
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: troubleshooting, mobile app development, capacitor framework, cordova plugins, extensibility configuration
outsystems-tools:
  - odc studio
helpids:
---
# Troubleshooting common configuration errors

When building your mobile app, you may encounter errors related to misconfigurations. For detailed information about build errors, refer to [MABS errors](https://success.outsystems.com/support/errors/mabs_errors/).

Here are some common scenarios for extensibility configuration errors:

## Error: Using a legacy extensibility configuration with a Capacitor build

**Cause**: You're attempting to build your app using the Capacitor framework, but the Extensibility Configuration JSON in your app still uses the old, Cordova-based format.

**Recommended action**: Update your configuration to use the new Universal structure. Ensure your app-level settings are defined in the app extensibility configuration and any plugin-specific settings are defined in the library extensibility configuration of the respective library.

## Error: Plugin framework mismatch during build

**Cause**: Your app build is configured for the Capacitor framework, but it includes a plugin that is only compatible with Cordova, such as a Cordova-only plugin.
  
**Recommended actions**: Check the Forge for a version of the plugin that is compatible with your chosen framework. The Forge will use **Capacitor** and **Cordova** flags to identify plugin compatibility. If a compatible version isn't available, you may need to find an alternative plugin or migrate the existing one.

## Related resources

* [Common MABS errors](https://success.outsystems.com/support/errors/mabs_errors/)
  
* [Using extensibility configuration file](../extensibility-configurations-use-cases.md)
  
* [App extensibility configuration JSON schema](extensibility-app-reference.md)
  
* [Library (plugin) extensibility configuration JSON schema](extensibility-lib-reference.md)

