---
summary: The name '<Name>' is not supported as it begins with a number.
tags: error message, naming conventions, c# project, outsystems, troubleshooting
guid: 00b8ed9f-4e4f-4e3f-a0d5-c830bcedf4d1
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - unblock
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
---
# OS-ELG-MODL-05020

## Error message

`The name: '<Name>' is not supported as it begins with a number.`

## Cause

The error occurred because the specified name starts with a number, which isn't supported.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

To solve this issue, change the name to begin with a letter instead of a number. For example, if the name is `123InvalidName`, rename it to `ValidName123` or another suitable name that starts with a letter.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05020).
