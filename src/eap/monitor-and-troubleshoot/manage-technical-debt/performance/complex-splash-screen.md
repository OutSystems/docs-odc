---
summary: Keep the splash screen simple and fast by minimizing the number of requests to the server and avoiding complex UI logic.
tags: splash screen optimization, mobile app performance, ui complexity reduction, load time improvement, user experience
guid: ee32b593-673e-4edc-a344-e2487d6285dc
locale: en-us
app_type: mobile apps
platform-version: odc
figma:
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - odc studio
  - odc portal
---
# Complex splash screen

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Keep the splash screen simple and fast by minimizing the number of requests to the server and avoiding complex UI logic.

## Impact

A complex splash screen increases the app load time. Users may see a blank screen before the screen renders.

## Why is this happening?

The splash screen has a complex UI or has heavy/lengthy operations.

## How to fix

To lessen the slash screen loading time, avoid requests to the server and complex logic. Avoid a complex UI by keeping the number of Blocks to a minimum.
