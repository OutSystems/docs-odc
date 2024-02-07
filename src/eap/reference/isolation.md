---
summary: Learn about database transaction isolation level read-committed in ODC.
tags:
locale: en-us
guid: c20caef0-12af-4ebc-8d89-5bea8c5c0810
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Database transaction isolation level

Read committed is the ODC isolation level. It prevents sessions from seeing data from concurrent transactions until committed.

Database transactions start when there's a **write operation**. For example:

* Create
* CreateOrUpdate
* CreateOrUpdateSome
* Update
* Delete
* GetForUpdate

Database transactions end whenever there's a Commit, a Rollback, or at the end of a Request.

The Read-committed isolation level doesn't allow **dirty reads**. This means that data changed by one transaction is only visible by a concurrent transaction once those changes are committed by the first one.
