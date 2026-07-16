---
guid: c1e0f1f0-2355-47da-a1e3-ede416c92639
locale: en-us
summary: Apply these recommendations to protect data at rest, secure network communications, and harden ODC mobile apps against common security threats.
figma:
coverage-type:
  - evaluate
  - apply
app_type: mobile apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - Authorization
  - Best Practices
  - Mobile app
  - Plugins
  - Security
outsystems-tools:
  - odc studio
  - odc portal
  - forge
helpids:
isautopublish: true
---

# Best practices for mobile app security

Mobile apps face security threats that don't apply to web apps, or that apply differently in the mobile context. App binaries can be decompiled to reverse-engineer logic or extract embedded credentials, and repackaged with injected malicious code. Mobile devices travel with users, making physical theft a more likely risk than with a workstation. Following these recommendations closes the gaps that are specific to mobile: data left on the device, traffic intercepted in transit, and binaries exposed to reverse engineering.

## Avoid storing sensitive data on the device { #avoid-storing-sensitive-data }

A lost or compromised device can expose everything stored locally. Local entities, client variables, and app cache are not encrypted by default, so sensitive data stored on the device can be read by an attacker with physical access or by a malicious app.

### Recommendation

Keep sensitive data on the server and request it over authenticated HTTPS connections when the app needs it. Do not persist sensitive fields such as financial records, health data, or personal identifiers in local entities.

If your app requires offline functionality, identify the minimum subset of data users need to complete their tasks offline. Request only that subset from the server and exclude sensitive fields from the local copy. Apply server-side filtering when returning data to the client so the response does not include fields the offline view does not use. If sensitive fields are unavoidable in the offline dataset, refer to [Encrypt the local database for offline data](#ciphered-local-storage).

### Benefits

Keeping sensitive data on the server limits what an attacker can access from a compromised device. An attacker who reads local storage finds only non-sensitive operational data, not the records that matter to your users.

## Encrypt the local database for offline data {#ciphered-local-storage}

The local SQLite database that stores your app's local entities is not encrypted by default. If your app caches data for offline use, an attacker with physical access to the device can read that data directly from the database file.

The Ciphered Local Storage Plugin replaces the default SQLite engine with SQLCipher, which applies 256-bit AES encryption to the local database transparently. Your existing entity actions, aggregates, and local storage logic work without modification.

### Recommendation

Install the Ciphered Local Storage Plugin from Forge and add a dependency to all elements of the plugin in your application module. Once the dependency is in place, the app uses a new encrypted database that replicates the structure of the previous local database.

Adding the plugin to an app that already has data on users' devices requires a manual migration by users. Follow this sequence:

1. Publish and rebuild the app to replace the old local storage database with the encrypted one.
1. Ask users to uninstall the previous version to remove the old unencrypted database.
1. Ask users to install the new version, which references the encrypted database only.

If you cannot guarantee that all users complete this migration before using the updated app, the Ciphered Local Storage Plugin is not a viable upgrade path for an app already in production. Depending on what you need to protect, use the [Key Store plugin](#use-key-store) for specific secrets such as tokens and credentials, or explore other encryption plugins on Forge and custom encryption solutions.

The plugin affects only native builds running on a device. Testing with **Test in Browser** is unaffected.

Removing the plugin after deployment is destructive. The app fails to open the encrypted database and users lose all local data. If you need to remove the plugin, ask users to uninstall the app before installing the new version without encryption.

For more information, refer to the **Ciphered Local Storage Plugin** on Forge, which contains additional documentation on setup, limitations, and FAQs.

### Benefits

The local database is encrypted at rest with 256-bit AES. Encryption and decryption happen transparently, with no changes required to existing entity actions, aggregates, or client logic. The encryption key is stored in platform-managed secure storage: iOS Keychain on iOS and Android Keystore on Android.

## Use the Key Store plugin for small secrets {#use-key-store}

Authentication tokens, passwords, PINs, and certificates are small pieces of data that apps need to persist between sessions. Storing them in client variables or local entities leaves them unencrypted and accessible to anyone who can inspect the app's storage.

### Recommendation

Use the [Key Store plugin](../../../integration-with-systems/mobile-plugins/keystore-plugin/intro.md) to store small secrets. The plugin stores data in the iOS Keychain and the Android Keystore, both of which encrypt secrets using platform-managed keys. Secrets stored through the plugin are encrypted regardless of whether additional authentication is required to access them.

When storing secrets that protect sensitive operations, set **KeyAuthentication** to **True** in the **SetValue** action. This requires the user to authenticate with biometrics or a device passcode before the secret can be read.

For credentials that should become invalid when the device's biometrics change, such as when a new fingerprint is enrolled on a stolen device, set **InvalidateOnBiometricChange** to **True**. This prevents an attacker from enrolling their biometrics to access a stored token.

Before calling any Key Store action in a client action flow, call **CheckKeyStorePlugin** to verify the plugin is available. The plugin is unavailable in PWA distribution. **Test in Browser** is available for general testing, but Key Store client actions return an error because the plugin is unavailable in the browser.

For sensitive app settings used by server-side logic, such as API keys and connection strings, mark them as secrets in ODC Studio so their values are encrypted and never shown in plain text in the portal. Refer to [Set as secret](../../../security/set-as-secret.md).

### Benefits

Platform-level key management encrypts secrets with hardware-backed keys where supported. Requiring authentication to read high-sensitivity secrets adds a biometric or PIN gate that protects stored credentials even if the device screen lock is bypassed.

## Request only the device permissions your app uses { #minimal-permissions }

Mobile platforms require apps to declare the device capabilities they access. On iOS, the OS rejects an app that accesses a capability without a corresponding usage description. On Android, the OS prompts the user at runtime for each declared permission. Every permission you declare increases the app's attack surface and the level of trust users must grant to install it.

### Recommendation

Declare only the permissions your app actively uses. When you remove a plugin, check your app's **Extensibility Configurations** for any permissions you added manually to support that plugin, and remove them.

For each iOS permission key your app declares, such as **NSCameraUsageDescription**, **NSLocationWhenInUseUsageDescription**, or **NSFaceIDUsageDescription**, provide a clear and specific usage description that tells users exactly what the app does with that capability. Vague descriptions reduce user trust and increase the rate at which users deny the permission.

On Android, plugins add their required permissions to `AndroidManifest.xml` automatically through **Extensibility Configurations**. When you add a new plugin, review its **Extensibility Configurations** to understand which permissions it declares. If the plugin documentation doesn't list its permissions, contact the plugin author. Some plugins provide options to conditionally exclude certain permissions. For example, the [Health & Fitness Plugin](../../../integration-with-systems/mobile-plugins/health-fitness/intro.md#optional-opt-out-of-permissions-for-background-jobs-android-only) lets you opt out of permissions for background jobs on Android.

Before each store submission, review the **Extensibility Configurations** of your app and each plugin dependency in ODC Studio to confirm every declared permission corresponds to an active feature in that release.

### Benefits

Requesting only necessary permissions reduces the capabilities available to an attacker who exploits a vulnerability in your app or one of its plugins. A minimal permission list also builds user trust, as users who see a focused and justified permission request are more likely to grant it.

## Re-validate inputs on the server { #validate-server-side }

Client-side logic runs in the WebView and can be intercepted or bypassed. A malicious user who inspects network traffic can craft direct requests to your server actions and skip any checks your client-side logic performs.

### Recommendation

For any operation that reads or modifies sensitive data, validate the user's permissions in the server action before executing the operation. Use the **Check&lt;ROLENAME&gt;Role()** and **GetUserId()** functions in server-side logic to verify that the logged-in user is authorized. For guidance, refer to [Secure your app with roles](../../../user-management/secure-app-with-roles.md).

Do not expose server actions on screens that allow access to everyone. With the exception of authentication flows such as login, every screen that calls a server action should require at least one role.

Client-side validation improves the user experience by providing immediate feedback, but it is not a security control. Always apply equivalent validation in the server action that processes the input.

For apps that handle sensitive data, you have the option of configuring shorter session timeouts in ODC Portal to limit how long an inactive session remains valid, reducing the window an attacker has if a device is left unattended. Refer to [Configure user session](../../../user-management/configure-user-session.md).

### Benefits

Server-side validation ensures that a malicious client sending a crafted request cannot bypass authorization or corrupt data. Server actions run in a trusted environment outside the device and are not subject to the same tampering risks as client-side logic.

## Configure CSP for your mobile app {#configure-csp}

A Content Security Policy (CSP) restricts which scripts a WebView can run and which external sources it can load content from. ODC mobile apps use a WebView that behaves like an embedded browser, which can be vulnerable to cross-site scripting (XSS) attacks, where malicious scripts execute within your app and access sensitive data or make unauthorized requests.

CSP settings take effect only in mobile apps built with MABS 12 or later.

### Recommendation

Activate CSP for your stage in ODC Portal under **Management** > **Configure** > **Content security policy**. CSP applies at the stage level and covers all apps in that stage.

When defining the policy, follow these guidelines:

* List every external domain your app loads resources from. Include only domains your app actively uses and avoid the `*` wildcard in any directive.
* Always use explicit `https://` prefixes for all external domain values. On iOS, the WebView uses the `outsystems://` protocol internally. A domain listed without `https://` fails to match and blocks the resource on iOS. Use `https://*.amazonaws.com` rather than `*.amazonaws.com`.
* Keep `'unsafe-inline'` in `script-src` and `style-src`, and keep `'unsafe-eval'` in `script-src`. The ODC platform depends on these values, and removing them may break your app's functionality.
* Keep the total length of all directive values under 1500 characters for the stage.

When you update the CSP, each app fetches the change on its next online launch and applies it from the following one. Apps that launch offline use the policy bundled in their build as a fallback until they reconnect.

For the full list of directives and their defaults, refer to [Implement content security policy](../../../security/implement-csp.md).

### Benefits

CSP prevents unauthorized scripts from running in your app's WebView and blocks content from unauthorized external sources. If an attacker injects code into a response, CSP prevents the browser from executing it when the source is not listed in the policy.

## Implement SSL pinning to prevent man-in-the-middle attacks { #ssl-pinning }

HTTPS encrypts network traffic between the device and the server. However, an attacker on the same network who installs a rogue certificate authority on the device can intercept HTTPS connections and decrypt traffic in transit. SSL pinning adds a second verification step: the app compares the server's certificate public key against a list of approved hashes bundled in the app. If the hashes do not match, the connection is blocked.

Use SSL pinning for apps that handle high-sensitivity data where network interception represents a credible risk, such as banking or insurance apps.

### Recommendation

Install the [SSL Pinning plugin](../../../integration-with-systems/mobile-plugins/ssl-pinning/intro.md) from Forge and follow the setup instructions in the plugin documentation.

When configuring certificate hashes, follow these guidelines:

* Do not pin to specific OutSystems service certificates. ODC uses AWS Certificate Manager and rotates individual certificates over time. Pin to the [Amazon root certificate hashes](https://www.amazontrust.com/repository/) instead. Root certificates rotate far less frequently than the underlying service certificates, so your pinning configuration stays valid longer.
* Include at least two hash values per host: one for the active certificate and one as a backup.

Use the **CheckCertificateForUrl** client action during app startup to detect hash mismatches before they block server action calls. If the check fails, prompt users to update the app.

### Benefits

SSL pinning ensures the app communicates only with servers whose certificates match the pre-approved hashes, blocking interception even when the attacker controls the network and its certificate authority.

## Harden high-security apps with AppShield { #appshield }

The OutSystems AppShield plugin adds runtime and build-time protections to your app binary, making reverse-engineering, repackaging, and tampering significantly harder to carry out.

AppShield requires a license. Contact the OutSystems sales team if you do not have one.

### Recommendation

Install the [AppShield plugin](../../../security/app-shield/intro.md) from Forge and add it as a dependency to each app you want to protect. AppShield is enabled by default once the dependency is added.

AppShield releases follow a lifecycle with four states: **Stable and Current**, **Stable**, **Stable and Expiring**, and **Discontinued**. Always use the **Stable and Current** version. A **Discontinued** version blocks new builds, which prevents you from shipping app updates.

Use the **DisableAppShielding** setting in ODC Portal to disable the plugin in your development environment so you can run the app in emulators and attach a debugger. Prefer Portal-level settings over **Extensibility Configurations** for AppShield options, as settings are simpler to manage per environment.

Review the optional protections in the plugin documentation and enable those that match your app's security requirements.

Set **ExitOnURL** to a page that explains to users why the app exited. This reduces confusion when a protection triggers and the app closes unexpectedly.

If you distribute your app through Google Play App Signing, whitelist the Google signing certificate using the **ApplicationSignerCertificate** preference. Without this, repackaging detection triggers on the Google-signed package and blocks the app from launching.

### Benefits

AppShield detects tampering attempts at runtime and exits the app before an attacker can observe or modify its behavior.

## Related resources

The following resources group related mobile app security topics by area.

### Data protection

These resources cover storing and protecting sensitive data on the device and in app configuration.

* [Secure your mobile app's data](../../data/secure-data-mobile.md)
* [Key Store plugin](../../../integration-with-systems/mobile-plugins/keystore-plugin/intro.md)
* [Set as secret](../../../security/set-as-secret.md)

### Network security

These resources cover securing network communications and restricting what the mobile WebView can load and execute.

* [SSL Pinning plugin](../../../integration-with-systems/mobile-plugins/ssl-pinning/intro.md)
* [Content security policy](../../../security/configure-csp.md)
* [Implement content security policy](../../../security/implement-csp.md)

### App hardening

This resource covers hardening your app binary against reverse-engineering, repackaging, and tampering.

* [Harden the protection of mobile apps with AppShield](../../../security/app-shield/intro.md)
