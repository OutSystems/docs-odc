---
summary: 'ODC asset lifecycle explained: how publishing, revisions, versions, deployments, and merge work across apps, libraries, and workflows.'
tags:
  - 1-Click Publish
  - Agentic
  - Deploy
  - Development lifecycle
  - Libraries
  - Lifecycle
  - Workflows
locale: en-us
guid: 3d3772e6-8557-426d-9352-6b1a9a213cde
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Architect
  - Developer
  - Tech lead
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - remember
  - understand
topic:
  - 1-click-publish-steps
  - odc-deployment-terminology
  - library-revision-vs-version
  - merging-revisions
  - deploy-workflow
content-type:
  - conceptual
isautopublish: true
---
# Publishing your assets

In OutSystems Developer Cloud (ODC), publishing stores a revision of your asset and builds that revision for the Development stage. What happens next depends on the asset type. You deploy apps and workflows to other stages, and you release libraries so that other assets consume them.

This article defines the lifecycle concepts that apply across all ODC asset types: apps, agentic apps, libraries, and workflows.

## The asset lifecycle

The rest of this section explains how these concepts connect over an asset's lifecycle.

You **publish** your asset from ODC Studio or the workflow editor, which creates a **revision**, an automatic, incremental snapshot of its source code. ODC compiles each revision into a **build**: a debug build in the Development stage, and a release build everywhere else. A **deployment** moves an app or workflow's build to another stage. A **release** makes a library available to its consumers instead. A **version** marks a revision as stable, set at Production deployment or at library release. Before each publish, a **merge** reconciles your local work with the latest published revision.

<div class="info" markdown="1">

If you're coming from OutSystems 11, the number that increments on each publish is the revision. OutSystems 11 called that number the version. In ODC, a version is the separate semantic identifier you set at Production deployment or at library release.

</div>

## Concept definitions

The following table summarizes each concept and the moment it occurs.

| Concept | Moment | Definition |
| --- | --- | --- |
| Publish | Any time after you edit the asset | Stores your changes as a revision in the Development stage and starts a build. 1-Click Publish for apps and libraries, or Publish for workflows. You optionally add a message. |
| Revision | At each publish | Automatic, incremental, immutable whole-number snapshot of the asset's source code. Exists independently of any stage. |
| Build | At each publish, and ahead of a deployment | Compiles a revision into a deployable package. The Development stage runs debug builds. Apps and workflows run release builds in every other stage, which package a revision as a container image. |
| Deployment | When you move an app or workflow to another stage | Places the release build of a revision in that stage. At Production, you also set the version number. |
| Release | When you make a library available to other assets | Sets a version and release notes on a library revision. A library reaches other stages inside its consumers. |
| Version | At Production deployment, or at library release | A semantic identifier (major.minor.patch) set on a revision, unique within the asset. |
| Merge | Before a publish | Reconciles local work with the latest published revision. Automatic when the changes are compatible, manual when you resolve conflicts. |

## Asset-specific behavior

Every asset type starts with a publish and a revision. After that, apps and workflows move across stages, and libraries reach other stages inside their consumers. The following table summarizes the differences.

| Asset type | Revision | Version | How it reaches other stages |
| --- | --- | --- | --- |
| Web or mobile app | One revision runs per stage. A new deployment replaces the previous one. | Set in the ODC Portal when you deploy to Production. | Release build promoted across stages. |
| Agentic app | Same as apps. | Same as apps. | Same release build promotion. Deploy agentic apps before dependent workflows. For more information, refer to [Deployment considerations for agentic apps](../../deploying-apps/deploy-apps.md#deploy-agentic). |
| Library | Increments on publish. The number is immutable. | Set in the ODC Portal when you release the library. A release also requires release notes. | Inside its consumers. ODC merges the library's package into the container of each asset that consumes it. |
| Workflow | Multiple revisions run per stage at once. Each instance finishes on the revision that created it. | Set in the ODC Portal when you deploy to Production. | Release build promoted across stages. Multiple revisions coexist on one stage, each with its own version. |

## Related pages

The following pages cover each concept in detail:

* [Revisions](revisions.md): how revisions are created at publish time, publish messages, and per-asset revision behavior.
* [Merge the work](../merge/intro.md): automatic and manual merging in ODC Studio, conflict resolution, and the compare-and-merge window.
* [Deploying assets](../../deploying-apps/deploy-apps.md): deploying across stages, assigning version numbers, impact analysis, and rollback.
* [Understanding 1-Click Publish](../../deploying-apps/one-cp.md): the compilation and build steps that run when you publish an app or library.
* [Libraries versioning](../libraries/libraries.md#libraries-versioning): the develop, release, and update-consumers lifecycle for library versions.
* [Messages in workflows publishing](../workflows/publish-workflows.md): adding publish messages in the workflow editor, revision history, and merge conflicts for workflows.

ODC Studio and the ODC Portal expose this lifecycle through their interfaces. CI/CD pipelines create revisions, start builds, and deploy them through the ODC public APIs. For more information about retrieving revisions and release builds programmatically, refer to [Selecting the revision and build of your asset](../../reference/apis/public-rest-apis/ci-cd-apis-use-cases/select-revision-build.md).

## Related resources

The following training courses cover the asset lifecycle:

* [Architecture Fundamentals in ODC](https://learn.outsystems.com/training/journeys/architecture-fundamentals-in-odc-2395): covers how publishing, revisions, and deployments fit into the ODC architecture.
* [Continuous Delivery in ODC](https://learn.outsystems.com/training/journeys/continuous-delivery-2396): covers the deployment pipeline from Development through Production.
