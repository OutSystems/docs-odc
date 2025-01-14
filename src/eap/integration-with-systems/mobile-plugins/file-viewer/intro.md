---
summary: Learn how to use the File Viewer Plugin in OutSystems Developer Cloud (ODC) to open and manage files within mobile apps.
tags: file management, plugins, cross-platform development, user interface, app development
locale: en-us
guid: 0e246269-47c6-47c6-ba92-308f35edcd40
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A7639&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# File Viewer Plugin

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Use File Viewer Plugin to create logic that lets users open remote or app resource files. In Android users select an app to open the file. iOS provides a native preview for supported file types.

<div class="info" markdown="1">

See [Installing plugins](../intro.md) to learn how to install and reference a plugin in your OutSystems apps.

</div>

File Viewer Plugin can open:

* **File from the app resources**. The plugin can access the **resources** path to load the file that's part of the app static content. See [Working with app resources](#working-with-app-resources)
* **Remote file**. The plugin downloads the file to the app sandbox and then opens the file.

![Preview image of the File Viewer Plugin interface](images/file-viewer-preview.png "File Viewer Plugin Preview")


## Viewing files in Android and iOS

To let users view files in the mobile apps, create logic with the action **OpenDocument**. You need to supply a path to a local file in the **FilePath** property or to a remote file in the **URL** property.

If you want to open a file from the app resources see [Working with app resources](#working-with-app-resources).

For an example of how to use the plugin check the demo app or refer to [the example in this document](#example-of-using-file-viewer-plugin).

<div class="info" markdown="1">

For opening media files in the iOS apps, use the action **PreviewMediaContent** from **FileViewerPlugin** > **iOSOnly**. This action lets apps handle the media files better by opening them in a media player.

</div>

## Working with app resources

Here is how to add a file as a resource and open the file with the plugin.

1. In ODC Studio, go to the **Data** tab.

2. Right-click the **Resources** folder and select **Import resources**. A file dialog opens, where you can select the file you want to add as a resource.

3. Select the file you added under **Resources**, and:

    * Enter `resources` in the **Target Directory** property. Note that this value must be `resources` and you can't change it.
    * Select **Deploy to Target Directory** in the **Deploy Action** list.

    ![Screenshot showing the resources properties settings for the File Viewer Plugin in ODC Studio](images/resources-file-viewer-ss.png "Resources Properties for File Viewer")

4. In the **OpenDocument** action enter `"resources\<file name>"` in the **FilePath** property. For example, if you add **sample.pdf** to **Resources**, the value of  **FilePath** is `"resources\sample.pdf"`.


<div class="info" markdown="1">

The plugin can access only resources you deploy in the **resources** path. This is a security limitation by design. Limiting access of the plugin prevents accidental access to the resources of the app.

</div>

## Example of using File Viewer Plugin

Here is an example of how to use File Viewer Plugin.

![Screenshot of the logic flow for using the File Viewer Plugin in a mobile app](images/logic-file-viewer-ss.png "Logic for File Viewer Plugin")

A good practice is to check if the plugin is available to the app, and report an error if it's not. You can check the plugin availability by using the **CheckPlugin** action and checking the value of the **CheckPlugin.IsAvailable** boolean (1).

When you confirm the plugin is available, use the **OpenDocument** (2) action to ask the operating system to view the file. The action accepts either a **URL** for remote files or **FilePath** for a [file from the app resources](#working-with-app-resources) (3). 

## Reference

More information about parts of the plugin.

### Actions

Here is the reference of the actions you can use from the File Plugin. File Plugin uses a Cordova plugin, and for more information check out [cordova-outsystems-file-viewer](https://github.com/OutSystems/cordova-outsystems-fileviewer).

| Action                  | Description                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------ |
| **CheckPlugin**         | Checks if the plugin is available in the app.                                        |
| **OpenDocument**        | Opens a remote file or a [file from the app resources](#working-with-app-resources). |
| **PreviewMediaContent** | iOS only. Action to preview media content.                                           |
