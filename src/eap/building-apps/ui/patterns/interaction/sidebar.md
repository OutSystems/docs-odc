---
tags: user interface patterns, native apps, ui design, mobile app development, outsystems
summary: OutSystems Developer Cloud (ODC) enhances app functionality with a Sidebar UI Pattern for displaying additional content.
locale: en-us
guid: 9bb5e9f0-3a33-4a07-951a-08fdb67267a1
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A17424&t=ZwHw8hXeFhwYsO5V-1
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
---

# Sidebar

You can use the Sidebar UI Pattern to display additional information in the margin of the main content. The additional information supports the user's understanding of the main content.

![Example of a sidebar UI pattern in a mobile app](images/sidebar-example.png "Sidebar Example")

<div class="info" markdown="1">

**Note:** To avoid conflicts with the browser native gestures, the Sidebar pattern only works with gestures on Native Apps not running as PWA.  

</div>

**How to use the Sidebar UI Pattern**

In this example, we create a button that opens and closes the Sidebar widget.

1. In ODC Studio, in the Toolbox, search for `Sidebar`.

    The Sidebar widget is displayed.

    ![Screenshot showing how to search for the Sidebar widget in ODC Studio](images/sidebar-widget-ss.png "Sidebar Widget Search")

1. From the Toolbox, drag the Sidebar widget into the Main Content area of your application's screen.

    ![Dragging the Sidebar widget into the main content area in ODC Studio](images/sidebar-drag-ss.png "Dragging Sidebar Widget")

    By default, the Sidebar widget contains Header and Content placeholders.

1. On the **Properties** tab, in the **Name** field, enter a name for the Sidebar widget.

    In this example, we enter it `MySidebar`.

    ![Entering a name for the Sidebar widget in the Properties tab](images/sidebar-name-ss.png "Naming the Sidebar Widget")

1. Select and right-click your screen name, and select **Add Local Variable**.

    ![Adding a local variable to the screen in ODC Studio](images/sidebar-add-var-ss.png "Adding a Local Variable")

1. Enter a name for the variable.

    In this example, name the variable ``IsSidebarOpen``, set the **Data Type** as Boolean, and the **Default Value** to **False**.

    ![Entering a name for the Sidebar local variable with Boolean data type](images/sidebar-var-name-ss.png "Naming the Sidebar Variable")

1. Select the Sidebar widget, and on the **Properties** tab, from the **StartsOpen** dropdown, select the newly created variable.

    ![Setting the StartsOpen property of the Sidebar widget to a local variable](images/sidebar-isopen-ss.png "Setting StartsOpen Property")

1. Add your content to the **Header** and **Content** placeholders, for example, forms, images and text. 
    
    In this example we add some text.
   
    ![Adding text content to the Header and Content placeholders of the Sidebar widget](images/sidebar-content-ss.png "Adding Content to Sidebar")

1. From the Toolbox, drag the **Button** widget just below the **Sidebar** widget and on the **Properties** tab, in the **Text** field, enter the text you want to appear on the button.

    In this example, we enter `Open Sidebar`.

    ![Adding a button below the Sidebar widget to open the Sidebar](images/sidebar-button-ss.png "Adding a Button to Open Sidebar")

1. To create a screen action to toggle the Sidebar:

    a. Double-click the **Open Sidebar** button.

    b. Drag an **If** statement to the screen action, and on the **Properties** tab, set the **Condition** to the **IsSidebarOpen** variable.

    ![Adding an If statement to the screen action for toggling the Sidebar](images/sidebar-if-ss.png "Adding If Statement")

    c. On the **True** branch, add the **SidebarClose** client action and set the **WidgetId** parameter to the Sidebar Id.

    ![Adding the SidebarClose client action to the True branch of the If statement](images/sidebar-close-ss.png "Adding SidebarClose Client Action")

    d. On the **False** branch, add the **SidebarOpen** client action and set the **WidgetId** parameter to the Sidebar Id.

    e. Drag an **Assign** to the screen action and set **IsSidebarOpen** variable to ``not IsSidebarOpen``.
    
    ![Adding an Assign action to toggle the IsSidebarOpen variable](images/sidebar-assign-ss.png "Adding an Assign Action")

1. You can customize the Sidebar by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties.

    ![Setting optional properties of the Sidebar pattern in the Properties tab](images/sidebar-properties-ss.png "Setting Sidebar Pattern Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartsOpen (Boolean): Optional         | Set to True to display the Sidebar. The default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Direction (Direction Entity): Optional | Set the position of where the Sidebar appears on the screen. The predefined options are Left and Right.<p>**Examples** <ul><li>Entities.Direction.Right - The sidebar is displayed on the right side of the screen.</li><li>Entities.Direction.Left - The sidebar is displayed on the left side of the screen. </li></ul></p>                                                                                                                                                                                                                                                                                                 |
| HasOverlay (Boolean): Optional         | Set to True to display an overlay when the Sidebar is open. When you click on the overlay, the Sidebar is closed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Width (String): Optional               | Sets the Sidebar width. All unit types accepted (px, %, vw).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ExtendedClass (Text): Optional         | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>**Examples** <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied. </li><li>"myclass1" "myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |

