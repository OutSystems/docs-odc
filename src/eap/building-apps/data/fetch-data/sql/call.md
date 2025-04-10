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

`CALL` executes an action on an external system.

The action must be specified using the `"connectionId"."actionName"` syntax. The `connectionId` identifies the connection to the data source in ODC Portal. You can obtain the `connectionId` by following the [instructions here](stored-procedure.md).

Parameter values may be assigned with names (using the `"name" = value` or `[name] = value` syntax) or assigned positionally.

When using named assignments, the parameters may be specified in any order. The names must match the names used in the definition of the action in the external system.

When using positional assignments, values of the correct type must be provided in the same order as the parameters are declared in the definition of the action in the external system.

If the action has optional parameters (can be `NULL` or have a default value) then a combination of positional and named assignments may be used.
In this case, the positional assignments must be specified before the named assignments. If a parameter can be `NULL` and has a default value, then assigning the parameter to `NULL` will set the parameter to `NULL`. For the default value to be used, the parameter must not be assigned at all.

Values must be assigned for all mandatory parameters (`NOT NULL` and no default value). This applies to parameters of all types including outputs.
The values can only be literals or dynamic parameters, expressions containing operators or functions aren't supported.

The result of `CALL` depends on the definition of the action in the external system. If the action returns a result using `SELECT`, then `CALL` will return that result.
If an action returns multiple results using `SELECT`, then `CALL` will only return the result of the last `SELECT`.
For all other actions, `CALL` will return a single record containing a value of `-1`.

<div class="info" markdown="1">

* The user configured on the connection must have permission to execute the action on the external system.
* Overloaded actions (with the same name but different parameter types) aren't supported and won't appear in ODC Portal.
* All mandatory parameters must be of supported [data types](../../../../integration-with-systems/external-databases/external-data-type.md). Optional parameters of other types must not be included in the list of assignments
* If the action returns any attributes of an unsupported type, the attributes will be present in the result of `CALL` however the values for those attributes will always be `NULL`.
* ODC does not support the declaration of variables, so it is not possible to retrieve the (mutated) value of an output parameter after the action has been executed.

</div>

## Known issues

* `CALL` can only be used in a multi statement context with at least one other statement that uses an entity from the same connection.
* Named assignments can't be used with Microsoft SQL Server

## Examples

```sql
-- No parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ();

-- Named parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ("param1" = 'test', "param2" = 123, "param3" = @dynamic);

-- Positional parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ('test', 123, @dynamic);

-- Combination of positional and named parameters
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ('test', 123, "param" = @dynamic);
```

## Compatibility { #compatibility }

| Data source          | Supported actions | Positional parameters | Named parameters |
|----------------------|-------------------|-----------------------|------------------|
| Microsoft SQL Server | Stored procedures | Yes                   | No               |
| Oracle               | Stored procedures | Yes                   | Yes              |
| PostgreSQL           | Stored procedures | Yes                   | Yes              |
| Salesforce           | None              | No                    | No               |
| SAP OData            | None              | No                    | No               |

## Microsoft SQL Server

* Stored procedures that use `EXEC` or `EXECUTE` may not return the expected result.
* Named assignment of parameters is not supported, please use the positional assignment syntax instead.

```sql
SELECT 1 FROM {entity1} LIMIT 1;
CALL "connectionId"."actionName" ('test', 123, @dynamic);
```

## Oracle

* `CALL` will always return a single record with a value of `-1`, it is not possible to receive results from a stored procedure.

## PostgreSQL

* Parameters defined without a name may be specified in `CALL` using the syntax `"$1" = value` where `$1` specifies the first parameter, `$2` the second, and so on.

```sql
SELECT 1 FROM {entity1} LIMIT 1;
-- Call a procedure with unnamed parameters using named assignments
CALL "connectionId"."actionName" ("$1" = 123, "$2" = 'test', "$3" = @dynamic);
```
