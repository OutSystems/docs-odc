---
summary: The class that implements the interface decorated with OSInterface '<InterfaceName>' must be public.
tags: error handling, external libraries, c# programming, interface implementation, public access modifiers
guid: 536ffe0b-b810-4c80-b6f8-ecb0c60794d3
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

# OS-ELG-MODL-05018

## Error message

`The class that implements the interface decorated with OSInterface '<InterfaceName>' must be public.`

## Cause

The error occurs because the class implementing the interface decorated with `OSInterface` isn't public.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

To solve this error, ensure that the implementing class is public. For example, if you have an interface `IMyInterface` decorated with `OSInterface`:

    [OSInterface]
    public interface IMyInterface {
        // Interface methods
    }

Make sure the class that implements this interface is public:

    public class MyImplementation : IMyInterface {
        // Implement interface methods
    }



If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05018).
