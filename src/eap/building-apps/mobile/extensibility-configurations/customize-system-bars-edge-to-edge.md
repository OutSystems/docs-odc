---
summary: Customize system bars in mobile apps with edge-to-edge display for Android 16+ devices, covering both Cordova and Capacitor in ODC.
tags: mobile apps, system bars, edge-to-edge, android 16, cordova, capacitor, safe area insets
locale: en-us
guid: 4d346434-3ac0-50e0-82c6-03f62006b8d5
app_type: mobile apps
figma:
platform-version: odc
audience:
  - mobile developers
coverage-type:
  - apply
outsystems-tools:
  - none
---
# Customize system bars with edge-to-edge display

<div class="info" markdown="1">

Applies to mobile apps only.

</div>

Android 16 introduces mandatory edge-to-edge enforcement for all apps targeting SDK 36 and above. Edge-to-edge display extends your app content to the full screen, including areas behind the status bar and navigation bar. This document explains how to configure your ODC mobile apps to handle system bars correctly on modern Android devices.

## Understanding edge-to-edge display

Edge-to-edge display removes the traditional system bar backgrounds, making them transparent and allowing your app content to extend behind them. While this creates a modern, immersive experience, it requires careful handling to prevent content from being hidden behind system UI elements such as:

* Status bar (top of screen)
* Navigation bar or gesture area (bottom of screen)
* Camera notches and cutouts

By default, ODC mobile apps opt out of edge-to-edge to maintain backward compatibility with existing UI designs. However, you can opt in to create modern, full-screen experiences.

## What changed

To support edge-to-edge display, several CSS variables have been added.

### CSS variable changes

| Variable | Status | Description |
| --- | --- | --- |
| --safe-area-inset-top | Added | Top inset (status bar area). |
| --safe-area-inset-bottom | Added | Bottom inset (navigation bar area). |
| --safe-area-inset-left | Added | Left inset (safe area). |
| --safe-area-inset-right | Added | Right inset (safe area). |
| --status-bar-height | Deprecated | Use `--safe-area-inset-top` instead. |

## Capacitor apps

This section covers system bar customization for Capacitor-based mobile apps.

### Capacitor configuration changes

| Property | Status | Description |
| --- | --- | --- |
| systemBars.style | Added | Controls the style (icon color) of system bars. |
| StatusBarBackgroundColor | Modified | Now part of SystemBars; controls status bar background color. |
| StatusBarDefaultScrollToTop | Removed | No longer supported. |
| StatusBarStyle | Replaced | Now configured using `systemBars.style` in app configurations. |

<div class="info" markdown="1">

Capacitor apps handle edge-to-edge display automatically based on Android system requirements. The safe area insets are provided through CSS variables for both Android and iOS.

</div>

### Customizing system bars in Capacitor

To configure how your Capacitor mobile app handles system bars, follow these steps:

1. In ODC Studio, open the **home module** of your mobile app.

1. In the module tree, select the module, then in the properties panel, open the **Extensibility Configurations** editor.

1. Add the JSON configuration according to the [Capacitor configuration reference](#capacitor-reference) below. If you already have extensibility configurations, merge the new properties.

1. Publish your app and generate a new build using mobile distribution.

### Capacitor configuration reference {#capacitor-reference}

**SystemBars style**
**Type:** String  
**Default:** `default`  
**Values:** `default`, `light`, `dark`  
**Platforms:** Android and iOS  
**Configuration:** Capacitor app configuration

Sets the style of the system bars (status bar and navigation bar). The style determines the color of text and icons.

* **`default`:** System automatically determines icon colors based on the background color for optimal contrast.
* **`light`:** Light-colored icons (use with dark backgrounds).
* **`dark`:** Dark-colored icons (use with light backgrounds).

You can set a global style and override it per platform using `android` or `ios` configurations.

**StatusBarBackgroundColor**
**Type:** String (hex color)  
**Default:** App primary color  
**Format:** `#RRGGBB`  
**Platforms:** Android  
**Configuration:** Extensibility configuration

Sets the background color of the status bar. The text and icon color (light or dark) is automatically determined for optimal contrast when using `style: "default"`.

### Capacitor configuration examples

#### Custom status bar background color

To set a custom background color for the status bar use the following configuration:

```json
{
    "preferences": {
        "global": [{
            "name": "StatusBarBackgroundColor",
            "value": "#AF9200"
        }]
    }
}
```

#### Default system bar style

Set a global style that applies to all platforms:

```json
{
    "appConfigurations": {
        "systemBars": {
            "style": "light"
        }
    }
}
```

#### Platform-specific system bar style

Set a global style and override it for specific platforms:

```json
{
    "appConfigurations": {
        "systemBars": {
            "style": "light"
        },
        "android": {
            "systemBars": {
                "style": "default"
            }
        }
    }
}
```

#### Combined configuration

Combine background color (extensibility configuration) with system bar style (app configuration):

```json
{
    "preferences": {
        "global": [{
            "name": "StatusBarBackgroundColor",
            "value": "#AF9200"
        }]
    },
    "appConfigurations": {
        "systemBars": {
            "style": "default"
        }
    }
}
```

## Cordova apps

This section covers system bar customization for Cordova-based mobile apps.

### Cordova configuration changes

| Preference | Status | Description |
| --- | --- | --- |
| AndroidEdgeToEdge | Added | Cordova preference that controls whether the app uses edge-to-edge display on Android. This only effects Android 15+, as lower versions of Android don't support edge to edge mode. |
| NavigationBarBackgroundColor | Added | Controls the background color of the navigation bar. |
| StatusBarBackgroundColor | Modified | Now part of SystemBars; controls status bar color when edge-to-edge is disabled. |
| StatusBarDefaultScrollToTop | Removed | No longer supported. |
| StatusBarOverlaysWebView | Removed | Behavior now controlled by AndroidEdgeToEdge. |
| StatusBarStyle | Removed | Automatically determined based on background color. |

### Customizing system bars in Cordova

To configure how your Cordova mobile app handles system bars, follow these steps:

1. In ODC Studio, open the **home module** of your mobile app.

1. In the module tree, select the module, then in the properties panel, open the **Extensibility Configurations** editor.

1. Add the JSON configuration for `StatusBarBackgroundColor` according to the [Cordova configuration reference](#cordova-reference) below. If you already have extensibility configurations, merge the new properties.

    <div class="info" markdown="1">

    The `AndroidEdgeToEdge` preference is a Cordova build configuration setting, not an extensibility configuration. It must be configured under `appConfigurations.cordova.preferences.android` as shown in the [edge-to-edge example](#edge-to-edge-display-modern-full-screen).

    </div>

1. Publish your app and generate a new [build](../creating-mobile-package.md) using MABS.

### Cordova configuration reference {#cordova-reference}

#### AndroidEdgeToEdge

**Type:** Boolean  
**Default:** `false`  
**Platforms:** Android  
**Configuration:** Cordova build preference

Controls whether your app uses edge-to-edge display on Android devices.

* **`false` (default):** App content displays between system bars (traditional layout). The status bar has a solid background color.
* **`true`:** App content extends behind transparent system bars (modern, immersive layout). You must handle safe area insets to prevent content occlusion.

When set to `true`, use the `--safe-area-inset-*` CSS variables to prevent content from being hidden behind system UI.

**NavigationBarBackgroundColor**
**Type:** String (hex color)
**Default:** Value of `BackgroundColor` preference
**Format:** `#RRGGBB` or `#00000000`
**Platforms:** Android
**Configuration:** Extensibility configuration

The background color of the navigation bar.

* If set to `#00000000`, the navigation bar follows the device theme.
* If set to any other hex color, the navigation bar uses that color and it does not change when the device theme changes.
* If not set, it matches the color defined in the `BackgroundColor` preference, which by default is your application's primary color.

Has no effect when `AndroidEdgeToEdge` is set to `True` on Android 15+.

**StatusBarBackgroundColor**
**Type:** String (hex color)  
**Default:** Value of `BackgroundColor` preference, which is your app primary color  
**Format:** `#RRGGBB` or `#00000000`
**Platforms:** Android  
**Configuration:** Extensibility configuration
The background color of the status bar.

Operates the same way as `NavigationBarBackgroundColor`,with the addition that the status bar style (light or dark text and icons) is automatically determined based on the color for optimal contrast.

### Cordova configuration examples

#### Default behavior (opt out of edge-to-edge)

No configuration needed. By default, apps display with traditional system bar backgrounds. The `AndroidEdgeToEdge` Cordova preference defaults to `false`.

#### Custom status bar color

To set a custom background color for the status bar use the following configuration:

```json
{
    "preferences": {
        "global": [{
            "name": "StatusBarBackgroundColor",
            "value": "#AF9200"
        }]
    }
}
```

#### Custom navigation bar color

To set a custom background color for the navigation bar, use the following configuration:

```json
{
    "preferences": {
        "global": [{
            "name": "NavigationBarBackgroundColor",
            "value": "#AF9200"
        }]
    }
}
```

#### Edge-to-edge display (modern, full-screen)

To enable edge-to-edge display, configure the `AndroidEdgeToEdge` Cordova preference:

```json
{
    "appConfigurations": {
        "cordova": {
            "preferences": {
                "android": {
                    "AndroidEdgeToEdge": true
                }
            }
        }
    }
}
```

<div class="warning" markdown="1">

When using edge-to-edge display, you must handle safe area insets in your CSS to prevent content from being hidden behind system UI. Refer to [Safe area inset support](#safe-area-insets).

</div>

### Cordova JavaScript API

| API | Supported Platforms | Notes |
| --- | --- | --- |
| window.OSNavigationBar.setNavigationBarColor | Android | Sets the background color behind the navigation bar when an Android app isn't in EdgeToEdge mode |
| window.statusbar.setBackgroundColor | Android | Sets the background color behind the status bar when an Android app isn't in EdgeToEdge mode |

## Safe area inset support {#safe-area-insets}

<div class="info" markdown="1">

Applies to both Cordova and Capacitor apps.

</div>

To prevent your app content from being hidden behind system UI elements (status bar, navigation bar, camera notches), use the safe area inset CSS variables.

### Available CSS variables

```css
--safe-area-inset-top
--safe-area-inset-bottom
--safe-area-inset-left
--safe-area-inset-right
```

These variables provide the size (in pixels) of the unsafe areas on each edge of the screen.

### When are insets available?

The inset variables behave differently depending on your configuration:

**For Cordova apps:**

| Scenario | Inset Values |
| --- | --- |
| `AndroidEdgeToEdge` = `false` | All insets return `0` (webview is already positioned between system bars) |
| `AndroidEdgeToEdge` = `true` | Insets reflect actual system UI dimensions |

**For Capacitor apps:**

| Scenario | Inset Values |
| --- | --- |
| Default behavior | Insets reflect actual system UI dimensions |

### Best practices for using insets

For maximum compatibility across Android versions and WebView implementations, use the safe area inset variables with the standard environment variables as fallback:

```css
var(--safe-area-inset-top, env(safe-area-inset-top))
var(--safe-area-inset-bottom, env(safe-area-inset-bottom))
var(--safe-area-inset-left, env(safe-area-inset-left))
var(--safe-area-inset-right, env(safe-area-inset-right))
```

### Example implementation

Apply safe area insets to your layout containers:

```css
.app-header {
    padding-top: calc(var(--space-base) + var(--safe-area-inset-top, env(safe-area-inset-top)));
}

.app-content {
    padding-left: var(--safe-area-inset-left, env(safe-area-inset-left));
    padding-right: var(--safe-area-inset-right, env(safe-area-inset-right));
}

.app-footer {
    padding-bottom: calc(var(--space-base) + var(--safe-area-inset-bottom, env(safe-area-inset-bottom)));
}
```

<div class="info" markdown="1">

For best results with safe area insets, ensure your app uses the latest version of OutSystemsUI. Older versions may not fully support the new CSS variables.

</div>

## Troubleshooting

### Content hidden behind system bars

**Problem:** App content is partially hidden behind the status bar or navigation bar.

**Solution:** Apply safe area insets to your layout. Refer to [Safe area inset support](#safe-area-insets).

### Status bar color not changing

**Problem:** `StatusBarBackgroundColor` preference has no effect.

**Solutions:**

* Verify that `AndroidEdgeToEdge` is set to `false`. Status bar color only applies when edge-to-edge is disabled.
* Ensure you've generated a new build after changing the configuration.
* Check that the color format is correct: `#RRGGBB`.

### Insets are always zero

**Problem:** Safe area inset CSS variables always return `0`.

**Possible causes:**

* `AndroidEdgeToEdge` is set to `false` (expected behavior)
* Status bar is hidden
* Running on an older Android version or WebView implementation

**Solution:** Verify your configuration and test on an Android 15+ device.

## Related resources

For more information about mobile app configurations and CSS techniques, refer to the following resources:

* [Extensibility configurations reference](extensibility-app-reference.md)
  
* [MDN: CSS env() function](https://developer.mozilla.org/en-US/docs/Web/CSS/env)
