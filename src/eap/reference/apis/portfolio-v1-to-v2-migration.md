---
summary: Learn how to migrate an existing Portfolio API v1 integration to v2, including updated URL paths, changed Environment fields, and new endpoints.
locale: en-us
guid: 8bb7022b-2e70-4f1d-b5ea-2807b7135e97
app_type: mobile apps, reactive web apps
platform-version: odc
content-type:
  - procedure
audience:
  - Developer
  - Front-end developer
figma:
tags:
  - REST
  - Web services
outsystems-tools:
  - odc portal
isautopublish: true
---

# Migrate from Portfolio API v1 to v2

Portfolio API v2 is a superset of v1. This guide covers only what you need to change to migrate an existing v1 integration. Anything not listed here behaves the same as v1: authentication, query parameters, pagination, error format, and the top-level `DeployedAsset` structure.

## What's new in v2

In addition to everything available in v1, v2 introduces:

| New capability | Endpoint |
| --- | --- |
| List portfolios | `GET /portfolios/v2/portfolios` |
| Rename a portfolio | `PATCH /portfolios/v2/portfolios/{portfolioKey}` |
| Rename or reorder a single environment | `PATCH /portfolios/v2/environments/{environmentKey}` |
| Batch rename or reorder environments | `PATCH /portfolios/v2/environments` |
| List libraries (with their portfolio and revisions) | `GET /portfolios/v2/libraries` |

## Update the URL path

All endpoint paths change their version segment from `/portfolios/v1/` to `/portfolios/v2/`. For example:

* `GET /portfolios/v1/deployed-assets` → `GET /portfolios/v2/deployed-assets`
* `GET /portfolios/v1/environments` → `GET /portfolios/v2/environments`

## Environment fields that no longer exist

The `Environment` object returned by `GET /portfolios/v2/environments` removes the following fields:

| Removed field (v1) | Replace with (v2) | Notes |
| --- | --- | --- |
| `hostname` | `builtinDomain` | Same value, renamed. |
| `isConfigured` | `status` | Boolean replaced by a richer lifecycle enum (refer to the following section). |
| `isDeployedToCluster` | `status` | Boolean replaced by the same `status` enum. |

v2 also adds these fields:

* `defaultDomain`: the environment's default domain if a custom domain is configured, otherwise the built-in domain.
* `status`: self-hosted environment lifecycle state. Values: `Pending`, `Configured`, `Deployed`, `MissingConfigurations`, `Ready`, `Hibernating`, `WakingUp`.
* `portfolioKey`: the portfolio the environment belongs to.

## `EnvironmentPurpose`: Unknown no longer returned

v2 returns one of `Development`, `NonProduction`, or `Production`. The `Unknown` value is no longer returned. Instead, the `purpose` field may be absent or `null` when the purpose cannot be determined. Replace any handling of `Unknown` with handling for a missing value.

## Deployment URLs use the default domain

In v1, deployment URLs in `GET /deployed-assets` were built from the environment's built-in domain. In v2 they are built from the environment's default domain: the custom domain if configured, otherwise the built-in domain. If you store, display, or compare these URLs, account for this change.

## New optional field on `Deployment`

Each `Deployment` (nested inside `DeployedAsset`) gains an optional `portfolioKey` field indicating the portfolio of the deployment's environment. This is a non-breaking addition. No action is required unless you want to use it.

## Related resources

For more information, refer to the following resources:

* [Portfolio API v2 reference](portfolio-v2.md)
* [Portfolio API v1 reference](portfolio-v1.md)
