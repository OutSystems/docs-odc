---
summary: CSS and HTML should be kept separate. 
tags: 
guid: 76e4d096-b330-4c9e-b94d-a23d18a9bf8d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3608-10&node-type=CANVAS&t=fthXEWMKgTfJEg1k-0
---

# Inline CSS style

CSS style is defined as an extended property of a screen element.

## Impact

CSS and HTML should be kept separate. Inline styles are inefficient, harder to maintain, and make your HTML larger.

## Why is this happening?

Inline CSS occurs when styles are directly applied to screen or web block elements through extended properties.

![Screenshot of the extended properties panel showing inline CSS styles applied to a screen element.](images/odcs-extended-properties.png "Extended Properties Panel")

## How to fix

CSS should be centrally managed in the application style guide to avoid loading a large number of CSS files. If the CSS is specific to one screen or web block, define your CSS at the screen/web block level instead of in extended properties.
