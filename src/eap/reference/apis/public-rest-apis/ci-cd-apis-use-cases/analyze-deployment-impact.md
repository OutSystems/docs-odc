---
guid: 1d6bb781-2b2e-45a6-896f-853c637167cd
locale: en-us
summary: OutSystems Developer Cloud (ODC) deployment impact analysis identifies dependent assets and blocking conflicts before CI/CD deployment.
figma:
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - dependency analysis
  - deployment gates
  - deployment impact
  - outsystems apis
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---
# Analyzing deployment impact

Before you deploy an asset to a stage, analyze which other assets depend on it and confirm that the assets it depends on are already deployed to the target stage. This helps you make informed decisions about testing, coordination, and potential risks. This article explains how to use OutSystems APIs to analyze deployment impact and use those findings to gate deployments in your CI/CD pipeline.

## Prerequisites

Before analyzing deployment impact, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) from an API client with this [permission](../authentication/create-api-client.md#edit-permissions-of-api-client):

    * **Release management** > **Deploy assets**

* The [key of the asset](select-revision-build.md#prerequisites) to be deployed.

* The [revision number](select-revision-build.md#select) you plan to deploy.

* The environment key of the target stage. For how to retrieve it, refer to the prerequisites in [Deploying your asset to the target stage](deploy-asset.md#prerequisites).

## Understand deployment impact

When you deploy a new revision of an asset, you introduce changes that affect other assets that depend on it. For example:

* Changing a library's public API breaks dependent apps.

* Modifying an entity structure affects apps that consume it.

* Updating connector configurations affects downstream integrations.

Analyzing deployment impact helps you identify these risks before deploying to production.

## Trigger a deployment impact analysis

To analyze what assets depend on your revision and whether your changes introduce breaking conflicts, follow these steps:

1. To start a deployment impact analysis, use:

    `POST /api/dependency-management/v1/deployment-analyses`

    In the body, pass the asset key, the revision you plan to deploy, and the environment key of the target stage:

    ```javascript
    {
    "assetKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11",
    "revision": 2,
    "environmentKey": "1ee11e11-1111-1111-e1ee-1e111e11eee1"
    }
    ```

    The response contains the analysis key, necessary to check the status.

1. To check the analysis status, use:

    `GET /api/dependency-management/v1/deployment-analyses/{analysisKey}`

    Poll this endpoint until the `processStatus` becomes **Finished** or **Failed**. Use a back-off strategy (for example, 5-10 seconds initially, then 15-30 seconds).

    Once `processStatus` is **Finished**, the response `report` contains the impact findings.

## Review deployment impact findings

Once the analysis is finished, review the report to understand the scope of impact.

### Check the report status

The report's `status` field indicates the severity:

* **NoIssuesFound**: No dependencies detected. Safe to deploy with minimal risk.

* **WarningsFound**: Dependent assets detected, but no blocking conflicts. Review the dependent assets and plan re-testing.

* **ErrorsFound**: Blocking conflicts detected. Resolve the conflicts before deployment.

### Check the impacted assets

The report's `impactedAssets` list contains the assets related to yours. The `referenceType` of each impacted asset shows whether it's a `Consumer` (depends on your asset) or a `Producer` (your asset depends on it). Each impacted asset lists its `applicationLevelIssues` and `elementLevelIssues`, and each issue has a `conflictSeverity`:

* **Error**: A breaking conflict. The dependent asset fails or behaves unexpectedly after you deploy. Resolve the conflict before deployment.

* **Warning**: A potential impact that requires review. Plan to re-test the dependent asset after deployment.

### Example impact report

The following example shows a report with an `ErrorsFound` status and one impacted consumer app:

```javascript
{
  "analysisKey": "c111c111-1cc1-1cc1-111c-c1111c1c1c11",
  "processStatus": "Finished",
  "report": {
    "status": "ErrorsFound",
    "impactedAssets": [
      {
        "assetKey": "d222d222-2dd2-2dd2-222d-d2222d2d2d22",
        "type": "App",
        "referenceType": "Consumer",
        "applicationLevelIssues": [
          {
            "conflictType": "MissingApplication",
            "conflictSeverity": "Error",
            "hint": "PublicAction renamed in library"
          }
        ]
      }
    ]
  }
}
```

## Apply deployment impact gates

Use the impact analysis results to decide whether to proceed with deployment.

### Suggested gate strategies

Choose a gate strategy based on the `status` of the report:

* **Block on errors**: If `status` is `ErrorsFound`, stop the deployment, fix the breaking changes, and redeploy.

* **Warn on warnings**: If `status` is `WarningsFound`, allow the deployment, and notify dependent teams to schedule re-testing.

* **Safe to deploy**: If `status` is `NoIssuesFound`, deploy without additional coordination.

### Coordinate dependent deployments

When errors are found, you have the following options:

1. **Fix the breaking change**: Update your asset to remain backward-compatible, then redeploy.

1. **Coordinate multi-asset deployment**: Deploy together with dependent assets in a planned rollout.

    * Deploy your asset.

    * Immediately redeploy dependent assets.

    * Test the integration end-to-end.

Document the approach in your deployment plan.

## Error handling

Implement error handling to make deployment impact analysis reliable.

### Analysis not available

If the endpoint returns an unexpected response, check the `processStatus` field:

* **InProgress**: Analysis is still running. Wait and poll again.

* **Failed**: Analysis didn't complete. Investigate the error and retry.

If the analysis fails repeatedly, contact support.

### API errors

If the API call fails and returns a 5xx status, implement retry logic with exponential backoff:

* First retry: wait 2 seconds.

* Second retry: wait 4 seconds.

* Third retry: wait 8 seconds.

* After 3 failed attempts, stop and report the error.

## Next steps

To continue with related tasks, refer to the following topics:

* [Retrieving generated code for SAST analysis](generated-code-sast.md): Run external security testing alongside dependency analysis

* [Setting the release version and release notes](set-version-release-notes.md)

* [Reviewing asset configurations](asset-configurations.md)

* [Deploying your asset to the target stage](deploy-asset.md)
