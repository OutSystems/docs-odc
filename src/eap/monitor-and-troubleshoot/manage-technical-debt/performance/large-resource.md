---
summary: Large resources included in an app.
tags: large resources, app performance, publishing issues, mobile apps, reactive web apps
guid: e93b4d71-951f-414f-affc-61c1d39c7f48
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
  - frontend developers
  - platform administrators
outsystems-tools:
  - none
---
# Large resource

The app includes large resources. 

## Impact

When publishing to the environment, large resources in the app can slow down publishing and downloading, impacting the development team.

## Why is this happening?

Large resources increase the size of the app, slowing down publishing and downloading by requiring more time and bandwidth. 

## How to fix

Reduce the size of the resources to the minimum needed for their usage (below 150KB/500KB for Mobile/Web Applications). Consider serving the resources externally to the application. For example, have a screen to upload the resource and then store it in the file system or a Binary database table.
