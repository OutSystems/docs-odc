---
summary: OS-APPS-40047 in OutSystems Developer Cloud (ODC) occurs when a non-Latin app display name normalizes to Module, causing a URL path collision.
tags:
  - Deploy
  - Mobile app
  - Troubleshooting
guid: db1102e0-5ff7-4c9c-a3ee-09337fae15c6
locale: en-us
platform-version: odc
app_type: mobile apps, reactive web apps
figma:
coverage-type:
  - unblock
audience:
  - Developer
outsystems-tools:
  - odc studio
  - odc portal
  - mentor web
isautopublish: true
---

# OS-APPS-40047

## Error message

`Asset Url path already in use`

The error description has the form:

`There is already another asset using the path '<ApplicationUrlPath>', with key '<OtherApplicationKey>'.`

## Cause

ODC normalizes the app's display name to an internal name that becomes part of the app's URL path. The internal name only allows letters, digits, and underscores. When the display name contains only non-Latin characters, normalization strips every character and the internal name falls back to the default value `Module`. A second app whose display name also normalizes to `Module` collides on the URL path and fails to publish.

## Impact

The publish operation fails for the second and any later apps whose display names normalize to `Module`.

## Recommended action

Include at least one Latin letter in the app's display name so the internal name resolves to a unique value. For an existing app, rename it to a name that includes at least one Latin letter and republish.

## More info

To learn how ODC converts a display name to a URL path, refer to [Application naming and URLs](../../eap/building-apps/app-naming.md).
