---
summary: No public properties/fields found in the struct decorated with OSStructure '<StructureName>'.
tags: error handling, struct declaration, c# programming, code examples, outsystems error codes
guid: 68de8b43-f63f-4791-909b-ca1a8869824f
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - unblock
---

# OS-ELG-MODL-05013

## Error message

`No public properties/fields found in the struct decorated with OSStructure '<StructureName>'.`

## Cause

The error occurs because there are no public properties or fields in the struct decorated with the `OSStructure` attribute.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Add at least one public property or field to the struct.

For example, suppose you have the following code with a struct that has no public properties or fields:

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure
    {
        private int PrivateValue;
    }

To resolve the error, add a public property or field to the struct:

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure
    {
        private int PrivateValue;
        public int PublicValue;
    }

Now the struct has a public property/field, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05013).
