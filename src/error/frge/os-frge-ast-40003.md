---
summary: The limit value for the paged request is incorrect. Check the documentation for further guidance. If the problem persists, let us know.
tags: error handling, pagination, api requests, data retrieval, outsystems support
guid: 3e1e7caa-8cf1-11ed-a1eb-0242ac120002
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

# OS-FRGE-AST-40003

## Error message

`The limit value for the paged request is incorrect. Check the documentation for further guidance. If the problem persists, let us know.`

## Cause

The provided limit value is not valid. The limit sets the number of assets that you will receive in the request. It should be a number between 1 and 1000.

## Impact

You won't be able to get your request.

## Recommended action

Use a correct limit value (between 1 and 1000) or leave it empty to use the default value of 10.
If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-FRGE-AST-40003).
