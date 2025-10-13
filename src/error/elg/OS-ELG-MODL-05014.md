---
summary: More than one structure, '<StructureName>', was found with the name '<Name>'.
tags: error handling, c# programming, software development, application publishing, external libraries
guid: 1a9f211a-fad0-4cbf-8dda-21c3359f0ee6
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

# OS-ELG-MODL-05014

## Error message

`More than one structure, '<StructureName>', was found with the name '<Name>'.`

## Cause

The error occurs because multiple structures are using the same name in the `Name` parameter of the `OSStructure` attribute.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

To solve this issue, you should ensure that each structure with the `OSStructure` attribute has a unique name. For example:

**Before**

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure1
    {
        public int Value;
    }

    [OSStructure(Name ="MyStructure")]
    public struct MyStructure2
    {
        public float Value;
    }

**After**

    [OSStructure(Name = "MyStructure1")]
    public struct MyStructure1
    {
        public int Value;
    }

    [OSStructure(Name = "MyStructure2")]
    public struct MyStructure2
    {
        public float Value;
    }

In the corrected example, the `OSStructure` attribute names are unique: `MyStructure1` and `MyStructure2`. This resolves the error.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05014).
