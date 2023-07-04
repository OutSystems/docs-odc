---
summary: "More than one object with name <ObjectName> was found."
tags:
guid: cbbd399f-76f8-489d-a4ad-8e06dc61c3a3
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-ELG-MODL-05025

## Error message

`More than one object with name '<ObjectName>' was found.`

## Cause

The error occurs because multiple objects have the same name in the project code.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make sure every object in your external library has a unique name.

For example, imagine you have two structs, in two different namespaces, with the same name:

    namespace namespace1 {

        [OSStructure]
        struct MyStruct{
            //some struct attributes
        }

    }

    namespace namespace2 {

        [OSStructure]
        struct MyStruct{
            //some struct attributes
        }

    }

Although this is valid in .NET, it's not for your external library. In the example, you should change the name of one of the structures:

    namespace namespace1 {

        [OSStructure]
        struct MyStruct{
            //some struct attributes
        }

    }

    namespace namespace2 {

        [OSStructure]
        struct AnotherStruct{
            //some struct attributes
        }

    }

Now each object has a unique name and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05025).
