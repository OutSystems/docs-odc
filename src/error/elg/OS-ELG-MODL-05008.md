---
summary: "The interface decorated with OSInterface '<InterfaceName>' is implemented by multiple classes: <ClassNames>."
tags:
guid: e876d995-612b-4997-9e59-fe8d51826032
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05008

## Error message

`The interface decorated with OSInterface '<InterfaceName>' is implemented by multiple classes: <ClassNames>.`

## Cause

The error occurs because more than one class in the file is implementing the interface decorated with `OSInterface`.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make sure only one class implements the interface decorated with `OSInterface`. 

For example, suppose you have the following code with two classes (`MyLibraryA` and `MyLibraryB`) implementing the same OSInterface-decorated interface (`IMyLibrary`):

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        int Add(int a, int b);
    }

    public class MyLibraryA : IMyLibrary
    {
        public int Add(int a, int b)
        {
            return a + b;
        }
    }

    public class MyLibraryB : IMyLibrary
    {
        public int Add(int a, int b)
        {
            return a + b;
        }
    }

To resolve the error, remove one of the classes implementing the interface or make one of them implement a different interface:

    [OSInterface(Name = "MyLibrary")]
    public interface IMyLibrary
    {
        int Add(int a, int b);
    }

    public class MyLibraryA : IMyLibrary
    {
        public int Add(int a, int b)
        {
            return a + b;
        }
    }

    // Removed the implementation of IMyLibrary from MyLibraryB
    public class MyLibraryB
    {
    }

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05008).
