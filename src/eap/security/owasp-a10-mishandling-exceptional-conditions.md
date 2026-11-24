---
guid: c30940ef-a884-41db-a232-227fff8561bf
locale: en-us
summary: ODC exception handling in OutSystems Developer Cloud (ODC) covers rollbacks, REST errors, exception handlers, logging, and timeouts.
figma:
coverage-type:
  - understand
app_type: reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Logging
  - Logic
  - OWASP
  - REST
  - Security
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# OWASP A10 mishandling of exceptional conditions in ODC

Mishandling of Exceptional Conditions covers how apps respond to errors and unexpected states. An unhandled error can leave data in an inconsistent state. It can also show internal details to users. The OWASP Top 10:2025 report adds this category at rank #10.

This article covers A10 in OutSystems Developer Cloud (ODC). It lists the error handling that applies by default, the mechanisms you set up, and the error handling that remains yours. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Error handling that ODC applies by default {#covered-by-default}

The following error handling applies to every app in cloud stages without any setup.

### Rollback of uncaught exceptions {#rollback}

ODC creates a single transaction for the OutSystems database at the start of a request. If an exception isn't caught, ODC rolls back that transaction. The rollback doesn't cover external systems. Each request to an external entity runs in its own transaction. When a service action ends, ODC commits its transaction, and you can't roll it back.

For more information, refer to [Transactions in external entities](../building-apps/data/fetch-data/transaction-external-entities.md).

### Default handler for unhandled exceptions {#global-exception-handler}

Each app has a Global Exception Handler. This action runs when an unhandled exception occurs anywhere in the app. By default, the **Global Exception Handler** property is `Common\OnException`. That's the On Exception action of the Common UI flow.

For more information, refer to [Advanced settings](../building-apps/libraries/app-lib-properties-edit.md#advanced-settings).

### Built-in error handling in exposed REST APIs {#exposed-rest-errors}

An exposed REST API method can raise an exception that you don't handle. In that case, ODC rolls back the database changes and returns the HTTP status code 500. The response body includes the error message of the exception, so the API consumer receives that message. To return a different status code and message, throw a custom error.

For more information, refer to [Built-in error handling](../integration-with-systems/exposing_rest/throw-a-custom-error-in-an-exposed-rest-api.md#built-in-error-handling).

### Platform timeouts {#platform-timeouts}

ODC limits how long some operations run. An exposed REST API method times out after 60 seconds. A call to a service action times out after 100 seconds without a response.

For more information, refer to [Platform limits](../getting-started/system-requirements.md#platform-limits).

## Error handling that you set up {#you-configure}

You handle exceptions in your logic with the following mechanisms.

### Exception handlers in actions, UI flows, and apps {#exception-handlers}

You handle exceptions at the following levels:

* An Exception Handler element in the flow of an action
* An On Exception action in a UI flow
* The Global Exception Handler of the app

When an exception occurs, the flow restarts in the first Exception Handler that handles that exception type. The Global Exception Handler doesn't cover the **OnApplicationReady** event handler, so handle errors in that action itself. In logic that a timer starts, only Exception Handler elements handle exceptions.

For more information, refer to [Exception Handling Mechanism](../building-apps/handling-exceptions/handling-mechanism.md).

### Exception types and logging {#exception-types}

Exception handlers catch the All Exceptions, User, Database, Security, and Communication exception types. If handlers exist for both a parent type and a child type, the handler for the child type runs. The **Log Error** property of an Exception Handler sets whether ODC logs the exception. ODC always logs the exceptions of integrations, whatever the **Log Error** value.

For more information, refer to [Handling exceptions](../building-apps/handling-exceptions/handle-exceptions.md).

### Error responses from consumed REST APIs {#consumed-rest-errors}

A consumed REST API can return an HTTP status code of 400 or above. In that case, ODC raises an exception, and you handle it in your logic. To change the error response before ODC raises the exception, use the **OnAfterResponse** callback.

For more information, refer to [Handling REST Errors](../integration-with-systems/consume_rest/handling-rest-errors.md).

## Error handling that remains your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, handle errors in your logic, and control the messages that users see.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about errors and security in ODC, refer to the following articles:

* [Monitoring and troubleshooting apps](../monitor-and-troubleshoot/monitor-apps.md)
* [Security of OutSystems Developer Cloud](security.md)
* [OWASP A07 authentication failures in ODC](owasp-a07-authentication-failures.md)
