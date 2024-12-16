---
summary: No methods found in the interface decorated with OSInterface '<InterfaceName>'.
tags: external libraries, c# integration, error resolution, outsystems interfaces, outsystems platform
guid: 8ef3fd68-a777-4e16-94c4-025446c7d4e1
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - backend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc studio
coverage-type:
  - unblock
---

# OS-ELG-MODL-05007

## Error message

`No methods found in the interface decorated with OSInterface '<InterfaceName>'.`

## Cause

The interface decorated with `OSInterface` has no methods defined in it.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Add methods to the interface decorated with `OSInterface`.

For example, suppose you have the following code with an interface decorated with `OSInterface`, but no methods are defined:

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        // No methods
    }

To resolve the error, add methods to the interface:

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        int Add(int a, int b);
        int Subtract(int a, int b);
    }

Now, there are methods defined in the OSInterface-decorated interface (`IMyLibrary`), and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05007).
