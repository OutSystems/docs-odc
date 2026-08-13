---
summary: Manage domains in OutSystems Developer Cloud (ODC), understanding organization and stage built-in and custom domains, and the impact of domain changes.
tags:
  - Domains
locale: en-us
guid: c14800bd-f88f-4bd9-ac4e-534351681267
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=5017-10
platform-version: odc
audience:
  - Architect
  - Platform administrator
outsystems-tools:
  - odc portal
coverage-type:
  - understand
isautopublish: true
---

# Domains in ODC

When you work with ODC, domains are involved in how your organization and apps are accessed. Understanding how they relate to each other, and what happens when any of them changes, helps you plan domain changes safely and avoid disruption.

## Domain types {#domain-types}

ODC uses two domain types: built-in and custom. The organization domain is always built-in. Each stage always has a built-in domain, and you can optionally add one or more custom domains alongside it to make your apps accessible through your own company address.

### Built-in domain {#built-in-domain}

A built-in domain is automatically created by OutSystems when your ODC organization is provisioned. There are two types:

* **Organization domain**: used to access the ODC Portal and ODC Studio. It follows the format `<subdomain>.outsystems.dev`.
* **Stage domain**: used by end-users to access your apps on each stage. It follows the format `<subdomain>.outsystems.app`.

Both are based on a subdomain assigned during provisioning. You can change this subdomain at any time from the ODC Portal. Each level is independent: changing the organization subdomain does not affect stage subdomains, and vice versa.

When you change a subdomain, ODC creates a new one. It isn't set as default automatically, and both subdomains keep working until you delete the previous one. [Setting the new subdomain as default](change-subdomain.md#set-default) only changes [which address is used by default](#default-domain); it doesn't affect either subdomain's availability. This lets your organization and apps continue to run as expected while you update all configurations that reference the previous address. Once you've set the new subdomain as default and updated everything that depends on it, you can delete the previous subdomain.

You can't delete the only built-in subdomain, but you can [change it](change-subdomain.md) at any time.

### Custom domain {#custom-domain}

A custom domain is a domain you own, with any subdomain you choose, that you configure to make your apps accessible through your organization's own address. Custom domains apply at the stage level and are managed separately from built-in domains.

For instructions on setting up custom domains, see [Configure custom domains for apps](custom-domains.md).

To make an app the entry point for a custom domain's root URL, refer to [Default app for a custom domain](default-app-for-domain.md).

## Default domain {#default-domain}

The default domain is the domain ODC uses:

* in calls to ODC REST APIs to retrieve the organization and stage domains.
* in emails sent from your OutSystems apps that contain links to specific screens.
* to open apps via ODC Studio and ODC Portal.
* to connect to the app during debugging in the development stage.
* in app logic that uses the [GetDefaultDomain](../../reference/system-actions/get-default-domain.md) action.

The organization and each stage can have a maximum of 2 built-in domains active at a time, with only one of those set as default. You can also set a custom domain as default for a stage, independently of the built-in domains. When a custom domain is set as default, it takes precedence and the built-in default has no effect. The built-in default only applies when no custom domain is set as default.

| Custom domain default     | Effective default |
|---------------------------|-------------------|
| None                      | Built-in domain   |
| Active and set as default | Custom domain     |

When your organization is first provisioned, the built-in domain is set as the default for each stage. This automatic assignment only happens at provisioning. Later on, whether you [change the built-in subdomain](change-subdomain.md#set-default) or [add a custom domain](custom-domains.md#set-default-domain), you must explicitly set the new one as default.
You can't delete a default domain. To delete it, first set another domain as default. If you are deleting the only custom domain that is set as default, switch the default to the built-in domain first.

## Planning a domain change {#planning-change}

Changing a domain is a process you control at your own pace. Depending on your setup, it can affect your identity providers, private gateways, native mobile builds, self-hosted stage setup, and your users' ability to access the ODC Portal and apps.

<div class="info" markdown="1">

Before making any domain change read [Domain planning and domain changes](domain-planning.md). It covers how to choose your domains from the start to minimize future disruption, and provides guidance for every system a change can affect.

</div>
