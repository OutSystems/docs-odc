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

`Application file size is too big. Uploaded application file size must be under 100 MB.`

## Cause

In ODC apps and libraries have a limit of 100 MB.

## Impact

You can't publish apps or libraries that have more than 100 MB. 

## Recommended action

Please consider removing any unused resources, e.g. this may include Excel files you have used in the past to bootstrap some data into the application.
Consider moving static resources to a library and take advantage of library versioning, this is a typical pattern when you have Libraries that act as mobile plugins, connectors to other systems, or UI widgets that use external JavaScript libraries. It can be used in situations where reusability is not the primary driver, but instead to allow for a better separation of concerns and management of static resources.
Once the usage of resources are optimized consider reviewing your App architecture, following the best practices to isolate business agnostic code elements into libraries (reusable UI blocks, themes, integration wrappers, logic utilities, etc), revisiting the business concepts and respective bounded contexts contained in your app to identify candidates to be split into new apps.

## More info

Please check the [Building a well-architected app](https://success.outsystems.com/documentation/outsystems_developer_cloud/app_architecture/building_a_well_architected_app/) for more details on building lean apps.