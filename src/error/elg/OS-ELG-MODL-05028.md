---
summary: "The assembly <AssemblyName>, which contains the interface decorated with the OSInterface attribute, is not located in the root directory of the zip file."
tags:
guid: 2aebb901-40e1-4c06-9fe9-2e004b1f0f56
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05028

## Error message

`The file <FileName> can not be uncompressed.`

## Cause

The file contained in the compressed high code package cannot be uncompressed.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must upload the new ZIP file.

## Recommended action

* Ensure that the compressed folder only contains the necessary assemblies and not the entire source code of your dotnet solution.
* If the file isn't necessary for your high code package, remove it. If the file is necessary, or the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05028).
