---
guid: 72cf6e91-01e0-483b-a3aa-1538eddea351
locale: en-us
summary: Learn how to use the ANSI-92 UPDATE statement to modify records in external entities from OutSystems Developer Cloud (ODC) apps.
figma: 
coverage-type:
  - apply
  - remember
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - tech leads
tags: sql, database operations, queries, data manipulation, examples
outsystems-tools:
  - odc studio
---

# UPDATE statement in ANSI-92 queries

```sql
UPDATE entity
SET assignment [, assignment ]*
[ WHERE condition ]

assignment:
        attribute = expression
```


`UPDATE` updates records in an entity on an external system.

One or more attributes must be assigned a new value in the `SET` clause. Attributes may be assigned in any order but a given attribute may only be assigned once. The attributes may be qualified (`{entity}.[attribute]`) and this is recommended to avoid potential issues when attributes are renamed in ODC Portal.

If the `WHERE` clause isn't specified, the operation will update all records in the entity.

If the `WHERE` clause is specified, the operation will only update records for which the `condition` evaluates to true.

`UPDATE` never returns a result.


<div class="info" markdown="1">

* The user configured on the connection must have permission to update records in the entity on the external system.

</div>

## Examples

```sql
-- Update all records in an entity to have uppercase [first] and [last] attributes
UPDATE {entity}
SET {entity}.[first] = UPPER({entity}.[first]), {entity}.[last] = UPPER({entity}.[last])

-- Update only matching records in an entity to increment each [counter] by 1
UPDATE {entity}
SET {entity}.[counter] = {entity}.[counter] + 1
WHERE {entity}.[id] = 1 OR {entity}.[id] = @dynamic;
```

## Compatibility

| Data Source          | Update          |
|----------------------|-----------------|
| Microsoft SQL Server | Yes             |    
| Oracle               | Yes             |    
| PostgreSQL           | Yes             |    
| Salesforce           | Yes             |     
| SAP OData            | Yes<sup>1</sup> |

<sup>1</sup>: The entity must have a `PATCH` or `PUT` API. `UPDATE` doesn't support writing to SAP OData Navigation Properties (`Record` attributes).
