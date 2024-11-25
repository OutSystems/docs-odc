---
tags:
summary: OutSystems Developer Cloud (ODC) provides functions to display and manage feedback messages in Mobile and Reactive Web Apps.
locale: en-us
guid: b4ff7637-2425-4f5a-9d27-6c2517ad6072
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
content-type:
  - reference
---

# FeedbackMessage

Displays a customized feedback message on the current screen.

## Summary

|Function|Description|
|---|---|
|[closeFeedbackMessage](#closefeedbackmessage)|Closes the FeedbackMessage that is currently open.|
|[showFeedbackMessage](#showfeedbackmessage)|Shows a FeedbackMessage with a specified message. You can enable HTML encoding, add CSS classes, and set the behavior on click.|

## Functions

### closeFeedbackMessage

**closeFeedbackMessage(): void**

Closes the FeedbackMessage that is currently open.

Returns: void

### showFeedbackMessage

**showFeedbackMessage(message: string, messageType: FeedbackMessageType, [encodeHTML: boolean = true], [extraCssClasses: string], [closeOnClick: boolean = true], [onClick: function]): void**

Shows a FeedbackMessage with a specified message. You can enable HTML encoding, add CSS classes, and set the behavior on click.

Example:

```javascript
/**
 * Show a feedback message that:
 * - Shows the message 'Your data has been submitted'
 * - Has 'Success' message styling & behavior
 * - Encodes any HTML in the provided message (there is none here)
 * - Doesn't use any extra CSS classes
 * - Prevents feedback message's default close-on-click behavior
 */
$public.FeedbackMessage.showFeedbackMessage("Your data has been submitted.", 1, true, "", false);
```

Parameters:

* **message**: string<br/>The message to be displayed.
* **messageType**: [FeedbackMessageType](#feedbackmessagetype)<br/>Type of feedback message to show, represented by a number.
* (Optional) **encodeHTML**: boolean (default: true)<br/>When `true`, HTML characters will be printed literally in the message. When `false`, HTML characters will be interpreted as HTML.
* (Optional) **extraCssClasses**: string<br/>Whitespace-separated CSS class names to be added to the feedback message container to customize the appearance of the message.
* (Optional) **closeOnClick**: boolean (default: `true`)<br/>When `true`, the message will be closed when the user clicks on it. When `false`, the [closeFeedbackMessage](#closefeedbackmessage) API must be used to close the message.
* (Optional) **onClick**: function<br/>A function to be executed whenever the feedback message is clicked.

Returns: void

## Type aliases

### FeedbackMessageType

The type of the feedback message. There are four numeric values that correspond to different types of messages:
- 0 = Info
- 1 = Success
- 2 = Warning 
- 3 = Error

The type specified when creating the feedback message affects its CSS styling:

| Name | Numeric Value | Message Background Color |                                   Icon                                   |
|:----:|:-------------:|:------------------------:|:------------------------------------------------------------------------:|
|  0   |     Info      |           Blue           |        [Info Circle](https://fontawesome.com/v4/icon/info-circle)        |
|  1   |    Success    |          Green           |       [Check Circle](https://fontawesome.com/v4/icon/check-circle)       |
|  2   |    Warning    |          Orange          | [Warning Triangle](https://fontawesome.com/v4/icon/exclamation-triangle) |
|  3   |     Error     |           Red            |       [Error Circle](https://fontawesome.com/v4/icon/times-circle)       |

The type specified when creating the feedback message affects if it will automatically close after a set period of time:

| Name | Numeric Value | Will Auto-Close? |
|:----:|:-------------:|:----------------:|
|  0   |     Info      |       Yes        |
|  1   |    Success    |       Yes        |
|  2   |    Warning    |        No        |
|  3   |     Error     |        No        |
