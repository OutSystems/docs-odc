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

# Add a SAML 2.0 identity provider

This article provides step-by-step instructions for adding SAML 2.0 identity providers in OutSystems Developer Cloud (ODC).

## Prerequisites

Before you begin, make sure you have:

* A setup that meets ODC's [System considerations](intro.md#system-considerations) for external IdPs (for example, ODC only supports SP-initiated flows and recommends signed responses).
* The [**Manage authentication**](../../user-management/roles.md#permissions-registry) permission.

From your provider, have the following ready:

* SAML metadata URL or metadata XML file.
* Provider configuration details (Entity ID, SSO URL, certificates).

## Add a SAML 2.0 provider

To add a SAML 2.0 provider in the ODC Portal:

1. Go to **Manage** > **Identity providers**.
1. Open the **Add provider** menu and choose **SAML 2.0**.

After selecting **SAML 2.0**, complete these steps:

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

    You can't change the scope once the provider is configured.

    </div>

1. Click **Next**.

### Step 3: Retrieve SP metadata

1. Retrieve the service provider metadata for the assigned scope:

    * Identifier
    * X509 certificates
    * Redirect URLs

    You can retrieve this information from the ODC Portal using an XML file or manually.

1. Enter this metadata in your identity provider's configuration page.

1. Click **Next**.

### Step 4: Configure provider

1. From your provider, retrieve the **identity provider metadata** and import it into the ODC Portal.

    * Identity provider entity ID
    * Single sign-on service URL
    * Single logout service URL
    * X509 certificates

    You can import this data using an XML file or URL, or enter it manually.

1. Click **Get metadata**.

1. Enter the **claim mapping** details.

    <div class="info" markdown="1">

    Attribute names are case-sensitive. Ensure that the attribute names you enter match exactly as provided by the identity provider.

    </div>

    * Username
    * Email
    * Name/Given name
    * Surname
    * Photo URL
    * Verified email

    <div class="info" markdown="1">

    There is a 255-character limit for the claim mapping details.

    </div>

    <div class="info" markdown="1">

    For more details about mapping claims when configuring an IdP, refer to [Understand the user creation and claim mapping logic](identity-claims-email-verification.md#claim-mapping-logic).

    </div>

1. (Optional) Click **Show advanced options** to configure additional SAML settings:

    **Signature key name**: Signed SAML documents sent using POST binding contain the identification of the signing key in the **KeyName** element. You can choose from the following:

    * **Cert_Subject**: Uses the subject from the certificate corresponding to the scope key.
    * **Key_ID**: Uses the certificate Key ID.
    * **None**: Omits the key name hint from the SAML message.  

    **Additional options**

    <div class="info" markdown="1">

    Changing any of these settings will modify the ``sp_metadata.xml`` file.

    </div>

    * HTTP-POST binding for Logout
    * HTTP-POST binding for AuthnRequests
    * Want assertions signed
    * NameID policy format

1. In the **Organization user email verification** section, choose one of the options for handling email verification. For more information about email verification methods, refer to [Email verification logic](identity-claims-email-verification.md#email-verification-logic).

1. Click **Next**.

### Step 5: Review and add provider

1. Review the details and click **Add provider**.

ODC adds the provider to the list of available providers.

## Next step

* [Assign an IdP](assign-idp.md)

## Related resources

* [Add an OpenID Connect identity provider](configure-openid-connect.md)
* [Add a social identity provider with accelerators](configure-social-accelerators.md)
* [Add Microsoft Entra ID for use as external identity provider](azure-ad.md)
* [Add Okta for use as an external identity provider](okta.md)
