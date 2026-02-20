---
guid: 7edaa93d-b5a7-4aba-b126-10ddfcced471
locale: en-us
summary: Learn how CI/CD works in OutSystems Developer Cloud (ODC) and how to automate it with OutSystems APIs.
figma: 
coverage-type:
  - understand
topic:
  - deployments-api-automation
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - architects
  - tech leads
  - full stack developers
  - platform administrators
  - infrastructure managers
tags: ci/cd, continuous integration, continuous delivery, deployment automation, outsystems api, jenkins integration, azure devops
outsystems-tools:
  - odc studio
  - odc portal
helpids:
---
# CI/CD in ODC

CI/CD is an approach to building and delivering software with automation across the app lifecycle. It combines continuous integration (CI) and continuous delivery (CD). Continuous integration involves frequently testing, verifying, and integrating changes into app code. Continuous delivery means building assets that can be released to production at any time. Together, CI/CD shortens the time from development to production while reducing the risk of breaking changes.

In ODC, the CI/CD process moves assets from development to production by publishing, testing, deploying, and configuring. OutSystems automates build and deployment tasks when you publish and deploy. To deploy assets in the ODC Portal, refer to [Deploying assets](../../../../deploying-apps/deploy-apps.md). You can also automate these steps in your CI/CD tool using [OutSystems APIs](#automating-cicd-with-outsystems-apis).

## CI/CD stages in ODC

The CI/CD process moves assets through stages. ODC includes development and production stages by default, but you can add stages to suit your needs, such as QA. The following is a typical CI/CD flow:

* **Development** — Publish your asset. Run automated tests (for example, unit and component tests) before promoting your asset to the next stage.

* **QA** — Deploy a specific revision of the asset from development. Run automated tests (for example, integration and end-to-end tests) and apply quality gates, such as code quality analysis and static application security testing (SAST). If the revision is ready for production, assign a semantic version (for example, 1.2.0) for the production deployment.

* **Production** — Deploy your asset.

For more information about deploying and testing your apps across stages, refer to [Deploying assets](../../../../deploying-apps/deploy-apps.md) and [Testing apps](../../../../testing-apps/testing-apps.md).

## Automating CI/CD with OutSystems APIs

You can use OutSystems APIs to integrate with third-party CI/CD tools such as [Jenkins](https://www.jenkins.io/) or [Azure DevOps](https://azure.microsoft.com/en-us/products/devops). This allows you to automate CI/CD and manage the process from code to production, reducing the need to trigger each step in the ODC Portal.

By integrating OutSystems APIs with the automation tools you already use, you can improve your processes, enforce quality gates, and deliver reliable apps to your users faster.

The following table maps each CI/CD step to the related API or action.

| Step | Purpose | API or action |
| ---- | ------- | ------------- |
| Select revision and build | Identify the correct build to deploy | [Select the revision and build](select-revision-build.md) |
| Evaluate code quality | Apply quality gates before deployment | [Evaluate code quality](code-quality.md) |
| SAST analysis | Run static application security testing (SAST) on generated code | [Retrieve generated code for SAST analysis](generated-code-sast.md) |
| Set version and notes | Define semantic version for production | [Set the release version and release notes](set-version-release-notes.md) |
| Configure asset | Set stage-specific configurations | [Review asset configurations](asset-configurations.md) |
| Deploy | Deploy the asset to the target stage | [Deploy your asset to the target stage](deploy-asset.md) |
| Release library | Publish a library for reuse | [Release a library](release-library.md) |

## Related resources

The following resources provide more information about deploying, testing, and managing assets in ODC.

* [Deploying assets](../../../../deploying-apps/deploy-apps.md) — Manual deployment in the ODC Portal.
* [Rollback apps](../../../../deploying-apps/rollback.md) — Deploy an older revision or version.
* [Testing apps](../../../../testing-apps/testing-apps.md) — Automated testing strategies and tools.
* [Test automation in the delivery lifecycle](../../../../testing-apps/test-automation-in-delivery-lifecycle.md) — Integrate automated tests in the delivery lifecycle.
* [Configuration management](../../../../manage-platform-app-lifecycle/configuration-management.md) — Manage stage-specific configuration changes.
* [Continuous Delivery in ODC](https://learn.outsystems.com/training/journeys/continuous-delivery-2396) — Online training course.
