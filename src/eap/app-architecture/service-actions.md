---
summary: OutSystems Developer Cloud (ODC) enhances app development with reusable service actions that encapsulate complex logic for efficiency and maintainability.
tags: api integration, code reuse, development service action usage, performance optimization
locale: en-us
guid: f540d163-f3b7-41c7-a898-b9f07d3f3b89
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
  - evaluate
topic:
  - service-actions-when-use
---

# Service actions

Service actions are reusable code components that can be called from any app, providing an efficient way to perform specific tasks such as accessing data, sending emails, or making API calls. They promote code reuse, maintainability, and modularity in OutSystems Developer Cloud (ODC) by encapsulating complex logic or functionality. Service actions also enable integration with other apps.

For example, you can use a service action to integrate with a third-party API to fetch weather data. You can create a service action to handle the API call, process the received data, and return a formatted weather report. You can then reuse the service action across multiple parts of an app. This ensures efficient development and easy maintenance in the event of changes to the API.

Benefits of using service actions include:

* Encapsulate complex logic and functionality for reuse across apps
* Facilitate maintenance and evolution of apps
* Reduce duplicate code and increase development efficiency
* Simplify creation of composite apps with existing functionality
* Enhance security by controlling access to sensitive information
* Improve performance with reduced data transfer and processing
* Operate in a loosely coupled way, without impacting the caller app's performance

## Exposing Service Actions

In ODC, a **Service Action** is a REST based remote call to another process, but its usage is very similar to public Server Actions.

Exposing a Service Action generates a [weak dependency](../building-apps/reuse/intro.md#weak-dependencies) from the consumer to the producer app, in a **loosely-coupled** way.

Each time the implementation of an exposed Service Action changes, that change **takes immediate** effect in the consumer apps.

Service Actions mix the advantages of loosely-coupled REST API methods with the Rapid Application Delivery (RAD) capabilities of tightly-coupled Server Actions:

* Findability: When publishing an app with a Service Action, the Service Action becomes immediately available to consumers in the internal catalog of reusable elements accessible through the **Add public elements** window.
* Impact analysis: OutSystems calculates the impact of changing the signature of a Service Action and shows it in the **Add public elements** window. This helps you to decide whether you need to create a new version of your service or if the changes in your service have no impact on consumers.
* Strong typing: Just like Server Actions, Service Actions are strongly typed logic elements. You can use entities and structures in Service Action signatures.
* Security: Service Actions are only accessible from the same environment. OutSystems passes the authentication context from the client session when making the call to a Service Action (UserId and TenantId).
* Exception handling: User Exceptions and Communication Exceptions thrown by a Service Action can be caught in the consumer apps.

## Best practices for using service actions

Follow these best practices to create efficient, maintainable, and reusable service actions in your ODC apps.

* **Keep it simple:** Focus on performing a single task, avoiding complex business logic.
* **Input and Output parameters:** Use clear and easy-to-understand input and output parameters, preferring structures over entities to avoid impacts from entity changes.
* **Error handling:** Implement robust error handling for graceful error management and informative logging.
* **Performance:** Optimize service actions to prevent slowdowns in the overall application.
* **Testability:** Design service actions with testability in mind, ensuring clear inputs and outputs.
* **Documentation:** Provide clear descriptions of the purpose, inputs, outputs, and limitations of your service actions.
