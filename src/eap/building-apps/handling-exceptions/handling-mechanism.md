---
summary: The exception handling mechanism in OutSystems allows for handling exceptions raised in the app.
tags:
locale: en-us
guid: 7f5c109f-a887-4f50-bd5d-ead38e50ff53
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21346&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Exception Handling Mechanism

The exceptions raised in your app are handled in a flow starting with an Exception Handler element. In an action, you can have more than one Exception Handler flow to handle different types of exceptions.

An exception can be raised by OutSystems or in your logic at any point of your app. For typical UI requests, you can handle the raised exceptions by:

* Adding an Exception Handler element and its logic in your action's flow.
* Adding an On Exception action in your UI Flows.
* Let the Global Exception Handler of your app do the work. By default, Global Exception Handler property of your app is set to the On Exception action of the "Common" UI Flow.

In action flows starting in Timers you can only handle the raised exceptions by adding Exception Handler elements in your logic, otherwise, the execution flow is interrupted and the error is logged.

When an exception is raised, the current execution flow is interrupted and the flow restarts in the first Exception Handler element which handles that type of exception.

As an example, consider an Action B raising a User Exception named MyUserException. Action B is invoked by Action A, which is a screen action. When MyUserException is raised in Action B, the exception handling mechanism works as follows:

![Flow diagram illustrating the exception handling mechanism in OutSystems, showing how an exception in Action B is handled by Action A.](images/handling-mechanism.png "Exception Handling Flow Diagram")

You should have, at least, one Exception Handler in your application flow to inform and allow the end-user to continue to navigate.

<div class="info" markdown="1">

**OnApplicationReady** is a special event handler that is not covered by the Global Exception Handler. For that reason, error handling should be implemented in the action itself.

</div>

## Handling exceptions raised by integrations

When you are handling exceptions raised by an integration you are consuming (such as an action of an Extension or a method of a REST API) you won't be able to determine the type of exception. In these situations, you should handle the exception with an All Exceptions Handler. Then, you can use the **ExceptionMessage** property of the Exception Handler element to identify the exception.

For more information on handling errors in consumed REST APIs, check [Handling REST Errors](../../integration-with-systems/consume_rest/handling-rest-errors.md).
