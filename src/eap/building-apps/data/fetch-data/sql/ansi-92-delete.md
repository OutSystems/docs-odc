---
guid: 08100981-f54c-4a3b-8e17-73cfe8a54d49
locale: en-us
summary: Learn how to use the DELETE statement in ANSI-92 queries to remove records from an external entity in OutSystems Developer Cloud (ODC).
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
tags: sql,delete statement,database,ansi-92,queries
outsystems-tools:
  - odc studio
---

# DELETE statement in ANSI-92 queries

```sql
DELETE FROM entity
[ WHERE booleanExpression ]
```

`DELETE` deletes records in an entity on an external system.
If the `WHERE` clause isn't specified, the operation will delete all records in the entity.
If the `WHERE` clause is specified, the operation will only delete records for which the boolean expression evaluates to true.
`DELETE` never returns a result.

<div class="info" markdown="1">

* The user configured on the connection must have permission to delete records in the entity on the external system.
*  Qualified attribute names, for example, `{entity}.[attribute]` are currently not supported.

</div>

## Examples

```sql
-- Delete all records in an entity
DELETE FROM { entity };

-- Delete only matching records in an entity
DELETE FROM { entity } WHERE [id] = 1 OR [id] = @dynamic;
```

## Compatibility

| Data Source          | Delete    |
|:---------------------|:----------|
| Microsoft SQL Server | Yes       |    
| Oracle               | Yes       |    
| PostgreSQL           | Yes       |    
| Salesforce           | Yes       |     
| SAP OData            | Yes. The entity must have a `DELETE` API. |     


