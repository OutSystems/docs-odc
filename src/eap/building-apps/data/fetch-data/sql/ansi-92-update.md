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
[ WHERE booleanExpression ]

assignment:
        attribute = expression
```


`UPDATE` updates records in an entity on an external system.

The assignments can be in any order but a given attribute may only be assigned once.
If the `WHERE` clause is not specified, the operation will update all records in the entity.
If the `WHERE` clause is specified, the operation will only update records for which the condition evaluates to true.

`UPDATE` never returns a result.

<div class="info" markdown="1">

* The user configured on the connection must have permission to update records in the entity on the external system.
* Qualified attributes (`{entity}.[attribute]`) aren't supported in assignments.

</div>

## Examples

```sql
-- Update all records in an entity
UPDATE { entity } SET [isDeleted] = true;

-- Update only matching records in an entity
UPDATE { entity }
SET [isDeleted] = true
WHERE [id] = 1 OR [id] = @dynamic;
```

## Compatibility

| Data Source          | Update          |
|----------------------|-----------------|
| Microsoft SQL Server | Yes             |    
| Oracle               | Yes             |    
| PostgreSQL           | Yes             |    
| Salesforce           | Yes             |     
| SAP OData            | Yes<sup>1</sup> |

<sup>1</sup>: The entity must have a `PATCH` or `PUT` API. `UPDATE` does not support writing to SAP OData Navigation Properties (`Record` attributes).
