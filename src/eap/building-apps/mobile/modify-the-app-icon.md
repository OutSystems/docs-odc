---
guid: ec332b4f-d0ce-48dc-b76b-55fad72d3633
locale: en-us
summary: Replace the default icon of your OutSystems Developer Cloud (ODC) mobile app by uploading a custom icon in ODC Studio.
figma:
coverage-type:
  - apply
  - remember
topic:
  - customize-mobile-apps
app_type: mobile apps
platform-version: odc
audience:
  - Developer
  - Front-end developer
tags:
  - Android
  - Capacitor
  - Cordova
  - iOS
  - Mobile app
  - Troubleshooting
outsystems-tools:
  - odc studio
  - odc portal
isautopublish: true
---

# Modify the app icon

<div class="info" markdown="1">

Applies only to mobile apps.

</div>

The app icon identifies your app on the device home screen, in the app switcher, and in the ODC Portal. When you create a mobile app, OutSystems Developer Cloud (ODC) assigns a default icon. You can replace it with your own image to match your branding.

## Set a custom app icon

The recommended way to set a custom icon in ODC is through the app properties. You upload a single image, and ODC generates all the icon sizes and densities that Android and iOS require. This applies to both Capacitor and Cordova builds.

To replace the default icon with your own image, follow these steps:

1. Go to ODC Studio.
1. Click your app name to open the **Edit app properties** dialog.
1. On the **General** properties, select the **Details** page.
1. Next to **Icon**, select **Upload image**, then upload your icon image.  
   Ensure the image meets the [icon requirements](#icon-requirements).
1. Publish the app.
1. To make the icon available to end users, [generate a new mobile package](creating-mobile-package.md) and distribute it.

<div class="info" markdown="1">

Changing the icon requires a new build. The updated icon reaches end users only after you regenerate the mobile package and they install the new version.

</div>

## Icon requirements {#icon-requirements}

To make sure the icon renders correctly across devices, the image you upload must meet the following requirements:

* **Format**: PNG
* **File size**: 1024 * 1024 px up to 512 KB
* **Shape**: square, so ODC can scale it without distortion

For related branding settings, such as the **Primary color** refer to [Details settings](../libraries/app-lib-properties-edit.md#app-details).

## Reuse the app icon on the splash screen

You can display the app icon at the center of the splash screen. The way you configure this depends on the app type:

* For Capacitor apps, set the **Branding image** to **App icon** on the **Splash screen** page of **Edit app properties**. For detailed information, refer to [Set branding options](configure-splash-screen.md#set-branding).

## Troubleshoot icon errors

If the build fails because the platform can't parse the image you uploaded, you might see one of the following errors:

* [OS-MABS-CST-500000](https://www.outsystems.com/tk/redirect?g=71820c70-522c-475b-924f-921ef32accba): `This icon file is not supported, choose another one.`
* [OS-MCO-50014](https://www.outsystems.com/tk/redirect?g=393dcf10-53b3-4775-aab1-20c8cd907a13): `The app icon is invalid.`

Confirm that the icon meets the [icon requirements](#icon-requirements), then publish and build again.

## Related resources

The following resources provide more detail on configuring mobile apps:

* [Configure mobile apps](configuring-mobile-apps.md)
  
* [Customize the splash screen](configure-splash-screen.md)
  
* [Create mobile app package](creating-mobile-package.md)
  
* [Details settings](../libraries/app-lib-properties-edit.md#app-details)
