---
summary: OutSystems Developer Cloud (ODC) enhances app development with reusable service actions that encapsulate complex logic for efficiency and maintainability.
tags:
  - Architecture
  - Best Practices
  - Libraries
  - Logic
  - Performance
  - REST
  - Security
locale: en-us
guid: f540d163-f3b7-41c7-a898-b9f07d3f3b89
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Architect
  - Developer
  - Tech lead
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - evaluate
topic:
  - service-actions-when-use
isautopublish: true
---

# Service actions

Service actions are reusable code components that you call from other apps to perform tasks such as accessing data, sending emails, or making API calls. They help you reuse code, keep apps maintainable, and integrate functionality across apps in OutSystems Developer Cloud (ODC).

For example, you can use a service action to integrate with a third-party API to fetch weather data. You can create a service action to handle the API call, process the received data, and return a formatted weather report. You can then reuse the service action across multiple parts of an app. This ensures efficient development and easy maintenance in the event of changes to the API.

Benefits of using service actions include:

* Encapsulate complex logic and functionality for reuse across apps

* Facilitate maintenance and evolution of apps

* Reduce duplicate code and increase development efficiency

* Simplify creation of composite apps with existing functionality

* Enhance security by controlling access to sensitive information

* Improve performance with reduced data transfer and processing

* Operate in a loosely coupled way, without impacting the caller app's performance

## Exposing service actions

In ODC, a **service action** is a REST-based remote call to another process. It works similarly to a public server action.

Exposing a service action generates a [weak dependency](../building-apps/reuse/intro.md#weak-dependencies) from the consumer to the producer app, in a **loosely-coupled** way.

Each time the implementation of an exposed service action changes, that change takes effect immediately in the consumer apps.

In a multi-portfolio organization, service actions exposed by apps are available only within the same portfolio. To share logic across portfolios, use [libraries](../building-apps/libraries/libraries.md) or expose [REST APIs](../integration-with-systems/exposing_rest/intro.md).

Service actions mix the advantages of loosely-coupled REST API methods with the Rapid Application Delivery (RAD) capabilities of tightly-coupled Server Actions:

* Findability: When you publish an app with a service action, the service action becomes available to consumers in the internal catalog of reusable elements in the **Add public elements** window. In a multi-portfolio organization, the list includes service actions from apps only in the portfolio of the asset you're editing.

* Impact analysis: OutSystems calculates the impact of changing the signature of a service action and shows it in the **Add public elements** window. This helps you decide whether to create a new version of your service or confirm that your changes have no impact on consumers.

* Strong typing: Just like Server Actions, service actions are strongly typed logic elements. You can use entities and structures in service action signatures.

* Security: Service actions are only accessible from the same environment. OutSystems passes the authentication context from the client session when making the call to a service action (UserId and TenantId).

* Exception handling: User Exceptions and Communication Exceptions thrown by a service action can be caught in the consumer apps.

## Best practices for using service actions

Follow these best practices to create efficient, maintainable, and reusable service actions in your ODC apps.

* **Keep it simple:** Focus on performing a single task, avoiding complex business logic.

* **Input and output parameters:** Use clear and easy-to-understand input and output parameters, preferring structures over entities to avoid impacts from entity changes.

* **Error handling:** Implement robust error handling for graceful error management and informative logging.

* **Performance:** Optimize service actions to prevent slowdowns in the overall application.

* **Testability:** Design service actions with testability in mind, ensuring clear inputs and outputs.

* **Documentation:** Provide clear descriptions of the purpose, inputs, outputs, and limitations of your service actions.

* **Portfolios:** In a multi-portfolio organization, keep producer and consumer apps in the same portfolio when they share service actions. If you need to share logic across portfolios, move the shared logic into a [library](../building-apps/libraries/libraries.md) or expose it as a [REST API](../integration-with-systems/exposing_rest/intro.md).

## Related resources

For more information about reuse approaches and cross-portfolio alternatives to service actions, refer to:

* [Reuse elements across apps](reuse-elements.md)

* [Understand strong and weak dependencies](../building-apps/reuse/intro.md)

* [Expose REST APIs](../integration-with-systems/exposing_rest/intro.md)

* [Asset portfolios](../manage-platform-app-lifecycle/portfolios/portfolios-overview.md)
