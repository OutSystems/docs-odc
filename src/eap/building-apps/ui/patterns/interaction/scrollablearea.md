---
tags: 
summary: Simple scrollable Block with a placeholder for content. Ideal to display multiple elements in a single, scrollable row or column.
locale: en-us
guid: 2cb523f7-81e5-4505-949b-801853c28f34
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Scrollable Area

The Scrollable Area Pattern is a simple scrollable block with a placeholder for content. You can use this pattern to display multiple elements in a single, scrollable row or column.

**How to use the Separator UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Scrollable Area`.

    The Scrollable Area is displayed.

    ![Scrollabel Area widget](<images/scrollwidget-ss.png>)

1. From the Toolbox, drag the Scrollable Area widget into the Main Content area of your application's screen, 

    ![Drag widget to sreen](<images/scrolldrag-ss.png>)

    By default, the Scrollable Area widget contains a Content placeholder.
   
1. Add the relevant content to the Content placeholder.

    In this example, we add some images by dragging the Image widget into the Content placeholder, and on the **Properties** tab, from the **Image** dropdown, select the relevant images.

    ![Add images to Content placeholder](<images/scrollimage-ss.png>)
    
1. On the **Properties** tab, you can customize the Scrollable Area's look and feel by setting any of the optional properties, for example, the height and width of the scrollable area. 

    ![Set the optional properties](<images/scrollprop-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app.

Example result:

![Scrollable Area example](<images/scrollexample.png>)

## Properties

| **Property**                                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Orientation (Orientation Identifier): Optional     | Set the orientation to either horizontal or vertical. Note that, when the Orientation is set to vertical, a fixed height value must be added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Height (Text): Optional                            | Define the height of the scrollable area. If not defined, the height of the of the parent wrapper is used (100%).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Width (Text): Optional                             | Define the width of the scrollable area. If not defined, the width of the parent wrapper is used (100%).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ScrollbarType (ScrollbarType Identifier): Optional | Choose between different scrollbar types - Compact, Default, and None. If None is selected, the scrollbar is invisible, but you can still scroll. Horizontal scroll is not enabled with the mouse wheel but can be done with mousepad gestures.                                                                                                                                                                                                                                                                                                                                                                                         |
| ExtendedClass (Text): Optional                     | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
