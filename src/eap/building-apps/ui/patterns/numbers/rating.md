---
tags: ui components, user experience
summary: Explore how to implement and customize the Rating UI Pattern in OutSystems Developer Cloud (ODC) to enhance user interaction.
locale: en-us
guid: 31fc8803-e23e-4f60-8731-2fc03e5a51bf
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A20522&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# Rating

You can use the Rating UI Pattern to allow users rate, for example, products and services.

![Screenshot showing an example of the Rating pattern in use](images/rating-example-ss.png "Rating Pattern Example")

**How to use the Rating UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Rating`.

    The Rating widget is displayed.

    ![Screenshot of the Rating widget in the ODC Studio Toolbox](images/rating-widget-ss.png "Rating Widget in Toolbox")

1. From the Toolbox, drag the **Rating** widget into the Main Content area of your application's screen.

    ![Screenshot illustrating how to drag the Rating widget onto the application screen](images/rating-dragwidget-ss.png "Dragging Rating Widget")

    By default, the pattern is already prepared to work as a 5-Star rating pattern. However, you can change the icons to hearts, smiles, thumbs, or any other content.

1. On the **Properties** tab, from the **RatingValue** dropdown, enter the rating number you want displayed. In this example, we enter `3`.  

    ![Screenshot demonstrating setting the RatingValue property to 3](images/rating-value-ss.png "Setting Rating Value")

1. You can customize the Rating's look and feel by setting any of the optional properties.

    ![Screenshot showing the customization options for the Rating's properties](images/rating-properties-ss.png "Rating Properties Customization")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RatingValue (Decimal): Mandatory | Rating number to display.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RatingScale (Integer): Optional  | The number of items to display. The default is 5 which means the rating is from 0 to 5. If set to 1, the item behaves as a view only element and the **IsEdit** property is automatically set to False. The maximum value is 100. If the value introduced is bigger, only 100 items are displayed.                                                                                                                                                                                                                                                                                                                     |
| IsEdit (Boolean): Optional       | If True, the user can interact with the pattern. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Size (Size Identifier): Optional | The size of the rating pattern. There are 3 sizes available; small, medium, and base. Default size is Base.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional   | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
