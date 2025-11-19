---
guid: 9a0ba2bd-1a95-4d42-bbd4-45ef5d722e21
locale: en-us
summary: Learn how to use OutSystems APIs to programmatically deploy an asset to a target stage.
figma: https://www.figma.com/design/eFzsh8ZIP5AIbRUyjeTV26/Reference?node-id=4763-2&t=3FZzy4xrcBSUETGl-1
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: apis, deployment automation, ci/cd, outsystems, environment keys
outsystems-tools:
  - odc portal
helpids:
---

# Deploying your asset to the target stage

This article explains how to use OutSystems APIs to programmatically deploy an asset to a target stage and monitor the deployment status to confirm the process is complete. This is useful for automating deployments while reducing manual intervention.

## Prerequisites

Before using the APIs to deploy your asset to a target stage, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) with these [permissions](../authentication/create-api-client.md#edit-permissions-of-api-client):
    * [Configuration management \> Edit configurations](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/asset_configurations_api/#patch-/environments/-environmentKey-/applications/-applicationKey-/configurations)
    * [Stage > View stage](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/deployments_api/#get-/deployment-operations)  
    * [Release management > Deploy apps](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/deployments_api/#post-/deployment-operations)
* The [key of the build](select-revision-build.md) to be deployed
* The environment key of the target stage

    <div class="info" markdown="1">

    To get the environment key, go to **Portal** > **Apps**, and select an asset. Select the stage to which you want to deploy. In the URL, copy the environment (stage) key after “stageid=”, as shown in this example:

    ![Screenshot of the ODC Portal showing how to retrieve the environment (stage) key from the asset URL](images/environment-key-pl.png "Get the environment key")

    You can also retrieve the environment key programmatically, using `GET /api/portfolios/v1/environments`.

    </div>

## Set the asset configurations to the target stage {#configurations}

If you need to set [configurations](asset-configurations.md) for this asset in the target stage, set them before proceeding with the deployment.

To set the asset configurations, use:

`PATCH /api/asset-configurations/v1/environments/{environmentKey}/applications/{applicationKey}/configurations`

Pass the configurations in the body. To check all types of configurations you can set, refer to the [Asset Configurations API](../../asset-config-v1.md) reference. To check the key of each configuration, [review the available configurations for the asset](asset-configurations.md).

For example, to ensure that a specific timer is inactive after deployment:

    {
    "key": null,
    "revisionBaseline": "2",
    "timers": 
      [
        {
        "configs": [
          {
          "value": "False",
          "key": "IsActive"
          }
        ],
        "key": "2kk222k2-2222-2222-22k2-2k2k2222kk22"
        }
      ]
    }

<div class="info" markdown="1">

The revisionBaseline is used by the OutSystems platform to validate whether the configuration key and value type exist in that revision context. It’s not used to ensure that the configuration is only applied when the revision reaches the target stage.

</div>

After calling this endpoint, the changed configurations will be pending. These configurations are applied automatically during the [deployment](#deploy).

<div class="info" markdown="1">

If you want to apply the configurations without waiting for the next deployment, and the asset is already deployed in the target environment, you can trigger an **Apply Configurations** operation:

`POST /api/deployments/v1/deployment-operations`

In the body, set the operation as ApplyConfigs.

</div>

## Deploy your asset to the target stage {#deploy}

To deploy your asset to a target stage in your CI/CD pipeline, follow these steps:

1. To trigger the execution of the deployment, use:  

    `POST /api/deployments/v1/deployment-operations`

    In the body, pass the operation you want to trigger. In this case, the operation is `Deploy`. Pass also the environment key, asset key, build key, and revision number. Example:  

        {
        "operation": "Deploy",  
        "assetKey": "a111a111-1aa1-1aa1-111a-a1111a1a1a11",  
        "buildKey": "b111b111-1bb1-1bb1-111b-b1111b1b1b11",  
        "revision": 1,  
        "environmentKey": "1ee11e11-1111-1111-e1ee-1e111e11eee1"  
        }
        
    If this API call is successful, the response should show the status as "Running". If this is not the case, check the [Deployments API reference](https://www.outsystems.com/tk/redirect?g=acf7cd06-3fe1-4bd3-85e8-06cd11aa0a7d) for more information on other statuses.

    The response also contains the operation key, necessary for the next step.  

    <div class="info" markdown="1">

    The deployment operation applies any pending configurations to the asset.

    </div>

1. To get the list of deployment operations and check if your deployment finished successfully, use:  

    `GET /deployments/v1/deployment-operations/{operationKey}`

    A successful deployment shows the status as “Finished”. For more information on other statuses, refer to the [Deployments API reference](https://www.outsystems.com/tk/redirect?g=acf7cd06-3fe1-4bd3-85e8-06cd11aa0a7d).  

    These are the recommended guidelines for monitoring the deployment status until it changes to "Finished" or "FinishedWithError":  

    * Poll the API to get the deployment status using a consistent wait time (for example, every 5 seconds).  
    * Define a period after which you increase the wait time to reduce unnecessary calls (for example, poll every 5 seconds during the first 30 seconds, then switch to every 30 seconds).  
