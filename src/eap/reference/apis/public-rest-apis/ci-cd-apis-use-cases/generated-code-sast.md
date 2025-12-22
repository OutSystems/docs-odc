---
guid: 9bb1a3bf-d025-407a-b8fd-5ff339494f9b
locale: en-us
summary: Learn how to use OutSystems APIs to programmatically retrieve the generated code of your assets for SAST analysis.
figma:
coverage-type:
  - apply
topic:
  - deployments-api-automation
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: sast analysis, code retrieval, outsystems apis, security testing, high-code generation
outsystems-tools:
  - odc studio
  - odc portal
helpids:
---
# Retrieving generated code for SAST analysis

When your asset goes through the build process, OutSystems translates its low-code model into high-code. Accessing the generated high-code enables you to run static application security testing (SAST), which may be required by your business needs. This article explains how to use OutSystems APIs to programmatically retrieve the generated code of your assets.

## Prerequisites

Before using the [APIs](../../build-v1.md) to retrieve your asset’s generated code, ensure that you have:

* [Generated an access token](../authentication/get-access-token.md) with this [permission](../authentication/create-api-client.md#edit-permissions-of-api-client):
    * Asset management \> Open  
* The [key of the build](select-revision-build.md#select) for which you want to obtain the generated code

## Retrieve your asset’s generated code

To get the generated code of your asset, follow these steps:

1. OutSystems must package the generated code for SAST analysis. To do this, use:  

    `POST api/builds/v1/build-operations/{operationKey}/generated-code`  

    Pass the key of the build in the `operationKey` parameter.  

1. After the code is packaged, retrieve the generated code:  

    `GET api/builds/v1/build-operations/{operationKey}/generated-code`

    Pass the key of the build in the `operationKey` parameter.

1. Download the zip file obtained in the previous step and extract its contents.

## Run the SAST analysis

You can perform SAST analysis by adding the generated code to a repository where SAST is already configured. Follow these steps:

1. Create a pull request on your repository with the generated code.  
1. Run the pipeline that performs the SAST analysis.  
1. [Review the results](https://success.outsystems.com/support/security/static_application_security_testing/#review-results) and decide whether you want to [deploy the asset](deploy-asset.md) or not.

## Next steps

* [Setting the release version and release notes](set-version-release-notes.md)
* [Deploying your asset to the target stage](deploy-asset.md)
