---
summary: How to publish apps that exceed the 100 MB limit.
tags:
guid: dbeab3f4-4b7e-472d-be22-7650d42b0258
locale: en-us
platform-version: odc
app_type: mobile apps, reactive web apps
figma: 
---

# OS-APPS-40008


## Error message

Application file size too big. Uploaded application file size must be under 100 MB.

## Cause

In ODC apps and libraries have a limit of 100 MB.

## Impact

You can't publish apps or libraries that have more than 100MB. 

## Recommended action

Please check if the resources you have imported into your app or library (e.g: Excel, PDFs, Images, etc), and remove any unnecessary ones. If this does not apply, we recommend that you refactor your app into smaller parts and take advantage of using libraries.