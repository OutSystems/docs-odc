---
summary: "The following name <InterfaceName/MethodName> begins with underscores"
tags:
guid: cac9056a-b742-4962-a111-f86abf6269d2
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-ELG-MODL-05022

## Error message

`The following name: <InterfaceName/MethodName> begins with underscores`

## Cause

The error occurs because an interface or method name in your project code starts with one or more underscores (`_`). Interface and method names can't begin with underscores.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Rename your interface/methods so they don't start with an underscore. For example, if you have a method called `_MyMethod`, rename it to `MyMethod`.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05022).
