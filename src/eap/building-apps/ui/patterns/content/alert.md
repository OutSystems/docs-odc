---
tags:
summary: Explore how to implement and customize the Alert UI Pattern in OutSystems Developer Cloud (ODC) to display important messages in applications.
locale: en-us
guid: 1492d677-e96e-48f2-89af-1e0157058f58
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10303&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Alert

You can use the Alert UI Pattern to highlight and display important information, errors, or warnings.

![Example of an Alert UI Pattern in a mobile app interface](images/alert-1.png "Example of an Alert UI Pattern")

**How to use the Alert UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Alert`.

    The Alert widget is displayed.

    ![Screenshot showing the Alert widget in the ODC Studio Toolbox](images/alert-7-ss.png "Alert Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Alert widget into the Main Content area of your application's screen.

    ![Process of dragging the Alert widget into the main content area of an application screen](images/alert-8-ss.png "Dragging Alert Widget into Main Content Area")

1. Select the MessageText placeholder, and enter the Alert message you want to display.
    
    ![Selecting the MessageText placeholder to enter an Alert message](images/alert-11-ss.png "Setting Alert Message Text")

1. On the **Property** tab, set the **AlertType** property. In this example, the alert type is set to error which changes the message to display in red. 
    
    ![Setting the AlertType property to 'error' in the Property tab to display the message in red](images/alert-9-ss.png "Setting AlertType Property to Error")

After following these steps and publishing the app, you can test the pattern in your app. 


## Properties

| **Property**                           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AlertType (Alert Identifer): Mandatory | Select the type of alert. the predefined options are:<br/><br/><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li></ul><br/>Examples<br/><br/><ul><li>_Entities.Alert.Warning_ - Displays a yellow warning message.</li><li>_Entities.Alert.Info_ - Displays a blue information message.</li></ul>                                                                                                                                                                                                                                                                                                                 |
| ExtendedClass (Text): Optional         | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank No custom styles are added (default value).</li><li>"myclass" Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. |
