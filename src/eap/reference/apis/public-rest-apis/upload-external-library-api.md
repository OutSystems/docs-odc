---
guid: 94c22edf-3a6c-4bb9-9c3c-c9146af7227d
locale: en-us
summary: Learn how to use OutSystems APIs to programmatically upload an external library for your ODC assets to consume.
figma:
coverage-type:
  - apply
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
tags: external library upload, outsystems apis, odc assets, high-code libraries, programming external libraries
outsystems-tools:
  - odc portal
helpids:
---
# Upload an external library using OutSystems APIs

OutSystems lets you [extend your ODC apps with external logic](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_custom_code/) using high-code libraries. This article explains how to use OutSystems APIs to programmatically upload a high-code library for your ODC assets to consume. You can upload a new library or a new version of an existing library.

## Prerequisites

Before using APIs to upload your external logic library, ensure that you have:

* [Generated an access token](authentication/get-access-token.md) from an API client with these [permissions](authentication/create-api-client.md#edit-permissions-of-api-client):  
    * Asset management > Create (if you’re uploading a new library)  
    * Asset management > Change (if you’re uploading a new version of an existing library)  
* A .zip file with your external library. To learn how to create this file, refer to [Extend your apps with custom code](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_custom_code/#build-the-external-logic).

## Upload your external library

To upload an external library, follow these steps:

1. To obtain a URL to which you can upload your library, use:  

    `GET  /api/external-libraries/v1/uploads`

    The response contains the `uploadURL` and the `downloadURL`, which are necessary for the next steps.

1. Upload the external library .zip file to the `uploadURL`. To do this, make a call to the [Amazon S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html). Use:  

    `PUT {uploadURL}`  

   In the body, pass the .zip file.  

1. To finish the upload of the external library to your ODC portfolio, OutSystems needs the `downloadURL`, from which it will download your external library code. Use:  

    `POST /api/external-libraries/v1/generation-operations/`

    In the body, pass the external library file name and the `highCodeBinaryUri`, which is the `downloadURL` obtained previously :

        {
        "fileName": "string",
        "highCodeBinaryUri": "string"
        }

    A successful response contains the operation key.

1. To check the operation status, use:

    `GET /api/external-libraries/v1/generation-operations/{operationKey}`

    The response contains the `libraryKey`, which you can use as the `assetKey` when [releasing the library](ci-cd-apis-use-cases/release-library.md) using OutSystems APIs.

For more information on these or other endpoints, refer to the [External Libraries API reference](../external-library-generation-api-v1.md).

## Next steps

* [Releasing a library using OutSystems APIs](ci-cd-apis-use-cases/release-library.md)
