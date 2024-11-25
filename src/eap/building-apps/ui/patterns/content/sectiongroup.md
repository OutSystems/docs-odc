---
tags: ui patterns, widget implementation, application customization, ui design
summary: Explore how to implement and customize the Section Group UI Pattern in OutSystems Developer Cloud (ODC) to enhance application interfaces.
locale: en-us
guid: d179ae56-26b5-48d4-b426-85f8c4ded74e
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A11548&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
content-type:
  - procedure
  - reference
---

# Section Group

You can use the Section Group UI Pattern to keep the context of the header while scrolling through content.

**How to use the Section Group UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Section Group`.
  
    The Section Group widget is displayed.

    ![Screenshot of the Section Group widget in the ODC Studio Toolbox](images/sectiongroup-1-ss.png "Section Group Widget in ODC Studio Toolbox") 

1. To From the Toolbox, drag the **Section Group** widget into the **Main Content** area of your application's screen.

    ![Dragging the Section Group widget into the Main Content area of an application screen](images/sectiongroup-2-ss.png "Dragging Section Group Widget into Main Content Area")

    By default, the Section Group widget contains 3 Section widgets which contain Title and Content placeholders.

1. Add your content to the placeholders.

    In this example, we add a title to the Title placeholder and some text to the Content placeholder. 

    ![Example of adding a title and text to the Section Group placeholders](images/sectiongroup-3-ss.png "Adding Content to Section Group Widget Placeholders")

1. On the **Properties** tab, you can customize the Section Group's look and feel by setting any of the (optional) properties.

    ![Properties tab for customizing the Section Group Widget appearance](images/sectiongroup-4-ss.png "Section Group Properties Tab")

    **HasStickyTitles = False**

    ![Section Group with HasStickyTitles property set to False](images/sectiongroup-5-ss.png "Section Group Widget with Non-Sticky Titles")

    **HasStickyTitles = True**

    ![Section Group with HasStickyTitles property set to True, showing sticky titles](images/sectiongroup-6-ss.png "Section Group Widget with Sticky Titles")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HasStickyTitles (Boolean): Optional | If set to True, the section titles stay at the top of the page while the user scrolls through the content. If false, the section titles scroll with the content.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TopPosition (Integer): Optional     | Sets the position of the first section title. Only applicable when **HasStickyTitles** property is set to True.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ExtendedClass (Text): Optional      | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
