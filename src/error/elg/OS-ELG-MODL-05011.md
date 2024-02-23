---
summary: "The property/field decorated by OSStructureField '<ParameterName/StructureFieldName>' in struct <StructureName> is not public."
tags:
guid: 719b1e88-d65f-4db4-9edb-6cd306902364
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-ELG-MODL-05011

## Error message

`The property/field decorated by OSStructureField '<ParameterName/StructureFieldName>' in struct <StructureName> is not public.`

## Cause

The error occurs because a property or field decorated with the `OSStructureField` attribute in the struct is not defined with the `public` access modifier.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make the property or field public.

For example, suppose you have the following code with a non-public field decorated with `OSStructureField`:

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure
    {
        [OSStructureField(Name = "Value")]
        int Value;
    }

To resolve the error, change the access modifier of the `Value` field to `public`:

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure
    {
        [OSStructureField(Name = "Value")]
        public int Value;
    }

Now the field is public, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05011).
