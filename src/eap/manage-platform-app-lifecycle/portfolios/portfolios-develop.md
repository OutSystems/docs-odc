---
summary: OutSystems Developer Cloud (ODC) cross-portfolio development uses libraries for shared logic and REST APIs for shared data between portfolios.
tags:
  - CI/CD
  - Development lifecycle
  - Entities
  - Libraries
  - REST
locale: en-us
guid: f0a7b3c5-1d8e-4f4a-e963-2b7c9d5f1a6e
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
audience:
  - Developer
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
  - evaluate
isautopublish: true
---

# Development with multiple portfolios

In a multi-portfolio organization, each asset belongs to a single portfolio. Cross-portfolio reuse works differently for app elements, libraries, and REST APIs. This article covers how to work across portfolios.

<div class="info" markdown="1">

Developing in a multi-portfolio organization requires ODC Studio version 1.7.13 or later.

</div>

## Asset assignment

Every asset (app, library, workflow, agentic app) belongs to a specific portfolio, selected at creation. ODC doesn't provide a built-in way to move assets between portfolios. Choosing the right portfolio at creation helps you avoid rework.

## Element availability across portfolios

Which elements you can consume depends on the asset type and the portfolio the asset belongs to:

* **Libraries** are available across all portfolios. You can consume any library in your organization regardless of where it lives.

* **Public elements from apps** (service actions, entities) are only available within the same portfolio.

Accessing an element in another portfolio requires a [library](../../building-apps/libraries/libraries.md) for shared logic or a [REST API](../../integration-with-systems/exposing_rest/intro.md) for shared data.

## Libraries for shared logic

[Libraries](../../building-apps/libraries/libraries.md) are the primary way to share logic across portfolios. Common candidates include validation rules, UI components, integration connectors, and utility functions. Any asset in any portfolio can consume a library.

Libraries are stateless. They can't persist data. If you need to share data across portfolios, a REST API is the right approach.

ODC Studio notifies you when an updated library version is available. Reviewing the release notes before you accept an update helps you spot breaking changes. For details, refer to [Update to a library version](../../building-apps/libraries/libraries.md#update-consumers).

## REST APIs for shared data

To read or write data owned by an app in another portfolio, the data-owning app exposes a [REST API](../../integration-with-systems/exposing_rest/intro.md). You consume it like any external integration.

Unlike libraries, REST APIs aren't discoverable through the public elements mechanism. REST API consumption typically requires coordination with the API owner for the base URL, available methods, and authentication requirements.

## Breaking changes and cross-portfolio impact

ODC tracks cross-portfolio impact for libraries and shows which portfolios consume a library. For REST APIs, there is no automatic cross-portfolio impact analysis. If you change a REST API signature, you are responsible for notifying consumers. As a best practice, create a new version of the endpoint rather than modifying the existing one.

## Portfolio-scoped configurations

Each portfolio has its own configurations. If you work across multiple portfolios, be aware that:

* REST API endpoint URLs may have different values in different portfolios' stages.

* Identity providers may differ between portfolios, which affects how end users authenticate.

* Connection strings and credentials are configured for each portfolio.

Consuming a REST API from another portfolio requires configuring the base URL and authentication for each stage. For more information, refer to [Consume a REST API](../../integration-with-systems/consume_rest/consume-a-rest-api.md).

## Independent delivery pipelines

Each portfolio has its own stages and CI/CD delivery process. Deployments and promotions are scoped to the portfolio, which isolates delivery pipelines between portfolios. For more information, refer to [Asset deployment with multiple portfolios](portfolios-deploy-assets.md).

## Quick reference

| Element | Within a portfolio | Across portfolios |
| --- | --- | --- |
| Service actions | Available | Not available — use libraries or REST APIs |
| Entities (read-only) | Available | Not available — use REST APIs |
| Libraries | Available | Available |
| External libraries | Available | Available |
| Templates | Available | Available (one-time copy at creation) |

## Related resources

For more information about working across portfolios, refer to:

### Portfolio context

* [Asset portfolios](portfolios-overview.md)

* [Asset deployment with multiple portfolios](portfolios-deploy-assets.md)

### Reuse and integration

* [Reuse elements across apps](../../app-architecture/reuse-elements.md)

* [Libraries](../../building-apps/libraries/libraries.md)

* [Expose a REST API](../../integration-with-systems/exposing_rest/expose-a-rest-api.md)
