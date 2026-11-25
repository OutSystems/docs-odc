---
guid: f4d563ae-20a0-4106-a7fe-cb0316607844
locale: en-us
summary: Understand what ODC EU Sovereign Cloud is, how it differs from ODC Cloud, and the key benefits it offers regulated European organizations.
figma:
coverage-type:
  - understand
  - evaluate
topic:
  - eu-sovereign-overview
  - move-apps-to-eu-cloud
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Platform administrator
  - Tech lead
  - Architect
tags:
  - Architecture
  - Data
  - External Authentication
  - IdP
  - Infrastructure
  - OIDC
  - Security
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# ODC EU Sovereign Cloud

ODC EU Sovereign Cloud is an offering of OutSystems Developer Cloud (ODC) that runs your Test and Production stages on EU-owned infrastructure in Germany. OutSystems manages it end to end, and an EU-based operator runs the infrastructure for your stages. The offering targets EU-based organizations in regulated sectors, such as public sector and government, defense, financial services, healthcare, and critical infrastructure.

## Benefits of using ODC EU Sovereign Cloud

With ODC EU Sovereign Cloud, you can:

* **Keep your data inside the EU:** Your Test and Production business data, backups, logs, traces, and secrets are stored and processed in Germany.
* **Run on infrastructure and operations that are fully EU-based:** An EU-based operator manages your runtime infrastructure, and EU-based staff handle your support requests.
* **Control access to your Production stage:** OutSystems has no standing access to your Production stage. Access happens only when you grant it on a support ticket.

## How ODC EU Sovereign Cloud differs from ODC Cloud

ODC EU Sovereign Cloud is a fully managed, EU-operated cloud offering. OutSystems operates the ODC Portal, the platform services, and the Development stage, the same way it does for ODC Cloud. Your Test and Production stages run on EU-owned infrastructure, operated under the ODC EU Sovereign Cloud program to keep your runtime inside the sovereignty boundary. Refer to the [Shared responsibility model for ODC EU Sovereign Cloud](esc-shared-responsibility.md) for the full division of responsibilities.

The following table compares ODC EU Sovereign Cloud with ODC Cloud:

| Question | ODC EU Sovereign Cloud (Test and Production stages) | ODC Cloud (EU region) |
| --- | --- | --- |
| Where does your data stay? | Your Test and Production business data, backups, logs, traces, and secrets are stored and processed in Germany. | Application data stays in the EU. |
| Who resolves your support requests? | EU-resident staff, every time. Support is opened and resolved inside the EU. | A global support team. |
| How does capacity scale? | Fixed tiers, changed by change request. | Automatic scaling. |

## Who operates ODC EU Sovereign Cloud {#who-operates}

OutSystems is accountable for your entire ODC EU Sovereign Cloud offering, from the ODC Portal to your runtime stages. OutSystems operates the platform directly. It delivers your Test and Production runtime through its Sovereign Operator, an EU-based operator that runs your stages on EU-owned infrastructure. This keeps your Test and Production stages inside the EU sovereignty boundary.

For example, if your application becomes unresponsive in Production, the issue is detected through monitoring of your runtime.

For the full division of responsibilities, refer to the [Shared responsibility model for ODC EU Sovereign Cloud](esc-shared-responsibility.md).

## Use cases

ODC EU Sovereign Cloud fits organizations whose production applications need to operate independently of non-EU cloud providers, particularly if you operate in a sector with strong sovereignty requirements:

* **Public sector and government organizations** that are restricted from using cloud infrastructure controlled by non-EU companies.
* **Financial services, healthcare, and critical infrastructure providers** subject to sector-specific data-residency requirements.
* **Defense organizations** that need EU-only access to their application data and operations.

## Prerequisites and moving existing apps

To use ODC EU Sovereign Cloud, you need an external OIDC identity provider for each stage and named technical contacts for your organization. Only these technical contacts can open and manage support tickets. For how to register them, refer to [Getting support for ODC EU Sovereign Cloud](esc-getting-support.md).

If your organization already runs OutSystems, you can move to ODC EU Sovereign Cloud, but not through an in-place migration. The move requires a fresh setup under a new contract. You export your applications from your current environment and import them into ODC EU Sovereign Cloud. Business data, end users, settings, and secrets don't move with your apps.

For the tasks to get started, refer to [Getting started with ODC EU Sovereign Cloud](esc-get-started.md).

## Related resources

Refer to the following resources for related concepts:

* [Getting started with ODC EU Sovereign Cloud](esc-get-started.md)
* [Shared responsibility model for ODC EU Sovereign Cloud](esc-shared-responsibility.md)
* [ODC EU Sovereign Cloud limitations](esc-limitations.md)
