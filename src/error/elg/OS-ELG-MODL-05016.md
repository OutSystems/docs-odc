---
summary: The parameter '<ParamaterName>' in action '<ActionName>' is passed by reference. Passing parameters by reference is not supported.
tags: error handling, c# development, external libraries, parameter passing, sdk usage
guid: c8853561-096d-4400-b070-1159b4463503
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - none
coverage-type:
  - unblock
---

# OS-ELG-MODL-05016

## Error message

`The parameter '<ParamaterName>' in action '<ActionName>' is passed by reference. Passing parameters by reference is not supported.`

## Cause

A parameter in an action is passed by reference, which isn't supported by the External Libraries SDK. In this context, "passed by reference" means any parameter declared using the `ref` or `in` keywords.

Parameters declared with the `out` keyword - used solely to return values - are permitted.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Instead of using a reference parameter (using `ref` or `in`), pass the parameter by value and return the modified value if necessary.

For example, if you have the following code:

    public void UpdateValue(ref int value)
    {
        value = value + 1;
    }

Modify it to:

    public int UpdateValue(int value)
    {
        return value + 1;
    }

Now, the parameter is passed by value, and the modified value is returned.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05016).
