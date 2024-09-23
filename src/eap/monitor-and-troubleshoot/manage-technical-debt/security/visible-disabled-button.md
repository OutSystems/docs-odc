---
summary: Disabled button that is still visible. 
tags: 
guid: 80a844f0-57f8-43eb-af04-5e727cd3bb38
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3616-10&node-type=CANVAS&t=E0BY5XjNnogt1jmq-0
---

# Visible disabled Button

Disabled button that's still visible.

## Impact

A disabled button doesn't prevent an experienced person from re-enabling the button at runtime by using, for example, the development tools on a browser. This allows the user to enable the functionality and press the button, even without permission or if they were originally unable to press it.

## Why is this happening?

A disabled button remains visible when the **Enabled** property is set to False, and the **Visible** property is set to True. 

![Button properties configuration showing Enabled set to False and Visible set to True.](./images/odcs-enable-visible.png "Button Properties Configuration")

## How to fix

Instead of setting the **Enable** property to False, consider setting the **Visible** property instead, or use both properties together. This prevents the button from rendering completely on the client browser and prevents an experienced user from hacking the button and enabling the functionality.
