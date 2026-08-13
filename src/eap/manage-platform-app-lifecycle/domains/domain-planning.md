---
summary: Plan domain and subdomain strategy early in OutSystems Developer Cloud (ODC) to minimize disruption and safely manage future organization or stage changes.
tags:
  - Domains
  - External Authentication
  - IdP
  - Mobile app
  - OIDC
  - Private Gateway
  - SAML
locale: en-us
guid: e739f9eb-3200-4559-9cfa-fcbb0f8d5923
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=5030-313
platform-version: odc
audience:
  - Architect
  - Platform administrator
outsystems-tools:
  - odc portal
coverage-type:
  - understand
  - apply
  - evaluate
isautopublish: true
---

# Planning domain changes

How you set up your domains at the start of your ODC journey directly affects how much work a domain change requires later. This article covers both: how to make domain decisions early to minimize future disruption, and how to manage a domain change safely when one becomes necessary.

For an introduction to domains in ODC, see [Domains in ODC](domains.md).
For step-by-step instructions on performing a subdomain change in the ODC Portal, see [Change your built-in organization or stage subdomain](change-subdomain.md).
See also [Configure custom domains for apps](custom-domains.md) for more information on how to use custom domains.

## Decide your domains early {#decide-early}

When you provision a new ODC tenant, two domain decisions are worth making deliberately before you build apps, generate native mobile builds, or configure external identity providers:

* **What subdomain do you want for your organization domain?** This is the address your developers and admins use to access the ODC Portal and ODC Studio (`<subdomain>.outsystems.dev`). Choose a subdomain that reflects your organization's identity clearly and that you expect to keep. Subdomains based on a parent company's legal name, a temporary project name, or an internal code are more likely to need changing later than one based on your public brand.

* **What domains and subdomains do you want for your stages?** For each stage, consider whether the built-in domain (`<subdomain>.outsystems.app`) is the address you want end-users to use long-term, or whether you plan to use a [custom domain](custom-domains.md). Configure it and set it as default as early as possible before apps are built and before external identity providers are configured against the built-in address. Once downstream systems depend on one address, changing it requires updating each of them. Acting early avoids that entirely.

## When circumstances demand a change {#when-change}

Even carefully chosen domains may need to change. Company rebrands, mergers and acquisitions, SDLC restructuring are all common reasons.

Changing a domain is a process you control at your own pace. It has four steps:

1. **Add the new domain**: ODC creates it, but the previous domain remains the default. Both work simultaneously, giving you time to manage the impacts below.

1. **Update dependent configurations**: While the previous domain is still default, update all configurations that reference it. The configurations you need to update depend on which domain you changed (organization or stage) and your setup.

1. **Change the default**: Once you've finished the updates above, set the new domain as default. This is when members or end-users are logged out and reauthenticate through the new address, and when `GetDefaultDomain()` starts returning it.

1. **Delete the previous domain**: Test that everything works correctly with the new default, and once confirmed, delete the previous domain.

The single most important rule across all of the guidance is to **complete all reconfiguration before deleting the previous domain**.

<div class="warning" markdown="1">

Deleting a domain is immediate and permanent. Any traffic still using the previous address stops working instantly, returning a 404 error. Only delete a domain once you've set the new one as default and confirmed that all dependent configurations have been updated.

</div>

The following summaries list what is affected by each type of change, when the impact occurs, and where to find the guidance.

### Organization subdomain change {#org-subdomain-change}

* [Access to ODC Portal and ODC Studio](#access) — Members must reauthenticate twice: once when you add the new subdomain, and again when you set it as default.
* [OIDC providers](#oidc) — Add new redirect URIs alongside existing ones.
* [SAML 2.0 providers](#saml) — Create a new provider in ODC and a new SAML app in the IdP before your organization members start using the new domain.
* [Self-hosted configurator](#self-hosted-configurator) — Apps aren't affected. Reconfigure to configure new self-hosted stages.
* [Bookmarks and links](#bookmarks-links) — Break once you delete the previous domain; SEO may be affected if it was indexed.

### Stage domain change {#stage-domain-change}

* [End-user access to apps](#access) — End-users must reauthenticate once you set the new domain as default. Both domains work until you delete the previous one.
* [Default domain behavior](#default-domain-behavior) — `GetDefaultDomain()` starts returning the new address once you set it as default.
* [Native mobile builds](#mobile-builds) — New builds, distribution and ample time for app updates is required.
* [Private gateways](#private-gateways) — Start a new connector before stopping the previous one for zero-downtime.
* [OIDC providers](#oidc) — Add new redirect URIs alongside existing ones. Old URIs work until you delete the previous domain.
* [SAML 2.0 providers](#saml) — Create a new provider in ODC and a new SAML app in the IdP before your end users start using the new domain.
* [Bookmarks and links](#bookmarks-links) — Break once you delete the previous domain; SEO may be affected if it was indexed.

## Impact details {#impact-details}

### Access and re-authentication {#access}

**Organization domain change**: All members of your organization are temporarily logged out of the ODC Portal and ODC Studio and must log back in. This happens twice: once when you add the new built-in subdomain, and again when you set it as default. Both domains work until you delete the previous one, so members can always log back in using either address. Communicate the new URL to your team before you delete the previous subdomain, giving ample time for adjustment so you don't interrupt the development lifecycle. Once you delete the previous domain, its address returns a 404.

**Stage domain change**: All end-users of apps on this stage are logged out when you set the new domain as default and must reauthenticate. Apps are accessible at both addresses until you delete the previous one. Before deleting it, communicate the new address to your users through appropriate channels for your apps.

### Bookmarks and links {#bookmarks-links}

This applies to both organization and stage domain changes.

Once you delete a domain, any bookmarks or links pointing to it stop working and return a 404 error. If the previous address was indexed by search engines, deleting it removes that URL from search results, which can affect SEO. Communicate the new address to anyone who might have bookmarked or linked to the previous one before you delete it.

### External identity providers {#external-idps}

If you have external identity providers configured, a domain change affects the providers assigned to the scope of the domain you changed: organization-scoped providers for an organization domain change, stage-scoped providers for a stage domain change. What you need to do depends on whether those providers use OpenID Connect (OIDC) or SAML 2.0.

#### OIDC providers {#oidc}

OIDC providers work with redirect URI allowlists. Adding the new URI is additive, so the old one continues working alongside it. After the domain change:

1. In ODC Portal, go to **Manage** > **Identity providers** and click the affected OIDC provider.
1. Go to the **Redirect URLs** tab and copy the new **Login URL** and **Logout URL** for the affected scope.
1. In your provider's portal (for example, Microsoft Entra ID), open the existing app registration and add the new redirect URIs alongside the existing ones. Do not remove the old URIs yet.
1. Verify that authentication works using the new address.
1. Keep both sets of redirect URIs registered in your provider until after you have deleted the previous domain from ODC. Once you delete it, remove the old URIs from your provider as cleanup.

Removing the old redirect URIs before you delete the previous domain causes 401 authentication errors for anyone who still tries to authenticate through that address.

#### SAML 2.0 providers {#saml}

SAML requires more care. When ODC creates a SAML provider, it generates SP metadata, an XML document that contains an EntityID and an Assertion Consumer Service (ACS) URL, both of which embed the domain at that point in time. The EntityID is treated as a permanent, immutable identifier by the SAML standard. Changing it means creating an entirely new service provider as far as the identity provider is concerned. Upon a domain change you must create a new SAML provider in ODC from scratch.

This migration requires coordinating with whoever administers your identity provider:

1. In ODC Portal, [add a new SAML provider](../external-idps/configure-saml2.md).
1. Give the new provider a name that distinguishes it from the old one. Appending the new subdomain or "v2" works well.
1. Select the appropriate scope.
1. In Step 3 (Retrieve SP metadata), the generated SP metadata already contains the new subdomain's EntityID and ACS URL. Download or copy this metadata.
1. Provide the new SP metadata to your IdP administrator. They need to create a new SAML application or entity in the identity provider (for example, a new SAML app in Okta).
1. Once the IdP administrator has configured the new application, they provide you with the IdP metadata (Federation Metadata XML) for it.
1. Upload that metadata to the new SAML provider configuration in ODC Portal and complete the claims mapping.
1. If the provider has end-user group mappings (stage scope only), recreate them on the new provider.
1. Assign the new SAML provider to the same scope as the old one.
1. Test authentication with several accounts through the new provider before proceeding.
1. Only after confirming the new provider works: unassign and then delete the old SAML provider in ODC Portal.
1. Ask your IdP administrator to delete the old SAML application from the identity provider as cleanup.

Do not delete the previous domain until the new SAML provider is fully operational and tested. Until then, the old provider is the only working authentication path.

### Default domain behavior {#default-domain-behavior}

This applies only to stage domain changes.

If the built-in domain is set as the default domain for this stage, ODC doesn't update the default domain automatically when you add a new subdomain. Only once you explicitly set the new subdomain as default does it take effect. Timers, workflows, emails with screen links, ODC Studio debugging, and any app logic using the `GetDefaultDomain()` action all switch to the new address at that point.

One thing to be aware of: any emails already sent before the change that contain links using the previous address break once you delete the previous domain. Keep it active long enough for time-sensitive links (password reset emails, workflow task notifications) to be actioned or expired.

### Native mobile builds {#mobile-builds}

This applies only to stage domain changes.

This is the highest-risk impact of a stage domain change, and it determines the minimum time you must keep the previous domain active.

Native mobile apps have the backend domain hardcoded at build time. While both the previous and new domain continue to work while active, when a domain is deleted, users of the app are unable to connect to the server. Both domains are active while you work through the transition. The risk is in deleting the previous domain before all users have migrated to a new build and in the time new builds may take to be fully distributed.

Before changing the stage domain, inventory all published native mobile apps targeting this stage. For each app, note which stores it is distributed through and its approximate active user base. This tells you how long you need to keep the previous domain active after the change.

After changing the stage domain:

1. [Generate new mobile app packages](../../building-apps/mobile/creating-mobile-package.md) for all affected apps in ODC.
1. Submit the new builds to the Apple App Store and Google Play Store or to any other distribution method. Allow time for store review.
1. Once the new builds are approved and available in the stores, prompt users to update through in-app messaging, push notifications, or release notes.
1. Monitor the adoption of the new build version through app store analytics or other means.
1. Do not delete the old domain until the active user count on old builds is at an acceptably low level.

Deleting the old domain while a significant number of users are still on old builds permanently breaks their ability to connect to the server.

### Private gateways {#private-gateways}

This applies only to stage domain changes.

The Cloud Connector (`outsystemscc`) maintains an outbound connection to the [Private gateway](../private-gateway.md) using the stage's built-in domain address. ODC supports multiple simultaneous Cloud Connector instances on the same Private gateway, so you can start a new connector before stopping the old one and avoid any gap in private resource access.

After changing the stage domain:

1. In ODC Portal, go to the stage's Private Gateway configuration and copy the new address.
1. Start a new `outsystemscc` instance using the new address. The token remains the same.
1. Confirm the new connector is connected by checking the logs for `client: Connected (Latency Xms)`.
1. Stop the old connector instance.
1. If your network uses a Layer 7 firewall that filters by domain name, update the allowed domain to the new subdomain.

If you stop the old connector before the new one is connected, there is a gap in private resource access.

### Self-hosted configurator {#self-hosted-configurator}

This applies only to organization domain changes in Self-hosted ODC tenants.

If you have self-hosted stages, the self-hosted configurator maintains an outbound connection to ODC platform services using the portal address (`https://<subdomain>.outsystems.dev`). When the organization subdomain changes, that connection breaks and must be reconfigured to use the new address. Apps already running on the stage continue to function.

If you don't reconfigure the self-hosted configurator before deleting the previous domain, two critical issues occur:

* The cluster stops receiving OutSystems service updates.
* New revisions published in development aren't available to deploy to self-hosted stages.

After changing the organization domain:

1. [Reopen the self-hosted configurator](../self-hosted/sh-open-configurator.md) using the new organization domain and login.
1. Do this before you delete the previous domain to ensure the cluster continues receiving OutSystems service updates.
