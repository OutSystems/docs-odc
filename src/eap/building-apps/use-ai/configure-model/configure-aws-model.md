---
summary: Explore how to integrate Amazon Bedrock foundation AI models with OutSystems Developer Cloud (ODC) for enhanced AI capabilities.
tags:
locale: en-us
guid: 6550169c-eb62-46d3-9181-68a71bed10f9
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Set up Amazon Bedrock foundation AI models

With [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), you can use foundation models (FMs) to build AI agents for your use case. You can also add your data source and customize the models using techniques such as Retrieval Augmented Generation (RAG). This article explains how to set up Amazon Bedrock FMs. 

It is intended for administrators and DevOps engineers with good working knowledge of setting up AI services in the AWS management console.

OutSystems only supports using Anthropic's **Claude** FMs with the AI Agent Builder app.  Specifically, we support the following Claude FMs:

* Claude Instant
* Claude v2
* Claude v2.1
* Claude 3 Sonnet
* Claude 3 Haiku

## Prerequisites

Before you set up Amazon Bedrock AI foundation models, ensure that you:

* Have an active AWS account subscription. If you don’t already have one, you can [sign up](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email) for an AWS account.

* Are an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) and have [sufficient permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-permissions) to request access to the model through the console.

* (Optional) Have the permissions to create users to use the Bedrock foundation models. If you do not have these permissions, you can request the AWS account administrator to create a user for you. 

## Set up model 

To set up the Amazon Bedrock foundation AI models, follow these steps:

### Step 1: Request access to the foundation models

1. Log into the AWS management console.

1. Access the Amazon Bedrock page. You can search for the page on the search bar or select the page from your favorite pinned resources. For more information, refer to [Set up Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/setting-up.html).

1. Request model access by following the steps at [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

1. Submit your use case details to access Anthropic and Claude FMs. Once you complete the use case details form, you can request access to the model. If your request is successful, you’ll be granted access to the model. For more information, refer to refer to [Add model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-add).

### Step 2:  Create a user and assign access permissions for using the model

1. [Create an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) to use the Amazon Bedrock foundation models.

    <div class="info" markdown="1">

    Once you've created a user, save the access key ID and the secret access key securely. The secret access key is available only at the time you create it. If you lose your secret access key, you must delete the access key and create a new user. However, you can retrieve the access key ID at any time. For more information, refer to the [Managing access key for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html). 

    </div>

    The access key ID and secret key are then used in the AI Agent Builder app to add the Amazon Bedrock AI model.

1. Create and assign policies to the user to provide necessary permissions to use the Bedrock AI model. At a minimum, the AI Agent Builder requires the following policy to work with Amazon Bedrock foundation models:

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "bedrock:InvokeModel",
                "Resource": "arn:aws:bedrock:*::foundation-model/*"
            }
        ]
    }
    ```

    For more information on configuring policies, refer to [Identity-based policy examples for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html).
   
## Next steps
 
* [Add Amazon Bedrock AI model in the AI Agent Builder app](add-aws-model-to-aibuilder.md)

* [Create an agent](../create-agent.md)

## Additional resources

**Amazon Bedrock**

* [What is Amazon Bedrock? - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids-arns.html)

* [Set up Amazon Bedrock - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/setting-up.html)

* [Amazon Bedrock endpoints and quotas - AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/bedrock.html)

**Configuring users**

* [User types](https://docs.aws.amazon.com/signin/latest/userguide/user-types-list.html)

* [IAM user](https://docs.aws.amazon.com/signin/latest/userguide/iam-user-type.html)

* [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html)

* [Resetting lost or forgotten access for IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys_retrieve.html)
