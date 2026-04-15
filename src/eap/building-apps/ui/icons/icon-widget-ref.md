---
guid: d2e16ce8-4da2-431d-953e-2eb222138742
locale: en-us
summary: Reference guide for the Icon widget properties, events, and runtime properties in OutSystems Developer Cloud (ODC).
figma:
coverage-type:
  - remember
topic:
app_type: reactive web apps
platform-version: odc
audience:
  - frontend developers
tags: ui components,icon widget,phosphor icons,widget properties,user interface
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Icon widget reference

Depending on the icon library selected at the theme level, the Icon widget displays icons from either the FontAwesome or Phosphor icon libraries. Use icons to provide visual cues for actions, indicate functionality, or enhance navigation in your app’s user interface.

OutSystems uses icon fonts instead of images, ensuring crisp display at any size, faster load times, and full styling flexibility with CSS. Icon fonts also support responsive design and adapt smoothly to different screen resolutions.

## Properties

| Name | Description | Mandatory | Default value | Observations |
| ------ | ------------- | ----------- | --------------- | -------------- |
| Name | Identifies the element within the scope where it's defined, such as a screen, action, or module. | Yes | | |
| Icon | Scalable icon displayed using icon font from the Phosphor icon library. | Yes | flag | OutSystems uses icon fonts (not SVG vectors) to display icons. Browse the icon library to select from over 9,000 Phosphor icons. |
| Size | Size of the icon relative to the font-size of the first ancestor of this widget. | Yes | 2x font size | Available sizes typically include: 1x, 1.5x, 2x, 3x, and 4x font size. You can also specify custom sizes using CSS. |
| Visible | Boolean expression that determines whether the widget is displayed. | Yes | True | Set to False to hide the icon. You can use dynamic expressions to show or hide icons based on conditions. |
| Style Classes | Specifies one or more CSS classes to apply to the widget. Separate multiple values with spaces. | No | "icon" | Use custom CSS classes to override default styling, colors, or animations. |

### Attributes

| Name | Description | Mandatory | Default value | Observations |
| ------ | ------------- | ----------- | --------------- | -------------- |
| Property | Name of an HTML attribute to add to the element. | No | | You can select a property from the drop-down list or enter custom text. The platform doesn't validate property names. Duplicate properties aren't allowed. Spaces, " or ' are also not allowed. |
| Value | Value of the attribute. | No | | You can enter the value directly or use expressions. If the Value is empty, the HTML tag renders as property="property". For example, the nowrap property renders as nowrap="nowrap". |

## Events

| Name | Description | Mandatory | Observations |
| ------ | ------------- | ----------- | -------------- |
| Event | JavaScript or custom event to handle. | No | Common events include OnClick, OnMouseOver, and OnMouseOut. |
| Handler | Client action or JavaScript handler for the event. | No | Define the action that runs when the event triggers. For example, use OnClick to navigate to another screen or execute a client action. |

## Runtime properties

| Name | Description | Read Only | Type | Observations |
| ------ | ------------- | ----------- | ------ | -------------- |
| Id | Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties. | Yes | Text | Use this property to reference the icon in custom JavaScript or CSS selectors. |

## Related resources

* [Icons overview](intro.md)
* [Icon weights and styles](intro.md#icon-weights-and-styles)
* [Best practices](intro.md#best-practices)
* [Phosphor Icons library](https://phosphoricons.com/)
