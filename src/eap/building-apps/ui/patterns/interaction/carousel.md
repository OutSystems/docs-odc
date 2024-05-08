---
tags: 
summary: OutSystems Developer Cloud (ODC) offers a Carousel UI Pattern for displaying images horizontally, utilizing Splide.js library.
locale: en-us
guid: 84e84647-8129-4467-ade7-72b6102f9959
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A13594&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Carousel

You can use the Carousel UI Pattern to display multiple items in a horizontal slide.  The Carousel Pattern optimizes screen space by displaying only a few images from a larger collection which you can view using the navigation controls. 

![Example of a Carousel UI Pattern with multiple items in a horizontal slide](images/carousel-example.png "Carousel Example")

<div class="info" markdown="1">

The Carousel Pattern is based on the Splide.js library (v3). For more information about the Carousel’s behaviors and extensibility methods, see [Splide.js](https://splidejs.com/).  

</div>

## How to use the Carousel UI Pattern

1. In ODC Studio, in the Toolbox, search for `Carousel`.
  
     The Carousel widget is displayed.

    ![Screenshot of the Carousel widget in the ODC Studio Toolbox](images/carousel-widget-ss.png "Carousel Widget in Toolbox")

1. From the Toolbox, drag the Carousel widget into the Main Content area of your application's screen. 

    ![Dragging the Carousel widget into the Main Content area of an application screen](images/carousel-dragwidget-ss.png "Dragging Carousel Widget to Screen")

    By default, the Carousel pattern contains a **CarouselItems** placeholder with a **List** widget and **Image** widget. If you want a Carousel with static images, you can remove the **List** widget and add your images inside the **CarouselItems** placeholder.

1. Add your content to the **Carousel Items** placeholder. 

    In this example, the List is deleted and 3 Image widgets are added.  

    ![Adding three Image widgets to the Carousel Items placeholder](images/carousel-addimages-ss.png "Adding Image Widgets to Carousel") 

1. Select the **Image** widget, and on the **Properties** tab, from the **Image** drop-down, select or import the image you want in the Carousel. 

    **Note:** In this example, the image property Type is set to **Local** image. You can also add External and Binary Data images.

    ![Setting the image property type to Local in the Carousel Image widget](images/carousel-imagetype-ss.png "Setting Image Property Type  in Carousel")   

1. Repeat step 4 for each of the images in the Carousel. 

1. You can configure the Carousel by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties, for example, **Navigation** or **ItemsPerSlide**.For more configurations, expand the **OptionalConfigs** property.

    ![Configuring Carousel properties such as Navigation and ItemsPerSlide in the Properties tab](images/carousel-properties-ss.png "Carousel Widget Properties Configuration")  

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| **Property**                                         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Navigation (CarouselNavigation Identifier): Optional | Sets the navigation behavior:<ul><li>Dots</li><li>Arrows</li><li>Both (dots and arrows)</li><li>None</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Height (Text): Optional                              | Set a custom height for the Carousel. The parameter accepts any CSS format, except percentage (library constraint). The default value is Auto (the height of the items inside Carousel).                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ItemsPerSlide (CarouselItems): Optional              | Number of Carousel items simultaneously visible on each slide.<ul><li>DesktopItems (Integer)</li><li>TabletItems (Integer)</li><li>PhoneItems (Integer)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ExtendedClass (Text): Optional                       | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul><br/>You can also use the classes available on the OutSystems UI. |
| OptionalConfigs.AutoPlay (Boolean)                   | If True, the Carousel slides change automatically. If False, slides must be changed manually. The default value is True.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| OptionalConfigs.Loop (Boolean)                       | If True, once the last item in the Carousel is reached, it loops around to the first item and begins displaying all of the items again. If False, the Carousel does not loop; it ends when the last item is reached. The default value is True.                                                                                                                                                                                                                                                                                                                                                                                            |
| OptionalConfigs.Padding (Text)                       | Distance between the Carousel edges and the visible items on each slide. Accepts any CSS size unit (such as, px, vw, %) or  CSS variables, for example, "100px".                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OptionalConfigs.ItemsGap (Text)                      | Distance between each Carousel item. Accepts any CSS size unit (lsuch as px, vw, %) or CSS variables, for example, "var(--space-base)".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| OptionalConfigs.StartingPosition (Integer)           | Set the first item to display first in the Carousel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  
## Compatibility with other patterns

Avoid using the Carousel inside patterns with swipe events, such as the Tabs and Stacked Cards Patterns.
