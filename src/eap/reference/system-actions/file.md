---
summary: OutSystems Developer Cloud (ODC) File system actions generate signed URLs, copy files into your app, and check whether a file exists in cloud storage.
tags:
  - Data
  - Logic
  - Security
locale: en-us
guid: 73e228e4-6887-49a7-a38f-d530fa17b6d2
app_type: mobile apps, reactive web apps
platform-version: odc
content-type:
  - reference
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - remember
topic:
  - file-storage
isautopublish: true
---

# File system actions

Use the File system actions to generate access URLs for **File** values, copy a file into your app, and check whether a file exists in cloud storage. The actions are in the **(System)** folder under **Server Actions** in the Logic tab in ODC Studio.

These actions are server actions. They don't appear in the **(System)** folder under **Client Actions**. The File type isn't available on ODC Self-Hosted. For more information, refer to [File data type](../../building-apps/data/binaries/binaries-native-cloud.md#quick-facts).

The following table lists the File system actions. Select an action name to go to its description.

| Name | Description |
| --- | --- |
| [GetFileSignedURL](#getfilesignedurl) | Generates a signed URL to access a stored file. |
| [GetMultipleFilesSignedURLs](#getmultiplefilessignedurls) | Generates signed URLs to access a list of stored files in a single call. |
| [CopyFile](#copyfile) | Creates a copy of a file and its content as a temporary file that the current app owns. |
| [FileExists](#fileexists) | Checks whether a file exists in cloud storage. |

## Actions

### `GetFileSignedURL`

#### Server action

Generates a signed URL to access a stored file. The URL grants temporary access to the file. The action returns the link, a success indicator, and an error message. For more information about how signed URLs work and how to use them safely, refer to [File access and signed URLs](../../building-apps/data/binaries/file-signed-urls.md).

#### Inputs

**File**
:   Type: File. Mandatory.
    The file to generate a signed URL for.

**URLExpiration**
:   Type: Integer. Optional.
    Number of minutes the URL stays valid. If you don't set it, the URL stays valid for 30 minutes. The value can't exceed 48 hours. For more information, refer to [Time to live](../../building-apps/data/binaries/file-signed-urls.md#ttl).

**ResponseHeaders**
:   Type: [ResponseHeaders](#responseheaders). Optional.
    Settings that control how the delivery layer and the client device cache and present the file.

**URLDomain**
:   Type: Text. Optional.
    Custom domain to use when generating the signed URL. If you don't set it, ODC uses the default domain of the environment.

#### Outputs

**FileURL**
:   Type: Text.
    Signed URL for the file. The URL contains the path to access the file's storage location.

**Success**
:   Type: Boolean.
    Indicates whether ODC generated the URL.

**ErrorMessage**
:   Type: Text.
    Reason for a failure while generating the URL.

### `GetMultipleFilesSignedURLs`

#### Server action

Generates signed URLs to access a list of stored files in a single call. Each URL grants temporary access to its file. The action returns the links, a success indicator, and an error message.

Use this action when a screen renders a collection of files, such as the images that an aggregate returns.

#### Inputs

**Files**
:   Type: [FileURLRequest](#fileurlrequest) List.
    The files to generate signed URLs for. Each item holds a file and optional response header settings for that file. The list holds up to 100 items.

**URLExpiration**
:   Type: Integer. Optional.
    Number of minutes the URLs stay valid. If you don't set it, the URLs stay valid for 30 minutes. The value can't exceed 48 hours. The value applies to every URL in the list.

**URLDomain**
:   Type: Text. Optional.
    Custom domain to use when generating the signed URLs. If you don't set it, ODC uses the default domain of the environment.

#### Outputs

**FileURLs**
:   Type: Text List.
    Signed URLs for the files, in the same order as the **Files** input.

**Success**
:   Type: Boolean.
    Indicates whether ODC generated all the URLs. **Success** is `True` only when every requested URL is generated.

**ErrorMessage**
:   Type: Text.
    Reason for a failure while generating the URLs.

### `CopyFile`

#### Server action

Creates a copy of a file and its content as a temporary file that the current app owns. The copy isn't persistent until you store its reference in an entity attribute.

Use **CopyFile** when your app receives a **File** value that another app owns and your app needs to keep it. ODC doesn't let you save a file that another app owns in your app's entity. If you try, the save fails with the error `Cannot persist a file owned by a different asset`. Copy the file first, then store the copy. To decide whether a copy is needed, use the [IsOwnedByCurrentApp](../built-in-functions/file.md#isownedbycurrentapp) and [IsTemp](../built-in-functions/file.md#istemp) built-in functions.

ODC deletes a temporary file that you don't store in an entity. For more information about temporary files, refer to [File lifecycle in Upload files](../../building-apps/ui/patterns/interaction/upload-files.md#file-lifecycle).

#### Inputs

**File**
:   Type: File. Mandatory.
    The file to copy.

#### Outputs

**CopiedFile**
:   Type: File.
    The temporary copy of the file in the current app. To persist the file, store this reference in an entity attribute.

If the input file is empty, **CopyFile** returns an empty file.

### `FileExists`

#### Server action

Checks whether a file exists in cloud storage. **FileExists** is a function, so it works in expressions.

#### Inputs

**File**
:   Type: File. Mandatory.
    The file to check.

#### Outputs

**Exists**
:   Type: Boolean.
    `True` if the file exists in cloud storage. `False` if it doesn't exist or if the input file is empty.

## Structures

### `FileURLRequest`

Bundles a file with its response header settings. Use it as the item type of the **Files** input of [GetMultipleFilesSignedURLs](#getmultiplefilessignedurls).

**File**
:   Type: File.
    The file to generate a signed URL for.

**ResponseHeaders**
:   Type: [ResponseHeaders](#responseheaders). Optional.
    Settings that control how the delivery layer and the client device cache and present the file.

### `ResponseHeaders`

Overrides the default HTTP response headers that control how the delivery layer caches and serves the file.

**CacheControl**
:   Type: Text. Default: `private`.
    Caching rules for the content.

**ContentDisposition**
:   Type: Text.
    Whether the browser displays the content directly or downloads it as an attachment. For guidance on setting this value safely, refer to [Set the Content-Disposition header safely](../../building-apps/data/binaries/file-signed-urls.md#set-the-content-disposition-header-safely).

**ContentType**
:   Type: Text.
    Media type of the file. It tells the client how to interpret and render the data, such as an image or a document.

**CacheExpiration**
:   Type: DateTime.
    Date and time when the cached file becomes invalid.
