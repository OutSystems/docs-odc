---
summary: Learn how to customize UI styles to create a unique look and feel to your apps.   
tags:
locale: en-us
guid: A15EFAFE-CE22-4974-B90E-CB0E18D263B1
app_type: mobile apps, web apps
---

# Customize UI styles

Users interact with your apps through the user interface (UI). As a developer, your goal is to follow UI standards defined by your organization but also to create an app that looks good and is easy to use.

In the UI, you define the structure of how your apps look when built. OutSystems provides a UI framework which is the base. On top of the framework, you apply the styles you want to customize and incorporate into your design.  

Templates and style guides help to guide you and provide consistency across all your organization's apps. Depending upon the app you create, you may want to make changes.

As you work with the UI, it's helpful to be familiar with the following tools:

* **Style editor** - use to edit the visual properties such as font color and margins
* **Style sheet editor** - use to make changes to the style sheet
* **Theme editor** - use to customize the overall style of your app

When styling your app follow your organization's guidelines to make it easier for users to learn how to use your app. As a developer, you can make changes to the look and feel by changing the:

* **Look of widgets** - A widget is a visual element that you can use to design and organize the UI. To help you get started, OutSystems comes with a variety of widgets such as a check box, a button, a table, or an input. You use the Style editor to make changes to a widget.
* **Cascading Style Sheets (CSS)** - A base CSS comes as part of the UI Framework. You can add new styles, or modify existing ones by copying them from the base CSS. You use the Style sheet editor to make changes to the CSS.  
* **Layout using a Placeholder** - A layout identifies where you want always position certain elements. You can also define a space for dynamic content using a placeholder. For example, assume users are completing a form and enter their name and address. On the following page, you would use a placeholder to display the name and address.
* **Themes** - Let you make changes to the look and feel of your app. A theme includes layouts you can use for screens, the global style sheet, the grid definition for positioning, and the size of the elements on the screen. You can add, delete, or modify any of the components that are part of the theme.
* **Responsive UI** - OutSystems provides a responsive UI which means you can build apps that work on all devices and your apps display correctly. The OutSystems UI theme comes with different rules for each type of device. Using different adaptive patterns and actions, you can define how you want your apps to respond.
* **Right-to-left (RTL) display** - Most apps display content on the screen from the left to the right. But some languages are read right to left (for example, Arabic and Hebrew). By making a few simple changes such as the locale, OutSystems patterns adjust automatically from left-to-right to right-to-left.
