---
summary: "The assembly <AssemblyName>, which contains the interface decorated with the OSInterface attribute, is not located in the root directory of the zip file."
tags:
guid: 2aebb901-40e1-4c06-9fe9-2e004b1f0f56
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-ELG-MODL-05027

## Error message

`The assembly <AssemblyName>, which contains the interface decorated with the OSInterface attribute, is not located in the root directory of the zip file.`

## Cause

The error message means the .NET assembly containing the interface decorated with the `OSInterface` attribute isn't located in the root directory of the ZIP file.

The error is often caused by uploading a ZIP file containing the parent folder of the interface rather than the files inside the folder.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must upload the new ZIP file.

## Recommended action

Make sure the interface decorated with the `OSInterface` attribute is located in the root folder of the ZIP file.

If you have a .NET project with a structure like this:

    |__MyExternalLibrary
       |--MyDll.dll
       |--AnotherDll.dll

Select all files inside `MyExternalLibrary` and zip them instead of the `MyExternalLibrary` folder itself.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05027).
 
