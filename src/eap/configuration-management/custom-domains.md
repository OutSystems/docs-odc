---
summary: This article explains how to configure custom domains for apps in OutSystems Developer Cloud.
tags: 
locale: en-us
guid: da18534d-84c8-4a52-bca8-85ebb3b1e082
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Configure custom domains for apps

For each stage in which you deploy apps, OutSystems Developer Cloud (ODC) comes with a **built-in** OutSystems domain for end-user access. The table below shows built-in domains if you have three stages.


| Stage       | Built-in domain                      |
| ----------- | ------------------------------------ |
| Development | `<customername>-dev.outsystems.app`  |
| Test        | `<customername>-test.outsystems.app` |
| Production  | `<customername>.outsystems.app`      |

Apps are always accessible to end-users through built-in domains. For example, an app named MyApp deployed to the Development stage is accessible at `<customername>-dev.outsystems.app/MyApp`. If you want to restrict access, you can use [end-user roles](../building-apps/secure-app-with-roles.md).

In addition, ODC lets you make your apps accessible to end-users through your organization's domain(s). In a given stage, your apps can be available through one or more custom domains that you add to that stage. Each custom domain must be unique to a customer and stage.

You can add top-level domains (such as `example.com`), subdomains (such as `dev.example.com`), and multi-level subdomains (such as `odc.dev.example.com`). When you add a custom domain to a stage, all apps deployed to that stage are accessible through the domain.

The following table shows a possible setup for a customer who has three stages and wants one custom subdomain for each stage:

| Stage       | Custom domain    |
| ----------- | ---------------- |
| Development | dev.example.com  |
| Test        | test.example.com |
| Production  | www.example.com  |

## Add a custom domain

To add a custom domain, from the ODC Portal, select **Configurations** > **Domains** and then follow these steps.

1. From the Stage dropdown menu, select the stage for which you want to add a domain.
1. From the top-right, click the **Add domain** button to display the **Add a domain** popup box.
1. Enter the domain you want to add, then click **Add**. The **Set up your domain** screen displays with the **Pending validation** status next to the domain name.
1. Now, you must **Validate ownership of the domain** and **Point the domain to your apps**. You do this by adding the two provided CNAME records, two name-value pairs, to the DNS records of your domain registrar (the company that manages the reservation of your domain name). To add a **CNAME** record, follow the steps in the [box below](#add-CNAME-box).
1. ODC uses AWS Certificate Manager (ACM) to issue certificates. If your domain has Certification Authority Authorization (CAA) enabled, you must add a DNS record to specify that ACM is allowed to issue a certificate for your domain. The process of adding a DNS record is detailed in the [ACM documentation](https://docs.aws.amazon.com/acm/latest/userguide/setup-caa.html).

<div class="warning" markdown="1">

You must complete these steps within **72 hours** or the CNAME records expire and you must restart the process.

</div>

<div class="info" markdown="1">

For each external identity provider in use by your apps, a new pair of redirect URLs is generated for this domain. You must add the new pair of redirect URLs to each active external provider to ensure end-users maintain the ability to authenticate. See the [external IdP documentation](../configuration-management/external-idps/intro.md#apply-an-external-idp) for guidance on how to do this. If end-users lose their ability to authenticate, they get 401 errors when trying to access the apps. You can diagnose the problem by looking at the [logs](../../eap/monitor-apps.md#logs).

</div>

Once ODC detects the provided CNAME records in the domain's DNS records, ownership is validated and traffic is routed from the domain to your apps. This may take up to 20 minutes, before which the domain may not be ready to use and an error displays if visiting an app through it. Once ownership is validated, the status of the domain changes to **Active** and it's ready to use.

ODC generates a public X.509 certificate to enable TLS communication over the domain. The generated certificate is valid for 395 days. If the provided CNAME records remain in the domain's DNS records, ODC automatically renews the certificate before expiry.

---

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

1. Click the dropdown menu and select the stage for which you want to add a domain. The list of domains displays showing the built-in domain and any custom domains already added to the selected stage.
1. Click the card of the custom domain you want to delete. The **Set up your domain** screen displays and you see the status next to the domain name.
1. Click the **ellipsis** (3-dots) to the right of the domain status and select **Delete domain**.
1. Before confirming the deletion of the domain, review the information in the popup box. Then do one of the following:
     * To confirm, click the **Delete domain** button.
     * To cancel, click **Cancel** and exit.

<div class="info" markdown="1">

You can now delete the CNAME records you added for the domain from the DNS records of your domain registrar. To delete records, see your domain registrar's support documentation for instruction. The certificate ODC issued for the domain won't automatically renew and so will expire when you delete the records.

</div>

## Developing apps with custom domains

When an app uses a background process to generate the URL of a screen, the built-in domain is used. You override the build-in domain by building an expression of the URL with the custom domain, for example in the case of a [link widget in an email](../building-apps/emails/widgets.md#widgets-available-in-emails). To help you build multiple expressions you can create an app setting, for example **App_Domain**, containing the domain.
