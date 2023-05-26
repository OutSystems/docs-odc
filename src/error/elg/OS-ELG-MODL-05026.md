---
summary: "The default value specified for <ParameterName> is unsupported."
tags:
guid: 2cc2a5df-6b8e-45aa-9c4b-82ad0719d153
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05026

## Error message

`The default value specified for <ParameterName> is unsupported.`

## Cause

The error occurs when the default value specified for a parameter in the method signature is unsupported.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make sure the default values for the parameters in the method signatures are supported.

For example, if you have a method `MyMethod` with a parameter `MyParameter` that has an unsupported default value:

    public void MyMethod(string MyParameter = someInvalidDefaultValue) { ... }

Change the default value to something that's supported:

    public void MyMethod(string MyParameter = someValidDefaultValue) { ... }

The default value is now supported, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05026).
