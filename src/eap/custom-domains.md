---
summary: Information about custom domains and how to add and delete them for your apps.
tags: 
locale: en-us
guid: da18534d-84c8-4a52-bca8-85ebb3b1e082
app_type: mobile apps, reactive web apps
---

# Custom domains for apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

For each stage in which you deploy apps, Project Neo comes with a **built-in** OutSystems domain for end-user access.


| Stage       | Built-in domain                      |
| ----------- | ------------------------------------ |
| Development | `<customername>-dev.outsystems.app`  |
| Test        | `<customername>-test.outsystems.app` |
| Production  | `<customername>.outsystems.app`      |

Apps are always accessible to end-users through built-in domains. For example, an app named MyApp deployed to the Development stage is accessible at `<customername>-dev.outsystems.app/MyApp`. If you want to restrict access, you can use [end-user roles](building-apps/secure-app-with-roles.md).

In addition, Project Neo lets you make your apps accessible to end-users through your organization's domain(s). Your apps in a given stage can be available through one or more custom domains you add to that stage. Each custom domain must be unique to a customer and stage.

You can add top-level domains (such as `example.com`), subdomains (such as `dev.example.com`), and multi-level subdomains (such as `neo.dev.example.com`). When you add a custom domain to a stage, all apps deployed to that stage will be accessible through the domain.    

The following table shows a possible setup for a customer who wants one custom subdomain for each stage:

| Stage       | Custom domain    |
| ----------- | ---------------- |
| Development | dev.example.com  |
| Test        | test.example.com |
| Production  | www.example.com  |

## Add a custom domain

To add a custom domain, navigate to the **Domains** tab in the Project Neo Portal. Then follow these steps.

1. Click the dropdown menu and select the stage for which you want to add a domain.
1. Click the **Add domain** button. In the popup box that displays, enter the domain you want to add click **Add**. The **Set up your domain** screen displays with the **Pending validation** status next to the domain name.
1. You must now **Validate ownership of the domain** and **Point the domain to your apps**. You do this by adding the two provided CNAME records, two name-value pairs, to the DNS records of your domain registrar. To add a CNAME record, follow the steps in the [box below](#add-CNAME-box).

<div class="warning" markdown="1">

You must complete these steps within 72 hours else the CNAME records expire and you must restart the process.

</div>

<div class="info" markdown="1">

For each external identity provider in use by your apps, a new pair of redirect URLs is generated for this domain. You must add the new pair of redirect URLs to each active external provider to ensure end-users maintain the ability to authenticate. See the [external IdP documentation](./external-idps.md#apply-an-external-idp) for guidance on how to do this. If end-users lose their ability to authenticate, they get 401 errors when trying to access the apps. You can diagnose the problem by looking at the [logs](../eap/monitor-apps.md#logs).

</div>

Once Project Neo detects the provided CNAME records in the domain's DNS records, ownership is validated and traffic routed from the domain to your apps. This may take up to 20 minutes, before which the domain may not be ready to use and an error displayed if visiting an app through it. Once ownership is validated, the status of the domain changes to **Active** and it's ready to use.

Project Neo generates a public X.509 certificate to enable TLS communication over the domain. The generated certificate is valid for 395 days. If the provided CNAME records remain in the domain's DNS records, Project Neo automatically renews the certificate before expiry.

---

### Add a CNAME record to your domain's DNS records  { #add-CNAME-box }

<div class="info" markdown="1">

There may be a dedicated person or team at your organization responsible for administering the organization's domains. If so, you may want to contact them for help with the process.

</div>

To add the CNAME record to your domain registrar, complete the following steps. See your domain registrar's support documentation for more specific instructions.

1. Go to your domain's DNS records.
1. Add a record to your DNS settings. Select CNAME as the record type.
1. In the Portal screen, copy the contents of the Name field. Paste the content into the Name field of the DNS record.
1. In the Portal screen, copy the contents of the Value field. Paste the content into the Value field of the DNS record.
1. For the Time To Live (TTL) setting, set as 1 hour or leave as default.
1. Save the record.

---

## Delete a custom domain

To delete a custom domain, navigate to the **Domains** tab in the Project Neo Portal. Then follow these steps.

1. Click the dropdown menu and select the stage for which you want to add a domain. The list of domains displays showing the built-in domain and any custom domains already added to the selected stage.
1. Click the card of the custom domain you want to delete. The **Set up your domain** screen launches and you see the status next to the domain name.
1. Click the ellipsis to the right of the domain status and select **Delete domain**.
1. Before confirming the deletion of the domain, review the information in the popup box. Then do one of the following:
     * Click the **Delete domain** button to confirm.
     * Click the **Cancel** button to exit.

<div class="info" markdown="1">

You can now delete the CNAME records you added for the domain from the DNS records of your domain registrar. See your domain registrar's support documentation for instructions on how to delete a record. Once you delete the records, the certificate Project Neo issued for the domain won't automatically renew and will expire.

</div>
