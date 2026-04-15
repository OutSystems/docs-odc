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

Some actions from an external MCP server may be disabled in any ODC app, not just agentic apps, because their underlying data structures are too complex for ODC to handle. This is a built-in safety feature to prevent errors. The fix requires simplifying the action's schema on the external MCP server itself.

## Why you can't import an action or find a specific parameter

The ODC Portal automatically checks the JSON schema of every action you try to import. If an action's inputs or outputs use a data structure that is too complex, ODC marks it as unsupported and disables it to ensure your application remains stable.

Depending on the pattern, the action can be completely disabled or a parameter or field can be omitted from the action's signature instead. The following sections explain the patterns and results.

## Unsupported data structures that lead to disabled actions

If a field within a parameter is unsupported, the parent parameter is automatically flagged as unsupported. This flag immediately causes the entire action to be marked as unsupported.

If any part of an action uses one of the patterns below, the entire action is disabled:

* **anyOf**, **oneOf** or **allOf** with more than one type (unless one is **null**).
* An array of types like `["string", "number"]` with more than one item (unless one is `null`).
* Array without an `items` schema.

Example:

```
    {
      "type": "array",
      "prefixItems": [
        { "type": "string" }
      ]
    }
```

* Array of arrays.

Example:

```
    {
      "type": "array",
      "items": [
        {
          "type": "array",
          "items": { "type": "string" }
        }
      ]
    }
```

* References that aren't included in the input/output schema.

Example:

```
    {
      "ReferenceToExternalSchema": {
        "$ref": "otherFile.json#/definitions/ExternalType"
      }
    }
```

* An object without `properties`.

Example where only `additionalProperties` is defined:

  ```
    {
      "type": "object",
      "additionalProperties": {
        ...
      }
    }
  ```

Example where the only property is recursive (recursive properties are omitted)

  ```
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "$dynamicAnchor": "node",
      "type": "object",
      "properties": {
        "nextNode": {
            "$dynamicRef": "#node"
        }
      }
    }
  ```

## Unsupported data structures that lead to omitted parameters or fields

If an action's inputs or outputs contain a recursive parameter or field, ODC omits them from the action's signature to ensure your app remains stable.

* Properties that create recursive references are omitted.

Example where `children` is omitted:

  ```
    "inputSchema": {
      "type": "object",
      "properties": {
        "person": {
          "$ref": "#/$defs/PersonType"
          }
      },
      "$defs": {
        "PersonType": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "age": {
              "type": "number"
            },
            "children": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/PersonType"
              }
            },
          }
        }
      }
    }
  ```

* Properties with dynamic references `$dynamicRef` or the older `$recursiveRef` are omitted.

Example where `children` is omitted:

  ```
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "$dynamicAnchor": "node",
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "age": {
          "type": "number"
        },
        "children": {
          "type": "array",
          "items": {
            "$dynamicRef": "#node"
          }
        }
      }
    }
  ```

## How to fix a disabled action or omitted parameters and fields

You can't enable an unsupported action from within ODC. To enable the action, you must make the necessary data structure changes on the external MCP Server, where it is defined as a **tool**. To successfully fix these issues, you must have direct control and modification access to the external MCP Server.

### Option 1: Simplify the original tool

The best solution is to refactor the tool to use simpler data structures. For example, if a tool receives as input a field that supports multiple data types, modify it to support only a single data type.

### Option 2: Create a wrapper tool

If you can't change the original tool, create a wrapper tool on the MCP Server. This new tool acts as a middleman. It calls the complex tool in the background but uses a simplified set of inputs and outputs that are compatible with ODC.
