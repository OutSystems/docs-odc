---
tags: ui patterns, user interface design
summary: Explore how to style and implement the Tag UI Pattern in OutSystems Developer Cloud (ODC) to enhance user interfaces with customizable tags.
locale: en-us
guid: b2b8939e-3fc0-418b-abfe-cc20d2971442
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A11638&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Tag

You can use the Tag UI Pattern to style small texts in a colored tag format. Use the Tags UI Pattern to display statuses, labels, or categories thus providing great user experience.

**How to use the Tag UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Tag`.
  
    The Tag widget is displayed.

    ![Screenshot of the Tag widget in the ODC Studio Toolbox](images/tag-1-ss.png "Tag Widget in ODC Studio Toolbox")

1. To From the Toolbox, drag the Tag widget into the Main Content area of your application's screen.

    ![Dragging the Tag widget into the main content area of the application screen](images/tag-2-ss.png "Dragging Tag Widget into Main Content Area")

1. Add your content to the placeholders. In this example, we add some text.

    ![Adding text to the placeholders in the Tag widget](images/tag-3-ss.png "Adding Text to Tag Widget")

1. On the properties tab, you can change the Tag's look and feel by setting the (optional) properties, for example, size and color.

    ![Properties tab for changing the look and feel of the Tag widget](images/tag-4-ss.png "Tag Widget Properties Tab")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color (Color Identifier): Optional | Set the Tag's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. <p>Examples <ul><li>_Blank_ - Displays the badge in the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The Tag's background is red.</li></ul></p>                                                                                                                                                                                                                                                                                        |
| Shape (Shape Identifier): Optional | Set the Tag's shape. Rounded, soft rounded, and sharp are the predefined shapes available. <p>Examples <ul><li>_Blank_ - Displays a rounded shaped Tag (default value).</li><li>_Entities.Shape.Sharp_ - Displays a square shaped Tag.</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                   |
| Size (Size Identifier): Optional   | Set the Tag's size. Small and medium are the predefined sizes available. <p>Examples <ul><li>_Entities.Size.Medium_ - Displays a medium-sized badge.</li><li>_Entities.Size.Small_ - Displays a small sized Tag.</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                                         |
| IsLight (Boolean): Optional        | Specify the Tag's background color. <p>Examples <ul><li>_Blank_ - A darker hue of the color is applied to the Tag and a lighter color to the text (default value).</li><li>_True_ - A brighter hue of the color is applied to the Tag and a darker color to the text.</li><li>_False_ - A darker hue of the color is applied to the Tag and a lighter color to the text.</li></ul></p>                                                                                                                                                                                                                                 |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
