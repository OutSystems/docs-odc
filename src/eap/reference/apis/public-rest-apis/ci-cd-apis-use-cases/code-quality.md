---
guid: 81642257-b77d-44ad-b469-28a71efa7c8d
locale: en-us
summary: Learn how to use OutSystems APIs to programmatically retrieve the code quality analysis of an asset revision.
figma:
coverage-type:
  - apply
topic:
  - tech-debt-basics
  - deployments-api-automation
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: code quality analysis, outsystems apis, asset revision, ai mentor system, tech debt basics
outsystems-tools:
  - odc portal
helpids:
---
# Evaluating code quality

OutSystems provides built-in [code quality analysis](https://www.outsystems.com/tk/redirect?g=6be15662-74c5-4c35-9a7d-16a28816614c) powered by Mentor. This article explains how to use OutSystems APIs to programmatically retrieve the code quality analysis of an asset revision. This allows you to assess the quality of your asset based on your quality gates.

## Prerequisites

Before using [APIs](../../code-quality-api-v1.md) to retrieve the code quality analysis, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) from an API client with these [permissions](../authentication/create-api-client.md#edit-permissions-of-api-client):  
    * AI Mentor System > View Code Quality findings  
    * AI Mentor System > Manage Code Quality findings (if you need to trigger a new analysis)  
* The [key of the asset](select-revision-build.md#prerequisites) to be deployed
* The [revision number](select-revision-build.md#select) you want to release

## Get the code quality analysis summary for a revision {#get-analysis}

OutSystems periodically runs code quality analysis on your assets. To check if the code quality analysis of your asset revision has already run and retrieve the analysis summary, use:

`GET /api/code-quality/v1/assets/{assetKey}/revisions/{revision}/analysis-summary`

Pass the asset key and revision number.

If the analysis is available, the response contains the latest summary for that revision, including per-category findings and the overall quality score.

If the analysis isn’t available yet, the endpoint returns a `404 Not Found` response. In that case, you can [trigger the start of the code quality analysis](#start-analysis).

## Start a new code quality analysis {#start-analysis}

If the [analysis summary](#get-analysis) for your asset revision isn’t available yet, request the start of the code quality analysis. Follow these steps:

1. To start the analysis, use:

    `POST /api/code-quality/v1/code-analyses`

    In the body, pass the asset key and revision number. Example:

        {
        "assetKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11",
        "assetRevision": 2
        }

    The response contains the analysis key, necessary to check the status of the request.

1. To check the status of a running analysis, use:

    `GET /api/code-quality/v1/code-analyses/{analysisKey}`

    Poll this endpoint until the status becomes **Completed**, **Failed** or **Timeout**. Use a back-off strategy (for example, 5-10 seconds initially, then 15-30 seconds) and apply a reasonable overall timeout.

    If the status becomes **Failed** or **Timeout**, stop and surface the error in your pipeline. If the status is **Completed**, the response also contains a list of findings.

To review the code quality analysis of your asset, you can refer to this list of findings or, alternatively, [retrieve the analysis summary](#get-analysis).

## Apply your quality gates

Once you have the analysis results for your revision, you can apply your quality gates. For example, you might want to ensure that no asset with critical findings is allowed to pass to the next phase of the CI/CD pipeline:

* Pass if every category reports `criticalSeverity = 0`.  
* Fail otherwise.

You can also extend the policy to consider, for example, quality score, high-severity findings, or category-specific thresholds.

## Next steps

* [Retrieving generated code for SAST analysis](generated-code-sast.md)
* [Setting the release version and release notes](set-version-release-notes.md)
* [Reviewing asset configurations](asset-configurations.md)
* [Deploying your asset to the target stage](deploy-asset.md)
