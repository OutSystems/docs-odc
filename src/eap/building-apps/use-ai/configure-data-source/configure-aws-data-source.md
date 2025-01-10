---
summary: OutSystems Developer Cloud (ODC) is not mentioned in the provided article about setting up Amazon Kendra with Amazon S3 as a data source.
tags: cloud services, aws, amazon s3, search services, amazon kendra
locale: en-us
guid: c0920667-ced6-4aeb-b4fa-a096244c406f
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - platform administrators
outsystems-tools:
  - none
coverage-type:
  - apply
---

# Set up Amazon Kendra with a data source

[Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) is an intelligent search service that uses natural language processing and advanced machine learning algorithms to return specific answers to search questions from your data. With Amazon Kendra, you can connect to various data sources such as file systems, websites, Box, DropBox, Salesforce, SharePoint, relational databases, and Amazon S3. 

This article explains how to set up Amazon Kendra search service using Amazon S3 as a data source. It is intended for administrators and DevOps engineers with good working knowledge of configuring search services using Amazon Kendra.

## Prerequisites

Before setting up the Amazon Kendra with a data source, ensure you have:

* An active AWS account subscription. If you don't already have one, you can [sign up](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email) for an AWS account 

* An active user in the AWS account.

* Necessary permissions to:

    * Create indexes in Amazon Kendra. For more information, refer to [IAM roles for indexes](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-index)

    * Create S3 bucket and upload documents, For more information, refer to [IAM access roles for data sources](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-ds).

    * Create policies to assign them to the user. For more information, refer to  [Understanding access level summaries within policy summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.html).

## Set up data source

To set up the Amazon Kendra with a data source, follow these steps:

1. [Create](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html) an index in Amazon Kendra. Once the index is created, copy the Index ID for use in the AI Agent Builder app.

1. [Create](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) an Amazon S3 bucket.

1. [Upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) data to your bucket.
4. Add the Amazon S3 data source to your index and sync the data. 

    For more information, refer to [Amazon S3](https://docs.aws.amazon.com/kendra/latest/dg/data-source-s3.html).

1. Create and assign a policy to the user to access Amazon Kendra. 
For more information, refer to [Amazon Kendra Identity-based policy examples](https://docs.aws.amazon.com/kendra/latest/dg/security_iam_id-based-policy-examples.html).
    
**Note:** You can either create a policy to provide full access to Amazon Kendra resources or create a policy with minimum required access to Kendra.

## Next Steps

* [Add Amazon Kendra data source AI Agent Builder app](add-aws-data-source-to-aibuilder.md)

* [Create an agent](../create-agent.md)

## Related resources

[Getting started with the Amazon Kendra console](https://docs.aws.amazon.com/kendra/latest/dg/gs-console.html)
