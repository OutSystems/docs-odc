---
summary: OutSystems Developer Cloud(ODC) enables the creation of custom app templates to streamline app development with predefined functionalities and aesthetics.
tags: app development branding guidelines integration
guid: d02b8b25-ab59-493c-a950-837d5dee56db
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - procedure
---

# Create a custom app template

In OutSystems Developer Cloud(ODC), a Custom app template is a starting point for developing an app. Templates can be used to define the look and feel of apps, implement common functionality, or manage dependencies.

To create a template for an app, follow these steps:

1. Create a new app and select the type of app you want this template to be used.
1. Create an app and name it `Template_<app_name>,` where `<app_name>` is the name you wish to assign to the new template.
1. Open the app. In the app's properties, insert a description and an icon. Along with the syntax of the app name in the previous step, the app must have a description and an icon to be considered a template.
1. Add to your app the developments you want to provide to the apps based on the template, like blocks or user permission logic.
1. Publish to make the template available. Next time you create an app, this app appears as a template in the templates list.

Once an app is created based on a template, further changes to the template do not impact that app.

When a new app is created based on a template, it inherits the template's colors, even if different colors are chosen in the new app. You can set the primary color via the  CSS declarations in your template.

## Example

Imagine you plan to develop a group of mobile apps for a company called BrandTwee. These applications need to follow the company's branding guidelines and contain a set of screens with forms with custom validations.

To help with that task, we will create a template to be the base of all planned applications:

1. Create a new application, and select Mobile App as the type of app to build.

1. Write down the name `BrandTweeTemplates` as the app's name.

1. Create the app that will be the template.

1. Insert the name `Template_BrandTwee`, where `Template_` is a required prefix to your name to set the app as a template.

1. Open the app. Along with a name, for it to be considered a template it also needs a description and an icon.

1. Go to the app properties and insert a description:

    `This is the BrandTwee corporate template, which provides a set of common forms using our corporate image guidelines.`

1. Define an icon for the app.
1. Develop what you want to provide with this template, such as the form screens and their validations, and adjust the base theme to match the company's brand image. 
1. Publish. Once published, it becomes available in the templates list when we create a new application.


