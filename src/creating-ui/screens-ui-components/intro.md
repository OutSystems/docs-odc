---
summary:
tags:
---
# UI Overview

Before designing the UI for your application, it is important to learn about elements. This document provides an overview of the following terms:

* Screens
    * Screen Input Parameters and Local Variables
    * Empty Screens
    * Screen Templates
* Widgets
* OutSystems UI Patterns

The following image shows some available templates on the left and an empty screen on the right.

[new screen template](https//../images/new-screen-template.png)

## Screens

Screens are composed of basic building blocks and other elements to create a rich UI. A rich UI is one that is stylized and interactive. This means that your UI should be:

* Clear (uncluttered) and easy to navigate
* Targeted to your audience
* Consistent in the use of colors, buttons, links, and layouts

Screens are responsive and display differently depending on the device. You can pass data between screens and this eventually determines what displays on a screen. Input parameters also enable you to pass data between screens.

### Screen input parameters and local variables

When designing a screen, consider how and where the data comes from that you want to display. You can design your screens so users enter information into an input parameter when using the app. Or you might want to consider using variables.

**Local variables** temporarily store data and exist only in the scope of the screen in which it is defined. With a **Client variable** you can store data and then share the value of the stored data in your apps. A **Session variable** lets you store data on the server. The data in a session variable clears when users log out of the app.  

### Empty screens

As shown above, an empty screen contains a basic layout for you to add elements. To guide you in creating screens and the UI, you can use an OutSystems template as a starting point. You can use the templates  as-is or make changes to the templates to create your own. OutSystems also provides you with a style guide.You can use the style guide as-is or as a blueprint to create your own style guide.

### Screen templates

Screen templates provide you with a starting point that enables you to develop the UI and your app faster. OutSystems screen templates come with sample data so you can see how the screen displays with information. Screen templates include predefined layouts, widgets, built-in logic, and other components.

You can create your own templates by starting from a blank screen or by using an OutSystems supplied template and then make changes. One of the benefits of using custom screen templates is that it ensures your team is implementing your company standards.

## Widgets

Widgets are visual elements and basic building blocks that help you design, organize the data that displays on the UI, and accelerates building the UI. You can define widgets to react automatically to changes in data.

Widgets are easy to use. OutSystems comes with a variety of predefined widgets for you to use. From the toolbox on the left-side of the Screen Editor, you can drag widgets to the screen, and then set the properties for the widget. The available widgets vary by the type of app you are creating.

Widgets help to speed up some development tasks, because you can use:

* **Table** widgets - to display one or more records or lines of information
* **Text and Input** widgets - to take input from users
* **Button or Link** widgets - to navigate between screens or to trigger other actions
* **If** widgets - to display one or two areas on a screen based on a Boolean condition
* **Checkbox or Radio Button** widgets - to enable yes or no input options or the option for users to choose one item
* **Container** widgets - to group other widgets and apply the same style to all widgets in the container
* **Block or Web block** widgets - to create UI elements for use within an app or across apps
  
## OutSystems UI Patterns

A UI Pattern is a reusable design that provides a common way of presenting information on the screen. Using drag and drop you can quickly and easily design. UI Patterns also help to enforce design standards ensuring for example, all 2 or 3-column layouts look the same.

## Next steps

**TO DO:  Add a sentence and a link to where they should go for more content.**
