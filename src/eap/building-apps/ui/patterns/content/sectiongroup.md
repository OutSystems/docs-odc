---
tags: 
summary: Use the Section Group UI Pattern to keep the context of the header while progressively viewing more content by scrolling.
locale: en-us
guid: d179ae56-26b5-48d4-b426-85f8c4ded74e
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Section Group

You can use the Section Group UI Pattern to keep the context of the header while scrolling through content.

**How to use the Section Group UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Section Group`.
  
    The Section Group widget is displayed.

    ![](<images/sectiongroup-1-ss.png>) 

1. To From the Toolbox, drag the **Section Group** widget into the **Main Content** area of your application's screen.

    ![](<images/sectiongroup-2-ss.png>)

    By default, the Section Group widget contains 3 Section widgets which contain Title and Content placeholders.

1. Add your content to the placeholders.

    In this example, we add a title to the Title placeholder and some text to the Content placeholder. 

    ![](<images/sectiongroup-3-ss.png?width=800>)

1. On the **Properties** tab, you can customize the Section Group's look and feel by setting any of the (optional) properties.

    ![](<images/sectiongroup-4-ss.png>)

    **HasStickyTitles = False**

    ![](<images/sectiongroup-5-ss.png>)

    **HasStickyTitles = True**

    ![](<images/sectiongroup-6-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HasStickyTitles (Boolean): Optional | If set to True, the section titles stay at the top of the page while the user scrolls through the content. If false, the section titles scroll with the content.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TopPosition (Integer): Optional     | Sets the position of the first section title. Only applicable when **HasStickyTitles** property is set to True.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ExtendedClass (Text): Optional      | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
