---
summary: "The property/field decorated by OSIgnore '<ParameterName/StructureFieldName>' in struct '<StructureName>' is not public."
tags:
guid: 634c055e-4230-4fad-a61a-28e05bbdc3e0
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05012

## Error message

`The property/field decorated by OSIgnore '<ParameterName/StructureFieldName>' in struct '<StructureName>' is not public.`

## Cause

The error occurs because a property or field decorated with the `OSIgnore` attribute in the struct isn't defined with the `public` access modifier.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make the property or field public.

For example, suppose you have the following code with a non-public field decorated with `OSIgnore`:

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure
    {
        [OSIgnore]
        int IgnoredValue;
    }

To resolve the error, change the access modifier of the `IgnoredValue` field to `public`:

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure
    {
        [OSIgnore]
        public int IgnoredValue;
    }

Now the field is public, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05012).
