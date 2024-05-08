---
summary: OutSystems Developer Cloud (ODC) enhances app development with reusable service actions that encapsulate complex logic for efficiency and maintainability.
tags:
locale: en-us
guid: f540d163-f3b7-41c7-a898-b9f07d3f3b89
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Service actions

Service actions are reusable code components that can be called from any app, providing an efficient way to perform specific tasks such as accessing data, sending emails, or making API calls. They promote code reuse, maintainability, and modularity in OutSystems Developer Cloud (ODC) by encapsulating complex logic or functionality. Service actions also enable integration with other apps or systems, improve performance by reducing data transfer, and can be secured using authentication and authorization mechanisms.

For example, you can use a service action to integrate with a third-party API to fetch weather data. You can create a service action to handle the API call, process the received data, and return a formatted weather report. You can then reuse the service action across multiple parts of an app. This ensures efficient development and easy maintenance in the event of changes to the API.

Benefits of using service actions include:

* Encapsulate complex logic and functionality for reuse across apps
* Facilitate maintenance and evolution of apps
* Reduce duplicate code and increase development efficiency
* Simplify creation of composite apps with existing functionality
* Enhance security by controlling access to sensitive information
* Improve performance with reduced data transfer and processing
* Operate in a loosely coupled way, without impacting the caller app's performance

## Best practices for using service actions

Follow these best practices to create efficient, maintainable, and reusable service actions in your ODC apps.

* **Keep it simple:** Focus on performing a single task, avoiding complex business logic.
* **Input and Output parameters:** Use clear and easy-to-understand input and output parameters, preferring structures over entities to avoid impacts from entity changes.
* **Error handling:** Implement robust error handling for graceful error management and informative logging.
* **Performance:** Optimize service actions to prevent slowdowns in the overall application.
* **Testability:** Design service actions with testability in mind, ensuring clear inputs and outputs.
* **Documentation:** Provide clear descriptions of the purpose, inputs, outputs, and limitations of your service actions.
