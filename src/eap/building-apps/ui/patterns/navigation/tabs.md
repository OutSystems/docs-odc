---
tags: ui patterns, navigation patterns
summary: Learn how to implement and customize the Tabs UI Pattern in OutSystems Developer Cloud (ODC) to enhance application navigation and content organization.
locale: en-us
guid: 01e14d73-1043-4401-a2d4-0903b3068a5b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A18118&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Tabs

You can use the Tabs UI Pattern to divide content into meaningful sections. This pattern is useful when you want the user to be able to switch between sections within the same context while not having to not to navigate to different areas.

<iframe src="https://player.vimeo.com/video/977630907" width="750" height="300" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Switching between different tabs in the Tabs UI Pattern.</iframe>

## How to use the Tabs UI Pattern

1. In ODC Studio, in the Toolbox, search for `Tabs`.

    The Tabs widget is displayed.

    ![Screenshot of the Tabs widget in the ODC Studio Toolbox](images/tab-widget-ss.png "Tabs Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Tabs widget into the Main Content area of your application's screen.

    ![Process of dragging the Tabs widget into the Main Content area of an application screen](images/tab-dragwidget-ss.png "Dragging Tabs Widget to Screen")

    By default, the Tabs widget contains 3 Header Items (tab titles) and 3 Content Items (tab content). You can add or delete as many as required.

1. Add the relevant content to the Header Item and Content Item placeholders, for example, forms, images, link, and text.

    In this example, text is added.

    ![Screenshot showing the addition of text content to the Header Item and Content Item placeholders in Tabs](images/tab-content-ss.png "Adding Content to Tabs Widget")

1. On the **Properties** tab, you can customize the Tabs look and feel by setting any of the optional properties, for example, which tab is displayed as the active tab when the page is rendered and whether the tabs are displayed vertically or horizontally.  

    ![Screenshot of the Properties tab where customization options for the Tabs UI Pattern are set](images/tab-properties-ss.png "Tabs Properties Pattern Settings")

After following these steps and publishing the app, you can test the pattern in your app.

### Add styles to tabs and content

The following CSS code is an example of how to change the style of selected items in the tabs:

```css
.osui-tabs__header-item {
    background-color: #ebebeb;
}

.osui-tabs__header-item.osui-tabs--is-active {
    border-bottom: 3px solid #000;
    background-color: #ebebeb;
    color: #0097eb;
}

.osui-tabs__content {
    background-color: #ccc;
    padding: 20px;
    font-size: 18px;
    font-stretch: condensed;
}
```

## Properties

| Property                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TabsOrientation (Orientation Identifier): Optional    | Set the direction of the tabs. By default, the tabs are displayed horizontally.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| StartingTab (Integer): Optional                       | Set the index of the currently active tab. The index begins at 0.<br/>Examples<ul><li>Blank - The 1st tab is the active tab. This is the default.</li><li>1 - The 2nd tab is the active tab.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Height (Text): Optional                               | Height of the tabs container. <br/>Examples<ul><li>Auto - The tab height adjusts to the content. This is the default.</li><li>400px - The height of the tab is 400px.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| TabsVerticalPosition (Direction Identifier): Optional | Sets the position of the tabs. by default, the tabs appear on the left.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OptionalConfigs.JustifyHeaders (Boolean): Optional    | If True, the Tabs are evenly distributed in the space available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ExtendedClass (Text): Optional                        | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1" "myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |

<div class="info" markdown="1">

To ensure predictable behavior and avoid runtime issues, the Tabs component is designed to include at least one TabsHeaderItem and one TabsContentItem.

</div>

## Events

### Tabs

|Event| Description  |
|---|---|
|OnTabChange: Optional| Event triggered when switching Tabs. |

## Device and pattern compatibility

Avoid using the Tabs Pattern inside patterns with swipe events, such as the Stacked Cards or Carousel Patterns.
