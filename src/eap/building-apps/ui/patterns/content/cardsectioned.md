---
tags: 
summary: Card Sectioned groups short pieces of information in sections and highlights them on the screen.
locale: en-us
guid: 7ac603a7-60c1-48cf-b47d-fed2ac2e544b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10663&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Card Sectioned

Groups information in a small block organized with different sections for title, image and content that can be easily noticeable in the screen.

Use the Card Sectioned pattern to group short pieces of information and highlight them on the screen.

![Overview of Card Sectioned pattern with different sections for title, image, and content.](images/cardsection-3.png "Card Sectioned Pattern Overview")

**How to use the Card Sectioned UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Card Sectioned`.

    The Card Sectioned widget is displayed.

    ![Screenshot showing the Card Sectioned widget in the ODC Studio Toolbox.](images/cardsection-1-ss.png "Card Sectioned Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Card Sectioned widget into the Main Content area of your application's screen.

    ![Process of dragging the Card Sectioned widget into the main content area of an application screen.](images/cardsection-2-ss.png "Dragging Card Sectioned Widget into Main Content Area")

    By default, the Card Sectioned widget contains an Image, Title, Content, and Footer placeholder.

1. Add your content to the placeholders.

    In this example we add an image, a title, some text, and a link.

    ![Example of adding an image, title, text, and link to the Card Sectioned widget placeholders.](images/cardsection-4-ss.png "Adding Content to Card Sectioned Widget")

1. On the **Properties** tab, you can change the look and feel of the Card Sectioned widget, for example, the orientation, and padding properties.

    ![The Properties tab of the Card Sectioned widget showing options to change orientation and padding.](images/cardsection-5-ss.png "Card Sectioned Widget Properties Tab")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UsePadding (Boolean): Optional   | If True, content has padding. This is the default. If False, the content has no padding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IsVertical (Boolean): Optional   | If True, the Card Sectioned pattern displays vertically. This is the default. If false, the pattern displays horizontally.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ImagePadding (Boolean): Optional | If True, a padding of 24px is applied to the image. This is the default. If False, no padding is applied to teh image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional   | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
