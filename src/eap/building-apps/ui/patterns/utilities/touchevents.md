---
tags: ui patterns, customization, mobile development, event handling, frontend development
summary: Explore touch event customization in mobile apps using OutSystems Developer Cloud (ODC).
locale: en-us
guid: ab744c4d-12f5-4b92-aa63-0e2a91d693f0
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A22041&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Touch Events

You can use the Touch Events UI Pattern to enable touch events on a specific widget.

![Screenshot of touch events utilities in a mobile app interface](images/touch_events_utilities.png "Touch Events Utilities")

## How to create custom patterns using the Touch Events UI Pattern

You can call the **event.preventDefault()** to prevent the default action associated with each event from occurring. The touchstart and touchend events don't need this action, but touchmove requires it to stop screen scrolling when the user is moving the finger inside the element.

![Illustration of custom touch events patterns in code](images/touch_events_custom_patterns.png "Custom Touch Events Patterns")

To use the **event.preventDefault()**, use the following string of code:

`$parameters.Evt.preventDefault();`

## How to hide a header during a scroll action

You can use the Touch Events UI pattern to hide a header during a scroll action.

1. Add the **TouchEvents** pattern to the **Layout** block.

    ![Image showing how to add Touch Events pattern to the layout block](images/touch_events_layour.png "Touch Events Layout")

1. Add an **End** event.

    ![Step-by-step image of adding an End event in Touch Events UI](images/add_end_event.png "Adding an End Event")

1. Add logic.

    ![Flowchart demonstrating the logic for Touch Events](images/touch_events_logic.png "Touch Events Logic")

After following these steps and publishing the module, you can test the pattern in your app.

| Element | Code |
|---|---|
|![JavaScript code snippet for hiding a header on scroll](images/JS_hide.png "JavaScript Code to Hide Header") |  var header = document.querySelector(".header");<br/>header.classList.add("hide");<br/>header.classList.add("header-on-scroll"); |
|![JavaScript code snippet for showing a header on scroll](images/JS_show.png "JavaScript Code to Show Header") |  var header = document.querySelector(".header");<br/>header.classList.remove("hide");<br/>header.classList.remove("header-on-scroll"); |
  
**Result**

<iframe src="https://player.vimeo.com/video/991471309" width="492" height="750" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the end result of using Touch Events to hide a header during scroll.</iframe>

## Properties

|**Property** |  **Description** |
|---|---|
| WidgetId  |  This is the element that responds to the touch you configure.|

## Compatibility with other patterns

There might be conflicts with any pattern with touch events (unless the code is altered to expect this behavior).

## Samples

The following sample uses the Touch Events pattern:

![Sample image of a mobile app using Touch Events pattern](images/TouchEvents-Sample-1.png "Touch Events Sample")
