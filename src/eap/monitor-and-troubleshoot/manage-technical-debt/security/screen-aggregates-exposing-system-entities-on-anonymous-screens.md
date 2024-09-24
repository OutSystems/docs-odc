---
summary: A Screen Aggregate exposes System Entity data on a screen accessible by anyone. 
tags: 
guid: 54d94ffd-dca4-41fb-8196-1071af65c1e4
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3526-397&node-type=CANVAS&t=fro20soaPpjjIXwf-0
---

# Screen aggregates exposing system entities accessible by anyone

A Screen Aggregate exposes System Entity data on a screen accessible by anyone. 

## Impact

If anyone can access the screen, any end user, including users who aren't logged in, can access sensitive system data (for example, user data).

## Why is this happening?

The configuration allows the screen to be accessible by **Everyone**.

![Screenshot of the UsersInfo screen settings showing the 'Accessible by' option set to 'Everyone'.](images/odcs-screen-accessible-everyone.png "Screen Authorization Settings")

## How to fix

Remove the exposed information or set the authorization to **Authenticated users**. .
