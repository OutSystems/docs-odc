---
tags:
summary: Explore validation functions for widgets in OutSystems Developer Cloud (ODC), including checking validity and setting validation statuses.
locale: en-us
guid: 27a8a508-630d-4b24-bf12-b76d41fa1a79
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
content-type:
  - reference
---

# Validation

Provides functions to show validation messages on widgets and set their validation values. This is useful when validating widgets inside iterators (e.g. inside a `For Each` node).

## Summary

|Functions|Description|
|---|---|
|[isWidgetValid](#iswidgetvalid)|Checks if a given widget is currently valid.|
|[setWidgetAsInvalid](#setwidgetasinvalid)|Sets a widget as invalid, with a given validation message.|
|[setWidgetAsValid](#setwidgetasvalid)|Sets a widget as valid.|

## Functions

### isWidgetValid

**isWidgetValid(widgetId: string): boolean**

Checks if a given widget is currently valid.

Parameters:

* **widgetId**: string<br/>The ID of the widget to check for validity. The ID of the widget corresponds to the name property on the widget in ODC.

Returns: boolean

Returns `true` if the widget identified by `widgetId` is valid.

### setWidgetAsInvalid

**setWidgetAsInvalid(widgetId: string, validationMessage: string): void**

Sets a widget as invalid, with a given validation message.

Parameters:

* **widgetId**: string<br/> The ID of the widget to mark as invalid. Widget ID identifies the widget instance at runtime and corresponds to the widget's ID Runtime Property.
* **validationMessage**: string<br/> The validation message.

Returns: void

### setWidgetAsValid

**setWidgetAsValid(widgetId: string): void**

Sets a widget as valid.

Parameters:

* **widgetId**: string<br/> The ID of the widget to mark as valid. Widget ID identifies the widget instance at runtime and corresponds to the widget's ID Runtime Property.

Returns: void

