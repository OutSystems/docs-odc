---
summary: How to publish apps that use JavaScript Nodes and violate Strict Mode.
tags:
guid: dbeab3f4-4b7e-472d-be22-7650d42b0258
locale: en-us
platform-version: odc
app_type: mobile apps, reactive web apps
figma: 
---

# OS-BLD-FE-40001


## Error message

Bundle Error at `<app>` `<flow>` `<screen>` `<action>` `<js-node>`: `<violation>`

## Cause

With the introduction of a new bundler in ODC, OutSystems enabled [Strict Mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode). 


## Impact

You can't publish apps that use JavaScript Nodes and violate Strict Mode. 

## Recommended action

Please check the [Strict mode documentation by MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) and fix any violations identified on your JavaScript Nodes. The breadcrumbs described in the error message should lead you to identify on which JavaScript Node the Strict Mode violation is happening. 

## More info

On apps where Strict Mode violations have multiple occurrences, OutSystems shows only the list the first six findings.
