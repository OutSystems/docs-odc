---
tags: runtime-mobileandreactiveweb;  
summary: Alert gets the end user's attention and highlights important information, errors or warnings on the screen.
locale: en-us
guid: 1492d677-e96e-48f2-89af-1e0157058f58
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Alert

You can use the Alert UI Pattern to highlight and display important information, errors, or warnings.

![](<images/alert-1.png>)

**How to use the Alert UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Alert`.

    The Alert widget is displayed.

    ![](<images/alert-7-ss.png>)

1. From the Toolbox, drag the Alert widget into the Main Content area of your application's screen.

    ![](<images/alert-8-ss.png?width=800>)

1. Select the MessageText placeholder, and enter the Alert message you want to display.
    
    ![](<images/alert-11-ss.png>)

1. On the **Property** tab, set the **AlertType** property. In this example, the alert type is set to error which changes the message to display in red. 
    
    ![](<images/alert-9-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app. 


## Properties

| **Property**                           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AlertType (Alert Identifer): Mandatory | Select the type of alert. the predefined options are:<br/><br/><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li></ul><br/>Examples<br/><br/><ul><li>_Entities.Alert.Warning_ - Displays a yellow warning message.</li><li>_Entities.Alert.Info_ - Displays a blue information message.</li></ul>                                                                                                                                                                                                                                                                                                                 |
| ExtendedClass (Text): Optional         | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank No custom styles are added (default value).</li><li>"myclass" Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. |
