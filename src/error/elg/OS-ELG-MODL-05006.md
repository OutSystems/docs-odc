---
summary: No class implementing the interface decorated with OSInterface '<InterfaceName>' found in your file.
tags: mobile apps, c# development, error handling
guid: f23fd77e-9324-48f7-be5a-4cf607f25202
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
content-type:
  - error or warning
---

# OS-ELG-MODL-05006

## Error message

`No class implementing the interface decorated with OSInterface '<InterfaceName>' found in your file.`

## Cause

The error occurs because there is no class implementing the `OSInterface`-decorated interface in the project code.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Create a class that implements the interface decorated with `OSInterface`.

For example, suppose you have the following code with an interface decorated with `OSInterface`, but no class is implementing it:

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        // Some methods
    }

To resolve the error, add a class that implements the interface:

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

        // Interface methods
    }

Now, there is a class (`MyLibrary`) implementing the OSInterface-decorated interface (`IMyLibrary`), and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05006).
