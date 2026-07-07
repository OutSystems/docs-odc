---
summary: "OutSystems Developer Cloud (ODC) asset portfolio best practices: dependency planning, libraries, REST APIs, and least-privilege permissions."
tags:
  - Architecture
  - Best Practices
  - Libraries
  - REST
  - Security
locale: en-us
guid: 8c4a3f2e-1b7d-4e9a-9f15-3d6e8a2b1c4f
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
audience:
  - Architect
  - Platform administrator
  - Tech lead
outsystems-tools:
  - odc portal
  - odc studio
coverage-type:
  - evaluate
isautopublish: true
---

# Best practices for asset portfolios in ODC

Asset portfolios in ODC shape how you group, govern, and deliver assets. This article summarizes key practices for designing portfolio boundaries, sharing logic and data across them, and governing access in a multi-portfolio organization.

This article assumes you're familiar with [Asset portfolios](portfolios-overview.md) and have reviewed [Portfolio planning and setup](portfolios-plan.md).

## Audit dependencies before grouping assets into portfolios

Apps within a portfolio share service actions and entities. Apps in different portfolios don't. Splitting assets across portfolios without understanding existing dependencies leads to broken consumers and unplanned refactoring.

### Recommendations

Before grouping assets into portfolios, identify the service actions and public entities each app exposes and which apps consume them. Refactor cross-portfolio dependencies into [libraries](../../building-apps/libraries/libraries.md) for shared logic or [REST APIs](../../integration-with-systems/exposing_rest/intro.md) for shared data before separating the assets.

### Benefits

Auditing dependencies up front avoids surprise breakages and reduces the need to move or restructure assets after creation, which ODC doesn't support natively.

## Keep apps that share public elements in the same portfolio

Service actions and entities are portfolio-scoped. Apps that need to consume each other's public elements only work when they're in the same portfolio.

### Recommendations

Map your apps to bounded contexts and keep apps in the same bounded context together in one portfolio. When in doubt, group apps that share service actions, public entities, or tightly coupled business logic.

### Benefits

Keeping related apps together preserves the loosely-coupled reuse model that ODC apps rely on and avoids forcing every cross-app integration through a REST API.

## Use libraries for shared logic across portfolios

Libraries are the only mechanism for sharing logic across portfolio boundaries. Functionality exposed through service actions is reusable only within the same portfolio.

### Recommendations

Move shared stateless functionality (UI components, validation rules, integration connectors, utility functions) into [libraries](../../building-apps/libraries/libraries.md). Any asset in any portfolio can consume a library.

### Benefits

Libraries give you a single source of truth for shared logic, avoid duplication across portfolios, and let you update shared functionality independently of the apps that consume it.

## Use REST APIs for cross-portfolio data sharing

Libraries are stateless and can't persist data. When an app in one portfolio needs to read or write data owned by an app in another portfolio, the only supported integration is a REST API.

### Recommendations

Expose data through a [REST API](../../integration-with-systems/exposing_rest/intro.md) from the app that owns the data. Apps in other portfolios consume the API like any external integration. Coordinate the API contract, authentication, and base URL with the owners of consuming apps.

### Benefits

REST APIs preserve portfolio isolation while enabling necessary cross-portfolio data flow, with explicit contracts that make ownership and dependencies clear.

## Use a dedicated portfolio for shared building blocks

When shared libraries are developed and released alongside application code, their delivery cadence is tied to the apps that consume them.

### Recommendations

Place shared libraries (UI themes, integration connectors, validation logic) in a dedicated portfolio owned by a Center of Excellence (CoE). Other portfolios consume these libraries across the portfolio boundary.

### Benefits

A dedicated portfolio gives the CoE its own delivery process and governance for shared components, while consuming portfolios adopt updates on their own schedule.

## Choose the portfolio at asset creation

ODC doesn't provide a built-in way to move assets between portfolios. The portfolio you select when creating an asset is where the asset stays.

### Recommendations

Verify the portfolio selection in the ODC Portal before creating any asset. If your organization uses tools like Mentor or installs assets from Forge, confirm the target portfolio at the start of each flow.

### Benefits

Choosing the right portfolio at creation avoids the effort of recreating or refactoring assets later, which can require reworking dependencies and reconfiguring stage-level settings.

## Apply least privilege with portfolio-scoped permissions

Portfolio-scoped permissions let you control what each user can do in each portfolio. Granting broad permissions across all portfolios increases the impact of mistakes and security incidents.

### Recommendations

Group users by responsibility (for example, developer, tech lead, platform admin) and identify which portfolios each group needs access to. Define custom roles with portfolio-scoped permissions only for the portfolios users actively work in. For details, refer to [User management with multiple portfolios](portfolios-user-management.md).

### Benefits

Least-privilege roles reduce the risk of unintended changes outside a user's responsibility and keeps accountability clear.

## Related resources

For more information about planning, designing, and governing portfolios, refer to:

### Planning and architecture

* [Asset portfolios](portfolios-overview.md)

* [Portfolio planning and setup](portfolios-plan.md)

* [App architecture with multiple portfolios](portfolios-app-architecture.md)

### Configure and govern

* [User management with multiple portfolios](portfolios-user-management.md)

* [Configuration management with multiple portfolios](portfolios-configurations.md)

### Develop and deploy

* [Development with multiple portfolios](portfolios-develop.md)

* [Asset deployment with multiple portfolios](portfolios-deploy-assets.md)
