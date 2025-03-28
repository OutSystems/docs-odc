---
summary: Explore how OutSystems Developer Cloud (ODC) enhances mobile and reactive web apps through its comprehensive JavaScript API for custom user experiences.
tags: javascript api, mobile app development, reactive web apps, outsystems developer cloud, feedback handling
guid: f58513d5-9cae-419d-b7a7-81dca37bdd61
locale: en-us
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
  - odc studio
  - odc portal
---
# JavaScript extensibility

The OutSystems JavaScript extensibility allows you to call OutSystems specific actions and act upon mobile app events in your JavaScript code. For example, to show and hide feedback messages in JavaScript, or handle application upgrade/load events in a specific way.

The available API modules can be accessed through the predefined object, `$public`. This object contains references to each supported JavaScript API.

The following example shows how to call the showFeedbackMessage function of the FeedbackMessage module:

```javascript
$public.FeedbackMessage.showFeedbackMessage("Your data has been submitted.", 1);
```

## Summary

|API|Description|
|---|---|
|[ApplicationContext](applicationcontext.md)|Provides contextual information based on the screen that is being presented. Used to identify the screen, module and application that is currently running.|
|[ApplicationLifecycle](applicationlifecycle.md)|Provides information about the status of the application's lifecycle. Used to protect the app during upgrades, when local model access shouldn't be allowed, and to customize the application loading process.|
|[Device](device.md)|Provides functions to access native capabilities of the device.|
|[FeedbackMessage](feedbackmessage.md)|Displays feedback messages to the user. Used to display personalized feedback messages, specifying options like custom style and auto-close behavior.|
|[Logger](logger.md)|Provides functions to log messages or errors in ODC Portal.|
|[Navigation](navigation.md)|Provides the ability to perform normal and history navigations, and to override some navigation behaviors (e.g. back). Used to create new transition animations instead of overriding the existing ones using CSS.|
|[Validation](validation.md)|Provides functions to show validation messages on widgets and set their validation values. Used when validating widgets inside iterators, since it's not possible to do it in the usual way.|
|[View](view.md)|Provides functions to deal with active view components and their state.|
