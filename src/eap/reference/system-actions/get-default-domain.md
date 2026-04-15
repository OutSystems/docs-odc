---
summary: OutSystems Developer Cloud (ODC) provides a server action to get the default domain configured in the stage.
tags: url handling, domain management, system actions
locale: en-us
guid: 7f3e8a91-4c2d-4b5e-9a1f-3d6c8e5b2a7c
app_type: mobile apps, reactive web apps
platform-version: odc
content-type:
  - reference
figma:
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# GetDefaultDomain server action

Returns the domain set as default in the stage where this app is running.

## Output

**DefaultDomain**; data type **Text**

If no custom domain is set as default, the built-in domain is returned.  

## Examples

```
GetDefaultDomain() = "example.com"
```
