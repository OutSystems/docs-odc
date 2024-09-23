---
summary: Avoid setting screens as accesible by everyone. 
tags: 
guid: a79460d2-73d4-4db2-9a28-bb32219c3d72
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# Avoid setting screens as accessible by everyone

## Impact

The default authorization for screens is accessible only by authenticated users. When you change it to be accessible by **Everyone**, any end-user can log in.

## Why is this happening?

The screen authorization is accessible to **Everyone**. 

![Screen authorization settings showing the option to set accessibility to Everyone or Authenticated Users.](./images/odcs-accessible-everyone.png "Screen Authorization Settings")

## How to fix

Set screens to be accessible by **Authenticated Users** unless you prefer to make them public to everyone. In that case, set them to **Everyone**. 

