---
tags: 
summary: Card Background groups short pieces of information and highlights them on the screen while providing additional relevance by using a background image.
locale: en-us
guid: 8460d7b9-4aa2-410b-8869-635625d64a4f
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A11449&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Card Background

You can use the Card Background UI Pattern to group small pieces of information and highlight them on the screen using a background image. The information is grouped into a small block that is easily noticeable on-screen. 

![Screenshot showing an overview of the Card Background UI Pattern in a mobile app interface](images/cardbackground-1-ss.png "Card Background UI Pattern Overview")

**How to use the Card Background UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Card Background`.

    The Card Background widget is displayed.

    ![Screenshot of the Card Background widget found in the ODC Studio Toolbox](images/cardbackground-2-ss.png "Card Background Widget in Toolbox")

1. From the Toolbox, drag the Card Background widget into the Main Content area of your application's screen.

    ![Screenshot depicting the process of dragging the Card Background widget into the Main Content area in ODC Studio](images/cardbackground-3-ss.png "Dragging Card Background Widget")

    By default, the Card Background widget contains Content and Background Image placeholders.

1. Add your content to the placeholder.

    In this example, we add text to the Content placeholder and an image to the Background Image placeholder. To do this, from the Widget Tree, select the Image, and on the **Properties** tab, from the **Image** drop-down, select the image you want to display.

    ![Screenshot showing how to add text and an image to the Card Background widget placeholders in ODC Studio](images/cardbackground-4-ss.png "Adding Content to Card Background")

1. On the **Properties** tab, you can change the look and feel of the Card Background widget, by setting the (optional) properties, for example, the background color and a minimum height for the card.

    ![Screenshot of the Properties tab in ODC Studio where properties of the Card Background widget can be customized](images/cardbackground-5-ss.png "Card Background Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color (Color Identifier): Optional | Set the background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - No background color is applied. This is the default (Entities.Color.Transparent).</li><li>_Entities.Color.Red_ - Applies a red background color to the card.</li></ul></p>                                                                                                                                                                                                                                                               |
| MinHeight (Integer): Optional      | Sets the minimum height of the card (in pixels).  <p>Examples</p><ul><li>_500_ - The Card height is 500 pixels. </li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Height (Integer): Optional         | Set the height of the Card (in pixels). By default, the content is vertically aligned. <p>Examples</p><ul><li>_Blank_ - The Card height is 300 pixels. </li><li>_500_ - The Card height is 500 pixels. </li></ul>                                                                                                                                                                                                                                                                                                                                                                                                     |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. |
