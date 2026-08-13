---
summary: How ODC converts an app's display name into a URL path, allowed characters, and how to avoid URL collisions.
tags:
  - Best Practices
guid: f56b5edb-5ca4-487c-b806-5bb849622696
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - odc portal
  - mentor web
coverage-type:
  - understand
  - apply
isautopublish: true
---

# Application naming and URLs

Each ODC app has two names. The **display name** appears in ODC Portal, ODC Studio, and the editors. The **internal name** appears in the app's URL path. ODC derives the internal name from the display name with a fixed set of rules.

This page explains those rules and how to avoid collisions between two apps on the same URL path.

## Display name and internal name

* **Display name**. You set the display name in **Create app** in ODC Portal, in ODC Studio, or in Mentor Web. All characters are allowed except the curly braces.

* **Internal name**. ODC derives the internal name from the display name and only allows letters, digits, and underscores. The internal name appears in the app's URL path.

For example, the display name "Order Management" becomes the URL path "OrderManagement".

## How ODC converts a display name

ODC applies these rules in order to produce the internal name:

1. Remove leading characters until the first letter. Leading digits and underscores are also dropped, so a display name like `123abc4` becomes `abc4` and `_abc` becomes `abc`.
1. Delete spaces, hyphens, and ampersands.
1. Replace any other unsupported character with an underscore.
1. If the result is empty, ODC uses the default value `Module`.

The last rule is the key one for non-Latin display names. If a display name has no Latin letter, every character is dropped and the internal name becomes `Module`.

## URL path collisions

Each app in a stage has a unique URL path. If two apps' display names both normalize to `Module`, the second app fails to publish with [OS-APPS-40047](../../error/bld/OS-APPS-40047.md).

## Recommended practice

To make the URL path predictable and unique:

* Include at least one Latin letter in the display name.
* If the business term uses a non-Latin script, include a Latin transliteration so the URL path stays readable and predictable.
* Avoid renaming a published app. Renaming changes the URL path, which breaks deployed mobile packages and any external references. To learn more, refer to [Considerations when changing the app name](mobile/creating-mobile-package.md#changing-app-name).

## Related

* [OS-APPS-40047: Asset URL path already in use](../../error/bld/OS-APPS-40047.md)
* [OS-ELG-MODL-05021: Invalid characters in name](../../error/elg/OS-ELG-MODL-05021.md)
* [URL discrepancy in deployment inconsistencies](../deploying-apps/deployment-inconsistencies.md#url-discrepancy)
