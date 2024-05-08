---
summary: OutSystems Developer Cloud (ODC) supports custom domain configuration for app stages, with automatic SSL certificate issuance and domain validation.
tags: 
locale: en-us
guid: da18534d-84c8-4a52-bca8-85ebb3b1e082
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/AOyPMm22N6JFaAYeejDoge/Configuration-management?type=design&node-id=3675%3A159&mode=design&t=GIMRhVcd5jweHOdq-1
---

# Configure custom domains for apps

For each stage in which you deploy apps, ODC comes with a **built-in** OutSystems domain for end-user access. The table below shows built-in domains if you have three stages.


| Stage       | Built-in domain                      |
| ----------- | ------------------------------------ |
| Development | `<customername>-dev.outsystems.app`  |
| Test        | `<customername>-test.outsystems.app` |
| Production  | `<customername>.outsystems.app`      |

It's not possible to change the built-in OutSystems domain that is defined when the ODC infrastructure is created. Apps are always accessible to end-users through built-in domains. For example, an app named MyApp deployed to the Development stage is accessible at `<customername>-dev.outsystems.app/MyApp`. If you want to restrict access, you can use [end-user roles](../user-management/secure-app-with-roles.md).

In addition, ODC lets you make your apps accessible to end-users through your organization's domain(s). In a given stage, your apps can be available through one or more custom domains that you add to that stage. Each custom domain must be unique to a customer and stage.

When you add a custom domain to a stage, all apps deployed to that stage are accessible through the domain. The following table shows a possible setup for a customer who has three stages and wants one custom subdomain for each stage:

| Stage       | Custom domain    |
| ----------- | ---------------- |
| Development | dev.example.com  |
| Test        | test.example.com |
| Production  | www.example.com  |

<div class="info" markdown="1">

ODC automatically issues X.509 certificates after verifying the domain ownership. You don't need to purchase SSL certificates for Custom Domains in ODC.

</div>

## Add a custom domain

Some domain registrars may not allow creating CNAME records when existing DNS records exist for the same name. This typically applies to root domains (such as `example.com`) and subdomains(such as `dev.example.com`) that already have other records. 

You need to use a custom domain without linked DNS records if your domain registrar has restricted CNAME creation.

To add a custom domain, from the ODC Portal, select **Configurations** > **Domains** and then follow these steps.

1. From the Stage dropdown menu, select the stage for which you want to add a domain.
1. From the top-right, click the **Add domain** button to display the **Add a domain** popup box.
1. Enter the domain you want to add, then click **Add**. The **Set up your domain** screen displays with the **Pending validation** status next to the domain name.
1. Now, you must **Validate ownership of the domain** and **Point the domain to your apps**. You do this by adding the two provided CNAME records, two name-value pairs, to the DNS records of your domain registrar (the company that manages the reservation of your domain name). To add a **CNAME** record, follow the steps in the [box below](#add-CNAME-box).
1. ODC uses AWS Certificate Manager (ACM) to issue certificates. If your domain has Certification Authority Authorization (CAA) enabled, you must add a DNS record to specify that ACM is allowed to issue a certificate for your domain. The process of adding a DNS record is detailed in the [ACM documentation](https://docs.aws.amazon.com/acm/latest/userguide/setup-caa.html).

**Note**: To set a custom domain as the default domain, refer to [Default domain](#default-domain).

<div class="warning" markdown="1">

You must complete these steps within **72 hours** or the CNAME records expire and you must restart the process.

</div>

<div class="info" markdown="1">

For each external identity provider in use by your apps, a new pair of redirect URLs is generated for this domain. You must add the new pair of redirect URLs to each active external provider to ensure end-users maintain the ability to authenticate. See the [external IdP documentation](../manage-platform-app-lifecycle/external-idps/intro.md#apply-an-external-idp) for guidance on how to do this. If end-users lose their ability to authenticate, they get 401 errors when trying to access the apps. You can diagnose the problem by looking at the [logs](../monitor-and-troubleshoot/monitor-apps.md#logs).

</div>

Once ODC detects the provided CNAME records in the domain's DNS records, ownership is validated and traffic is routed from the domain to your apps. This may take up to 20 minutes, before which the domain may not be ready to use and an error displays if visiting an app through it. Once ownership is validated, the status of the domain changes to **Active** and it's ready to use.

ODC generates a public X.509 certificate to enable TLS communication over the domain. The generated certificate is valid for 395 days. If the provided CNAME records remain in the domain's DNS records, ODC automatically renews the certificate before expiry.

---

## Default domain

You can set your custom domain as the default domain. This means that:

* Apps running on a stage are accessed from ODC Portal and ODC Studio using the default domain instead of the built-in one
* Debugging in the development stage connects to the app using the default domain configured in development
* You can use the [GetDefaultDomain](../reference/built-in-functions/url.md) system action to build URLs within your apps, explicitly using the default domain
* Emails that are sent from your OutSystems app that contain links to specific screens use the default domain instead of the built-in one

To set a custom domain as the default domain, follow the [Add a custom domain](#add-a-custom-domain) steps. Once the domain is active, click the ellipsis menu, and select **Set as default**.

![Set domain as default](images/set-default-domain-odcs.png "Set domain as default")

<div class="info" markdown="1">

* When a tenant is first created, the **built-in domains are always set as default**.
* You can set any domain as default only if it is **active**.
* You can only set **one custom domain as the default** domain per stage.
* You **cannot delete a default domain**. You'll must set another domain as default first before deleting the current one.

</div>

### Add a CNAME record to your domain's DNS records  { #add-CNAME-box }

<div class="info" markdown="1">

There may be a dedicated person or team at your organization responsible for administering the organization's domains. If so, you may want to contact them for help with the process.

</div>

To add the CNAME record to your domain registrar, complete the following steps. For more specific instructions, see your domain registrar's support documentation.

1. Go to your domain's DNS records.
1. Add a record to your DNS settings. Select CNAME as the record type.
1. In the ODC Portal screen, copy the contents of the Name field. Paste the content into the Name field of the DNS record.
1. In the ODC Portal screen, copy the contents of the Value field. Paste the content into the Value field of the DNS record.
1. For the Time To Live (TTL) either set it to 1 hour or leave the default setting.
1. Save the record.

---

## Delete a custom domain

To delete a custom domain, from the ODC Portal, navigate to **Configurations** > **Domains** and then follow these steps.

1. Click the dropdown menu and select the stage for which you want to add a domain. The list of domains displays the built-in domain and any custom domains already added to the selected stage.
1. Click the card of the custom domain you want to delete. The **Set up your domain** screen displays and you see the status next to the domain name.
1. Click the **ellipsis** (3-dots) to the right of the domain status and select **Delete domain**.
1. Before confirming the deletion of the domain, review the information in the popup box. Then do one of the following:
     * To confirm, click the **Delete domain** button.
     * To cancel, click **Cancel** and exit.

<div class="info" markdown="1">

The certificate ODC issued for the domain will automatically renew if the CNAME Record that was added remains in the DNS records for your domain registrar. You can remove the DNS entry if you do not want the certificate to auto-renew. To delete records, see your domain registrar's support documentation for instructions.

</div>

## Developing apps with custom domains

When an app uses a background process to generate the URL of a screen, the built-in domain is used. You override the built-in domain by building an expression of the URL with the custom domain, for example in the case of a [link widget in an email](../building-apps/sending-emails/widgets.md#widgets-available-in-emails). To help you build multiple expressions you can create an app setting, for example **App_Domain**, containing the domain.
