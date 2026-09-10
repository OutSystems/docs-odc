---
summary: How to address production incidents in OutSystems Developer Cloud using code hotfixes when faster alternatives cannot resolve the issue.
tags:
  - CI/CD
  - Deploy
  - Development lifecycle
  - Troubleshooting
guid: ac332d54-4413-4abb-9a0a-a1ad0e9e70a8
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - understand
  - apply
  - unblock
content-type:
  - procedure
  - best practice
audience:
  - Developer
  - Tech lead
  - Platform administrator
outsystems-tools:
  - odc studio
  - odc portal
isautopublish: true
---

# Production code hotfixes in ODC

When a production incident occurs, your goal is to restore service quickly. This article covers code hotfixes, a targeted approach for emergencies when faster alternatives cannot resolve the issue. Before attempting a hotfix, evaluate simpler options such as disabling features, updating configuration settings, rolling back, or promoting a fix through your normal pipeline.

## ODC deployment architecture

Code in ODC is built and compiled once on the development stage. All downstream stages (test, pre-production, production) host the compiled build and run the same application code. This architecture means publishing code directly to a downstream stage is not possible. Code always originates in development and moves through the pipeline to other stages.

Code in ODC is built and compiled once, and two container images are generated, a development one and a production one. The development stage hosts the development container image. All downstream stages (test, pre-production, production) host the production image generated from the same application code. This architecture ensures that any code change goes through the pipeline and is tested before reaching the production stage. This is the normal process for all in-order code changes, but a code hotfix is an out-of-order code change, one that requires a break-glass solution.

## Incident responses

Before pursuing a code hotfix, evaluate which approach best fits your situation. The following options are listed in order of preference, from fastest and safest to slowest and most complex.

### Assess the impact

Determine whether the incident requires immediate action. If the issue permits waiting for your next planned release cycle, use your standard deployment process. Reserve emergency procedures for incidents that are actively impacting your users. A code hotfix is always a riskier approach and will always impact the development team’s activities.

### Disable the problematic feature

If the issue comes from a recent feature or code change, the quickest recovery path is to disable that feature. This option requires a feature toggle to control behavior at runtime without redeploying. Introducing feature toggles must be considered up front and embedded in the team’s development practices.

### Roll back to a previous version

Rolling back to the last stable app version often restores service faster than writing and testing a fix. Evaluate whether redeploying the previous asset version is an acceptable option and whether it eliminates the errors. This is especially valuable when you can identify the exact deployment that introduced the problem, and this is often the fastest way to recover the system.

### Promote a fix from development

To fix the issue in code, implement the fix in your current development version and promote it through your deployment pipeline. This approach works when:

* You have in-progress work behind feature toggles that do not affect production.

* You can verify that the new build does not introduce regressions.

This is the preferred approach because it uses your normal deployment controls and maintains the integrity of your pipeline.

## Code hotfixes in production

If none of the incident response options resolve your incident, you can perform a targeted code hotfix. This procedure modifies the exact revision running in production, then merges the fix back to development to prevent it from being lost.

### How hotfixes work

A hotfix lets you make targeted fixes to a production revision. The key difference from normal deployments is that you work backward from production, then merge the fix forward to development.

After you deploy the fix to production, you must assess if you need to merge it back to development. This is the critical step. Without this validation, the hotfix can be lost when you deploy a newer revision to production, and the previous errors will reappear.

### How to apply a hotfix

To apply a hotfix, you work from the production revision backward to development, then merge the fix forward to ensure future deployments include the correction.

Follow these steps:

1. Pause all deployments and development work, and prevent any other changes from entering the pipeline while the hotfix is in progress.

1. In ODC Studio, open the exact revision currently running in production (not the latest development revision). You can do this by opening the asset and choosing **View revisions** from the **App** menu.

1. Make the necessary code changes.

1. Publish the fix to development.

1. Take the fix through the pipeline to the production stage, ensuring it is properly tested and that no regressions are introduced.

1. Apply the same fix to the previous development revision, so it is included in future deployments. To do this, open the asset if needed, and choose **Compare and merge with another revision or file** from the **App** menu. You can use commit messages to identify each revision with the hotfix code and the latest developments.

1. If applicable, consider pushing this revision to non-production environments so others can resume their work.

### Hotfix automation

The OutSystems REST APIs provide operations to automate hotfix steps, such as publishing to development, promoting to specific stages, and redeploying versions. Automation reduces manual steps and lowers the risk of missing a stage or step. Refer to [CI/CD automation](../reference/apis/public-rest-apis/ci-cd-apis-use-cases/intro.md) for the available REST APIs and usage details.

## Related resources

The following resources provide more information about deploying, managing, and troubleshooting apps in ODC.

* [Deploying assets](deploy-apps.md): Deploy apps to stages in your pipeline.

* [Rollback apps](rollback.md): Revert to a previous app version when issues occur.

* [Testing apps](../testing-apps/testing-apps.md): Verify app quality and behavior across stages.

* [Configuration management](../manage-platform-app-lifecycle/configuration-management.md): Manage stage-specific app configurations.
