---
guid: b6c0c043-0b0a-4825-9271-afaa60bd2ee9
locale: en-us
summary: Minimum Platform Server, LifeTime, and IDE versions required for each O11 and ODC interoperability capability.
figma:
coverage-type:
  - remember
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Authentication
  - Data
  - External Authentication
  - Infrastructure
  - Logic
  - Platform Server
outsystems-tools:
  - platform server
  - lifetime
  - service studio
  - odc studio
helpids:
isautopublish: true
---

# Interoperability version requirements

Before you set up O11 and ODC interoperability, make sure your O11 infrastructure and development tools meet the minimum version requirements for the capabilities you want to use.

## Data interoperability {#data-interop}

The following table lists the minimum **Platform Server** and **LifeTime** versions required for each data interoperability capability:

| Capability | Minimum Platform Server | Minimum LifeTime |
| --- | --- | --- |
| - ODC read/write O11 data for SQL Server<br/>- ODC read O11 data for Oracle<br/>- Support for infrastructures with additional pipelines | 11.40.0 | 11.29.0 **\*** |
| - ODC write O11 data for Oracle<br/>- User and Tenant system entities exposed to ODC | 11.41.0 | 11.29.0 **\*** |

<div class="info" markdown="1">

**\*** **LifeTime 11.29.0** ensures connectivity through a LifeTime service account bound to your ODC organization. If you have a previous version of LifeTime, existing LifeTime service account access tokens continue to work until they expire.

Creating or generating a new LifeTime service account access token for data interoperability requires LifeTime 11.29.0 or later.

After upgrading LifeTime to 11.29.0 or later, update your integration to use service accounts created with the new version. For the updated steps, see [Configure LifeTime access for ODC interoperability](data-interoperability/configure-connection.md#connect-o11-infrastructure).

</div>

<div class="info" markdown="1">

Version requirements are only part of the setup. For the full list of data interoperability prerequisites, including network and other infrastructure requirements, refer to [data interoperability prerequisites](data-interoperability/data-interop.md#prerequisites).

</div>

### Incremental Platform Server updates

You can update the **Platform Server** version of your O11 environments incrementally:

* Update your [O11 baseline environment](data-interoperability/expose-entities.md#configure-baseline) first, so you can expose O11 entities in that environment and import them from ODC. This enables you to start developing in ODC.

* Then, update the remaining O11 environments (for example, QA or Production) when you need to [promote the exposed entities](data-interoperability/expose-entities.md#promote) to those environments.

## Logic interoperability {#logic-interop}

The following table lists the minimum **Platform Server** version required for logic interoperability:

| Capability | Minimum Platform Server |
| --- | --- |
| Logic interoperability | 11.41.0 |

Your development teams also need the following tool versions:

* **Service Studio 11.55.59.64640** or later
* **ODC Studio 1.6.21 (Build 9475)** or later

## User interoperability {#user-interop}

The following table lists the minimum **Platform Server** version required for user interoperability with O11 built-in authentication:

| Capability | Minimum Platform Server |
| --- | --- |
| User interoperability with O11 built-in authentication | 11.27.0 |

<div class="info" markdown="1">

User interoperability with **O11 external authentication** doesn't require any specific version of OutSystems components.

</div>
