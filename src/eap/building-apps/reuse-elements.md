---
summary: Learn what elements can be shared across app types to achieve a solid app architecture. 
tags:
locale: en-us
guid: 7e20ed99-3098-4d7c-b7fd-1a5794f8377d
app_type: mobile apps, reactive web apps
---

# Reuse elements across apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

You can share public elements across your apps to accelerate development and enable consistency. Sharing elements creates dependencies between producer and consumer apps.

**Strong dependencies** (for example, those in which a consumer executes logic from a producer) can only exist between the following app types:
 
* Library (producer) and an app (consumer). The app can be a Web or Mobile App. You can share Client Actions and Server Actions in Libraries (producer), and use them in apps (consumer). Apps can't be a producer when sharing Client and Server Actions.

* Two libraries. Libraries can be producers or consumers.
 
**Weak dependencies** (for example, reusing a static entity) can exist between the following app types:
 
* Web Apps or Mobile Apps. Web and Mobile Apps can share Service Actions, Entities, Static Entities, and Screens.

## Libraries
 
Project Neo elevates Libraries to a top-level concept. Libraries exist at the same level as apps (Web or Mobile), and they have their own lifecycle. For example, you can make a branding change by updating the style guide in a Library.
 
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
| Roles                     | No                              | Not applicable                       |
| Screens                   | Yes                             | Not Applicable                                   |
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
 
## View app reuse in the Portal

You can view a list of apps and the stage on which they're deployed in the Project Neo Portal. When you click an app, you see the following details:

* The stage on which the app is deployed
* The app's consumers or producers
