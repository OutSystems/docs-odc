---
summary: No OSInterface found in your file. Make sure only one interface decorated with OSInterface is defined.
tags: api design, c# programming, library development, error handling, technical support
guid: 7a5decd1-2274-4335-9170-d1ccfbf39604
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

# OS-ELG-MODL-05002

## Error message

`No OSInterface found in your file. Make sure only one interface decorated with OSInterface is defined.`

## Cause

There is no interface with the `OSInterface` attribute in the project code.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make sure there's a public interface with the `OSInterface` attribute in your project code. For example:

    [OSInterface(Name = "MyLibrary", Description = "A sample library")]
    public interface IMyLibrary
    {
        [OSAction(Description = "A sample action")]
        void MyAction();
    }

Implement this interface in a public class with a public parameterless constructor:

    public class MyLibrary : IMyLibrary
    {
        public void MyAction()
        {
            // Your action implementation
        }
    }

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05002).
