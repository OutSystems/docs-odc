---
tags:
summary: OutSystems Developer Cloud (ODC) features the Animate UI Pattern for enhancing app usability by animating elements on screen.
locale: en-us
guid: bd23a378-5bd7-4fcb-8c53-5455b46be344
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A12821&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Animate

You can use the Animate UI Pattern to create animations within your app. This UI pattern allows you to emphasize elements as they appear on screen which enhances the overall usability of the app.

<iframe src="https://player.vimeo.com/video/973090176" width="454" height="492" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating Animate UI pattern effect in an app.</iframe>

**How to use the Animate UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Animate`.

    The Animate widget is displayed.

    ![Screenshot of the Animate widget in the ODC Studio Toolbox](images/animate-3-ss.png "Animate Widget in Toolbox")

1. From the Toolbox, drag the Animate widget into the Main Content area of your application's screen.

    ![Dragging the Animate widget into the Main Content area of an application screen](images/animate-1-ss.png "Dragging Animate Widget")

    By default, the Animate widget contains a Content placeholder.

1. Add the content you want to animate to the Content placeholder.

    In this example, we add an image by dragging the Image widget into the Content placeholder, and on the **Properties** tab, from the **Image** dropdown, selecting image from the sample OutSystems UI images.

    ![Adding an image to the Content placeholder of the Animate widget](images/animate-4-ss.png "Adding Content to Animate Widget")

1. Select the Animate widget, and on the **Properties** tab, set the relevant properties, for example, where you want the animation to enter the screen and at what speed.

    ![Setting properties of the Animate widget in the Properties tab](images/animate-5-ss.png "Setting Animate Widget Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AnimationType (AnimationType Identifier): Mandatory | Set how the animation enters the screen. <p>The following are the available options: <ul><li>BottomToTop</li> <li>Bounce</li><li>FadeIn</li><li>LeftToRight</li><li>RightToLeft</li><li>Scale</li><li>ScaleDown</li><li>Spinner</li><li>TopToBottom</li></ul></p> <p>Examples <ul><li>_Entities.AnimationType.BottomToTop_ - Enters from the bottom of the screen to the top of the screen.</li><li>_Entities.AnimationType.Bounce_ - Bounces onto the screen.</li></ul></p>                                                                                                                                           |
| Delay (Integer): Optional                           | Time to wait before animation starts (in milliseconds). The default value is 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Speed (Speed Identifier): Optional                  | Animation duration. Fast, normal, and slow are the predefined speeds available for the animation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ExtendedClass (Text): Optional                      | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
