---
guid: debf6461-bb1c-45cb-9335-c2d8111dc937
summary: Unsupported MCP actions in OutSystems Developer Cloud (ODC) occur due to complex data structures; fix by simplifying schemas on the external MCP Server.
locale: en-us
figma:
tags: mcp servers,ai agents,external tools,enterprise integration
app_type: mobile apps,reactive web apps
platform-version: odc
coverage-type:
  - understand
  - apply
topic:
  - integration
audience:
  - full stack developers
  - tech leads
  - backend developers
outsystems-tools:
  - odc portal
  - odc studio
---

# Unsupported MCP data structures

Some actions from an external MCP server may be disabled in any ODC app, not just agent apps, because their underlying data structures are too complex for ODC to handle. This is a built-in safety feature to prevent errors. The fix requires simplifying the action's schema on the external MCP server itself.

## Why you can't import an action

The ODC Portal automatically checks the JSON schema of every action you try to import. If an action's inputs or outputs use a data structure that is too complex, ODC marks it as unsupported and disables it to ensure your application remains stable.

If any part of an action uses one of the patterns below, the entire action is disabled.

## Unsupported data structures

* Arrays of objects
* **anyOf** or **oneOf** with more than two types (unless one is **null**)
* An array of types like **["string", "number"]** with more than two items (unless one is **null**)
* **allOf** with more than one type
* Schema references, which use **$ref**

## How to fix a disabled action

You cannot enable an unsupported action from within ODC. The change must be made on the external MCP Server where the action is defined.

## Option 1: Simplify the Original Action

The best solution is to refactor the action to use simpler data structures. For example, if an action returns an array of objects, modify it to return a JSON string of that array. You can then easily deserialize that string into a structure within your ODC logic.

## Option 2: Create a Wrapper Action

If you cannot change the original action, create a wrapper action on the MCP Server. This new action acts as a middleman: it calls the complex action in the background but uses a simplified set of inputs and outputs that are compatible with ODC.