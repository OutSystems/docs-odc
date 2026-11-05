---
summary: OutSystems Developer Cloud (ODC) File built-in functions return the size, MIME type, ownership, and temporary state of a File value, and create an empty File.
tags:
  - Data
  - Logic
locale: en-us
guid: 83d3decf-cb7f-48d1-aa28-30d84914a4be
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

# File

This reference lists the built-in functions that work with **File** values. They're in the **File** folder under **Built-in Functions** in the expression editor in ODC Studio. The File type isn't available on ODC Self-Hosted. For more information, refer to [File data type](../../building-apps/data/binaries/binaries-native-cloud.md#quick-facts).

The following table lists the File built-in functions. Select a function name to go to its description.

| Name | Description |
| --- | --- |
| [IsOwnedByCurrentApp](#isownedbycurrentapp)(File) | Checks if a file is owned by the current app. |
| [IsTemp](#istemp)(File) | Checks if a file is in temporary storage and hasn't been persisted. |
| [MIMEType](#mimetype)(File) | Returns the MIME type of a file. |
| [NullFile](#nullfile)() | Returns a null File value. |
| [Size](#size)(File) | Returns the size of a file in bytes. |

## `IsOwnedByCurrentApp`

Checks if a file is owned by the current app. Returns `True` if the file exists and is local to the app. Returns `False` if the file is null, invalid, or owned by another app.

When you call the function from a library, the current app is the consumer app in which the code runs.

Use this function to decide whether to copy a file before you store it. For more information, refer to the [CopyFile](../system-actions/file.md#copyfile) server action.

Available in:

* Server-side logic: Yes
* Client-side logic: No
* Database: Cannot be used inside aggregates with entity attributes as parameters.

### Parameters

file
:    Type: File. Mandatory.  
The file to check for ownership by the current app.

### Output

Type: Boolean

### Examples

```
IsOwnedByCurrentApp(Entity.Attribute) = True
```

## `IsTemp`

Checks if a file is in temporary storage and hasn't been persisted. Returns `True` if the file is temporary. Returns `False` if the file is persisted, null, or invalid.

A file is temporary until you store it in an entity attribute. For example, a file that a user uploads with the **Upload** widget is temporary until your app saves it.

Available in:

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Cannot be used inside aggregates with entity attributes as parameters.

### Parameters

file
:    Type: File. Mandatory.  
The file to check for temporary storage status.

### Output

Type: Boolean

### Examples

```
IsTemp(Entity.Attribute) = True
```

## `MIMEType`

Returns the MIME type of a file.

Available in:

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Can be used with attributes in server-side aggregates.

### Parameters

file
:    Type: File. Mandatory.  
The file to obtain the MIME type from.

### Output

Type: Text

### Examples

```
MIMEType(MyFile) = "application/pdf"
```

## `NullFile`

Returns a null File value. Use it to represent a file reference that points to no file. For more information about empty **File** values, refer to [The File data type](../../building-apps/data/binaries/binaries-native-cloud.md#quick-facts).

Available in:

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Can be used with attributes in server-side aggregates.

### Output

Type: File

### Examples

```
MyFile = NullFile()
```

## `Size`

Returns the size of a file in bytes.

Available in:

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Can be used with attributes in server-side aggregates.

### Parameters

file
:    Type: File. Mandatory.  
The file to obtain the size from.

### Output

Type: LongInteger

### Examples

```
Size(MyFile) = 245760
```
