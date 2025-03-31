---
guid: 471e19f6-210c-4e3f-b328-da14bd3d0886
locale: en-us
summary: Execute stored procedures on external databases with support for named and positional parameter assignments in OutSystems Developer Cloud (ODC).
figma:
coverage-type:
  - apply
  - remember
topic:
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - mobile developers
tags: sql queries, call statement, named parameters, positional parameters
outsystems-tools:
  - odc studio
---

# CALL statement in ANSI-92 queries

```sql
CALL action ( assignment, assignment )

assignment:
        [ parameterName = ] @dynamic | literal
```

`CALL` executes an action on an external system and returns a result (if any).

Parameter values can be assigned with names (using the `"name" = value` syntax) or assigned
positionally without names.

Assignment by name is recommended as a best practice and is supported with all external systems. The
parameter names must be the same as those defined on the action in the external system. In the case
of Microsoft SQL Server, this includes the mandatory `@` prefix, i.e. `"@param" = value`.

Positional assignment isn't supported in all data sources. When assigning parameters positionally,
they must be assigned in the same order as they are defined on the action in the external data
source.

If the action has optional parameters, it's possible to use a mixed combination of positional and
named assignments. In this case, the positional assignments must be before the named assignments.

<div class="info" markdown="1">

* The user configured on the connection must have permission to execute the action on the external system.
* Overloaded procedures (with the same name but different parameters) aren't supported.
* Expressions are currently not supported as parameter values.

</div>

## Examples

```sql
-- CALL without parameters
CALL "connectionId"."actionName" ();

-- CALL with named parameters
CALL "connectionId"."actionName" ("param1" = 'test', "param2" = @dynamic);

-- CALL with positional parameters
CALL "connectionId"."actionName" ('test', @dynamic);

-- CALL with mixed parameters
CALL "connectionId"."actionName" ('test', "param2" = @dynamic);
```

<div class="info" markdown="1">

See further examples, general and specific rules for calling stored procedures in [this article](stored-procedure.md).

</div>

## Compatibility

| Data source          | Supported actions | Positional parameters | Named parameters |
|----------------------|-------------------|-----------------------|------------------|
| Microsoft SQL Server | Stored procedures | Yes                   | Yes              |
| Oracle               | Stored procedures | Yes                   | Yes              |
| PostgreSQL           | Stored procedures | Yes                   | Yes              |
| Salesforce           | None              | No                    | No               |
| SAP OData            | None              | No                    | No               |
