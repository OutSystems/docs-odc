---
tags: ui design patterns, mobile apps development, section ui pattern
summary: Learn how to organize on-screen content using the Section UI Pattern in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 938450a3-c869-4c7b-82f2-7599c196d482
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A11352&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Section

You can use the Section UI Pattern to organize on-screen content into different sections. This pattern can also be used with the Section Index UI Pattern to create anchors for each section.

![Screenshot showing an overview of the Section UI Pattern in a mobile app interface](images/section-5-ss.png "Section UI Pattern Overview")

**How to use the Section UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Section`.
  
    The Section widget is displayed.

    ![Screenshot of the Section widget found in the ODC Studio Toolbox](images/section-1-ss.png "Section Widget in ODC Studio Toolbox") 

1. To From the Toolbox, drag the Section widget into the Main Content area of your application's screen.

    ![Screenshot depicting the process of dragging the Section widget into the main content area of an application screen](images/section-2-ss.png "Dragging Section Widget into Main Content Area")

    By default, the Section widget contains Title and Content placeholders.

1. Add your content to the placeholders.

    In this example, we add a title to the Title placeholder as well as  text and a button to the Content placeholder. We also set the button to redirect the user to a new page when clicked.

    ![Screenshot showing the addition of a title, text, and a button to the Section widget placeholders](images/section-3-ss.png "Adding Content to Section Widget Placeholders")

1. On the **Properties** tab, you can customize the Section's look and feel by setting any of the (optional) properties.

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UsePadding (Boolean): Optional | If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
