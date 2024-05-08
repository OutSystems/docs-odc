---
tags:
summary: OutSystems Developer Cloud (ODC) features the Bottom Bar Item UI Pattern for easy navigation and feature access in applications.
locale: en-us
guid: a47f6440-0442-42ec-8674-e4cfb134957b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A17038&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Bottom Bar Item

You can use the Bottom Bar Item UI Pattern to provide access to a bottom navigation drawer and up to four actions, including the floating action button. Main pieces of core functionality are made available with one tap while allowing rapid switching between features.

![Screenshot of the Bottom Bar Item in ODC Studio interface](images/bottombaritem-1-ss.png "Bottom Bar Item in ODC Studio")

**How to use the Bottom Bar Item UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Bottom Bar Item`.
  
    The Bottom Bar Item widget is displayed.

    ![Bottom Bar Item widget displayed in the ODC Studio Toolbox](images/bottombaritem-3-ss.png "Bottom Bar Item Widget in Toolbox")

1. From the Toolbox, drag the Bottom Bar Item  widget into the Bottom placeholder area of your application's screen.

    ![Dragging the Bottom Bar Item widget into the Bottom placeholder on the screen](images/bottombaritem-2-ss.png "Dragging Bottom Bar Item Widget")

    By default, the Bottom Bar Item contains Icon and Text placeholders. You can add as many Bottom Bar Items as required.

    In this example, we add another three more Bottom Bar Items.

    ![Example of multiple Bottom Bar Items added to the Bottom placeholder](images/bottombaritem-4-ss.png "Multiple Bottom Bar Items Added")

1. For each of the Bottom Bar Items, add the relevant content.

    In this example we add linked icons and linked text to each of placeholders.

    ![Adding linked icons and text to each Bottom Bar Item placeholder](images/bottombaritem-5-ss.png "Adding Content to Bottom Bar Items")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

### Bottom Bar Item

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
