---
summary: Error fetching the entity list
tags:
guid: 3b1172f2-e949-4099-8c8d-f2f67127c0f5
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-INTC-60005

## Error message

`Error fetching the entity list.`

## Cause

There is an error when retrieving the list of entities from the external system and the you are on the **Connection List** screen.

## Impact

If this happens after creating a connection, you can't select entities and attributes to include in the connection. This error prevents you from integrating with the external system.<br/>
If it happens after editing a connection or refreshing the entity list, you might be unable to select new entities or attributes recently added to the external system.

## Recommended action

If the **Select entities** button is enabled, click it and refresh the entity list. If the error persists, verify your connection configuration by editing and testing.<br/>
If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-INTC-60005).
