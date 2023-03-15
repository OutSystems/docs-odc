---
summary: Displays content in a specific set of columns, configurable per device type and orientation. 
tags: 
locale: en-us
guid: 6ae27265-f93e-465d-ae49-d98f7dedb86c
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Gallery

You can use the Gallery UI Pattern to display groups of content. This UI pattern allows users to sequentially browse images, with the notion of a beginning and an end.

## How to use the Gallery UI Pattern

1. In ODC Studio, in the Toolbox, search for `Gallery`.

    The Gallery widget is displayed.

    ![Gallery widget](<images/gallery-widget-ss.png>)

1. From the Toolbox, drag the Gallery widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/gallery-dragwidget-ss.png>)

1. Add the required content to the Gallery widget.

    By default, the Gallery widget expects a list.

    ![Gallery widget placeholders](<images/gallery-list-ss.png>)

    To use the Gallery UI Pattern with items from a database, drag a List into the Gallery widget and create your custom content.

    In this example, we delete the list and add local images to the Gallery widget.

    ![Add images to Gallery](<images/gallery-image-ss.png>)

1. On the Element tree, select the **Image** widget, and on the **Properties** tab, from the **Image** drop-down, select or import the image you want in the Gallery.

    **Note:** In this example, the image property **Type** is set to **Local** image. You can also add External and Binary Data images.

    ![Import local images](<images/gallery-localimage-ss.png>)
  
1. You can configure the Gallery's look and feel by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties, for example, the number of items you want to display on each device (see below for examples).

    ![Set optional properties](<images/gallery-properties-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app.

**4 items per row**

![4 items per row](<images/gallerymob-14-ss.png>)

**3 items per row**
    
![3 item per row](<images/gallerymob-15-ss.png>)

**2 items per row**

![2 items per row](<images/gallerymob-16-ss.png>)

**1 item per row**

![1 item per row](<images/gallerymob-17-ss.png>)

## Properties

| Property                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RowItemsDesktop (Integer): Optional  | Number of items displayed simultaneously per row on a desktop. Default value is 4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| RowItemsTablet (Integer):            | Number of items displayed simultaneously per row on a tablet. Default value is 3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RowItemsPhone (Integer):             | Number of items displayed simultaneously per row on a phone. Default value is 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ItemsGap(Space Identifier): Optional | Defines the space between the items. The predefined sizes are the following:<p><ul><li>None</li><li>Extra Small</li><li>Small</li><li>Base (default value)</li><li>Medium</li><li>Large</li><li>Extra Large</li><li>Extra Extra Large</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (text): Optional       | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI.
