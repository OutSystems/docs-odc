---
summary: Explore app development with OutSystems Developer Cloud (ODC), a scalable platform for building and deploying enterprise-grade applications.
tags: cloud-native, enterprise applications, scalability, deployment, app management
locale: en-us
guid: 6B0090D9-8EE9-479F-9251-CCB490D2EBB6
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/zohMj3VpAEA6P9J9azwqQq/Getting-started-with-ODC?node-id=3570-10
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - understand
  - apply
topic:
  - outsystems-overview
  - download-and-set-up
---

# Getting started

OutSystems Developer Cloud (ODC) is a cloud-native app development platform that provides a modular, scalable environment in which you develop and deploy your apps. With ODC you can build and deploy enterprise-grade, mission-critical apps in weeks. You can build web apps, web portals, mobile apps, and business workflows faster than with traditional development tools. You can then deploy your apps in a scalable, secure, and high-performance environment.

## Access the ODC Portal

When your company acquires ODC you'll be registered as user, this will generate an email, from which you can start using ODC. To do it, open the email and locate the link to the ODC Portal. Then click the link to go to the login page.

**ODC Portal** provides a unified experience that consolidates all your SDLC experience in one place. The ODC Portal and ODC Studio work together, making it quick to get the tools you need to develop and deploy your apps.

![Screenshot of the OutSystems Developer Cloud Portal interface showing various management options such as Apps, Delivery, Monitoring, Users & Access, Configurations, and Forge](images/apps-pl.png "ODC Portal Interface")

From the ODC Portal, you have access to:

* **Create** - use to access all your apps and libraries and workflows
* **Deliver** - use to deploy apps, view apps deployed to a specific stage, and their delivery status
* **Monitor** - use to view all logs, traces and analytics
* **Analyze** - use to check and ensure code quality and app security
* **Integrate** - use to integrate your apps with other systems
* **Manage** - use to do all your user management and API permissions management
* **Configure** - use to make all your relevant configurations
* **Forge** - use to access a repository of apps and components developed by a community of ODC developers to create your own apps.

## Create an app

From the ODC Portal, when you click **Create**, ODC gives you the option to create an app:

* With Mentor, OutSystems AI App generator, where from a prompt you can use AI to generate your app.
* Using ODC Studio, which if select, automatically opens ODC Studio and displays some choices. From it, you can select:

    * **App** to create a new Web, Tablet, or Phone app from scratch
    * **Library** to create a new library from scratch

You create apps in the ODC Portal, and then you use ODC Studio to build out your app. In ODC you deploy to a **stage**. A stage, such as Development, is a step within your continuous delivery pipeline.

You can create templates, which you can use as a starting point to develop your apps. You can use templates to define the look and feel of your apps, put in place common functionality or to manage dependencies. To learn more about templates, see [create a custom app template.](../app-architecture/reuse-templates.md)

## Preview an app

Preview your app from ODC Studio or ODC Portal. You can choose different previews, depending on the app type you are developing.

In ODC Studio, every time you publish changes you can click the preview link in the **TrueChange** tab.

In ODC Portal, go to the app details and click **View app**. Web apps run in the browser. ODC shows the preview of the mobile app in the browser as well, and lets you see how your app looks with a different screen size or orientation. To preview the mobile app on a device, to see how the app works natively on the hardware, [create a mobile package](../building-apps/mobile/creating-mobile-package.md) and install it on your device.

## Access ODC Studio

Before you can use ODC Studio, download it from the ODC Portal. You can use the link on the top-right of the ODC Portal.

Once you install ODC Studio, you are ready to create an app. When you start the **Create App** process in ODC Portal, it triggers the opening of ODC Studio. You are now ready to develop your app.

In ODC Studio you use visual programming elements to build your apps faster. ODC Studio accelerates the speed of development because you can share such things as templates, elements, and themes. You can also use drag and drop to quickly create UIs, business processes, and business logic in your apps.

Within each type of app, there are pre-built screen templates you can use to speed up development. The templates come with a user interface and logic. You can also use Forge which provides you with different apps and plugins as a starting point.

To publish your app, click **1-Click publish**. By default your app publishes to the Development stage.

## Related resources

* [ODC Overview](https://learn.outsystems.com/training/journeys/odc-overview-576) online course

* [ODC Studio Overview](https://learn.outsystems.com/training/journeys/odc-studio-overview-577) online course
