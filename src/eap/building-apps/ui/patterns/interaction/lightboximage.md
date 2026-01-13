---
tags: ui patterns, image gallery, ux design, how-to, widgets
summary: Explore the Lightbox Image UI Pattern in OutSystems Developer Cloud (ODC) for creating detailed image galleries in applications.
locale: en-us
guid: 575c188f-fb02-4d70-8241-4b3e4518d66c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A15772&t=ZwHw8hXeFhwYsO5V-1
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

# Lightbox Image

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Lightbox Image UI Pattern to open smaller thumbnail images in full screen mode. This UI pattern is often used when creating an image gallery, allowing you to navigate through each of the images and view them in more detail.

## How to Use the Lightbox Image UI Pattern

1. In ODC Studio, in the Toolbox, search for `Lightbox Image`.

    The Lightbox Image widget is displayed.

    ![Screenshot of the Lightbox Image widget in the ODC Studio Toolbox](images/lightboxmob-image-1.png "Lightbox Image Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Lightbox Image widget into the Main Content area of your application's screen.

      ![Process of dragging the Lightbox Image widget into the application's main content area](images/lightboxmob-image-2.png "Dragging Lightbox Image Widget into Main Content Area")

      By default, the Lightbox Image widget contains an Image placeholder. You can add as many images as required by dragging the Image widget from the Toolbox into the Lightbox Image widget.

1. Select the **Image** placeholder and on the **Properties** tab, from the **Image** drop-down, select or import the thumbnail image you want to display. In this example, we use the sample OutSystems UI Images.

    ![Image placeholder selection and properties adjustment in the Lightbox Image widget](images/lightboxmob-image-3.png "Selecting Image Placeholder Properties")

    **Note:** In this example, the image property Type is set to **Local** image. You can also add External and Binary Data images.

1. Repeat step 3 for each of the images.

1. From the Widget Tree, select the Lightbox Image widget, and on the **Properties** tab, set the relevant (optional) properties.

## Properties

| **Property** | **Description** |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title (Text): Optional | Image title that is displayed when previewing the image in full screen mode.<br/><br/>Examples<br/><br/><ul><li>"Image 1" - Displays Image 1 as the image title.</li></ul> |
| Group (Text): Optional | Name of the group of images. Similar to the concept of a picture album, images in the same group are displayed in a gallery. You can navigate through pictures with the same group name when viewing them in full screen mode.<br/><br/>Examples<br/><br/><ul><li>Gallery 1 - Adds this image to the Gallery 1 group.</li></ul> |
| ImageURL (Text): Optional | URL for the image you want to show in full screen mode. If empty, a zoomed version of the thumbnail is displayed. Use this if you want to load a lower quality image as a thumbnail and display a higher quality version in full screen mode. |
| ImageZoom (Decimal): Optional | Defines the size of the image that opens in full screen mode (based on the thumbnail size).<br/>To avoid rendering problems, try to use images with the same ratio.<br/><br/>Examples<br/><br/><ul><li>2 - A thumbnail with 100x100, and zoom 2 opens with 200x200.</li><li>0.5 - A thumbnail with 500x500, and zoom 0.5 opens with 250x250.</li></ul> |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>To disable the URL feature, you must use the "disable-url" class on this parameter.<br/><br/>Examples<br/><br/><ul><li>Blank - No custom styles are added (default value). </li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |

## Compatibility with other patterns

The Lightbox Image UI pattern can be used only with images.

## Samples

Watch how the [Product Overview sample](https://silkui.outsystems.com/Samples_Mobile.aspx#Mobile_Details-Samples_ProductOverview) uses the Lightbox Image UI Pattern:

<iframe src="https://player.vimeo.com/video/977630859" width="372" height="666" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video exhibiting an application using the Lightbox Image UI Pattern.</iframe>
