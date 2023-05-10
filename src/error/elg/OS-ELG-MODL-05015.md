---
summary: "The struct decorated with OSStructure '<StructureName>' contains a public property/field that uses an unsupported parameter type '<ParameterType>'."
tags:
guid: d9196bdf-4c67-44a1-bc6f-3dc0031eb260
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05015

## Error message

`The struct decorated with OSStructure '<StructureName>' contains a public property/field that uses an unsupported parameter type '<ParameterType>'.`

## Cause

A public property or field within the struct, decorated with `OSStructure`, has an unsupported parameter type.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Replace the unsupported type with one from the list of supported types:

    * Basic .NET types: `string`, `int`, `long`, `bool`, `byte[]`, `decimal`, `float`, `double`, `DateTime`.
    * Structs decorated with the `OSStructure` attribute.
    * Lists (any type inheriting from [IEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable?view=net-6.0)) of any of the previous two types.

For example:

    [OSStructure("MyStructure")]
    public struct MyStructure
    {
        public int Value;
        public UnsupportedType UnsupportedField; // This type is not supported by the SDK
    }

To fix the issue, change the `UnsupportedType` field to a supported type:

    [OSStructure("MyStructure")]
    public struct MyStructure
    {
        public int Value;
        public string SupportedField; // Replace the unsupported type with a supported one
    }

In the updated example, the unsupported `UnsupportedType` field has been replaced with a supported `string` field.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05015).
