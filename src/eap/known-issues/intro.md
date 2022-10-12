---
summary: A list of known issues and workarounds.
tags:
locale: en-us
guid: ebae908a-42f3-475f-be53-28aef8454497
app_type: mobile apps, reactive web apps
---

# Known issues and workarounds

A list of known issues and workarounds.

## Inconsistent overflow behavior of LongIntegerToInteger

Depending on where you use LongIntegerToInteger and get an overflow, your logic returns the following:

* On client and client side, LongIntegerToInteger on overflow returns 0.
* On the database, LongIntegerToInteger on overflow throws an error.
