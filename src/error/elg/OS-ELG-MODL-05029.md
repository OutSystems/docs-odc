---
summary: "The assembly <AssemblyName>, which contains the interface decorated with the OSInterface attribute, is not located in the root directory of the zip file."
tags:
guid: 2aebb901-40e1-4c06-9fe9-2e004b1f0f56
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05029

## Error message

`The package was compressed using an unsupported compression method: <CompressionMethodName>`

## Cause

The high code package was compressed using an unsupported compression method.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must upload the new ZIP file.

## Recommended action

Use either the 'Deflated' or 'Stored' compression method whenever you're compressing your high code packages.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05027).
