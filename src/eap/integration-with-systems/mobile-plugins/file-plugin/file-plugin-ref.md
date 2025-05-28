---
summary: Explore the File Plugin functionalities on OutSystems Developer Cloud (ODC), including client actions, error handling, and deprecations.
tags: mobile app development, plugin integration, file management, error handling, deprecations
locale: en-us
guid: b6aad61f-35d7-4cf4-87bb-9a592d200984
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# File Plugin version 2 reference page

<div class="info" markdown="1">

If you are looking for information about version 1.x of the File Plugin, refer to the [Version 1 documentation](file-plugin-version-1.md).

</div>

<div class="info" markdown="1">

If you are looking to migrate from version 1.X.X of the File Plugin to 2.0.0 or higher, refer to the [migration guide](file-plugin-migration-guide.md).

</div>

This is the reference of all the functionality you can use from the [File Plugin version 2.0.0](intro.md). The File Plugin version 2.0.0 uses Cordova and Capacitor plugins. For more information see [cordova-outsystems-file](https://github.com/ionic-team/cordova-outsystems-file) and [capacitor/filesystem](https://github.com/ionic-team/capacitor-filesystem). For versions 1.X.X, see [cordova-plugin-file](https://github.com/OutSystems/cordova-plugin-file).

## Plugin elements

This section details the different elements exposed by the File Plugin, starting on version 2.0.0. For older versions, refer to [Deprecated Elements](#deprecated-elements).

### Actions

| Action               | Description                                                                           |
| -------------------- | ------------------------------------------------------------------------------------- |
| **AppendFile**       | Appends content to an existing file.                                                  |
| **CheckFilePlugin**  | Checks if the File Plugin is loaded.                                                   |
| **Copy**             | Copies a file from one location to another.                                             |
| **CreateDirectory** | Creates a directory in the file system.                                               |
| **DeleteDirectory**  | Deletes a directory in the file system.                                               |
| **DeleteFile**       | Deletes a single file.                                                                |
| **GetFileUri**       | Returns the file's URI.                                                               |
| **GetMetadata**      | Gets metadata information on a file or directory. See [File Info](#file-info).        |
| **ListDirectory**    | Lists the contents of a directory (any files and sub-directories).                    |
| **ReadFile**         | Reads the contents of a file.                                                         |
| **Rename**           | Renames an existing file or directory.                                                 |
| **WriteFile**        | Writes content to a file. This action overwrites data written to the file previously. |

### Path directory

Most operations in the File Plugin have two attributes: **Path** and **Directory**, each with a different purpose. The **Directory** is an optional specific location in the file system. If it is specified, then the **Path** should be the relative path from that directory. If not, then **Path** should contain the full path to file.

The table below details the types of **PathDirectory** entries.

| **PathDirectory**     | Description                                                                                                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DOCUMENTS**         | A directory to store documents. For iOS it's stored within the app's sandbox. On Android, it's a public directory, and access is limited for Android 11 and above.      |
| **DATA**              | The application's data directory for holding files on Android. On iOS, **DOCUMENTS** is used.                                                                          |
| **LIBRARY**           | The top-level directory for non user data files on iOS - backed by iCloud. On Android, **DATA** is used.                                                |
| **CACHE**             | The application's cache directory. The Operating System may delete files in this directory. Use this when you have non-persistent files that can be re-created easily. |
| **EXTERNAL**          | On Android, it's similar to the **DATA** directory, but it's stored in the primary external storage. On iOS, **DOCUMENTS** is used.                                      |
| **EXTERNAL_CACHE**    | On Android, it's similar to the **CACHE** directory, but it's stored in the primary external storage. On iOS, **DOCUMENTS** is used.                                     |
| **EXTERNAL_STORAGE**  | The device's primary external storage directory (e.g. SD Card) on Android; access is restricted for Android 11 and above. On iOS, **DOCUMENTS** is used.                  |
| **TEMPORARY**         | A directory for storing temporary files on iOS, within the app's sandbox. On Android, **CACHE** is used.                                                               |
| **LIBRARY_NO_CLOUD**  | Similar to **LIBRARY**, except that it's not backed by iCloud. On Android, **DATA** is used.                                                                           |

<div class="info" markdown="1">

There are several directory types to allow to access the different kinds of relevant locations in the device's file system for both Android and iOS. Some directories exist only on one platform, but the system uses fallbacks to ensure you can use all **PathDirectory** types on both Android and iOS.

If you're unsure which type of **PathDirectory** you need, try to think about the type of files you are handling, and whether your app runs on Android, iOS, or both. For instance, if you have an app on both operating systems, and you need to store temporary files, you can use **TEMPORARY**.

</div>

### File info

The **GetMetadata** and **ListDirectory** client actions return a structure containing information about a file or directory, named **FileInfo**. The table below describes the attributes of this structure.

| **FileInfo** attributes | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| **Name**                | Name of the file or directory.                         |
| **Type**                | The type - either **Directory** or **File**.           |
| **Size**                | File size in bytes.                                    |
| **CreationTime**        | Date Time of creation.                                 |
| **ModificationTime**    | Date Time of last modification.                        |
| **URI**                 | Full URI path to the file or directory (e.g. file://). |

### Errors

Starting on version 2.0.0 of the File Plugin, specific errors are returned on native platforms.

| Error code        | Platform(s)      | Message                                                                                             |
| ------------------| ---------------- | --------------------------------------------------------------------------------------------------- |
| OS-PLUG-FILE-0001 | Android, iOS     | Cordova and Capacitor isn't defined.                                                                |
| OS-PLUG-FILE-0002 | Android, iOS     | The app is running with an old version of the plugin. Please create a new mobile package.           |
| OS-PLUG-FILE-0003 | Android, iOS     | The File plugin is not defined. Make sure the mobile package is valid.                              |
| OS-PLUG-FILE-0004 | iOS              | Cordova / Capacitor bridge isn’t initialized.                                                       |
| OS-PLUG-FILE-0005 | Android, iOS     | The action input parameters aren’t valid.                                                           |
| OS-PLUG-FILE-0006 | Android, iOS     | Invalid path was provided.                                                                          |
| OS-PLUG-FILE-0007 | Android          | Unable to perform file operation, user denied permission request.                                   |
| OS-PLUG-FILE-0008 | Android, iOS     | Operation failed because file does not exist.                                                       |
| OS-PLUG-FILE-0009 | Android          | Operation not supported for provided input.                                                         |
| OS-PLUG-FILE-0010 | Android, iOS     | Directory already exists, cannot be overwritten.                                                    |
| OS-PLUG-FILE-0011 | Android, iOS     | Missing parent directory – possibly recursive=false was passed or parent directory creation failed. |
| OS-PLUG-FILE-0012 | Android, iOS     | Cannot delete directory with children; received recursive=false but directory has contents.         |
| OS-PLUG-FILE-0013 | Android, iOS     | The operation failed with an error.                                                                 |

## Deprecated elements

The following section details the elements that were available in version 1.X.X of the File Plugin. These were marked as deprecated in version 2.0.0.

<div class="warning" markdown="1">

All deprecated elements include the prefix **DEPRECATED_** before the element name.

</div>

### Deprecated actions

| Action                            | Description                                                       |
| --------------------------------- | ----------------------------------------------------------------- |
| **DEPRECATED_CheckFilePlugin**    | Enables to check if the plugin was loaded.                        |
| **DEPRECATED_CreateDirectory**    | Recursively creates a directory in the file system.               |
| **DEPRECATED_DeleteDirectory**    | Deletes a directory and all its content in the file system.       |
| **DEPRECATED_DeleteFile**         | Deletes a single file.                                            |
| **DEPRECATED_DeleteFileFromUri**  | Deletes a single file from a URI address.                         |
| **DEPRECATED_GetFileData**        | Returns the binary file encoded in Base64.                        |
| **DEPRECATED_GetFileDataFromUri** | Returns the binary file encoded in Base64 from a file's URI path. |
| **DEPRECATED_GetFileUri**         | Returns the file's URI path.                                      |
| **DEPRECATED_GetFileUrl**         | Returns the file's blob URL path (blob://).                       |
| **DEPRECATED_GetFileUrlFromUri**  | Returns the file's blob URL path from a file's URI path.          |
| **DEPRECATED_ListDirectory**      | Lists the directory's content.                                    |
| **DEPRECATED_SaveFile**           | Saves a file in a specific directory.                             |
| **DEPRECATED_SaveTemporaryFile**  | Saves a file in a temporary directory.                            |

### Storage type

These section contains information about the **StorageTypeId** property, which tells the app where to store the files. This property is available in some actions of the plugin. Newer versions of the File Plugin use [Path Directory](#path-directory).

| StorageTypeId                     | Description                                                                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entities.StorageType.Internal** | Sandboxed app data in the internal memory. Corresponds to Cordova's **cordova.file.dataDirectory** (for **StoragePersistence.Persistent**).             |
| **Entities.StorageType.External** | App data on an external storage. Corresponds to Cordova's **cordova.file.externalDataDirectory** (for **StoragePersistence.Persistent**). Android only. |

For more information check out the document [Where to Store Files](https://github.com/OutSystems/cordova-plugin-file#where-to-store-files) from Cordova.
