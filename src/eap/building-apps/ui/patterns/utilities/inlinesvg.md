---
tags: ui patterns, svg customization
summary: OutSystems Developer Cloud (ODC) supports the Inline SVG UI Pattern for customizing SVG properties and animations in applications.
locale: en-us
guid: 6db3a9a0-b82e-430c-b4b6-e5964bcd383f
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A21151&t=ZwHw8hXeFhwYsO5V-1
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

# Inline SVG

You can use the Inline SVG UI Pattern to change fill and stroke properties or animate the SVG paths.

**How to use the Inline SVG UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Inline SVG`.

    The Inline SVG widget is displayed.

    ![Screenshot of the Inline SVG widget in the ODC Studio Toolbox](images/inlinesvg-2-ss.png "Inline SVG Widget in ODC Studio Toolbox")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Inline SVG widget into the Main Content area of your application's screen.

    ![Screenshot showing how to drag the Inline SVG widget into the main content area of an application screen](images/inlinesvg-3-ss.png "Dragging Inline SVG Widget into Main Content Area")

1. On the **Properties** tab, in the **SVGCode** property, set your SVG code.

    In this example, we enter the following:

    ``"<svg height=""100"" width=""350"" fill=""yellow"">
    <circle cx=""50"" cy=""50"" r=""30"" stroke=""red"" stroke-width=""25"" fill=""white"" />
    <text x=""110"" y=""60"" fill=""black"" font-size=""40"" font-weight=""bold"" font-family=""open sans"">outsystems</text>
    Sorry, your browser does not support inline SVG.  
    </svg>"``

    ![Screenshot of the Properties tab where SVG code is set for the Inline SVG widget](images/inlinesvg-4-ss.png "Setting SVG Code in Properties Tab")

After following these steps and publishing the app, you can test the pattern in your app.

Using the example above, the results are as follows:

![Example of an Inline SVG UI pattern with a circle and text label 'outsystems' displayed in an application](images/inlinesvg-1-ss.png "Inline SVG UI Pattern Example")

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SVGCode (Text): Optional       | SVG markup code that is appended onto the HTML.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
