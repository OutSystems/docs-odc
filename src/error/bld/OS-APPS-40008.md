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

Consider removing any unused resources, such as Excel files previously used to bootstrap data into the app.

Move static resources to a library to take advantage of library versioning. This approach is common when using libraries as mobile plugins, connectors, or UI widgets that rely on external JavaScript libraries. It improves the management of static resources, even when reusability is not the primary goal.

After optimizing resource usage, review your app’s architecture. Follow best practices to isolate business-agnostic code elements into libraries, such as reusable UI components, themes, integration wrappers, and logic utilities. Revisit the business concepts and bounded contexts within your app to identify opportunities for splitting them into separate apps.

## More info

Please check the [Building a well-architected app](https://success.outsystems.com/documentation/outsystems_developer_cloud/app_architecture/building_a_well_architected_app/) for more details on building lean apps.
