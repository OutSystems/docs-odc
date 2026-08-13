---
summary: Learn how to plan, prepare, and set up portfolios in OutSystems Developer Cloud (ODC) based on governance, isolation, and delivery needs.
tags:
  - Architecture
  - CI/CD
  - Development lifecycle
  - Libraries
  - REST
  - Roles
locale: en-us
guid: f7a2c1d8-3e5b-4a9f-b812-6d8e4f2a1c3b
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
audience:
  - Architect
  - Platform administrator
  - Tech lead
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
  - apply
  - evaluate
isautopublish: true
---

# Portfolio planning and setup

This article is intended for architects, tech leads, and platform administrators who are planning to adopt Asset portfolios.

Before your organization starts using asset portfolios, plan how to group your assets, audit your dependencies, and prepare your configurations and governance model. The decisions you make affect governance, isolation, delivery independence, and cross-portfolio reuse. ODC doesn't provide a built-in capability to move assets between portfolios. Moving an asset requires effort and planning, so choosing the right portfolio at creation helps you avoid rework.

For an overview of what portfolios are and how they work, refer to [Asset portfolios](portfolios-overview.md).

<!-- The following diagram shows the portfolio planning flow described in this article. -->

## Grouping assets into portfolios

The following factors help you decide how to group assets into portfolios.

### Non-functional requirements

If your assets share the same non-functional requirements (NFRs), they are strong candidates for the same portfolio:

* Do these assets need the same security and compliance controls?

* Do these assets share the same network access rules and identity providers?

* Do these assets have similar performance and availability targets?

If the answers differ between asset groups, consider placing them in separate portfolios.

### Data isolation

Each portfolio has its own stages and databases. Consider separate portfolios when:

* Regulatory and audit requirements mandate data separation between asset groups.

* You need to prevent heavy database queries in one group from affecting another.

### Delivery process

Each portfolio has its own CI/CD delivery process. Consider separate portfolios when:

* You need to isolate deployment risk so that issues in one group don't block releases in another.

* Different asset groups follow different approval workflows or testing processes.

### Ownership and governance

Consider separate portfolios when:

* Different departments or business units own different groups of assets.

* Different groups require different portfolio level permissions for assets, stages, and stage-level configurations.

* Different asset groups follow different approval workflows or change governance.

## Decision checklist

The following checklist includes some of the questions that help you evaluate whether assets belong in the same portfolio or separate portfolios:

| Question | Same portfolio | Separate portfolios |
| --- | --- | --- |
| Do the assets share the same security and compliance requirements? | Yes | No |
| Do you need to isolate end-user authentication (for example, employee-facing apps versus customer-facing apps) or network configuration between assets? | No | Yes |
| Do the assets share the same release and certification workflow? | Yes | No |
| Are the assets managed by the same ownership group or department? | Usually yes | Usually no |
| Do the assets have different data isolation requirements? | No | Yes |
| Do you need to prevent one group's database load from affecting the other? | No | Yes |

Consider separate portfolios when you have at least one non-negotiable requirement that aligns with the **Separate portfolios** column.

## Common portfolio structures

The following examples show some common ways to structure portfolios. Many organizations combine more than one approach.

### By customer-facing and employee-facing apps

Customer-facing apps and employee-facing apps are common candidates for separate portfolios. Each group typically has different identity providers, custom domains, network access rules, and release schedules.

### By compliance or regulatory boundary

Apps with strict compliance requirements (for example, payment processing or healthcare) benefit from their own portfolio. This gives you dedicated database isolation, specific security configurations, and independent audit trails.

### By department or business unit

When departments operate independently (for example, finance and HR) with different budgets, priorities, and release schedules, separate portfolios give each department control of its delivery process and governance.

### By shared building blocks

A dedicated portfolio for shared libraries, integration connectors, and common UI components works well for a platform group or Center of Excellence (CoE). Assets in other portfolios can consume these libraries across portfolio boundaries.

## Preparation for using portfolios

After deciding your portfolio structure, the following preparation steps help avoid issues during setup.

### Dependency audit

Understanding how your existing apps communicate with each other is critical when you split assets across portfolios.

For each app, identify:

* Which service actions does it expose, and which apps consume them?

* Which entities does it expose as public, and which apps read them?

* Which libraries does it consume?

If an app consumes service actions or public entities from an app in a different portfolio, refactor the dependency by exposing the shared data or logic through a [REST API](../../integration-with-systems/exposing_rest/intro.md) in the data-owning app. Apps in other portfolios consume the REST API. Because REST APIs aren't authenticated by default, add authentication when exposing them across portfolios. For more information, refer to [Token-based authentication for exposed REST APIs](../../integration-with-systems/exposing_rest/token-based-auth-expose-dev-pattern.md).

### Library candidates

Based on the dependency audit, functionality that needs to be available across portfolios belongs in libraries. Common candidates:

* UI components and themes used by multiple asset groups

* Integration connectors (wrappers for external systems like SAP, Salesforce)

* Validation logic and utility functions

Functionality exposed through service actions in apps is only reusable within the same portfolio. Shared functionality that needs to be available across portfolios belongs in libraries.

### Configuration planning

Each portfolio has its own configurations. The following list includes some common settings you configure for each portfolio's stages:

* Custom domains

* Identity providers

* External database connections

* IP filter rules

* Private gateway settings

* SMTP/email settings

A portfolio starts with default configurations. Configuration values from other portfolios don't carry over. For details, refer to [Configuration management with multiple portfolios](portfolios-configurations.md).

### Roles and permissions planning

Roles are defined at the organization level. Portfolio-scoped permissions determine what a user can do in each portfolio. To plan portfolio level permissions, consider the following:

* Group users by responsibilities (for example, developer and tech lead).

* For each responsibility group, split users by the set of portfolios they work in.

* Use one organization role when users need the same permissions in the same set of portfolios. Define separate organization roles when the portfolio sets differ.

* Confirm that each role includes the required portfolio level permissions for its portfolios.

For details, refer to [User management with multiple portfolios](portfolios-user-management.md).

## Portfolio setup

Your existing assets remain in the main portfolio. The following steps prepare each portfolio for use:

<div class="info" markdown="1">

After you add a portfolio to your organization, its stages are provisioned separately. Until stage provisioning completes, stage-scoped features, for example, viewing or editing stage configurations, aren't available.

</div>

1. **Configure each portfolio.** Set up identity providers, custom domains, connections, IP filters, private gateways, and SMTP settings for each portfolio's stages.

1. **Assign roles and permissions.** Assign roles to users, and make sure those roles include portfolio level permissions for the portfolios the users work in.

1. **Create assets in the right portfolio.** When you create apps, libraries, or other assets, create them in the portfolio they belong to. You can't move assets between portfolios later.

For architectural guidance, refer to [App architecture with multiple portfolios](portfolios-app-architecture.md).

## Putting the plan into action

If your organization already has assets, adopting portfolios is an incremental effort. This section focuses on sequencing and adopting existing flows in the target portfolio. For feature-specific tasks, refer to [Configuration management with multiple portfolios](portfolios-configurations.md), [User management with multiple portfolios](portfolios-user-management.md), and [Asset deployment with multiple portfolios](portfolios-deploy-assets.md).

### Recommended sequence

1. **Confirm the target portfolio structure.** Validate the portfolio boundaries and ownership groups you defined in this article.

1. **Refactor cross-portfolio dependencies.** Use [libraries](../../building-apps/libraries/libraries.md) for reusable, stateless functionality, and use [REST APIs](../../integration-with-systems/exposing_rest/intro.md) when an app in another portfolio needs to read or write data.

1. **Prepare portfolio stages.** Set up identity providers, custom domains, connections, IP filters, private gateways, and SMTP/email settings for the stages in each portfolio.

1. **Review and update roles.** Ensure organization roles include the portfolio level permissions users need for the portfolios they work in. Revisit roles when an additional portfolio becomes available to ensure permissions are up-to-date.

1. **Adopt incrementally.** For each asset group, create assets in the target portfolio, validate the end-to-end flows in its stages, and then stop using the previous implementation when it is no longer needed.

### Readiness checklist

Before you start using the implementation in the target portfolio for an existing flow, confirm the following:

* Stage-level configurations required by the assets are set up in the target portfolio.

* Roles include the required portfolio level permissions in the target portfolio.

* Cross-portfolio dependencies use libraries or REST APIs, not service actions or public entities from apps.

* Monitoring and code quality access is available for the target portfolio's stages.

After you start using it, confirm the following:

* Apps don't depend on service actions or public entities across portfolios.

* Consumers use the intended library versions and REST API endpoints.

## Related resources

For more information about planning and working with portfolios, refer to:

### Overview and planning

* [Asset portfolios](portfolios-overview.md)

* [App architecture with multiple portfolios](portfolios-app-architecture.md)

### Configure and govern

* [Configuration management with multiple portfolios](portfolios-configurations.md)

* [Identity provider management with multiple portfolios](portfolios-identity-providers.md)

* [User management with multiple portfolios](portfolios-user-management.md)

### Develop and deploy

* [Asset deployment with multiple portfolios](portfolios-deploy-assets.md)

* [Development with multiple portfolios](portfolios-develop.md)
