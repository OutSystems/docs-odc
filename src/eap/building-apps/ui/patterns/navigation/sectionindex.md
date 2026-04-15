---
tags: ui pattern, navigation, content organization, screen design, user interface
summary: OutSystems Developer Cloud (ODC) features a Section Index UI Pattern for efficient content organization and navigation within app screens.
locale: en-us
guid: 117829a3-fdcf-4557-a4dd-99661992d73d
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A17605&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# Section Index

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Section Index UI Pattern to organize the content of a screen, enabling quick navigation within the page.

![Example of a Section Index UI Pattern on a mobile app screen](images/sectionindex-example.png "Section Index Example")

**How to use the Section Index UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Section Index`.

    The Section Index widget is displayed.

    ![Screenshot showing the Section Index widget in ODC Studio Toolbox](images/sectionindex-widget-ss.png "Section Index Widget")

1. From the Toolbox, drag the Section Index widget into the Main Content area of your application's screen.

    In this example, we drag the Section Index widget into a column (ColumnsSmallLeft). By default, the Section Index widget contains 2 Section Index Items. You can add or delete as many as required. In this example, 4 Section Index Items are required.

    ![Dragging the Section Index widget into the Main Content area of an application screen](images/sectionindex-dragwidget-ss.png "Drag Widget to Screen")

1. In the Toolbox, search for and drag the Section widget onto the screen. Add as many sections as you require for your app.

    In this example, we drag 4 Section widgets (to match the number of Section Index Items) onto the screen (Column2). Each section widget contains a **Title** and **Content** placeholder.

    ![Dragging Section widgets onto the application screen to match the number of Section Index Items](images/sectionindex-section-ss.png "Drag Section to Screen")

1. Add the relevant content to Section widget's **Title** and **Content** placeholders.

    In this example, we add employee names to the **Title** placeholders, and Card Sectioned widgets with some text and images to the **Content** placeholder.

    ![Adding employee names and Card Sectioned widgets to the Section widget's Title and Content placeholders](images/sectionindex-card-ss.png "Add Content to Section Widget")

1. Enter a name for each of the Card Sectioned widgets.

    This is so you can link them to each of the Section Index Items.

    ![Entering a name for each of the Card Sectioned widgets to link with Section Index Items](images/sectionindex-cardname-ss.png "Enter Name for Card Sectioned")

1. In the Toolbox, search for and drag the Text widget into the first Section Index Item and enter a title (in this example, the employee's name).

    ![Entering a title for the first Section Index Item using the Text widget](images/sectionindex-item-ss.png "Enter a Section Index Item Title")

1. To link the Section with the Section Index Item, select the Section Index Item, and on the **Properties** tab, set the **ScrollToWidgetId** property as the Section Id. In this example,  **AmosTesen.Id**.

    ![Setting the ScrollToWidgetId property on the Properties tab to link the Section with the Section Index Item](images/sectionindex-properties-id-ss.png "Set the Section Id")

1. Repeat steps 5,6 and 7 to add content and link your sections to the remaining Section Index Items.

1. On the **Properties** tab, you can customize the Section Index's look and feel by setting any of the optional properties.

    ![Customizing the Section Index's look and feel by setting optional properties on the Properties tab](images/sectionindex-properties-ss.png "Set the Section Index pattern Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

### Section Index

| **Property** | **Description** |
| --- | --- |
| SmoothScrolling (Boolean): Optional | If True, navigation to the destination is animated. If False, the navigation is instant. The default value is True. |
| IsFixed (Text): Optional | If True, the Section Index Pattern is always in the same position on the screen. This is the default. If False, the Section Index Pattern scrolls with the page content. The default value is False. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1" "myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |

### Section Index Item

| **Property** | **Description** |
| --- | --- |
| ScrollToWidgetId (Text): Mandatory | Element to where the page navigates. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1" "myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
