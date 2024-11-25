---
summary: Required descriptions of modules, modules' public elements, and their related input/output parameters.
tags:
guid: 1c910902-8db4-4b41-b00d-2bca550b7029
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3523-110&node-type=CANVAS&t=fro20soaPpjjIXwf-0
content-type:
  - troubleshooting
  - reference
---

# Missing descriptions on public element or parameter

Required descriptions of modules, modules' public elements, and their related input/output parameters.

## Impact

Meaningful descriptions in modules, public elements, entities, and input/output parameters clarify their purpose and expected behavior. This is crucial when consuming closed modules because the implemented logic isn't visible.

## Why is this happening?

The element or parameter is **Public**, but the **Description** input field is empty.

![Screenshot showing a public element with an empty description field in a module.](images/odcs-public-description.png "Empty Description Field in Public Element")

## How to fix

Add a description to the module that explains its purpose and identifies the concepts it contains. To solve the finding, add meaningful descriptions to all modules' public elements, related entities, and parameters. The only exceptions are Entities and Structures attributes whose descriptions are optional. Parameters whose names follow well-established naming conventions (e.g., Id, Name, Label, Description, CreatedBy, UpdatedBy, CreatedOn, UpdatedOn) are also exceptions.
