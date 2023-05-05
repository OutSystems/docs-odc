---
summary: Let your users take pictures in native mobile apps, PWAs, and web apps. Adjust the picture properties in the native mobile apps. Demo app available to see the plugin in action.
tags: 
locale: en-us
guid: 6df6f491-46e4-434f-924e-043929958fef
app_type: mobile apps
platform-version: odc
---

# Camera Plugin

Use the Camera Plugin to let users take pictures with their mobile device. This plugin works with, native mobile apps, progressive web apps (PWAs) and web apps. The plugin lets you select options like image quality, orientation, and the file format.

<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a demo app.

</div> 

## Demo app

Install **Camera Sample App** from Forge and open the app in ODC (OutSystems Developer Cloud) Studio. The demo app contains logic for common use cases, which you can examine and recreate in your apps. For example, the demo app shows how to:

* Take a single picture
* Take multiple pictures
* Select a picture from the gallery
* Create a settings page
* Edit a picture taken with the camera or selected from the gallery
* Edit the picture that now displays in the app

![Camera Plugin demo app](images/camera-sample-app.png?width=330)

<div class="info" markdown="1">

Documentation is under construction. It's frequently updated and expanded.

</div>

## Taking a picture

To let users take a picture and have a good user experience:

* Create a user interface
* Create logic to take a picture
* Create logic to handle errors

See the sections that follow for more information.

### Creating a user interface

You can start by defining a variable of the **Binary Data** data type to hold the image data (1). Use a Button (2) or other widget to run the action that takes a picture. Use an **Image** widget (3) to show the image after using the camera, by setting **Type** to **Binary Data** and **Image Content** to the variable you created.

![UI setup for taking pictures](images/camera-ui-setup-ss.png?width=700)

For more guidance on how to create an interface, see the UI accelerators that come with the Camera Plugin. In ODC Studio, navigate to **Interface** > **UI FLows** > **Camera Plugin** > **Camera Plugin**, and drag these Blocks to your Screen:

* **ChooseImage**
* **TakePicture**

### Creating logic to take a picture

The Camera Plugin actions are in the **Logic** tab of ODC Studio, in **Client Actions** >  **CameraPlugin**.

To prevent errors, it's a best practice to first check if the plugin is available (1) with the action **CheckCameraPlugin**. If the plugin isn't available to the app, display an error to the user. Otherwise, open the camera with **TakePicture** to let users take a picture (2). In the **TakePicture** action you can set the parameters for quality, width, back of front camera, and more.

Check if taking pictures on the device works by verifying the value of **TakePicture.Success** is **True** (3). If yes, handle the picture data in **TakePicture.ImageCaptured** by assigning it to a variable of the **Binary Data** data type (4).

![Take picture logic flow](images/camera-flow-take-picture-ss.png?width=700)

## Opening a picture from the gallery

Let users choose a picture from the device gallery with the **ChooseGalleryPicture** action. The action is in the **Logic** tab of ODC Studio, in **Client Actions** >  **CameraPlugin**.

The action **ChooseGalleryPicture** opens an image browser to let users select an image (1). [Check for errors](#handling-errors) by verifying **ChooseGalleryPicture.Success** is **True** (2). After users select the image, the binary data of the image is in the variable **ChooseGalleryPicture.ImageCaptured.** (3).

![Open from gallery](images/camera-flow-choose-from-gallery.png?width=700)

## Image quality and app responsiveness

When you set **100%** image **Quality** or use the **PNG** format, your app handles a large amount of image data. Users might notice a delay after taking an image with the highest quality settings. The more data the app has to handle, the less responsive it can become on low-end devices. 

When setting the image quality, consider the use case for your app. Check the following table.

| Example use case | Image quality          | Notes                                                     |
| ---------------- | ---------------------- | --------------------------------------------------------- |
| Profile image    | JPEG 60% (default)     | Sufficient quality for a profile image.                   |
| Insurance claims | JPEG 85% - 100% or PNG | High quality lets users examine all details in the image. |

<div class="info" markdown="1">

Changing the image quality setting applies only to .JPEG files.

</div>

## Handling errors

The app with the camera plugin can run on many Android or iOS devices, with different hardware and configurations. To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

Here is the list of actions you can use to handle the errors.

| Variable        | Action                   | Description                                                           |
| --------------- | ------------------------ | --------------------------------------------------------------------- |
| **IsAvailable** | **CheckCameraPlugin**    | True if the camera plugin is available in the app.                    |
| **IsPWA**       | **CheckCameraPlugin**    | True if the plugin works in PWA.                                      |
| **Success**     | **TakePicture**          | True if there aren't errors while taking a picture.                   |
| **Success**     | **ChooseGalleryPicture** | True if there aren't errors while opening a picture from the gallery. |
| **Success**     | **EditPicture**          | True if there aren't errors while editing a picture.                  |

You can use these actions with the **If** nodes to check for errors and control how the app works.

![Handling errors in the camera plugin](images/camera-handling-errors.png?width=800)

## Reference

More information about the plugin.

### Actions

Here is the reference of the actions you can use from the plugin. Camera Plugin uses a Cordova plugin, and for more information check [cordova-plugin-camera](https://github.com/OutSystems/cordova-plugin-camera).

| Action                   | Description                                   | Available in PWA |
| ------------------------ | --------------------------------------------- | ---------------- |
| **CheckCameraPlugin**    | Checks if the plugin is available in the app. | Yes              |
| **TakePicture**          | Opens the camera on the user device.          | Yes              |
| **ChooseGalleryPicture** | Opens the gallery on the user device.         | Yes              |
| **EditPicture**          | Opens an edit interface to edit the picture.  | Yes              |

## Picture options

Change the properties of the **TakePicture** action to adjust how the app handles the images.

| Property               | Description                                                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Quality**            | The quality of the picture, in percentage. See also the [notes about Quality](#image-quality-and-app-responsiveness).   |
| **Width**              | The width of the picture, in pixels.                                                                                    |
| **Height**             | The height of the picture, in pixels.                                                                                   |
| **CorrectOrientation** | If **True**, the plugin fixes the orientation if users take a photo and rotate the device. Only for native mobile apps. |
| **EncodingType**       | Select the **JPEG** or **PNG** format.                                                                                  |
| **SaveToPhotoAlbum**   | If **True**, the app saves the image to the device.                                                                     |
| **CameraDirection**    | Select the front or back camera as the default when taking a new picture.                                               |
| **AllowEdit**          | If **True**, an Edit step is added after the take or choose picture step.                                               |
| **AllowMultiplePictures**   | PWA only. Enables taking multiple pictures. Add the **CameraPlugin** theme to your app, to ensure this feature works. |      



### MABS compatibility

The table shows the compatibility of the Camera Plugin with the Mobile Apps Builds Service (MABS).

| Plugin version  | Compatible with MABS version | Notes |
| --------------- | ---------------------------- | ----- |
| 1.0.0 and later | MABS 9.0 and later.          |       |


## Known issues and workarounds

A list of known issues and possible workarounds.

### Taking multiple pictures not working in PWAs

In PWA, taking multiple pictures requires use of the browser stream capabilities. To ensure the app has access to the stream, add the theme **CameraPlugin** as an element to your app. **Keep the theme as dependency** even when the IDE reports it as not used by the app.

### Crashes on iOS 13.2 and 13.3 

**Applies to PWAs.**

In iOS 13.2 and 13.3 the camera may stop working because of the [WebKit 206219 bug](https://bugs.webkit.org/show_bug.cgi?id=206219). If the camera stops working, swipe the open app up in App Switcher and reopen the app. WebKit is working on the fix.

### CameraDirection setting has no effect 

**Applies to Android only.**

In some versions of Android, the app ignores the **CameraDirection** setting. Users can change the camera direction (back or front) once the camera app opens.

### The resolution and quality settings apply to app images only

Applies to native apps only.

When you change the resolution or quality setting, the plugin applies it only to the image the app uses. The device ignores the settings when saving the images in the device gallery. This means that the size of the image in the gallery depends on the device hardware.

### Choose from gallery wont allow for items to be selected

**Applies to Android only.**

In Android 13, when using "ChooseFromGallery", users are unable to select content from device's gallery.
When targeting Android 13, users should build their apps using MABS9 or later.
