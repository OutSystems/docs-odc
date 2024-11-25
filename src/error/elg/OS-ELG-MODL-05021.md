---
summary: "The name '<Name>' is not supported as it has the following invalid characters '<InvalidCharacters>'."
tags:
guid: 6befc8c5-56bf-4171-8df8-b49296bd2028
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
content-type:
  - error or warning
---

# OS-ELG-MODL-05021

## Error message

`The name: '<Name>' is not supported as it has the following invalid characters '<InvalidCharacters>'.`

## Cause

The error occurred because the specified name contains invalid characters other than letters, numbers, and underscores.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

To solve this error, replace the invalid characters with valid ones. For example, if the name is `Invalid*Name@123`, rename it to `Invalid_Name_123` or another suitable name that only contains letters, numbers, and underscores.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05021).
