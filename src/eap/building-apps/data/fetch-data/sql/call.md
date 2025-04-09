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
CALL action ( [ assignment ] [, assignment ]* )

assignment:
        [ parameterName = ] @dynamic | literal
```

`CALL` executes an action on an external system and returns a result.

Parameter values can be assigned with names (using the `"name" = value` syntax) or assigned positionally without names.

Assignment by name is recommended as a best practice and is supported with [most external systems](#Compatibility). The parameter names must be the same as those defined on the action in the external system.

Positional assignment is also supported. When assigning parameters positionally, they must be assigned in the same order as they are defined on the action in the external system.

If the action has optional parameters, it is possible to use a combination of positional and named assignments. In this case, the positional assignments must be before the named assignments.

If the action returns a result without using output parameters, then that result will be returned by `CALL`. For actions which do not return a result, a single record containing a value of `-1` will always be returned.

<div class="info" markdown="1">

* The user configured on the connection must have permission to execute the action on the external system.
* Overloaded actions (with the same name but different parameter types) aren't supported
* All mandatory action parameters must be of supported [Data types](ansi-92-data-types.md). Optional input parameters of unsupported types must not be set when calling the action.
* Unsupported types in the result of an action will be included in returned records with `NULL` values.
* Expressions are currently not supported as parameter values.
* `CALL` must be executed in a multi statement context with at least one statement that uses an entity from the same external system.

</div>

## Examples

```sql
-- No parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ();

-- Named parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ("param1" = 'test', "param2" = @dynamic);

-- Positional parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ('test', @dynamic);

-- Combination of positional and named parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ('test', "param2" = @dynamic);
```

<div class="info" markdown="1">

See further examples, general and specific rules for calling stored procedures in [this article](stored-procedure.md).

</div>

## Compatibility { #compatibility }

| Data source          | Supported actions | Positional parameters | Named parameters |
|----------------------|-------------------|-----------------------|------------------|
| Microsoft SQL Server | Stored procedures | Yes                   | Yes              |
| Oracle               | Stored procedures | Yes                   | Yes              |
| PostgreSQL           | Stored procedures | Yes                   | Yes              |
| Salesforce           | None              | No                    | No               |
| SAP OData            | None              | No                    | No               |
