---
summary: The offset value for the paged request is incorrect. Check the documentation for further guidance. If the problem persists, let us know.
tags:
guid: bc8c7fd8-8cf1-11ed-a1eb-0242ac120002
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-FRGE-AST-40004

## Error message

`The offset value for the paged request is incorrect. Check the documentation for further guidance. If the problem persists, let us know.`

## Cause

The provided offset value is not valid. The offset sets index of the first asset that will be shown. It should be a number higher or equal to 0.

## Impact

You won't be able to get your request.

## Recommended action

Use a correct offset value (0 or higher) or leave it empty to use the default value of 0.
If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-FRGE-AST-40004).
