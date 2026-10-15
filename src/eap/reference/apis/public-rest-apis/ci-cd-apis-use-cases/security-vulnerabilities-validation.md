---
guid: 5b273560-85a5-4ec1-b01d-82a253f0679e
locale: en-us
summary: OutSystems Developer Cloud (ODC) security vulnerability validation uses the Code Quality API to retrieve findings and block unsafe deployments.
figma:
coverage-type:
  - apply
topic:
  - security-vulnerabilities-validation
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - CI/CD
  - Deploy
  - Security
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---
# Validating security vulnerabilities

OutSystems provides code analysis for security vulnerabilities as part of its code quality evaluation. This article explains how to use OutSystems APIs to programmatically retrieve security vulnerabilities in your asset and validate them before deployment. This allows you to enforce security standards and block deployments that contain critical security issues.

The analysis runs in a batch every 12 hours, not when you publish a revision. A pipeline usually reaches the deploy step before the analysis runs, so your pipeline typically follows these steps:

1. Retrieve the analysis summary for your revision.

1. If the revision hasn't been analyzed yet, trigger an analysis and poll until it finishes.

1. Apply your security gate.

## Prerequisites

Before using the [Code Quality API](../../code-quality-api-v1.md) to retrieve and validate security vulnerabilities, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) from an API client with these [permissions](../authentication/create-api-client.md#edit-permissions-of-api-client):

    * View code quality findings

    * Manage code quality findings (if you need to trigger a new analysis)

* The [key of the asset](select-revision-build.md#prerequisites) to be deployed

* The [revision number](select-revision-build.md#select) you want to validate

## Retrieve security vulnerability findings

Use the analysis summary to check how many security findings exist per severity level, and use the findings list to review each one individually.

### Check the security severity counts

To get the number of security findings per severity level for a revision, use:

`GET /api/code-quality/v1/assets/{assetKey}/revisions/{revision}/analysis-summary`

Pass the asset key and revision number. The response's `summary.categories.security` field contains the count of findings at each severity level: `lowSeverity`, `mediumSeverity`, `highSeverity`, and `criticalSeverity`.

The counts exclude findings with the `Dismissed` status, but include findings with the `Snoozed` status. For example, dismissing a false positive unblocks a gate on `criticalSeverity = 0`, but snoozing it doesn't.

If the revision hasn't been analyzed yet, the endpoint returns a `404 Not Found` response. In that case, [trigger a new analysis](#start-analysis).

### Start a new security analysis {#start-analysis}

If the analysis summary for your asset revision isn't available yet, request the start of the code quality analysis. In a pipeline, this is the usual path.

1. To start the analysis, use:

    `POST /api/code-quality/v1/code-analyses`

    In the body, pass the asset key and revision number:

        {
        "assetKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11",
        "assetRevision": 2
        }

    The response contains the analysis key, necessary to check the status of the request.

1. To check the status of a running analysis, use:

    `GET /api/code-quality/v1/code-analyses/{analysisKey}`

    Poll this endpoint until the status becomes **Completed**, **Failed**, or **Timeout**. Use a back-off strategy (for example, 5-10 seconds initially, then 15-30 seconds) and apply a reasonable overall timeout.

    If the status becomes **Failed** or **Timeout**, stop and surface the error in your pipeline. If the status is **Completed**, the response includes a list of findings.

### List the individual security findings

The security category covers findings such as injection vulnerabilities, authentication and authorization issues, data exposure risks, and insecure cryptographic operations. To list each finding individually, use:

`GET /api/code-quality/v1/findings?AssetKeys={assetKey}&Categories=security&IsLatest=true&Since={startDate}`

Set `Since` to the start date of the findings you want to return. If you omit it, the endpoint returns only findings from the last 14 days. The `IsLatest=true` parameter returns only findings from the most recent analysis. Use `Status` to filter by status, such as `Status=Open,Snoozed`, and use `Limit` and `Offset` to page through the results.

Each finding includes a `severity`, a `status`, the affected `elementName` and `elementPath`, and a `patternId` that identifies the rule it violates. To retrieve a description of what the rule checks for and how to fix it, use:

`GET /api/code-quality/v1/patterns/{patternId}`

The response includes the pattern's `description`, `impact`, and `howToSolve` fields.

## Understand security severity levels

OutSystems reports security findings at two severity levels:

* **Critical**: Directly exploitable vulnerabilities with broad scope that are low effort to exploit (for example, remote code execution, authentication bypass, or data leak).

* **High**: Confirmed vulnerabilities with limited scope or that are hard to trigger (for example, cross-site scripting in an admin-only screen).

## Apply security vulnerability gates

Once you have the security vulnerability findings for your revision, apply your security gates to decide whether to proceed with deployment. For example, you might want to ensure that no asset with critical security vulnerabilities is allowed to pass to the next phase of the CI/CD pipeline.

Common security gate strategies include:

* **Block on critical vulnerabilities**: Pass only if `criticalSeverity = 0`. Fail otherwise.

* **Block on critical and high vulnerabilities**: Pass only if `criticalSeverity = 0` and `highSeverity = 0`. Fail otherwise.

* **Threshold-based gates**: Define acceptable severity thresholds per category. For example, allow up to 3 high-severity findings but no critical findings.

* **Risk-based gates**: Combine severity levels with finding type. For example, block any `ClientSideGetUserId` finding, which has High severity, but allow other High findings. To query this pattern, use `GET /api/code-quality/v1/findings?AssetKeys={assetKey}&PatternIds=ClientSideGetUserId&IsLatest=true`.

### Example security gate logic

The following example shows a security gate that blocks deployment if critical vulnerabilities exist. Retrieve the analysis summary, extract the security category, and evaluate the thresholds.

To retrieve the analysis summary, use:

`GET /api/code-quality/v1/assets/{assetKey}/revisions/{revision}/analysis-summary`

Response example, abbreviated:

    {
    "assetKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11",
    "assetRevision": 2,
    "qualityScore": 82,
    "summary": {
      "categories": {
        "security": {
          "lowSeverity": 0,
          "mediumSeverity": 0,
          "highSeverity": 2,
          "criticalSeverity": 0
        },
        "architecture": {
          "lowSeverity": 8,
          "mediumSeverity": 3,
          "highSeverity": 1,
          "criticalSeverity": 0
        }
      }
    }
    }

To apply the gate:

1. Extract `summary.categories.security` from the response.
1. Check the severity thresholds.
    * If `criticalSeverity` is greater than `0`, block the deployment.

    * If `highSeverity` is greater than `3`, block the deployment.

    * Otherwise, allow the deployment to proceed.

Adjust the thresholds (`criticalSeverity`, `highSeverity`) to match your organization's security policy.

## Review detailed security findings

For more detail about each security vulnerability, including its code location, combine two endpoints:

* `GET /api/code-quality/v1/findings?AssetKeys={assetKey}&Categories=security&IsLatest=true&Since={startDate}` lists the individual findings with their `elementName`, `elementPath`, `severity`, and `status`.

* `GET /api/code-quality/v1/patterns/{patternId}` retrieves the `description`, `impact`, and `howToSolve` guidance for the rule each finding violates.

Use this information to:

* Generate detailed security reports for stakeholders.

* Prioritize remediation efforts.

* Provide developers with specific guidance for fixing vulnerabilities.

## Error handling and retries

Implement robust error handling to make your security validation reliable in production pipelines.

### Analysis not available yet

If the endpoint returns `404 Not Found` when retrieving the analysis summary, the analysis hasn't started or hasn't finished yet. Use the following strategy:

1. Call the analysis summary endpoint.

1. If the response is `404 Not Found`, trigger a new analysis with `POST /api/code-quality/v1/code-analyses`.

1. Poll the analysis status with `GET /api/code-quality/v1/code-analyses/{analysisKey}` until it completes.

1. Retrieve the analysis summary again.

Use a back-off strategy when polling: start with 5-10 second intervals, then increase to 15-30 seconds to reduce API load.

### Timeout strategy

The service marks an analysis as **Timeout** after it has been pending for 10 minutes. Set your pipeline timeout above 10 minutes so that your pipeline receives the **Timeout** status instead of stopping first.

If the status becomes **Timeout**, stop the pipeline and report the error.

### Reporting gate failures

When security validation fails (critical or high-severity findings exceed your thresholds), communicate the failure clearly:

1. **Log the findings**: Include the severity counts and affected areas, for example, "Deployment blocked: 2 critical security vulnerabilities found" or "Deployment blocked: 5 high-severity findings (limit: 3)."

1. **Provide actionable details**: Include the type of each vulnerability, such as SQL injection, weak authentication, or unencrypted data transmission.

1. **Report to your CI/CD tool**: Send the failure details back to your pipeline so it stops further steps, notifies the team, and lets the security team review the findings.

1. **Create a ticket for remediation**: Optionally, create a ticket in your issue tracker with the detailed findings so developers can prioritize fixes.

### API errors

If the API call fails (returns 5xx status), implement retry logic with exponential backoff:

* First retry: wait 2 seconds.

* Second retry: wait 4 seconds.

* Third retry: wait 8 seconds.

* After 3 failed attempts, stop the pipeline and report the error.

If API errors persist, check the OutSystems status page and contact support.

## Next steps

* [Setting the release version and release notes](set-version-release-notes.md)

* [Reviewing asset configurations](asset-configurations.md)

* [Deploying your asset to the target stage](deploy-asset.md)

* [Retrieving generated code for SAST analysis](generated-code-sast.md) for additional external security testing
