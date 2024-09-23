---
summary: Large images included in the app.
tags: 
guid: 81471bb9-b81b-4f7e-90de-0b2d47e54074
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# Large image

Large images are included in the app.

## Impact

Large images have different kinds of impact on an app. When large images are used on a screen, they need to be fetched from the server, increasing bandwidth usage and request processing time in the browser. On the development side, an app with large images takes longer to be saved and published, consuming additional bandwidth when uploaded or downloaded from the server.

## Why is this happening?

There are large images contained in the app, increasing bandwidth usage and processing time.

## How to fix

Reduce the size of images to the minimum needed to be correctly displayed to the user (below 150KB for mobile apps, and 500KB for web apps). Reduce the image's resolution to a maximum of 1024px. Simply setting their width/height to lower values will not reduce the bandwidth fetch of the image from the server. Consider having big images as external resources not contained inside the app itself.
