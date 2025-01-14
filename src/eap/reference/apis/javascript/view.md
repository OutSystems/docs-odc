---
tags: view components, dom manipulation, mobile apps, reactive web apps, outsystems
summary: Explore functions for managing view components and states in OutSystems Developer Cloud (ODC) for mobile and reactive web apps.
locale: en-us
guid: 361b4c9a-3c90-4776-a311-2004d1e08660
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - remember
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - none
---
# View

Provides functions to deal with active view components and their state.

## Summary

|Functions|Description|
|---|---|
|[getCurrentScreenRootElement](#getcurrentscreenrootelement)|Returns the current screen DOM element. Used for class tweaks through DOM manipulation for animations.|
|[registerDeviceClassGetter](#registerdeviceclassgetter)|Register a function that provides a list of classes to apply to the document `body`. Expected classes to be returned are `portrait` or `landscape` — for orientation — and `phone` or `tablet` for device type. The function provided may emit other classes.|
|[render](#render)|Returns a `Promise` that will be resolved when the screen/block has been rendered with current model changes. Used to execute logic after the browser has rendered the current changes.|
|[wasCurrentViewRestoredFromCache](#wascurrentviewrestoredfromcache)|Checks if the current view state was restored from cache.|

## Functions

### getCurrentScreenRootElement

**getCurrentScreenRootElement(): Element**

Returns the current screen DOM element. Used for class tweaks through DOM manipulation for animations.

Between transitions there are two screens (the one leaving and the one entering), and this function will return the entering screen.

Example:

```javascript
// add custom class 'slide' to screen DOM element
$public.View.getCurrentScreenRootElement().classList.add("slide");
```

Returns: Element

### registerDeviceClassGetter

**registerDeviceClassGetter(getter: function): void**

Register a function that provides a list of values to apply to the document `body`'s `name` attribute.

The function is expected to return, at minimum:
- A string representing the orientation the device is in. Either `portrait` or `landscape` should be used.
- A string representing the device type. Either `phone` or `tablet` should be used.

The function provided may emit other class names in addition to the device orientation and type names.

This function will be called upon whenever certain events, such as device orientation changes. All classes returned in previous calls will be removed before applying results of new calls.

Parameters:

* **getter**: function<br/>A function that returns current orientation and device classes to apply. The function should accept no parameters, and return an array of strings. 

Returns: void

### render

**render(): Promise&lt;void&gt;**

Returns a `Promise` that will be resolved when the screen/block has been rendered with current model changes. Used to execute logic after the browser has rendered the current changes.

Returns: Promise&lt;void&gt;

`Promise` resolved when the screen/block has been rendered with current model changes.

### wasCurrentViewRestoredFromCache

**wasCurrentViewRestoredFromCache(): boolean**

Checks if the current view state was restored from cache.

Returns: boolean

Returns `true` when the current view state was restored from cache, or `false` otherwise.

