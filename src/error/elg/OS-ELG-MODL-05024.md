---
summary: The struct <StructName> used as <UsageName> is missing OSStructure decoration.
tags: error resolution, c# development, code decoration, struct usage, outsystems development
guid: faf619e7-0281-4f21-9038-bf9ae4e8e1e4
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

# OS-ELG-MODL-05024

## Error message

`The struct <StructName> used as <UsageName> is missing OSStructure decoration.`

## Cause

The error occurs because a struct is used as a parameter for an action, a return type or another struct's public field/property and is missing the `OSStructure` decorator.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Add the `OSStructure` decorator to every struct used as a parameter, a return type or in another struct's public field/property.

For example, if you have a struct `MyStruct` used as the return type of a method:

    struct MyStruct{
        // Some struct attributes
    }

    ...

    public MyStruct MyMethod{
        // Code
        return myStruct; //myStruct is of type MyStruct
    }

Make sure `MyStruct` has the `OSStructure` decorator:

    [OSStructure]
    struct MyStruct{
        // Some struct attributes
    }

    ...

    public MyStruct MyMethod{
        // Code
        return myStruct; //myStruct is of type MyStruct
    }

Now the struct (`MyStruct`) has the `OSStructure` decorator and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05024).
