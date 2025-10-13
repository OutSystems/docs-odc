---
tags: ui design, ui patterns, mobile app development, outsystems developer cloud
summary: Learn how to implement and customize the Action Sheet UI Pattern in OutSystems Developer Cloud (ODC) to enhance mobile app interfaces.
locale: en-us
guid: 7702c792-34d2-41e7-9bad-e9b88326a21e
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A12251&t=ZwHw8hXeFhwYsO5V-1
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

# Action Sheet

You can use the Action Sheet UI Patterns to add a menu that slides from the bottom of the screen when triggered by a user action.

![Screenshot of the Action Sheet trigger in a mobile app interface](images/actionsheet-1-ss.png "Action Sheet Trigger")

**How to use the Action Sheet UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Action Sheet`.

    The Action Sheet widget is displayed.

    ![Image showing the Action Sheet widget in the ODC Studio Toolbox](images/actionsheet-2-ss.png "Action Sheet Widget in Toolbox")

1. From the Toolbox, drag the Action Sheet widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Action Sheet widget into the Main Content area](images/actionsheet-3-ss.png "Placing Action Sheet Widget")

    By default, the Action Sheet widget contains 5 button placeholders.

1. Add the relevant content to the Button placeholders. In this example, we add buttons that navigate to other pages when clicked.

    ![Screenshot showing the addition of button placeholders to the Action Sheet Widget](images/actionsheet-5-ss.png "Adding Buttons to Action Sheet Widget")

1. Add a local variable. In this example, we call the variable **IsOpened**.

1. Select the Action Sheet pattern, and on the **Properties** tab, set the **IsOpen** property to the new local variable (in this example, **IsOpened**).

    ![Screenshot of the Properties tab with the IsOpen property set to a local variable](images/actionsheet-4-ss.png "Setting IsOpen Property")

1. To open the Action Sheet menu, we add a button and on the **Properties** tab, from the **OnClick** dropdown, select **New Client Action**.

    ![Screenshot of the Properties tab with the OnClick dropdown for creating a new client action](images/actionsheet-6-ss.png "Creating OnClick Event")

1. Add an Assign to the client action and set the **IsOpened** local variable to **True**.

    ![Screenshot of an Assign action setting the IsOpened local variable to True](images/actionsheet-7-ss.png "Assigning IsOpened to True")

1. To close the Action Sheet menu, on the **Properties** tab, from the **Handler** dropdrown of the **OnClose** event, select **New Client Action**.

    ![Screenshot of the Properties tab with the Handler dropdown for the OnClose event](images/actionsheet-8-ss.png "Setting OnClose Handler")

1. Add an Assign to the client action and set the **IsOpened** local variable to **False**.

    ![Screenshot of an Assign action setting the IsOpened local variable to False](images/actionsheet-9-ss.png "Assigning IsOpened to False")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IsOpen(Boolean): Mandatory | Assign a variable open/close the Action Sheet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ExtendedClass              | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
