---
summary: CSS in the screen's style sheet.
tags: css, screen style sheet, mobile apps, reactive web apps, maintenance
guid: f798d7d6-0b99-40e3-aef6-fcc43ed598e0
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3635-10&t=GQOBWGLkIWVooPGi-1
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - none
---
# CSS in the screen's style sheet

CSS in the screen's style sheet.

## Impact

Having CSS spread through different screens may create maintenance issues. Also, defining CSS on mobile screens creates a flicker when navigating through different pages.

## Why is this happening?

The app has CSS specific to one screen instead of having it centralized in the app's Theme.

![A screen's style sheet editor](images/screen-style-sheet-odcs.png "Screen's style sheet")

## How to fix

Centralize CSS in the app's Theme to reduce maintenance costs. If you're only making a small change, define a specific class for it in the app’s Theme (that can then be reused) rather than adding it to a particular page and copying the same class repeatedly.
