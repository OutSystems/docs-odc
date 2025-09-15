---
summary: Configure SAML 2.0 identity providers in OutSystems Developer Cloud (ODC) for enterprise authentication and single sign-on.
locale: en-us
guid: b5f8692d-68bf-41a1-89ec-5e8fc7069e31
app_type: mobile apps,reactive web apps
platform-version: odc
tags: saml configuration,identity providers,single sign-on,authentication
audience:
  - platform administrators
  - full stack developers
  - mobile developers
  - frontend developers
figma:
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
topic:
  - external-idps
  - idp-saml
helpids: 30672, 30673
---

# Configure SAML 2.0 identity providers

This article provides step-by-step instructions for configuring SAML 2.0 identity providers in OutSystems Developer Cloud (ODC).

## Prerequisites

You must have the **Manage authentication** permissions.

## Configure SAML 2.0 provider

You can configure a SAML 2.0 provider by navigating to the **ODC Portal** > **Manage** > **Identity providers**.

To launch the **New provider** configuration screen, click the **Add Provider** dropdown and select **SAML 2.0**. Then follow these steps:

### Step 1: Enter a provider name

1. Enter a name for the new provider in the **Provider name** field.

    This can be any name less than 255 characters and can't include special characters.

1. Click **Next**.

### Step 2: Select a scope

1. Select the scope you want to assign the provider to. 

    * **Organization**

      When assigned to the **Organization**, the provider can authenticate ODC Portal and ODC Studio users.

    * **Apps in (stage name)**

      When assigned to the apps in the stage, the provider can authenticate users in the selected stage.

    <div class="info" markdown="1">
    
    You cannot change the scope once the provider is configured. 
    
    </div>

1. Click **Next**.

### Step 3: Retrieve SP metadata

1. Retrieve the service provider metadata for the assigned scope:

    * Identifier
    * X509 certificates
    * Redirect URLs 

    You can retrieve this information using an XML file or manually.

1. Enter this metadata in your identity provider's configuration page. 

1. Click **Next**.

### Step 4: Configure provider

1. Retrieve and import the **identity provider metadata**.

    * Identity provider entity ID
    * Single sign-on service URL
    * Single logout service URL
    * X509 certificates

    You can import this data using an XML file or URL, or enter it manually.

1. Click **Get metadata**.

1. Enter the **claim mapping** details.

    * Username
    * Email
    * Name/Given name
    * Surname
    * Photo URL
    * Verified email

    <div class="info" markdown="1">

    There is a 255-character limit for the claim mapping details.
    
    </div>

1. (Optional) Click **Show advanced options** to configure additional SAML settings:

    **Signature key name**: Signed SAML documents sent using POST binding contain the identification of the signing key in the **KeyName** element. You can choose from the following:
    
    * **Cert_Subject**: Uses the subject from the certificate corresponding to the scope key
    * **Key_ID**: Uses the certificate Key ID
    * **None**: Omits the key name hint from the SAML message
    
    **Additional options**
    
    <div class="info" markdown="1">
    
    Changing any of these settings will modify the ``sp_metadata.xml`` file.
    
    </div>
    
    * HTTP-POST binding for Logout
    * HTTP-POST binding for AuthnRequests
    * Want assertions signed
    * NameID policy format

1. In the **Organization user email verification** section, choose one of the following options for handling email verification:

    * **User verification**: Choose this option to always verify users' emails using ODC's email verification flow, even if they’ve already been verified by the identity provider.

    * **Trust identity provider**: Choose this option if your identity provider includes email verification information in its attributes and you want to trust that verification status. If you choose this option, you must map the identity provider's email verification claim in the **Verified email** field. If no valid email verification claim is returned, users are considered to have an unverified email.

    * **Trust all user emails as verified:** Choose this option to automatically trust all email addresses from a provider, regardless of whether they are verified or not.

1. Click **Next**.

### Step 5: Review and add provider

1. Review the details and click **Add provider**.

ODC adds the provider to the list of available providers.

## Next steps

* [Assign the provider](intro.md#assign-an-external-idp) 
* [Implement the authentication logic](apps.md)

## Related resources

* [Configure OpenID Connect identity providers](configure-openid-connect.md)
* [Configure social providers with accelerators](configure-social-accelerators.md)
* [Microsoft Entra ID configuration](azure-ad.md)
* [Okta configuration](okta.md)
