---
guid: debf6461-bb1c-45cb-9335-c2d8111dc937
summary: Unsupported MCP actions in OutSystems Developer Cloud (ODC) occur due to complex input data structures; fix by simplifying schemas on the external MCP Server.
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
  - Developer
  - Tech lead
outsystems-tools:
  - odc portal
  - odc studio
isautopublish: true
---

# Unsupported MCP data structures

ODC supports a wide range of data structures from external MCP server actions. ODC imports an action when all its inputs are supported. For outputs, ODC supports nearly all structures. Fields it can type arrive as typed values. Other fields are typed as text and carry a JSON-formatted string at runtime. Deserialize the field to read its nested values.

## How ODC handles imported actions

ODC validates the JSON schema of every action during import. An action imports as a server action when its input structures are supported. Actions with unsupported output patterns also import, with the affected output fields typed as text. At runtime, those fields carry a JSON-formatted string.

The following sections describe how unsupported input patterns affect import. Some patterns make the entire action unavailable. Others cause specific input parameters or fields to be omitted from the action's signature.

## Unsupported input patterns that make an action unavailable

If a field within an input parameter is unsupported, the parent parameter is flagged as unsupported, which makes the entire action unavailable. The patterns below trigger this behavior only when they appear in inputs.

### Multi-type anyOf, oneOf, allOf

The action is unavailable when `anyOf`, `oneOf`, or `allOf` lists more than one type, unless one of the types is `null`.

### Array of multiple types

The action is unavailable when a parameter declares an array of types like `["string", "number"]` with more than one item, unless one is `null`.

### Array without an items schema

The action is unavailable when an array doesn't define `items`.

```json
{
  "type": "array",
  "prefixItems": [
    { "type": "string" }
  ]
}
```

### Array of arrays

The action is unavailable when an array contains arrays.

```json
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

### External references

The action is unavailable when a `$ref` points to a schema not included in the input schema.

```json
{
  "ReferenceToExternalSchema": {
    "$ref": "otherFile.json#/definitions/ExternalType"
  }
}
```

### Object without properties

The action is unavailable when an object schema has no typed properties. This happens directly, when only `additionalProperties` is defined, or indirectly, when every property is recursive and gets omitted.

Example where only `additionalProperties` is defined:

```json
{
  "type": "object",
  "additionalProperties": {
    ...
  }
}
```

Example where the only typed property is recursive, leaving the object without properties:

```json
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

## Unsupported input patterns that omit parameters or fields

If an input parameter or field uses a recursive reference, ODC omits it from the action's signature and imports the rest of the action.

### Recursive ref

Properties that reference themselves through `$ref` are omitted.

Example where `children` is omitted:

```json
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
        "name": { "type": "string" },
        "age": { "type": "number" },
        "children": {
          "type": "array",
          "items": { "$ref": "#/$defs/PersonType" }
        }
      }
    }
  }
}
```

### Dynamic references

Properties using `$dynamicRef` or the older `$recursiveRef` are omitted.

Example where `children` is omitted:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$dynamicAnchor": "node",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" },
    "children": {
      "type": "array",
      "items": { "$dynamicRef": "#node" }
    }
  }
}
```

## How to make an unavailable action available

To make an unavailable action available, change the data structures on the external MCP server, where the action is defined as a **tool**. You need direct control and modification access to the external MCP server to apply these fixes.

### Option 1: Simplify the original tool

The best solution is to refactor the tool to use simpler data structures. For example, if a tool receives as input a field that supports multiple data types, modify it to support only a single data type.

### Option 2: Create a wrapper tool

If you can't change the original tool, create a wrapper tool on the MCP Server. This new tool acts as a middleman. It calls the complex tool in the background but uses a simplified set of inputs that are compatible with ODC.
