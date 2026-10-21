---
guid: a0f61ed7-2583-4912-90fa-4a19278eb1f2
locale: en-us
summary: Cordova image catalog values in OutSystems Developer Cloud (ODC), with pixel sizes per iOS app icon, Android density, and splash screen identifier.
figma:
coverage-type:
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
  - Extensions
  - iOS
  - Mobile app
  - Native App
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# App icon and splash screen image catalogs

<div class="info" markdown="1">

Applies only to Cordova apps.

</div>

An image catalog sets your own image for each app icon or splash screen size of a Cordova app. Without a catalog, ODC creates the app icon images from the **Icon** in the app properties, and the splash screens from the **Primary color**. You can declare image catalogs in both the [universal extensibility configuration schema](extensibility-app-reference.md#icons) and the [Cordova-based extensibility configuration schema](../legacy-extensibility-configuration.md#icons-splashscreens).

## Image catalog items {#catalog-items}

Each item in an image catalog has two properties:

* **A property that points to the image**: `source` in the universal schema, or `resource` in the Cordova-based schema.
* **A property that identifies the image**: The value that the image is for, such as a size or a screen density. Each of the following sections names this property for both schemas.

## Image catalog requirements {#catalog-requirements}

Each image catalog must meet the following requirements:

* The catalog includes an image for every value in the matching table on this page.
* Each value matches the table exactly, including letter case.
* Each image is a PNG file.

ODC copies each image and doesn't resize or convert it. Provide each image at the width and height in pixels that the table lists.

If a catalog doesn't include every value, the build fails with error [OS-MCO-40002](https://www.outsystems.com/tk/redirect?g=fba5f221-0fdd-4b50-80d9-fd37370ce2ae). ODC also checks the catalogs of Capacitor apps. An incomplete catalog fails a Capacitor build even though Capacitor apps don't use the images.

## App icon sizes for iOS {#ios-icon-sizes}

To identify each image, use `size` in the universal schema, or `height` in the Cordova-based schema. Write each value as a string, such as `"180"`. The following table lists each value and the size of its image:

| Value | Width in pixels | Height in pixels |
| :---- | :---- | :---- |
| `20` | 20 | 20 |
| `29` | 29 | 29 |
| `40` | 40 | 40 |
| `48` | 48 | 48 |
| `50` | 50 | 50 |
| `55` | 55 | 55 |
| `57` | 57 | 57 |
| `58` | 58 | 58 |
| `60` | 60 | 60 |
| `72` | 72 | 72 |
| `76` | 76 | 76 |
| `80` | 80 | 80 |
| `87` | 87 | 87 |
| `88` | 88 | 88 |
| `100` | 100 | 100 |
| `114` | 114 | 114 |
| `120` | 120 | 120 |
| `144` | 144 | 144 |
| `152` | 152 | 152 |
| `167` | 167 | 167 |
| `172` | 172 | 172 |
| `180` | 180 | 180 |
| `196` | 196 | 196 |
| `1024` | 1024 | 1024 |

## App icon densities for Android {#android-icon-densities}

To identify each image, use `density` in both schemas. The following table lists each value and the size of its image:

| Value | Width in pixels | Height in pixels |
| :---- | :---- | :---- |
| `ldpi` | 36 | 36 |
| `mdpi` | 48 | 48 |
| `hdpi` | 72 | 72 |
| `xhdpi` | 96 | 96 |
| `xxhdpi` | 144 | 144 |
| `xxxhdpi` | 192 | 192 |

## Splash screen identifiers for iOS {#ios-splash-identifiers}

To identify each image, use `identifier` in the universal schema, or `defaultName` in the Cordova-based schema. The following table lists each value and the size of its image:

| Value | Width in pixels | Height in pixels |
| :---- | :---- | :---- |
| `Default@2x~universal~anyany` | 2732 | 2732 |
| `Default@2x~universal~comany` | 1278 | 2732 |
| `Default@2x~universal~comcom` | 1334 | 750 |
| `Default@3x~universal~anyany` | 2208 | 2208 |
| `Default@3x~universal~anycom` | 2208 | 1242 |
| `Default@3x~universal~comany` | 1242 | 2208 |
| `Default@2x~iphone~anyany` | 1334 | 1334 |
| `Default@2x~iphone~comany` | 750 | 1334 |
| `Default@2x~iphone~comcom` | 1334 | 750 |
| `Default@3x~iphone~anyany` | 2208 | 2208 |
| `Default@3x~iphone~anycom` | 2208 | 1242 |
| `Default@3x~iphone~comany` | 1242 | 2208 |
| `Default@2x~ipad~anyany` | 2732 | 2732 |
| `Default@2x~ipad~comany` | 1278 | 2732 |

## Splash screen densities for Android {#android-splash-densities}

To identify each image, use `density` in both schemas. Values that start with `land` are for landscape orientation, and values that start with `port` are for portrait orientation. The following table lists each value and the size of its image:

| Value | Width in pixels | Height in pixels |
| :---- | :---- | :---- |
| `land-ldpi` | 360 | 240 |
| `land-mdpi` | 480 | 320 |
| `land-hdpi` | 720 | 480 |
| `land-xhdpi` | 960 | 640 |
| `land-xxhdpi` | 1440 | 960 |
| `land-xxxhdpi` | 1920 | 1280 |
| `port-ldpi` | 240 | 360 |
| `port-mdpi` | 320 | 480 |
| `port-hdpi` | 480 | 720 |
| `port-xhdpi` | 640 | 960 |
| `port-xxhdpi` | 960 | 1440 |
| `port-xxxhdpi` | 1280 | 1920 |

## Related resources

The following resources provide more detail about app icons and splash screens:

* [App extensibility configuration JSON schema](extensibility-app-reference.md)
* [Cordova-based extensibility configuration JSON schema](../legacy-extensibility-configuration.md)
* [Modify the app icon](../modify-the-app-icon.md)
* [Customize the splash screen](../configure-splash-screen.md)
