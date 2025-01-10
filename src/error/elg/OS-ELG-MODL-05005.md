---
summary: The interface decorated with OSInterface is implemented by class '<ClassName>' which doesn't have a public parameterless constructor.
tags: error handling, c# programming, interface implementation, constructor definition, library publishing
guid: ead000a1-6236-4351-9060-0c981c834d47
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

# OS-ELG-MODL-05005

## Error message

`The interface decorated with OSInterface is implemented by class '<ClassName>' which doesn't have a public parameterless constructor.`

## Cause

The error occurs because the class implementing the `OSInterface`-decorated interface lacks a public parameterless constructor.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

To solve this issue, add a public parameterless constructor to the class implementing the interface.

For example, suppose you have the following code with a class implementing an interface without a public parameterless constructor:

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        // Some methods
    }

    public class MyLibrary : IMyLibrary
    {
        public MyLibrary(int value)
        {
            // Constructor logic
        }

        // Interface methods
    }

To resolve the error, add a public parameterless constructor to the class:

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        // Some methods
    }

    public class MyLibrary : IMyLibrary
    {
        public MyLibrary()
        {
            // Constructor logic
        }

        public MyLibrary(int value)
        {
            // Constructor logic
        }

        // Interface methods
    }

Now, the class (`MyLibrary`) has a public parameterless constructor, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05005).
