---
summary: Understand how installing and updating Forge assets works in a multi-portfolio organization in OutSystems Developer Cloud (ODC).
tags:
  - Forge
locale: en-us
guid: 2f5b8a1c-9d3e-4c61-8e7a-3b5d8f1a2c9e
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
audience:
  - Developer
  - Platform administrator
  - Tech lead
outsystems-tools:
  - forge
  - odc portal
  - odc studio
coverage-type:
  - understand
isautopublish: true
---

# Forge assets with multiple portfolios

In a multi-portfolio organization, installing and updating Forge assets is portfolio-scoped. An installed Forge asset belongs to a portfolio, and you manage it like any other asset in that portfolio.

## Portfolio ownership of installed assets

In a multi-portfolio organization, you choose the portfolio that owns the asset during installation. The asset follows that portfolio's stages, configurations, and access controls.

Forge installs each asset in one portfolio in your organization.

You can't move an asset to a different portfolio after installation.

## Portfolio level permissions

The permissions to install and update Forge assets are portfolio level. You install or update Forge assets only in portfolios where you have the relevant Forge permissions.

For more information about portfolio level permissions, refer to [User management with multiple portfolios](portfolios-user-management.md).

## Dependencies

When you install a Forge asset, Forge also installs required dependencies. Portfolio-scoped permissions apply to the asset you install and any dependencies that Forge installs with it.

## Cloned assets

After installation, Forge assets are locked. Locked means the asset is read-only:

* You use the Forge asset in your apps.
* You open the Forge asset in ODC Studio to inspect it.
* You don't edit the Forge asset's implementation.

Clone a Forge asset only when you need to modify its implementation. When you clone an installed asset, you choose which portfolio the clone belongs to. The clone is a separate copy of the asset in your organization that you can edit, and it follows the target portfolio's stages, configurations, and access controls. Apps that reference the original Forge asset continue to reference it until you update them to reference the clone.

Cloned assets aren't supported and don't receive updates from the original Forge asset. For more information, refer to [Modify an installed Forge asset](../../building-apps/forge/install.md#modify-an-installed-forge-asset).

## Related resources

For more information about Forge and portfolio context, refer to:

### Forge

* [Install or update a Forge asset](../../building-apps/forge/install.md)

* [Forge](../../building-apps/forge/intro.md)

### Portfolio context

* [Asset portfolios](portfolios-overview.md)
