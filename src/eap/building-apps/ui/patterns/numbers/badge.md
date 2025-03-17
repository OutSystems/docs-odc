---
tags: ui patterns, data retrieval, widget implementation, notifications, user management
summary: Learn how to use the Badge UI Pattern in OutSystems Developer Cloud (ODC) to display numerical notifications such as unread messages or registered users.
locale: en-us
guid: d97db143-3239-44d4-bdf7-0c49483b6939
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A19032&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Badge

You can use the Badge UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![Example of Badge UI Pattern displaying numerical notification](images/badge-image-7.png "Badge UI Pattern Example")

**How to use the Badge UI Pattern**

The following example demonstrates how you can display the number of registered users on your platform.

1. In ODC Studio, in the Toolbox, search for `Badge`.

    The Badge widget is displayed.

    ![Screenshot of Badge widget in ODC Studio Toolbox](images/badge-10-ss.png "Badge Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Badge widget into the Main Content area of your application's screen.

    ![Screenshot showing the process of dragging the Badge widget into the Main Content area in ODC Studio](images/badge-11-ss.png "Dragging Badge Widget into Main Content Area")

1. To create an aggregate that retrieves all of the users on your platform, right-click your screen name and select **Fetch Data from Database**.

    ![Screenshot of context menu highlighting the 'Fetch Data from Database' option in ODC Studio](images/badge-1-ss.png "Fetch Data from Database Option")

1. Click the Aggregate screen, and from the **Select Source** popup, select the relevant database entity (in this example, **Users**), and click **Select**.

    ![Screenshot of the 'Select Source' popup window for choosing a database entity in ODC Studio](images/badge-2-ss.png "Select Source Popup for Database Entity")

1. To reopen your screen, double-click on your screen name.

1. Select the Badge widget, and on the **Properties** tab, from the **Number** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the following expression and click **Close**.

    `(GetUsers.Count)`

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Count** output parameter.

    ![Screenshot of the Expression Editor in ODC Studio with the expression '(GetUsers.Count)' entered](images/badge-3-ss.png "Expression Editor in ODC Studio")

    The **Number** property is now set to display the Count property of the aggregate you created, which retrieves the number of users on your platform and displays it in your Badge.

1. On the **Properties** tab, you can also customize the Badge's look and feel by setting any of the optional properties, for example, the color, shape, and size. The following example displays a blue, medium-sized, soft-rounded badge.  

    ![Screenshot showing customization options for the Badge's appearance including color, shape, and size in ODC Studio](images/badge-4-ss.png "Customizing Badge Appearance")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number (LongInteger): Optional     | Number that appears inside the badge. Set this to a Data source that contains the value that the Badge will display. Common use cases include displaying a value contained in a Variable or the result of an Aggregate (for instance, querying a 'Messages' table for the current user to return the count of new messages). <p>Examples <ul><li>Blank - displays the number 8 (default value)</li><li>22 - displays the number 22</li><li>VariableName - displays the value that the variable "VariableName" holds at that time </li><li>ExampleAggregate.Count - displays the number of records returned by the "ExampleAggregate" aggregate execution</li></ul></p> |
| Color (Color Identifier): Optional | Set the badge color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>Blank - displays the badge in the color you chose when creating the app (default value)</li><li>Entities.Color.Red - displays a red badge</li></ul></p>                                                                                                                                                                                                                                                                                                                                                  |
| Size (Size Identifier): Optional   | Set the badge size. Small and medium are the predefined sizes available for the badge. <p>Examples <ul><li>Blank - displays a medium sized badge (default value)</li><li>Entities.Size.Small - displays a small sized badge</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Shape (Shape Identifier): Optional | Set the badge shape. Rounded, soft rounded, and sharp are the predefined shapes available for the badge. <p>Examples <ul><li>Blank - displays a rounded badge (default value)</li><li>Entities.Shape.Sharp - displays a square badge</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                                                                     |
| IsLight (Boolean): Optional        | Specify the badge's background color. <p>Examples <ul><li>Blank - A darker hue of the color is applied to the badge and a lighter color to the text (default value)</li><li>True - A brighter hue of the color is applied to the badge and a darker color to the text.</li><li>False - A darker hue of the color is applied to the badge and a lighter color to the text</li></ul></p>                                                                                                                                                                                                                                                                                 |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value)</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1" "myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
