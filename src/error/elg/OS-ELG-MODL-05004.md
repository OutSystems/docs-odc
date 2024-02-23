---
summary: "The interface decorated with OSInterface '<InterfaceName>' is not public."
tags:
guid: b4205081-0901-4083-b578-0d589d1b1515
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-ELG-MODL-05004

## Error message

`The interface decorated with OSInterface '<InterfaceName>' is not public.`

## Cause

The error occurs because the interface decorated with the `OSInterface` attribute isn't defined with the 'public' access modifier.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

You need to make the interface with the `OSInterface` attribute public.

For example, suppose you have the following code with an interface that's not public:

    [OSInterface(Name = "MyLibrary")]
    interface IMyLibrary
    {
        // Some methods
    }

To resolve the error, you can add the `public` access modifier to the interface:

    using OutSystems.ExternalLibraries.SDK;

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        // Some methods
    }

Now, the interface (`IMyLibrary`) is defined as public, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05004).
