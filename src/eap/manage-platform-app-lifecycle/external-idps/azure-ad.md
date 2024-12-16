---
summary: Configure Microsoft Entra ID (formerly Azure AD) as an external identity provider in OutSystems Developer Cloud (ODC) using the ODC Portal.
tags: azure ad, identity management, openid connect, single sign-on, app registration
locale: en-us
guid: fb6adbb0-7343-4858-8a87-e3f7d8693900
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/KpEoUxciqaFLGLlZxo7Hiu/User-management?type=design&node-id=3405%3A152&mode=design&t=Oyyu3fjPlmIYwh5h-1
platform-version: odc
audience:
  - platform administrators
  - full stack developers
  - mobile developers
  - frontend developers
outsystems-tools:
  - odc portal
coverage-type:
  - apply
---

# Add Microsoft Entra ID for use as external identity provider

<div class="info" markdown="1">

**Microsoft Entra ID** was formerly known as **Microsoft Azure AD**.

</div>

ODC admins can configure Microsoft Entra ID as an external IdP by going to the ODC Portal and selecting the **Identity providers** tab.

To launch the **New provider** configuration screen, click the **Add Provider** > **OpenID Connect** button. Now follow these steps:

1. Enter a name for the new provider in the **Provider name** field. This can be any name less than 255 characters and can't include special characters.

1. Login to the [**Azure Portal**](https://portal.azure.com/) and create a new app registration in the Microsoft Entra ID screen. For guidance, see Microsoft documentation [here](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

1. Open the app registration you created and click the **Endpoints** button. Copy the URL from the **OpenID Connect metadata document** field and paste it into the **Discovery endpoint** field in ODC Portal.

    ![Azure Portal showing the OpenID Connect metadata document URL under the Endpoints section.](images/open-endpoints-az.png "Screenshot of Azure Portal showing the OpenID Connect metadata document URL")

   <div class="info" markdown="1">

    Some Microsoft Entra ID configurations issue custom signing keys for their tokens, which requires using an app-specific discovery endpoint. An example of such an endpoint is `https://login.microsoftonline.com/{tenant}/discovery/.well-known/openid-configuration?appid={appid}`, where `{appid}` corresponds to the **Application (client) ID**. You can get **Application (client) ID** in the following steps. If you face errors while authenticating with Microsoft Entra ID, using custom signing keys may be a solution. For more information, refer to [Validate the signature](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens#validate-the-signature) by Microsoft.

   </div>

1. Click **Get details** in ODC Portal. This retrieves the JSON of the Microsoft Entra ID OpenID configuration and shows a preview.

1. Copy the value of the **Application (client) ID** field from the main screen of the app registration in Azure Portal and paste it into the **Client ID** field in ODC Portal.

    ![Azure Portal with the Application (client) ID field highlighted in the app registration main screen.](images/copy-application-cliend-id-az.png "Screenshot of Azure Portal with the Application (client) ID field highlighted")

1. Click the **Certificates & secrets** tab from the main screen of the app registration in **Azure Portal**. Click **New client secret** button. Enter a description for the new secret in the **Description** field and then click **Add** to generate the secret.

    ![Azure Portal showing the New client secret button highlighted in the Certificates & secrets tab.](images/add-a-client-secret-az.png "Screenshot of Azure Portal with the New client secret button highlighted")

1. Copy the newly generated value from the **Value** field and paste it into the **Client secret (secret value)** field in ODC Portal.

    ![Azure Portal showing the newly generated client secret value in the Certificates & secrets tab.](images/paste-secret-value-az.png "Screenshot of Azure Portal showing the newly generated client secret value")

    <div class="info" markdown="1">

    ODC safely stores the configuration details in a secret manager.

    </div>

1. Copy the pair(s) of **Redirect URLs** to the list of permitted redirects in the setup part of your external provider. Copy the pair(s) for the built-in and active [custom domains](../custom-domains.md). If configuring [Okta](okta.md), you can follow the embedded link for specific guidance. Otherwise, see your provider's support documentation for further guidance. For example, [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#add-a-redirect-uri). Click **Next**.

1. Complete the configuration in ODC Portal by leaving the **PKCE** as the default value (**SHA-256**) and fields in **Claim Mapping** section as default values (**name**, **email**) and clicking **Save**.

1. To enable additional Claims, such as JWT Tokens via Claims Mapping Policy in Microsoft Entra ID, manually add the required property to the app manifest configuration on Microsoft Entra ID. For more information, see [Adding user optional and mapped claims in the Microsoft Entra ID authentication token](https://devblogs.microsoft.com/premier-developer/adding-user-optional-and-mapped-claims-in-the-azure-ad-authentication-token/).

ODC tests the configuration and on success adds Microsoft Entra ID to the list of available providers. If the test fails, a notification with the error displays.

Now follow the steps [here](intro.md#apply-an-external-idp) to apply for the newly added Microsoft Entra ID provider for use by your organization or apps.
