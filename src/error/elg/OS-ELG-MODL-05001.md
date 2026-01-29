---
summary: File does not contain a valid compiled external library, or the compiled assembly was not built using a supported .NET version.
tags: .net 8, assembly validation, mobile app development, application publishing, troubleshooting
guid: 007f935e-fade-46ab-8058-61d57f294bc1
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

# OS-ELG-MODL-05001

## Error message

`File does not contain a valid compiled external library, or the compiled assembly was not built using a supported .NET version.`

## Cause

File does not contain a valid compiled external library, or the compiled assembly was not built using a supported .NET version.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Check that your project uses the .NET 8.0 framework and you [packaged the published project into a ZIP correctly](../../eap/building-apps/external-logic/README.md).

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05001).
