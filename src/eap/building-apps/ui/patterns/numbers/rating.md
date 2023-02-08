---
tags: runtime-mobileandreactiveweb;
summary: Allows users to rate a particular item or service.
locale: en-us
guid: 31fc8803-e23e-4f60-8731-2fc03e5a51bf
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Rating

You can use the Rating UI Pattern to allow users rate, for example, products and services.

![Example of Rating pattern](<images/rating-example-ss.png>)

**How to use the Rating UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Rating`.

    The Rating widget is displayed.

    ![Rating widget](<images/rating-widget-ss.png>)

1. From the Toolbox, drag the **Rating** widget into the Main Content area of your application's screen.

    ![Drag widget onto the screen](<images/rating-dragwidget-ss.png>)

    By default, the pattern is already prepared to work as a 5-Star rating pattern. However, you can change the icons to hearts, smiles, thumbs, or any other content.

1. On the **Properties** tab, from the **RatingValue** dropdown, enter the rating number you want displayed. In this example, we enter `3`.  
    
    ![Set the Rating Value property](<images/rating-value-ss.png>)

1. You can customize the Rating's look and feel by setting any of the optional properties.

    ![Set additional properties](<images/rating-properties-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RatingValue (Decimal): Mandatory | Rating number to display.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RatingScale (Integer): Optional  | The number of items to display. The default is 5 which means the rating is from 0 to 5. If set to 1, the item behaves as a view only element and the **IsEdit** property is automatically set to False. The maximum value is 100. If the value introduced is bigger, only 100 items are displayed.                                                                                                                                                                                                                                                                                                                     |
| IsEdit (Boolean): Optional       | If True, the user can interact with the pattern. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Size (Size Identifier): Optional | The size of the rating pattern. There are 3 sizes available; small, medium, and base. Default size is Base.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional   | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
