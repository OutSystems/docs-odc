---
tags: 
summary: Learn how to use the Counter UI Pattern in OutSystems Developer Cloud (ODC) to display numerical data effectively.
locale: en-us
guid: 7b33f1cb-f293-49c5-ad4a-8c781526acb7
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A19354&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Counter

You can use the Counter UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![Screenshot showing an example of the Counter UI Pattern used for notifications](images/counter-2-ss.png "Counter UI Pattern Notification Example")

**How to use the Counter UI Pattern**

The following example demonstrates how you can display the number of registered users on your platform.

1. In ODC Studio, in the Toolbox, search for `Counter`.

    The Counter widget is displayed.

    ![Screenshot of the Counter widget found in the ODC Studio Toolbox](images/counter-1-ss.png "Counter Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Counter widget into the Main Content area of your application's screen.

    ![Screenshot depicting the process of dragging the Counter widget into the main content area of an application screen](images/counter-3-ss.png "Dragging Counter Widget into Main Content Area")

    By default, the Counter widget contains a Content placeholder.

1. To create an aggregate (in this example to retrieve all the users on the platform), right-click the screen name and select **Fetch Data from Database**.

    ![Screenshot showing the option to fetch data from the database by right-clicking the screen name](images/counter-4-ss.png "Fetch Data from Database Option")

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant entity and click **OK**. In this example, we select the **User** entity.

    ![Screenshot of the Select Source pop-up with the User entity selected for data retrieval](images/counter-5-ss.png "Selecting User Entity for Data Retrieval")

    The aggregate **GetUsers** is created.

    ![Screenshot showing the creation of the GetUsers aggregate in the application](images/counter-6-ss.png "GetUsers Aggregate Creation")

1. To reopen your screen, select the **Interface** tab, and double-click on your screen.

1. From the Toolbox, drag an Expression widget into the Content placeholder, and in the **Expression Editor** enter the following expression and click **Done**.

    `GetUsers.Count`

    ![Screenshot of an Expression widget in the Counter's content placeholder with the expression GetUsers.Count entered](images/counter-7-ss.png "Expression Widget with GetUsers.Count")

   You have now created an expression that displays the Count property of the Aggregate you created earlier, which gets and displays the number of users on your platform.

1. On the **Properties** tab, you can customize the Counter's look and feel by setting any of the optional properties, for example, the height and orientation.

    ![Screenshot of the Properties tab where the Counter's appearance can be customized](images/counter-8-ss.png "Customizing Counter Pattern Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BackgroundColor (Color Identifier): Optional | The counter's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - No background color is applied to the counter. This is the default.</li><li>Entities.Color.Red - Displays a red counter.</li></ul></p>                                                                                                                                                                                                                                                                                              |
| IsVertical (Boolean): Optional               | If True, the content is displayed vertically. If False, the content is displayed horizontally. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Height (Text): Optional                      | The counter's height (in pixels units). By default the counter height is 100 (pixel units).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional               | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
