---
summary: Explore how to implement and customize the Accordion UI Pattern in OutSystems Developer Cloud (ODC) to enhance application interfaces.
tags: ui components, accordion pattern, user interface design
locale: en-us
guid: 794b75df-0091-4e62-b1f8-22c56e7ebf90
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10201&t=ZwHw8hXeFhwYsO5V-1
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
---

# Accordion

You can use the Accordion UI Pattern to allow users expand and hide content when clicked.

**How to use the Accordion UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Accordion`.

    The Accordion widget is displayed.

    ![Screenshot of the Accordion widget in the ODC Studio Toolbox](images/accordion-widget-ss.png "Accordion Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Accordion widget into the Main Content area of your application's screen.

    ![Dragging the Accordion widget into the Main Content area of an application screen](images/accordion-dragwidget-ss.png "Dragging Accordion Widget to Screen")

    **Note:** By default, the Accordion widget contains 3 **AccordionItem** widgets. You can add or delete Accordion Items as required.

1. Add the relevant content to the **AccordionItem** placeholders. In this example, some FAQs are added.
  
    ![Adding FAQ content to AccordionItem placeholders in the Accordion widget](images/accordion-addcontent-ss.png "Adding Content to AccordionItem Placeholders")

1. On the **Properties** tab, you can customize the Accordion's look and feel by setting any of the (optional) properties.

    ![Customizing the Accordion's appearance through the Properties tab in ODC Studio](images/accordion-properties-ss.png "Accordion Properties Tab")

    ![Setting properties for individual Accordion Items in ODC Studio](images/accordion-properties-item-ss.png "Accordion Item Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

### Accordion

| Property                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MultipleItems (Boolean): Optional | If True, you can have multiple Accordion Items expanded simultaneously. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ExtendedClass (Text): Optional    | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |

### Accordion Item

| Property                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartsExpanded (Boolean): Optional             | If set to True, when the page is rendered, the Accordion Item is open. If set to False, the Accordion Item is closed. The default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Icon (Accordion Icon Type): Optional           | Set the icons shown in  the Accordion Item. You can pick between the following: <br/> <ul><li>Carets: Arrow up icon when the item is expanded and arrow down icon when the item is collapsed. This is the default.</li><li> Plus/Minus: Minus icon (-) when the item is expanded and plus icon (+) when the item is collapsed.</li><li>Custom: Advanced option to customize the Accordion icons. To use custom icons, set the Icon property to Custom and drag and drop the Icon widget to the Accordion Item placeholder.</li></ul>                                                                                              |
| IconPosition (AccordionIconPosition): Optional | Set the position of the accordion icon. By default, the icon diplays on the right.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| IsDisabled (Boolean): Optional                 | If True, the Accordion item can't be expanded when clicked. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional                 | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. |
