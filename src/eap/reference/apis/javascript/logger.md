---
tags: logging, error handling, mobile development, reactive web development, outsystems
summary: OutSystems Developer Cloud (ODC) provides logging capabilities for Mobile and Reactive Web Apps, enabling both console and server-side logging in ODC Portal.
locale: en-us
guid: bdfd5092-a26c-4029-b211-276cefce2ae0
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
  - odc portal
---
# Logger

Provides functions to log messages or errors in ODC Portal.

When offline, the log messages will be temporarily saved in local storage. When network connectivity is re-established, logs in local storage will be sent to ODC Portal.

## Summary

|Functions|Description|
|---|---|
|[error](#error)|Logs an error.|
|[log](#log)|Logs a message.|

## Functions

### error

**error(category: string, messageOrError: string \| Error, [error: Error]): void**

Logs an error message.

If both `messageOrError` and `error` arguments are supplied, message information (and stack information, if `messageOrError` is an Error object) will be concatenated using `\n` as separator before being logged.

Example 1:

```javascript
try {
  // do some synchronous operations
} catch(err) {
  $public.Logger.error("MyCategory", err);
}
```

Example 2 (error logging in asynchronous code):

```javascript
yourClientAsyncAction().then(function() {
  // do some operations that can throw an error
}).catch(function(err) {
  $public.Logger.error("MyCategory", err);
});
```

Parameters:

* **category**: string<br/>A string that allows error logs to be grouped together. This is useful when you have multiple calls to `error()` in different parts of your application.
* **messageOrError**: string \| Error<br/>Error or message to log.
* (Optional) **error**: Error<br/>Error object.

Returns: void

### log

**log(category: string, message: string): void**

Logs an informational message.

Parameters:

* **category**: string<br/>A string that allows logs to be grouped together. This is useful when you have multiple calls to `log()` in different parts of your application.
* **message**: string<br/>The message to be logged.

Returns: void
