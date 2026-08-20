---
guid: 8faf9eab-4c5c-43d6-b994-598c4462cb36
locale: en-us
summary: OutSystems Developer Cloud (ODC) Code Quality flags database operations in client-side logic as a security risk.
figma:
coverage-type:
  - unblock
  - remember
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Developer
  - Front-end developer
tags:
  - Data Integrity
  - Front-End
  - Logic
  - Roles
  - Screens
  - Security
  - Technical Debt
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# Database operation in the client-side logic of a screen

This finding flags a create, update, or delete operation that runs directly from the screen's client-side logic without going through a server action first. This means data goes straight from the client to the database without any server-side validation.

<div class="info" markdown="1">

Local storage entity actions are out of scope. Using them in client actions is the standard pattern for offline apps.

</div>

## Impact

A malicious user, even an authenticated one, can:

* Change data before it reaches the database
* Tamper with attributes the UI never exposed
* Bypass business rules

Because the entire record travels from the client to the database unvalidated, corrupted or unauthorized changes get written directly to the database.

## Why is this happening?

Your app runs a database operation (create, update, or delete) directly in the client-side logic instead of inside a server action.

## How to fix

* Move the database operation into a server action.
* Add validation inside that server action before any data reaches the database.
* Validate the logged-in user's permissions in that server action using `Check<ROLENAME>Role()` and `GetUserId()` before the write.
* Treat all inputs to that server action as untrusted, including record IDs. Because server action calls are reachable over HTTP, any parameter, including IDs, can be tampered with.
* Get the user's ID with GetUserId() executed on the server (never passed as a parameter from the client). Verify that the logged-in user is allowed to operate on that specific record.
* As an extra layer of protection, use a non-guessable identifier (such as a GUID) generated on the server side instead of sequential numbers for sensitive records. This prevents users from guessing valid IDs, but it's not a replacement for the server-side permission check.
