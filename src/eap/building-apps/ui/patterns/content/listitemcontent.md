---
tags: ui design patterns, user experience
summary: OutSystems Developer Cloud (ODC) features the List Item Content UI Pattern for organizing and displaying content efficiently in applications.
locale: en-us
guid: af82326a-de20-4931-af2a-dc6ca092a60d
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A11189&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - ui designers
outsystems-tools:
  - odc studio
content-type:
  - procedure
  - reference
---

# List Item Content

You can use the List Item Content UI Pattern to quickly organize critical content in a readable way, helping the user understand the content. The List Item Content pattern is often used to organize content such as icons, text, and actions inside a list in a readable way.

![Screenshot of a List Item Content example in a mobile app](images/listitemcontent-1-ss.png "List Item Content Example")

**How to use the List Item Content UI Pattern**

1. In ODC Studio, in the Toolbox, search for `List Item Content`.

    The List Item Content widget is displayed.

    ![Screenshot showing the List Item Content widget in the ODC Studio Toolbox](images/listitemcontent-2-ss.png "List Item Content Widget in Toolbox")

1. From the Toolbox, drag the List Item Content widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the List Item Content widget into the Main Content area](images/listitemcontent-3-ss.png "Dragging List Item Content Widget")

1. Add the relevant content to the placeholders.

    In this example, we add some texts and icons. 

    ![Screenshot showing the addition of texts and icons to the List Item Content placeholders](images/listitemcontent-4-ss.png "Adding Content to List Item Content Widget")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
