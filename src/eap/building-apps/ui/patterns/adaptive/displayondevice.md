---
summary: OutSystems Developer Cloud (ODC) supports the Display on Device UI pattern for device-specific content rendering.
tags: ui patterns, cross-platform development
locale: en-us
guid: 4dd69c5c-c0a3-4c26-a4f7-b4c86313495f
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A9149&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Display on Device

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Display on Device UI pattern to select what elements are displayed on which device types. With this pattern you can improve the way information is displayed on different devices - computers, tablets, and phones - by specifically specifying which elements display on each of them.

![Overview of Display on Device pattern showing different device types](images/displayondevice-1.png "Display on Device Overview")

**How to use the Display on Device UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Display on Device`.

    The Display on Device widget is displayed.

    ![Screenshot of the Display on Device widget in the ODC Studio Toolbox](images/displayondevice-2-ss.png "Display on Device Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Display on Device widget into the Main Content area of your application's screen.

    ![Dragging the Display on Device widget into the Main Content area in ODC Studio](images/displayondevice-3-ss.png "Dragging Display on Device Widget")

    By default, the Display on Device widget contains OnDesktop, OnTablet, and OnPhone placeholders.

1. Add the required content to each of the placeholders.

    In this example, we add images by dragging the Image widget into each of the placeholders, and on the **Properties** tab, from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![Adding content to OnDesktop, OnTablet, and OnPhone placeholders in the Display on Device widget](images/displayondevice-4-ss.png "Configuring Display on Device Placeholders")

After following these steps and publishing the app, you can test the pattern in your app.
