---
guid: d001af5a-0dca-4394-a783-6e4dfdf884ad
locale: en-us
summary: OutSystems Developer Cloud (ODC) File data type stores large content in cloud storage and supports 2 GB files, unlike BinaryData.
figma:
coverage-type:
  - understand
  - apply
  - evaluate
topic:
  - file-storage
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Architect
  - Tech lead
  - Developer
tags:
  - Aggregates
  - Data
  - Data Model
  - Entities
  - Lifecycle
  - Performance
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---
# File data type

**File** is a data type for large content, whether text or binary, such as images, PDFs, and other files, that ODC stores in cloud storage instead of the database. It acts as a reference, not a container: instead of holding bytes in memory, a **File** value points to content in object storage and loads it on demand.

<div class="info" markdown="1">

The **File** type isn't supported in ODC Self-hosted.

</div>

## Why use the file type

The **File** type removes the constraints that come with storing large content in the database:

* **No memory pressure**: File content is not loaded into the application's memory. The platform streams content directly from cloud storage.
* **Large file support**: Files up to 2,147,483,648 bytes (2 GB) are supported. **BinaryData** content travels inside the request body, which is capped at ~29 MB.
* **No timeout constraints**: Large file transfers are not subject to the 60-second application server timeout.
* **Direct HTTP access**: Browsers download File content directly from cloud storage, without routing bytes through the application server.

## File type

This is different from **BinaryData**, which caches content in runtime memory and loads the entire byte array when used. The two types coexist, each suited to different scenarios.

The following table summarizes the key differences.

| | **File** | **BinaryData** |
| --- | --- | --- |
| Storage | Cloud object storage | Runtime memory (cached) |
| Loading | Lazy (streams content on demand) | Eager (full bytes in memory) |
| Parameter passing | By reference | By copy |
| Supported in Local Storage entities | No | Yes |
| Maximum size | Up to 2 GB | ~29 MB |
| Returned by aggregate queries | As a URL reference | As bytes |

### File access

When an aggregate or server action returns a **File** value, the platform generates a signed URL to grant direct, time-limited access to the file in cloud storage. Refer to [File access and signed URLs](file-signed-urls.md) if you need to change the URL's expiry or embed it safely in your app's logic.

Each ODC environment's **File** content lives in its own storage location, separate from other environments' content. Requests for **File** content route through a delivery layer in front of cloud storage, which validates the signed URL's signature and policy on every request. Refer to [File access and signed URLs](file-signed-urls.md#ttl) for details on that validation.

### File lifecycle

The platform automatically manages the lifecycle of a **File** alongside the entity record that holds it. Refer to [File lifecycle](file-reference-lifecycle.md) for details on file states, reference counting, and disaster recovery.

## Replace a BinaryData attribute with a file attribute { #replace-binarydata }

You can't change the data type of an existing attribute between **BinaryData** and **File**. Publishing fails with an error. ODC doesn't migrate the content stored in the old attribute, so you must write your own migration logic.

To replace a **BinaryData** attribute with a **File** attribute, do the following:

1. Add a new attribute to the entity with a different name and the **File** data type.
1. Update the screens and logic that use the old attribute to use the new attribute.
1. Publish the app with both attributes. The migration needs both attributes, so you can't delete the old attribute yet.
1. Run your migration logic to copy the content from the old attribute to the new attribute, for example, with a timer.
1. After the migration finishes, delete the old **BinaryData** attribute and publish the app again.

## Quick facts {#quick-facts}

A **File** value carries the following properties, size limit, and restrictions.

* **Properties**:
    * **MIMEType**: the media type of the file, for example, `application/pdf`.
    * **Size**: the file size in bytes.
* **Maximum size**: up to 2 GB, as shown in the comparison table.
* **Changing an existing attribute's type**: you can't change an attribute between **BinaryData** and **File**. Publishing fails with an error. To replace the attribute, add a new attribute with a different name. For more information, refer to [Replace a BinaryData attribute with a File attribute](binaries-native-cloud.md#replace-binarydata).
* **Not available in**:
    * **Local entities**: local entities exist on the device and don't support **File** attributes. The data type picker doesn't show **File** when you edit a local entity.
    * **Library asset types**: input and output parameters in libraries don't support **File** as a type, since libraries hold only logic and UI, not data.
    * **Default Value property**: ODC disables the **Default Value** property for **File** attributes. Use `NullFile()` in your logic to represent an empty file reference. For more information, refer to [File built-in functions](../../../reference/built-in-functions/file.md).
    * **Data mashup queries**: the File type isn't supported in mashup queries. For more information about data mashup, refer to [Combine data from different sources using data mashup](../fetch-data/data-mash.md).

## Next steps

After understanding when to use the **File** type, you can explore how to work with it in practice:

* [Choose between file and BinaryData for storing binary content](../data-best-practices/intro.md#choose-file-binarydata): learn when to use **File** instead of **BinaryData**.
* [File lifecycle](file-reference-lifecycle.md): learn how a **File** reference behaves in entities and aggregates, and how ODC manages it over time.
* [Upload files](../../ui/patterns/interaction/upload-files.md): learn how to handle file uploads from users and save them as **File** values.
* [Download files](../../ui/patterns/interaction/download-files.md): learn how to download files stored in cloud storage using the Download node.
* [Displaying images from cloud storage](../../ui/patterns/interaction/display-images.md): learn how to bind **File** values to the Image widget and configure caching.
* [File access and signed URLs](file-signed-urls.md): learn how ODC grants temporary access to files in cloud storage.
* [Working with file values](working-with-file-in-external-logic.md): learn how to read and write **File** values in External Library functions.
* [Preview file data in ODC Studio](file-data-preview.md): learn how ODC Studio previews **File** values in Edit Data, Advanced SQL test queries, and the debugger.
* [File system actions](../../../reference/system-actions/file.md): look up the inputs and outputs of the server actions that generate signed URLs, copy files, and check whether a file exists.
* [File built-in functions](../../../reference/built-in-functions/file.md): look up the functions that return the size, MIME type, ownership, and temporary state of a **File** value.
