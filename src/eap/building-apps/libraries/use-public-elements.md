---
summary: Explore how to extend app capabilities using public elements and libraries in OutSystems Developer Cloud (ODC).
tags: application development, library management, http communication, modular architecture
locale: en-us
guid: abe6d7fc-04ae-45ed-8630-cf3e7e9b86ef
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
topic:
  - add-module-dependency
---

# Use public elements

You can use public elements to extend the capabilities of your app. Public elements are elements [shared by members of your organization](../../app-architecture/reuse-elements.md#public-elements) or packaged into libraries that come bundled with OutSystems Developer Cloud (ODC).

For example, you can use elements in the HTTP library to extend your app to handle HTTP requests and responses. The HTTP library comes bundled with ODC.

## Add public elements

To use public elements, you must first add them to your app. Navigate to the **Add public elements** icon on the top toolbar of ODC Studio or use the **Ctrl+Q** shortcut. In the selection window, you can filter by name, description, and type of element. Select the element or elements you want to add and click **Add**.

### Libraries

ODC elevates libraries to a top-level concept. Libraries exist at the same level as apps and have their own lifecycle.

You can build you own libraries, but there are many provided by OutSystems available out-of-the-box. See the [OutSystems language and elements documentation](../../reference/intro.md#libraries) for a list of currently available libraries.

You can build your own libraries in the OutSystem visual language or [using external logic](../external-logic/intro.md). To learn more about how libraries and their versioning works see the [Libraries](libraries.md#libraries-versioning) article.

When you add a public element from a provided library, it becomes available to use as an action in the **Server Actions** folder of the **Logic** tab. You can use an action in the logic flow of any server action or service action.

The public element may also be available as function in the **User Functions** folder of the expression editor. You can use a function in the logic flow in any expression of any server action or service action. You can check if an action is available as a function in the [reference documentation](../../reference/intro.md#libraries). Public elements consumed from external logic are never available as functions. To learn more about external logic, see [external logic](../external-logic/intro.md). 

The functions available in the provided libraries complement the built-in functions found in the **Built-in Functions** folder of the expression editor.
