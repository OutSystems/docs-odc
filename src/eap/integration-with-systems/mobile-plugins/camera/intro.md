---
summary: OutSystems Developer Cloud (ODC) supports the Camera plugin for capturing and editing media in mobile apps, as demonstrated in the Camera Sample App.
tags: plugin implementation, media capture, user interface design, error handling, mobile app development
locale: en-us
guid: 6df6f491-46e4-434f-924e-043929958fef
app_type: mobile apps
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=9744-34
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - forge
coverage-type:
  - apply
  - remember
topic:
  - using-cordova-plugins
  - using-capacitor-plugins
isautopublish: true
---

# Camera Plugin version 2

<div class="info" markdown="1">

For information about Camera Plugin version 1.x, refer to the [Camera Plugin version 1 article](camera-version-1.md).

</div>

<div class="warning" markdown="1">

Camera Plugin version 2.0.0 includes breaking changes. To update from an older version to version 2.0.0, refer to the [migration article](camera-migration-guide-1-to-2.md).

</div>

Use the Camera plugin to let users take photos and capture video with their mobile devices.
This plugin works with both native mobile apps and progressive web apps (PWAs).

For more information about installing and referencing a plugin in your app, refer to [Mobile plugins](../intro.md).

## Add necessary permissions (property list keys) for the plugin — iOS only

To use the Camera plugin on iOS, provide descriptions for the following property list keys:

* **NSCameraUsageDescription**
* **NSPhotoLibraryUsageDescription**
* **NSPhotoLibraryAddUsageDescription**
* **NSMicrophoneUsageDescription**

The plugin provides default values for these descriptions. From version 1.4.0 of the plugin, you set your own descriptions using the extensibility settings: **CameraUsageDescription**, **NSPhotoLibraryUsageDescription**, **NSPhotoLibraryAddUsageDescription**, and **NSMicrophoneUsageDescription**. Set these in the **Mobile distribution** tab on your app's detail page in the Portal.

## Demo app

Install the **Camera Sample App** from Forge and open the app in ODC Studio.
The demo app contains logic for common use cases to examine and recreate in your apps.
For example, the demo app shows how to:

* Take a photo.
* Capture a video.
* Select media from the gallery.
* Edit a photo taken with the camera or selected from the gallery.
* Edit the photo displayed in the app.

![Screenshot of the Camera Sample App interface in ODC Studio](images/camera-sample-app-ss.png "Camera Sample App")

## Take a photo

To let users take a photo and have a good user experience:

* [Create a user interface](#user-interface-photo)
* [Create logic to take a photo](#logic-photo)
* [Handle errors](#handle-errors)

### Create a user interface {#user-interface-photo}

To set up the user interface for taking a photo, follow these steps:

1. Create a variable with the data type **MediaResult**. This variable holds the image data. For more information about the **MediaResult** structure, refer to the [reference article](./camera-ref.md#mediaresult-data-structure).
1. Add a Button or another widget to run the action that takes the photo.
1. Add an **Image** widget to show the image thumbnail after using the camera. Set **Type** to **Binary Data** and **Image Content** to the content of **MediaResult.Thumbnail**.

![User interface setup for taking photos with the Camera plugin](images/camera-interface-setup-ss.png "UI Setup for Taking Photos")

<div class="info" markdown="1">

Alternatively, use the pre-built widget included with the plugin. In ODC Studio, navigate to **Interface** > **UI Flows** > **Camera Plugin** > **Camera Plugin**, and drag the **TakePhoto** Block to your Screen. Then use the **OnClick** event to receive the returned result and assign it to the variable you created in step 1.

</div>

### Create logic to take a photo {#logic-photo}

To take a photo using the Camera plugin, configure the app logic that connects user actions to the device camera. The following steps outline how to enable the camera, specify options, and receive the captured image.

<div class="info" markdown="1">

Find all available actions for the Camera plugin by navigating to the **Logic** tab of ODC Studio, and going to **Client Actions** > **CameraPlugin**.

</div>

1. Use the **CheckCameraPlugin** action to verify if the plugin is available.
    * If the plugin is not available, display an error message to the user.
1. If the plugin is available, use the **TakePhoto** action to open the camera and let the user take a photo.
    * In the **TakePhoto** action, set parameters such as quality, width, and camera direction (back or front) based on your app's requirements.
1. Check if **TakePhoto.Success** is **True**.
1. If successful, assign **TakePhoto.MediaResult** to a variable of the **MediaResult** data type to handle the captured image.

![Flowchart demonstrating the logic for taking a photo with the Camera plugin](images/camera-flow-take-pic-ss.png "Take Photo Logic Flow")

For more information about error handling, refer to [Handle errors](#handle-errors).

## Record a video

<div class="info" markdown="1">

Applies to native mobile apps only. Not available in PWAs.

</div>

To let users record a video and have a good user experience:

* [Create a user interface](#user-interface-video)
* [Create logic to record a video](#logic-video)
* [Handle errors](#handle-errors)

### Create a user interface {#user-interface-video}

To set up the user interface for recording a video, follow these steps:

1. Create a variable with the data type **MediaResult**. This variable holds the video data.
1. Add a Button or another widget to run the action that captures a video.
1. Add the **PlayVideo** widget to play the video after using the camera. Set the URI to the variable you created with **MediaResult.Uri**.

The **PlayVideo** widget plays recorded or locally stored videos on a device.
To display videos from other sources, use the [**Video**](../../../building-apps/ui/patterns/interaction/video.md) widget.

<div class="info" markdown="1">

The **RecordVideo** action includes an **IsPersistent** parameter that persists videos in your app. It is **True** by default. Set it to **False** to save the video in cache instead. Video files stored in the cache are deleted when the app closes. If you set the URI parameter to a cached video file, the video might already be deleted.

If you don't plan to play the video after closing the app and want to save device storage, set **IsPersistent** to **False**.

</div>

![Flowchart showing the initial steps in the logic for capturing a video](images/capture-video-logic-1-ss.png "Capture Video Logic Flow 1")

### Create logic to record a video {#logic-video}

To capture and manage video recordings in your app, set up logic that checks for plugin availability, initiates the recording, and stores the resulting media.

To create logic to record a video, follow these steps:

1. Use the **CheckCameraPlugin** action to verify if the plugin is available.
    * If the plugin is not available, display an error message to the user.
1. If the plugin is available, use the **RecordVideo** action to open the camera and let users capture a video.
    * In the **RecordVideo** action, configure parameters such as saving the recorded media to the device's gallery.
1. Check if **RecordVideo.Success** is **True**.
1. If successful, assign **RecordVideo.MediaResult** to a variable of the **MediaResult** data type to handle the video data.

![Flowchart showing the subsequent steps in the logic for capturing a video](images/capture-video-logic-2-ss.png "Capture Video Logic Flow 2")

For more information about error handling, refer to [Handle errors](#handle-errors).

## Select media from the gallery

<div class="info" markdown="1">

Applies to both mobile apps and PWAs, but with [limited support on PWAs](#pwa-functionality).

</div>

The **ChooseFromGallery** action lets users choose a media file from the device gallery, either a photo, a video, or both. The following example illustrates selecting a single photo from the gallery.

To select media from the gallery, follow these steps:

1. Use the **ChooseFromGallery** action to open a media browser and let users select a media file.
1. Verify **ChooseFromGallery.Success** is **True**. For more information about error handling, refer to [Handle errors](#handle-errors).
1. After users select the image, retrieve the binary data from **ChooseFromGallery.MediaResult.Current.Thumbnail**.

![Flowchart illustrating the process of selecting media from the gallery](images/camera-flow-choose-from-gallery-ss.png "Open from Gallery")

## Upload media assets from URIs

Use the video and photo URIs returned in the **MediaResult** variable, together with the **FileTransfer** plugin, to upload media files to a server. Then use the hosted URLs to view the media files in your app.

In the following example, the **UploadFile** client action from the **FileTransfer** plugin uploads a video file to the app's REST endpoint `rest/tickets/video`.

![Screenshot of the FileTransfer plugin's UploadFile client action](images/file-transfer-upload-video-ss.png "Upload Video")

Upload the video file to an S3 bucket inside the REST endpoint, then use the video's presigned URL with the **Video** widget to play the uploaded video.

![Diagram showing the process of uploading a video file to an S3 bucket](images/object-put-ss.png "S3 Object Put")
![Diagram illustrating how to retrieve a presigned URL for a video stored in S3](images/get-url-ss.png "S3 Object Get PreSignedUrl")

## Image quality and app responsiveness

When you set **100%** image **Quality** or use the **PNG** format, your app handles a large amount of image data.
Users experience slower response times after taking an image with the highest quality settings.
The more data the app handles, the less responsive it becomes on low-end devices.

When setting the image quality, consider the use case for your app.
The following table shows examples of quality settings for common use cases.

| Example use case | Image quality          | Notes                                                     |
| ---------------- | ---------------------- | --------------------------------------------------------- |
| Profile image    | JPEG 60% (default)     | Sufficient quality for a profile image.                   |
| Insurance claims | JPEG 85% - 100% or PNG | High quality lets users examine all details in the image. |

<div class="info" markdown="1">

Changing the image quality setting applies only to .JPEG files.

</div>

## Handle errors

The app with the Camera plugin runs on many Android and iOS devices with different hardware and configurations.
To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

The following table lists the actions and variables that handle errors.

| Variable | Action | Description |
| - | - | - |
| **IsAvailable** | **CheckCameraPlugin** | True if the camera plugin is available in the app. |
| **Success** | **TakePhoto** | True if there aren't errors while taking a photo. |
| **Success** | **EditPhoto** | True if there aren't errors while editing a photo. |
| **Success** | **EditURIPhoto** | True if there aren't errors while editing a photo. |
| **Success** | **RecordVideo** | True if there aren't errors while recording a video. |
| **Success** | **ChooseFromGallery** | True if there aren't errors while opening a media file from the gallery. |
| **Success** | **PlayVideo** | True if there aren't errors while playing a video. |

Use these actions with **If** nodes to check for errors and control how the app works.

![Flowchart for handling errors within the Camera plugin](images/camera-handling-errors-ss.png "Handling Errors in the Camera Plugin")

Errors return an **Error** structure with **ErrorCode** and **ErrorMessage**. For information about specific error codes and how to handle them, refer to the [error codes section in the reference article](./camera-ref.md#error-codes).

## Reference

The following sections contain additional reference information about the plugin.

The plugin is compatible with both Cordova and Capacitor. Starting in version 2.0.0, a [Capacitor Plugin](https://github.com/ionic-team/capacitor-camera) is used for Capacitor apps and a <!-- vale OutSystems.BrandTerms = NO -->[Cordova plugin](https://github.com/ionic-team/cordova-outsystems-camera)<!-- vale OutSystems.BrandTerms = YES --> is used in Cordova apps. The plugin offers the same functionality in both runtimes, with no gaps between them.

For reference on available client actions and structures, refer to the [Camera Plugin reference article](camera-ref.md).

### MABS compatibility

The following table shows the compatibility of the Camera plugin with the Mobile Apps Builds Service (MABS).

| Plugin version | Compatible with MABS version | Notes |
| ---------------- | ---------------------------- | ----- |
| 2.0.0 and later | MABS 11.2 and later. | - |
| 1.3.3 and later | MABS 11.2 and later. | - |
| 1.1.4 to 1.3.2 | MABS 11.2 only. | Consider updating to MABS 12. When you do, also update the Camera Plugin to the latest version. For information about moving to version 2.0.0, refer to the [migration article](camera-migration-guide-1-to-2.md). |

## PWA functionality

In PWAs, the camera plugin has the following limitations compared to native mobile apps:

* The **RecordVideo** and **PlayVideo** client actions and Blocks aren't available. Video capture and playback are available in native mobile apps only.
* The **EditURIPhoto** client action and Block aren't available. Use **EditPhoto**.
* The **ChooseFromGallery** client action and Block have limited functionality. They only allow selecting one photo at a time and don't allow video selection.
* The **MediaResult** data structure only offers **Type** and **Thumbnail** attributes. **URI** and **Metadata** are available in native mobile apps only. Use **Thumbnail** to retrieve the image captured by the camera.

## Known issues and workarounds

The following sections describe known issues and possible workarounds.

### Taking multiple photos doesn't work in PWAs

In PWAs, taking multiple photos requires browser stream capabilities.
To ensure the app has access to the stream, add the theme **CameraPlugin** as an element to your app.
**Keep the theme as a dependency even when the IDE reports it as not used by the app**.

### Taking multiple photos doesn't work on some PWA devices

On some devices, the workaround described in the previous section shows a defective UI.
There's no workaround for this issue.

### Photos appear rotated

**Applies to PWAs.**

In some Chrome versions, the photo displays rotated in the **Image** widget.
There's no workaround for this issue.

### Resolution and quality settings apply to app images only

**Applies to native apps only.**

When you change the resolution or quality setting, the plugin applies it only to the image the app uses.
The device ignores the settings when saving the images in the device gallery.
The size of the image in the gallery depends on the device hardware.

## Related resources

* [Camera Plugin version 1](camera-version-1.md)
* [Camera Plugin migration article from version 1 to 2](camera-migration-guide-1-to-2.md)
* [Camera Plugin version 2 reference article](camera-ref.md)
