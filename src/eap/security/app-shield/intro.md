---
summary: OutSystems Developer Cloud (ODC) enhances mobile app security through the licensed AppShield plugin, integrating with MABS for runtime protection.
tags: mobile app security, licensed plugins, build service integration, runtime protection, security hardening
locale: en-us
guid: 5b3d48c3-ddcb-461c-a05d-414fceeb1eb4
app_type: mobile apps
platform-version: odc
helpids: 30472
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3963%3A21612&mode=design&t=TyGh9pLEHaqLAxxu-1
audience:
  - mobile developers
outsystems-tools:
  - forge
  - odc studio
coverage-type:
  - understand
  - apply
  - remember
---

# Harden the protection of mobile apps with AppShield

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

**OutSystems AppShield** is a licensed plugin available from the **Forge**. **AppShield** lets you harden the protection of your native Android and iOS apps. **AppShield** integrates with the Mobile Apps Build Service (MABS version 9.0 or later), adding app protection at runtime and rest.

<div class="info" markdown="1">

To use **OutSystems AppShield**, you must have a [license](../../manage-platform-app-lifecycle/subscription-console.md). If you still need to get a license, contact the sales team.

</div>

By using **AppShield**, you can prevent:

* Code from being injected into your app.
* Users from taking screenshots of the data.
* Data from being hijacked.

When the user launches a hardened app, the app performs multiple checks. Some examples of these checks are root and repackaging detection meaning the app takes slightly more time to launch, especially when starting for the first time. The start time varies depending on multiple factors, such as device hardware and app complexity.

To ensure your app users have protection against the latest security vulnerabilities, **OutSystems** provides continuous updates to **AppShield**.

## Understanding the AppShield life cycle

Before you install and use **AppShield**, it's important to understand the release cycle and how it improves security. For example, suppose you have a mobile banking application and your app data must always be secure, but your version of **AppShield** needs to be updated. OutSystems regularly updates **AppShield** and strongly recommends always installing the latest version of **AppShield** in your environment. Then, release a new version of your app to your users.

To identify the **AppShield** plugin releases, OutSystems uses the following tags:

* Stable
* Current
* Expiring
* Discontinued

The following list describes the tags:

* **Stable and Current** - This is the active version and has up-to-date protection. OutSystems **supports** this version and highly recommends that you install and use this version.
* **Stable** - You can use this version, but the protection isn't current. OutSystems **doesn't support** this version. You can build an app, but you get a warning message when you try to build the app.
* **Stable and Expiring** - This version becomes discontinued in three months. OutSystems **doesn't support** this version, but you can build an app with it. If you use this version, a warning message displays advising you to update to the most current version before the expiration date. Once this version **discontinues**, you won't be able to build your app with it.
* **Discontinued** - This plugin version is out of date. OutSystems security mechanisms prevent you from creating a new build for your users. OutSystems **doesn't support** this version.

The following diagram shows how release versions work in **AppShield**.

![Diagram illustrating the life cycle of AppShield releases, including Stable, Current, Expiring, and Discontinued versions.](images/appshield-lifecycle.png "AppShield Release Life Cycle Diagram")

<div class="warning" markdown="1">

To keep your apps and data secure, OutSystems recommends that you always use the current version of the **AppShield** plugin. Go to the Versions tab of the plugin Forge page to get the current version.

</div>

## Prerequisites

To ensure the integrity and protection of your apps with **AppShield**, you must meet the following requirements.

* You have a license for **AppShield**.

* You're using MABS 9.0 or later. 

    For more information about the supported operating systems, see [MABS and mobile operating systems life cycles](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions).

## How to enable AppShield on your mobile apps

To protect your mobile app using the AppShield plugin, follow these steps:

1. **Install the AppShield** plugin in your environment.
    
    To download the plugin, go to [OutSystems AppShield](https://www.outsystems.com/forge/list?q=shield) in Forge, and click install.     

1. **Add the dependencies for AppShield** plugin on each mobile app you want to protect.

    ![Screenshot showing how to add AppShield plugin dependencies in a mobile app project.](images/add-dependencies-odcs.png "Adding AppShield Dependencies")

1. **Generate and distribute a new mobile package** protected with AppShield.

Note the following:

* All AppShield capabilities, except [Screen reader](protection-features-description.md#android-screen-reader), [Keylogger](protection-features-description.md#keylogger-protection), [Tapjacking](protection-features-description.md#tapjacking-protection), and [Private space](protection-features-description.md#private-space-detection) detection are enabled by default.
* If any additional configuration is needed, go to the [Configuration](#configuration) section.
* The app file size increases after hardening the security.
* MABS takes more time to create a hardened build.

<div class="info" markdown="1">

To learn more about adding mobile plugins to your app, see [Adding plugins](../../integration-with-systems/mobile-plugins/intro.md).

</div>

## Supported features

These are the features you can use with the current release of the **AppShield** plugin.

### Android

Protections that are available for Android builds.

* Root detection
* Repackaging detection
* Code obfuscation
* Code injection protection
* Debugger protection
* Emulator detection
* Key logger protection
* Screen reader detection
* Untrusted keyboard detection
* Screenshot protection
* Task hijacking protection
* Tapjacking protection
* Private space and work profile security enforcement

### iOS

Protections that are available for iOS builds.

* Jailbreak detection
* Repackaging detection
* Code injection protection
* Debugger protection
* Screen mirroring detection
* Screenshot protection

## Configuration

**AppShield** is on by default when you install the plugin. You can turn it off in one or more environments for testing purposes.

### Settings

* To turn off **AppShield** in one or more environments, edit the **DisableAppShielding** settings in **ODC Portal** for the environment. For example, turning off the plugin in the development environment lets you run the app in emulators or debug the app.

If your application still specifies the configuration on its extensibility configuration and you're using a plugin version compatible with the settings, the application configuration will take precedence over the settings. OutSystems recommends that you revise this extensibility and consider removing it.

Refer to the Configuration Reference section to know all available options.

### Extensibility Configuration (Old method)

Here is an example of the JSON for **Extensibility Configurations**. You can use different sections for iOS and Android.

```
{
    "preferences": {
        "global": [
            {
                "name": "DisableAppShielding",
                "value": "false"
            },
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "false"
            },
            {
                "name": "ExitOnURL",
                "value": "https://example.com/protectionblocker/landing-page"
            }
        ],
        "android": [
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "true"
            },
            {
                "name": "AllowScreenshot",
                "value": "false"
            },
            {
                "name": "BlockUntrustedKeyboards",
                "value": "true"
            },
            {
                "name": "BlockUntrustedScreenreaders",
                "value": "true"
            }
        ],
        "ios": [
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "true"
            },
            {
                "name": "AllowScreenshot",
                "value": "false"
            }
        ]
    }
}
```


### AppShieldObfuscationRules

Regardless of whether the AppShield version you're using has settings or not, if you need to configure your own obfuscation rules for Android, *you must use the `AppShieldObfuscationRules` as an extensibility configuration on your application*. 

### Configuration reference

These are the values available in the **AppShield** configuration JSON.

| Configuration                   | Type         | Default Value | OS           | Description                                                                                       | 
| ------------------------------- | ------------ | ------------- | ------------ | ------------------------------------------------------------------------------------------------- |
| AddTrustedKeyboardSigner        | Text         |               | Android      | If BlockUntrustedKeyboards is set to True, this option can whitelist a third-party keyboard. This option can be a string with a semicolon separated value for each keyboard that you want to add to the whitelist. |
| AddTrustedScreenReaderSigner    | Text         |               | Android      | If BlockUntrustedScreenreaders is set to True, this option can whitelist a third-party screen reader. This option can be a string with a semicolon separated value for each screen reader software that you want to add to the whitelist. |
| AllowJailbrokenRootedDevices    | Boolean      | false         | iOS, Android | If set to True, users can run the app on the jailbroken devices.                            |
| AllowPrivateSpace               | Boolean      | true          | Android      | If set to false, the application is blocked from running if the application was started from a private space or a work profile.                                      |
| AllowScreenshot                 | Boolean      | false         | iOS, Android | If set to True, users can take screenshots of the app.                                      |
| AllowTapjacking                 | Boolean      | true          | Android | If set to false, the application will detect tapjacking attempts and remove the malicious overlay entirely for apps running on Android 12 and above or block inputs to the overlay for versions below Android 12.                                       |
| ApplicationSignerCertificate    | Text(Base64) |               | iOS, Android | Adds the given certificate to the accepted signers whitelist of the final package. This option can be a string with a semicolon separated value for each certificate that you want to add to the whitelist.|
| AppShieldObfuscationRules       | Text(base64) |               | iOS, Android | Custom rules for obfuscation. See [Creating custom obfuscation rules](obfuscate-custom-rules.md). |
| BlockDeveloperMode              | Boolean      | false         | iOS, Android | If set to True, the application is blocked from running on iOS devices that have Developer Mode enabled and Android devices with Developer Options unlocked.                                           |
| BlockUntrustedKeyboards         | Boolean      | false         | Android      | If set to True, untrusted keyboards are detected and blocked.                                           |
| BlockUntrustedScreenreaders     | Boolean      | false         | Android      | If set to True, untrusted screen readers are detected and blocked.                                      |
| DisableAppShielding             | Boolean      | false         | iOS, Android | Activates or deactivates App Shield.
| ExitOnURL                       | URL value    |               | iOS, Android| If an app feature is blocked due to a configured policy of the **AppShield** plugin, the default browser opens the URL where the problem may be explained. For more information, refer to ExitOnURL. |
| RemoveQueryAllPackagesPermission | Boolean | true (false for versions below 1.5.1) | Android | If set to True, it removes the app's ability to check other installed applications. For more information, see [here](query-all-packages.md). |
| android                         | JSON value   |               | Android      | The key denoting values that apply to Android devices. |
| global                          | JSON value   |               | iOS, Android | Settings in this section apply to both Android and iOS builds.|
| ios                             | JSON value   |               | iOS          | The key denoting values that apply to iOS devices.|

## Check if app with AppShield builds successfully

To ensure that your build passes the shield phase, check your [app’s build logs](../../building-apps/mobile/creating-mobile-package.md#download-mobile-app-build-logs--download-mobile-app-build-logs).

When you trigger a build with AppShield enabled and correctly configured, MABS includes a **shield phase** while generating the app's mobile package.

The shield phase occurs after the build phase, and a message at the end of the log file lets you know if the shield phase is successful.

![Log file snippet indicating the successful completion of the AppShield shield phase during the app build process.](images/appshield-log.png "AppShield Shield Phase Log")

## Obfuscation

The limitations that are specific to the obfuscation.

* The plugin obfuscates only the supported **OutSystems** mobile plugins.
* The plugin obfuscates native Android logs in ODC Portal. You need to use an external tool to deobfuscate the logs.
* JavaScript files obfuscation isn't supported.
* Native iOS bitcode obfuscation isn't supported.
* You need to contact Support to get the mapping files.

## Whitelist signing certificates

One of the security features of **AppShield** is repackaging detection, which prevents the re-signing of the app package.
However, there are some situations where a re-signing of the application is desired and/or required (for example, the Google Play App Signing is required when uploading .aab to the Google Play Store).
For those reasons, **AppShield** allows to whitelist certificates, so that a given signature is considered safe within the repackaging security analysis.

### How to obtain the signing certificate { #obtain-the-signing-certificate }

#### For iOS

If you have the **PKCS12 file**, do the following:

1. Run the command `keytool -storetype PKCS12 -keystore <pkcs12-file> -storepass <store-pass> -alias <alias> -exportcert -rfc > certificate.pem`. You should now have a **certificate.pem** file. An alternative is to run the command `openssl pkcs12 -in <pcks12-file> -nokeys -password pass:<password> -out certificate.pem`. Depending on the certificate and the openssl version, the `-legacy` option might be required.

1. Open the **certificate.pem** file in a text editor and copy the content between **-BEGIN CERTIFICATE-** and **-END CERTIFICATE-**.

#### For Android

If you have the **Keystore file**, do the following:

1. Run the command `keytool -keystore <keystore-file> -storepass <store-pass> -alias <alias> -exportcert -rfc > certificate.pem`. You should now have a **certificate.pem** file.

1. Open the **certificate.pem** file in a text editor and copy the content between **-BEGIN CERTIFICATE-** and **-END CERTIFICATE-**.


If the signing certificate is the **App Signing Certificate** from the Google Play App Signing feature, do the following:

1. From Google Play Console download the **App Signing Certificate** available in the **App Signing** fragment.

1. Convert the **.der** file to **.pem** by running the command `openssl x509 -inform der -in deployment_cert.der -out certificate.pem`. You should now have a **certificate.pem** file.

1. Open the **certificate.pem** file in a text editor and copy the content between **-BEGIN CERTIFICATE-** and **-END CERTIFICATE-**.

### How to whitelist the signing certificate

You can whitelist signing certificates using the `ApplicationSignerCertificate` preference. The value of the preference must be the signing certificate obtained by following the steps in the [How to obtain the signing certificate](#obtain-the-signing-certificate) section.

The `ApplicationSignerCertificate` preference can be specified multiple times. Each certificates provided in the value of that preference will be whitelisted by AppShield. This means that AppShield will detect applications signed with any of those certificates as secure.

With the `ApplicationSignerCertificate` feature, the certificate of the keystore provided to MABS is also whitelisted. This means that the app retrieved from MABS can be directly installed on any device (because the application will be signed with a trusted certificate).

In the **Android and/or iOS section** of the [Extensibility Configurations JSON](../../building-apps/mobile/extensibility-configurations-json-schema.md), add the **name** with `ApplicationSignerCertificate` and the **value** with the public key. Here is an example:
```json
{
    "preferences": {
        "android": [
            {
                "name": "ApplicationSignerCertificate",
                "value": "[public-key-certificate-1];[public-key-certificate-2]"
            }
        ],
        "ios": [
            {
                "name": "ApplicationSignerCertificate",
                "value": "[public-key-certificate-3];[public-key-certificate-4];[public-key-certificate-5]"
            }
        ]
    }
}
```

After these changes steps, generate a new build of your mobile app.

## Limitations { #limitations }

**AppShield** has the following limitations:

* After MABS creates a build with the **AppShield** plugin active and signs the build, you can't sign that build again manually because the app would recognize that as a sign of tampering.
