---
guid: 76297585-5efb-4b33-937d-e94a88ba6d8c
locale: en-us
summary: Learn how to use OutSystems APIs to review the configurations of your asset.
figma:
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: outsystems apis, asset configuration, deployment automation, configuration management, ci/cd
outsystems-tools:
  - odc portal
helpids:
---
# Reviewing asset configurations

This article explains how to use OutSystems APIs to check the current configurations of your asset and define the configurations you want to set in the target stage before deployment.

## Prerequisites

Before using the APIs to review asset configurations, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) with this [permission](../authentication/create-api-client.md#edit-permissions-of-api-client):
    * [Configuration management > View configurations](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/asset_configurations_api/#get-/environments/-environmentKey-/applications/-applicationKey-/revisions/deployed/configurations)
* The [key of the asset](select-revision-build.md#prerequisites) to be deployed
* The stage’s environment key for which you want to check the configurations

    <div class="info" markdown="1">

    To get the environment key, go to **Portal** > **Apps**, and select an asset. Select the stage to which you want to deploy. In the URL, copy the environment (stage) key after “stageid=”, as shown in this example:

    ![Screenshot of the ODC Portal showing how to retrieve the environment (stage) key from the asset URL](images/environment-key-pl.png "Get the environment key")

    You can also retrieve the environment key programmatically, using `GET /api/portfolios/v1/environments`.

    </div>

## Review asset configurations

Before proceeding with [deployment](deploy-asset.md), review the available configurations for your asset so that you can change them later in your CI/CD pipeline. Follow these steps:

1. Review the available configurations for your asset:

    `GET /api/asset-configurations/v1/environments/{environmentKey}/applications/{applicationKey}/revisions/deployed/configurations`

    Pass the environment’s key and the asset (app) key.

    The response includes the key of each configuration, which you’ll need when [changing the configurations](deploy-asset.md#configurations).

1. Prompt the user to define the configurations they want to set for that asset in the target stage.  
1. Store these defined configurations in your pipeline run context for use [before deployment](deploy-asset.md#deploy).

<div class="info" markdown="1">

The recommendation is to make the actual [configuration changes](deploy-asset.md#configurations) only right before deploying the asset. Otherwise, another parallel process might apply these pending configurations to the currently running version of the asset before your new revision is deployed.

</div>

## Next steps

* [Deploying your asset to the target stage](deploy-asset.md)
