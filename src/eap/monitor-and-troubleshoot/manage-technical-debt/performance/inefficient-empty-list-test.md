---
summary: Use the Count property of an Aggregate for SQL query to check if results were returned. 
tags: 
guid: 468193f3-a09a-4dfb-acc8-f14947476d95
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# Inefficient empty list test

Using the Count property of an Aggregate or SQL query to check if results were returned.

## Impact

For performance, the OutSystems query optimizer ensures that the output of Aggregates and advanced queries only contains the essential data to feed a screen. This means the Count property needs to execute an additional query to get the total number of registries.

## Why is this happening?

This occurs because the Count property of an Aggregate or SQL query results were returned. 

## How to fix

Use **List.Empty** property to test for lack of results instead of **List.Count.**
