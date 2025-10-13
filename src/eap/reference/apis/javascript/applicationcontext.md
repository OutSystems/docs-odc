---
tags: applicationcontext, screen context, odc, reactive web apps, mobile apps
summary: OutSystems Developer Cloud (ODC) features ApplicationContext for contextual details on the current screen, and application.
locale: en-us
guid: d55f5702-dea5-4bc3-bf39-de884d07bffd
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - remember
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - none
---
# ApplicationContext

Provides contextual information based on the screen that is being presented. Used to identify the screen and application that is currently running.

## Summary

|Functions|Description|
|---|---|
|[getCurrentContext](#getcurrentcontext)|Gets the current context based on the screen being presented.|

## Functions

### getCurrentContext

**getCurrentContext(): object**

Gets the current context based on the screen being presented.

Example:

```javascript
var context = $public.ApplicationContext.getCurrentContext();

// Example of the returned object:
// {
//     "applicationKey": "7926523f-0206-4f9e-8203-c8f009c12f2a",
//     "applicationName": "EmployeeApp",
//     "screenKey": "9584046a-827a-4035-aedc-23dfe4bf10b5",
//     "screenName": "MainFlow.HomeScreen",
//     "isReady": true
// }
```

Returns: object

Returns an object with the following attributes:

* `applicationKey`: string<br/>A UUID that uniquely identifies your application.
* `applicationName`: string<br/>The name of your application.
* `screenKey`: string<br/>A UUID that uniquely identifies the screen that was visible when `getCurrentContext` was called.
* `screenName`: string<br/>The name of the screen that was visible when `getCurrentContext` was called.
* `isReady`: boolean<br/>`true` if the application is ready, `false` otherwise
