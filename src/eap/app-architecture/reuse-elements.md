---
summary: OutSystems Developer Cloud (ODC) facilitates the sharing of reusable elements across applications, enhancing development efficiency and consistency.
tags:
locale: en-us
guid: 7e20ed99-3098-4d7c-b7fd-1a5794f8377d
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Reuse elements across apps

You can share public elements across your apps to accelerate development and enable consistency. Sharing elements creates dependencies between producer and consumer apps.

**Strong dependencies** (for example, those in which a consumer executes logic from a producer) can only exist between the following app types:

* Library (producer) and an app (consumer). The app can be a Web or Mobile App. You can share Client Actions and Server Actions in Libraries (producer), and use them in apps (consumer). Apps can't be a producer when sharing Client and Server Actions.

* Between two libraries. Libraries can be producers or consumers.

**Weak dependencies** (for example, reusing a static entity) can exist between the following app types:

* Web apps or Mobile apps. Web and Mobile apps can share Service Actions, Entities, and Static Entities. Web apps can share Screens with other Web apps.

## Libraries

OutSystems Developer Cloud (ODC) elevates Libraries to a top-level concept. Libraries exist at the same level as apps (Web or Mobile), and they have their own lifecycle. For example, you can make a branding change by updating the style guide in a Library.

## Public elements { #public-elements }

To expose and share a public element for reuse, you set the element's **Public** property to **Yes**. Some elements can't be shared, and in such cases, the element's **Public** property is set to **No** and can't be changed.

The following table lists elements and their possible Public property values.

| Element type    | Can elements be public in apps? | Can elements be public in libraries? |
| --------------- | ------------------------------- | ------------------------------------ |
| Blocks                    | No                              | Yes                                  |
| Client Actions            | No                              | Yes                                  |
| Entities                  | Yes                             | Not applicable                       |
| Exceptions                | No                             | No                       |
| Images                    | No                              | Yes                                  |
| Local storage Entities    | No                              | Not applicable                       |
| Processes                 | No                              | Not applicable                       |
| Resources                 | No                              | No                                   |
| Roles                     | Yes                             | Not applicable                       |
| Screens in web apps       | Yes                             | Not Applicable                       |
| Screens in mobile apps    | No                             | Not Applicable                       |
| Scripts                   | No                              | No                                   |
| Server Actions            | No                              | Yes                                  |
| Service Actions           | Yes                             | Not applicable                       |
| Static Entities           | Yes                             | Yes                                  |
| Structures                | No. However, structures become public if you use them in Service Actions as parameters. | No. However, structures become public if you use them in Server Actions as parameters. |
| Themes                    | No                              | Yes                                  |

## Expose a Server Action in an app

You can't set a Server Action as **Public** from within an app. However, to achieve the same outcome:

1. Right-click the Server Action.
2. Select **Expose as Service Action**.

This creates a Service Action that invokes the Server Action and its properties.  

## View app reuse in the ODC Portal

You can view a list of apps and the stage on which they're deployed in the ODC Portal. When you click an app, you see the following details:

* The stage on which the app is deployed
* The app's consumers or producers
