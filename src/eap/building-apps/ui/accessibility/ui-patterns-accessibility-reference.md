---
summary: ODC UI patterns and widgets that require extra configuration to meet WCAG 2.2 AA accessibility compliance.
tags:
  - Accessibility
  - Front-End
  - OutSystems UI
  - UI
  - UI Patterns
  - Widgets
locale: en-us
guid: 95cea8e4-df3b-4ed0-9251-d3fdf3825854
app_type: reactive web apps
figma:
platform-version: odc
audience:
  - Front-end developer
  - Developer
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - unblock
topic:
  - accessibility-screen-reader
isautopublish: true
---

# UI patterns accessibility

Most OutSystems UI patterns and widgets are **WCAG 2.2 AA** compliant by default. However, a few of them rely on complex interactions that assistive technologies don't always interpret correctly, so they need additional configuration to stay accessible.

## Known issues {#known-issues}

This section indicates the UI patterns and widgets that might require manual effort to be fully compliant with WCAG 2.2 AA.

### OutSystems UI patterns

The table below lists the UI patterns that might require manual effort to be fully compliant with WCAG 2.2 AA, depending on your **OutSystems UI** version. Follow the documentation link in the **UI pattern** column to see the detailed accessibility guidelines for each pattern.

Patterns not listed in this table are compliant by default since **OutSystems UI 2.24.0**.

<div class="info" markdown="1">

If you're upgrading OutSystems UI to a version that includes WCAG 2.2 AA compliance for a pattern, you must remove any manual workaround from that pattern before upgrading. Refer to the pattern documentation for specific details.

</div>

| UI pattern | WCAG 2.2 AA compliant by default? | Compliant since OutSystems UI version |
| --- | --- | --- |
| [Accordion](../patterns/content/accordion.md#accessibility) | Yes | 2.29.0 |
| [Action Sheet](../patterns/interaction/actionsheet.md#accessibility) | Yes | 2.29.0 |
| [Animated Label](../patterns/interaction/animatedlabel.md#accessibility) | No<br/> (requires manual effort) | - |
| [Badge](../patterns/numbers/badge.md#accessibility) | No<br/> (requires manual effort) | - |
| [Blank Slate](../patterns/content/blankslate.md#accessibility) | Yes | 2.29.0 |
| [Card Background](../patterns/content/cardbackground.md#accessibility) | No<br/> (requires manual effort) | - |
| [Carousel](../patterns/interaction/carousel.md#accessibility) | Yes | 2.29.0 |
| [Counter](../patterns/numbers/counter.md#accessibility) | No<br/> (requires manual effort) | - |
| [Inline SVG](../patterns/utilities/inlinesvg.md#accessibility) | Yes | 2.30.0 |
| [Lightbox](../patterns/interaction/lightboximage.md#accessibility) | No<br/> (requires manual effort) | - |
| [Master Detail](../patterns/adaptive/masterdetail.md#accessibility) | No<br/> (requires manual effort) | - |
| [Notification](../patterns/interaction/notification.md#accessibility) | No<br/> (requires manual effort) | - |
| [Progress circle](../patterns/numbers/progresscircle.md#accessibility) | No<br/> (requires manual effort) | - |
| [Range Slider Interval](../patterns/interaction/rangesliderinterval.md#accessibility) | No<br/> (requires manual effort) | - |
| [Submenu](../patterns/navigation/submenu.md#accessibility) | Yes, optional improvements recommended | 2.24.0 |
| [Tabs](../patterns/navigation/tabs.md#accessibility) | Yes | 2.29.0 |
| [Tag](../patterns/content/tag.md#accessibility) | No<br/> (requires manual effort) | - |
| [Tooltip](../patterns/content/tooltip.md#accessibility) | No<br/> (requires manual effort) | - |
| [User Avatar](../patterns/content/useravatar.md#accessibility) | Yes | 2.29.0 |
| [Wizard](../patterns/navigation/wizard.md#accessibility) | No<br/> (requires manual effort) | - |

<div class="info" markdown="1">

The following components are built on top of external libraries, thus OutSystems hasn't assessed them for WCAG 2.2 AA compliance:

* [OutSystems Data Grid](../patterns/interaction/data-grid/data-grid-overview.md)
* [OutSystems Maps](../patterns/interaction/map/intro.md)
* [OutSystems Charts](https://charts.outsystems.com/)

</div>

### Widgets

The built-in widgets listed below require manual effort to be fully compliant with WCAG 2.2 AA. Widgets not listed are compliant by default.

For the detailed accessibility guidelines, refer to the page for each widget:

* [Button](widgets/button.md#accessibility)
* [Dropdown](widgets/dropdown.md#accessibility)
* [List](widgets/list.md#accessibility)
* [Popover menu](widgets/popover-menu.md#accessibility)
* [Popup](widgets/popup.md#accessibility)
* [Switch](widgets/switch.md#accessibility)
* [Upload](widgets/upload.md#accessibility)
