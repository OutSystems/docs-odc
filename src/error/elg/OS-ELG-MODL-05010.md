---
summary: The struct decorated with OSStructure '<StructName>' is not public.
tags: c# programming, software development, public access modifier, code modification, error resolution
guid: 22aaeb98-4f58-4b37-ae14-eaf8502aabe7
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
outsystems-tools:
  - odc studio
coverage-type:
  - unblock
---

# OS-ELG-MODL-05010

## Error message

`The struct decorated with OSStructure '<StructName>' is not public.`

## Cause

The error occurs because the struct decorated with the `OSStructure` attribute isn't defined with the `public` access modifier.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make the struct public.

For example, suppose you have the following code with a non-public struct decorated with `OSStructure`:

    [OSStructure(Name = "MyStructure")]
    struct MyStructure
    {
        public int Value;
    }

To resolve the error, change the access modifier of the `MyStructure` struct to `public`:

    [OSStructure(Name = "MyStructure")]
    public struct MyStructure
    {
        public int Value;
    }

Now the struct is public, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05010).
