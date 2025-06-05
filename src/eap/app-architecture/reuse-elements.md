---
summary: OutSystems Developer Cloud (ODC) facilitates the sharing of reusable elements across applications, enhancing development efficiency and consistency.
tags: outsystems libraries,code reusability,app lifecycle management
locale: en-us
guid: 7e20ed99-3098-4d7c-b7fd-1a5794f8377d
app_type: mobile apps,reactive web apps
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
  - apply
  - remember
topic:
  - dependencies
helpids: 30644
---

# Reuse elements across apps

You can share public elements across your assets to accelerate development and enable consistency. When a public element is reused, it creates a **dependency** between the two assets involved: one as the **producer** and the other as the **consumer**.

Dependencies are categorized into two types: **strong** and **weak**, based on the nature of the assets involved.

* **Strong dependencies**: Strong dependencies are created when elements are shared between assets that are not deployed independently. These non-deployable assets include all types of libraries and connections. Examples of strong dependencies include:

    * Two libraries sharing elements

    * A library sharing elements with an app

* **Weak dependencies:** Weak dependencies are created between assets that are deployed independently. For example, a weak dependency occurs when:

    * One app reuses an element from another app

    * A workflow reuses an element from an app

    * An app reuses elements from a connection

For more information about dependencies, refer to [Understand strong and weak dependencies.](../building-apps/reuse/intro.md)

## Public elements { #public-elements }

To expose and share a public element for reuse, you set its **Public** property to **Yes**. However, some elements can't be shared, and in such cases, the element's **Public** property is set to **No** and can't be changed.

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
| Structures                | Yes, only if you use them as parameters in Service Actions. | Yes, only if you use them as parameters in public actions or public blocks. |
| Themes                    | No                              | Yes                                  |

In addition to the element types detailed in the table, other components can also become public for reuse:

* **Data fabric connections**: When you define or select entities and actions within a data fabric connection, they automatically become public elements. This allows you to reuse them in other assets such as Web and Mobile apps.

* **AI models**: Actions exposed by AI models can also be consumed as public elements, enabling their integration into various apps.

While you can't directly make a Server Action public within an app, you can expose it for reuse by right-clicking it and selecting **Expose as Service Action**. This action creates a Service Action that invokes the original Server Action and inherits its properties, effectively making it public.

## Validating consumers and producers in the ODC Portal 

In the ODC Portal, the asset detail page lists producers and consumers. Understanding your asset's consumers is crucial for communicating changes, such as a bug fix in a Service Action, to the development team. Similarly, it's important to know the producers from which you reuse elements for your asset's functionality.

The **Producers** tab displays the complete hierarchy of direct and indirect producers contributing to delivering your assets' functionality. When you select a producer,  the elements that the direct consumer of this producer is reusing are displayed. For each producer, the version (or revision) that is being used is also displayed.

The platform determines the versions (or revisions) being used in an asset based on the type of dependency:

* **For weak dependencies**: The revision used is the one currently deployed in the same stage where the consumer app is running.

* **For strong dependencies**: The platform uses the revision that is directly referenced by the asset itself (direct dependencies). If not directly referenced, it uses the revision in use by the closest producer in the dependency tree.

