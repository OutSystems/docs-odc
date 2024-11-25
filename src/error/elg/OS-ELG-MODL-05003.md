---
summary: "More than one OSInterface attribute found in your file '<InterfaceNames>'. Make sure only one interface decorated with OSInterface is defined."
tags:
guid: 6cf42628-a470-4c43-9624-3d003cc8435d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-ELG-MODL-05003

## Error message

`More than one OSInterface attribute found in your file: <InterfaceNames>. Make sure only one interface decorated with OSInterface is defined.`

## Cause

The error occurs because multiple interfaces in the project code are decorated with the `OSInterface` attribute, while only one is allowed.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

You need to remove the extra `OSInterface` attributes and make sure that only one interface is decorated with `OSInterface`.

For example, suppose you have the following code with two interfaces decorated with the `OSInterface` attribute:

    [OSInterface(Name = "FirstLibrary")]
    public interface IFirstLibrary
    {
        // Some methods
    }

    [OSInterface(Name = "SecondLibrary")]
    public interface ISecondLibrary
    {
        // Some methods
    }

To resolve the error, you can remove the `OSInterface` attribute from one of the interfaces:

    [OSInterface(Name = "FirstLibrary")]
    public interface IFirstLibrary
    {
        // Some methods
    }

    public interface ISecondLibrary
    {
        // Some methods
    }

Now, only one interface (`IFirstLibrary`) is decorated with the `OSInterface` attribute, and the error should be resolved.

Also make sure your project code isn't referencing any other project containing an interface decorated with `OSInterface`.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05003).
