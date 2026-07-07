---
summary: "ODC custom app templates: build reusable starting points using the Template_ prefix, an icon, and description to standardize look, feel, and logic."
tags:
  - CSS
  - Mobile app
  - Templates
  - Themes
  - UI
guid: d02b8b25-ab59-493c-a950-837d5dee56db
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - apply
isautopublish: true
---

# Create a custom app template

In OutSystems Developer Cloud (ODC), a custom app template is a starting point for app development. Use templates to define the look and feel of apps, implement common functionality, and manage dependencies.

<div class="info" markdown="1">

In a multi-portfolio organization, a custom app template you create in one portfolio is available when you create an app in another portfolio.

</div>

To create a template for an app, follow these steps:

1. Create a new app and select the app type that this template applies to.

1. Name the app with the `Template_` prefix (for example, `Template_CustomerPortal`).

1. Open the app. In the app properties, set a description and an icon. The app appears as a template only when it has the `Template_` prefix, a description, and an icon.

1. Add the elements you want apps to inherit from the template, such as blocks or user permission logic.

1. Publish the app to make the template available. When you create an app, the template appears in the templates list.

Once an app is created based on a template, further changes to the template do not impact that app.

When you create an app from a template, the app inherits the template's colors, even if you select different colors in the new app. Set the primary color in the template CSS declarations.

## Example

Imagine you plan to develop a group of mobile apps for a company called BrandTwee. These apps need to follow the company's branding guidelines and include a set of screens with forms with custom validations.

To support this scenario, create a template that serves as the base of all planned apps:

1. Create a new app and select **Mobile App** as the type of app to build.

1. Enter `BrandTweeTemplates` as the app name.

1. Create the app that will be the template.

1. Insert the name `Template_BrandTwee`, where `Template_` is a required prefix to your name to set the app as a template.

1. Open the app. For it to be considered a template, it also needs a description and an icon.

1. Go to the app properties and insert a description:

    `This is the BrandTwee corporate template, which provides a set of common forms using our corporate image guidelines.`

1. Define an icon for the app.

1. Develop what you want to provide with this template, such as the form screens and their validations, and adjust the base theme to match the company's brand image.

1. Publish. Once published, it becomes available in the templates list when you create a new app.
