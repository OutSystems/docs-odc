---
summary: The assembly <AssemblyName>, which contains the interface decorated with the OSInterface attribute, is not located in the root directory of the zip file.
tags: error handling, application packaging, library publishing, external libraries, compression
guid: a00f3190-e435-48cf-87c2-757c4036e693
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

# OS-ELG-MODL-05029

## Error message

`The package was compressed using an unsupported compression method: <CompressionMethodName>`

## Cause

The high code package was compressed using an unsupported compression method.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must upload the new ZIP file.

## Recommended action

Use either the 'Deflated' or 'Stored' compression method whenever you're compressing your high code packages.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05027).
