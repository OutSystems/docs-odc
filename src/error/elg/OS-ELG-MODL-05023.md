---
summary: "The assembly <AssemblyName> is required and could not be found in your file."
tags:
guid: 7a710394-e576-4885-8175-a5dbac24cb6d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05023

## Error message

`The assembly <AssemblyName> is required and could not be found in your file.`

## Cause

The error occurs because your project code uses a type in an assembly that isn't included in the ZIP file.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make sure the required assembly is included in your external library. Check:

-  It's properly referenced.
-  It's not marked as `PrivateAssets` in case it's a NuGet reference.
-  You're [using `dotnet publish`](../../eap/building-apps/external-logic/README.md#usage) and including all resulting assemblies in the ZIP file.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05023).
