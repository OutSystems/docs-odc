---
summary: CSS and HTML should be kept separate.
tags:
guid: 76e4d096-b330-4c9e-b94d-a23d18a9bf8d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3608-10&node-type=CANVAS&t=fthXEWMKgTfJEg1k-0
content-type:
  - troubleshooting
  - reference
---

# Inline CSS style

CSS style is defined as an attribute in the properties of a screen element.

## Impact

CSS and HTML should be kept separate. Inline styles are inefficient, harder to maintain, and make your HTML larger.

## Why is this happening?

Inline CSS occurs when styles are directly applied to screen or web block elements via the attributes section of an element's properties.

![Screenshot of the Attributes showing inline CSS styles applied to a screen element.](images/attributes-inline-style-odcs.png "Attributes section of an element's Properties")

## How to fix

CSS should be centrally managed in the application style guide to avoid loading a large number of CSS files. If the CSS is specific to one screen or web block, define your CSS at the screen/web block level instead of in an element's properties.

For more information, refer to the [CSS styles best practice](../../../building-apps/ui/creating-screens/best-practices-screens.md#css).
