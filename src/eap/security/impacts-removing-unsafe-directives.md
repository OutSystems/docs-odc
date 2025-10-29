---
summary: Learn about the impacts of removing unsafe directives in reactive web apps
tags: CSP, security, unsafe-inline, unsafe-eval
guid: 6c2f1c26-58b9-46a6-ba0f-f7c432c6a4bc
locale: en-us
app_type: reactive web apps
platform-version: odc
helpids: 30702
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - understand
  - apply
---

# Impacts of removing unsafe directives

The content security policy (CSP) is a critical security feature designed to mitigate risks such as cross-site scripting (XSS) and data injection attacks. By removing the `unsafe-eval` and `unsafe-inline` directives from your CSP configuration, you can significantly enhance the security of your apps. However, this change may affect the functionality of your apps.

* **`unsafe-eval`**: Permits the use of `eval()` and similar methods for executing JavaScript code. Removing this directive prevents the execution of dynamically generated code, enhancing security.

* **`unsafe-inline`**: Permits the use of inline JavaScript and CSS. Removing this directive ensures that all scripts and styles must be loaded from external files.

This document examines the potential consequences of removing these directives and provides practical guidance on how to address them effectively.

## Impacts on OutSystems components

### [OutSystems Charts](../reference/apis/chart-intro.md)

* **Issue**: Version 1 of the Charts component may experience runtime issues.

* **Recommendation**: Update to the latest version of the Charts component.

### [OutSystems Data Grid](../building-apps/ui/patterns/interaction/data-grid/data-grid-overview.md)

* **Issue**: The **Calculated Column**  won't work.

* **Workaround**: Avoid using **Calculated Columns**.

### [OutSystems Maps](../building-apps/ui/patterns/interaction/map/intro.md)

The following table summarizes the OutSystems map and Leaflet map functionality when the unsafe CSP directives are removed.

| Feature                      | Google Maps | Leaflet Maps |
|------------------------------|-------------|--------------|
| Loads the map | No functionality lost  |Image ``'<URL>'`` doesn't load because it violates the following CSP directive: "img-src 'self' data: blob: ". |
| Map center |  No functionality lost |Not possible to view, as the map tiles are not visible. |
| Change Map Center | No functionality lost |Not possible to view, as the map tiles are not visible. |
| Marker | No functionality lost  |Marker is visible but map tiles are not. |
| Marker: change (API)| No functionality lost |Marker is visible but map tiles are not. |
| Marker: events | No events are triggered, and the elements cannot be interacted with. | Marker is visible but map tiles are not |
| Localization |Not available in version 1.7.0 | Feature not available |
| Shapes | No functionality lost |Not possible to view where as the map tiles are not visible. |
| Shapes: change (API) | No functionality lost  |Not possible to view where as the map tiles are not visible. |
| Shapes: events |No events are triggered, and the elements cannot be interacted with. | Not possible to view where as the map tiles are not visible. |
| Drawing shapes |Drawing tools appear, but it’s not possible to draw any of them in the map | Not possible to view where as the map tiles are not visible. |
| Drawing shapes: change (API) |  No functionality lost|Not possible to view shapes as the map tiles are not visible. |
| Drawing shapes: events |No event is triggered |  Not possible to view where as the map tiles are not visible. |

#### Google maps

* **Issue**: Interaction and visual issues

* **Workaround**: Change CSP rules. For more information, refer to [Google's Content Security Policy guide](https://developers.google.com/maps/documentation/javascript/content-security-policy#example).

#### Leaflet maps

* **Issue**: Leaflet map tiles not visible

* **Workaround**: Missing in the CSP configuration the following domain: ``tile.openstreetmap.org``

### Mobile UI

<div class="info" markdown="1">

Mobile UI is only available to Early Access Program (EAP) customers.

</div>

* **Issues**: Some patterns, such as **Card**, **Date Picker**, **Input OTP**, and **Text Area**, may lose some styling.

* **Workarounds**

    * **Card**: Add`'unsafe-inline'` to the `style-src` directive

    * **Date Picker**: Add `'unsafe-inline'` and `connect-src: data:` to the `style-src` directive

    * **Input OTP**: Add `'unsafe-inline'` to the `style-src` directive

    * **Text Area**: Add `'unsafe-inline'` to the `style-src` directive

Some patterns may break visually due to missing CSS. Adjust the CSP configuration as needed to restore functionality.
