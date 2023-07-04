---
summary: "<ParameterName/StructureFieldName> has an incompatible DataType assigned and cannot be converted."
tags:
guid: c8d919be-c4be-4edf-a55f-fbd333ce5115
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-ELG-MODL-05017

## Error message

`<ParameterName/StructureFieldName> has an incompatible DataType assigned and cannot be converted.`

## Cause

The `DataType` assigned to a property or field is incompatible with its corresponding .NET type. It can't be automatically converted to the specified OutSystems type.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Ensure that the .NET type and `DataType` modifier are compatible according to the valid mappings table:

| C# type | OutSystems type | DataType modifier |
| --- | --- | --- |
| string | Text |     |
| string | Email | Email |
| string | PhoneNumber | PhoneNumber |
| decimal | Decimal |     |
| decimal | Currency | Currency |
| DateTime | DateTime |     |
| DateTime | Date | Date |
| DateTime | Time | Time |

Use the correct `DataType` modifier for the .NET type to map it to the desired OutSystems type.

For example, if you have the following code:

    [OSStructureField(DataType = "Currency")]
    public string Price { get; set; }

Modify if to:

    [OSStructureField(DataType = "Currency")]
    public decimal Price { get; set; }

Now, the .NET type `decimal` is correctly mapped to the OutSystems type `Currency`, which is specified by the `DataType` modifier.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05017).
