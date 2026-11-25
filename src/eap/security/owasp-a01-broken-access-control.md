---
guid: 5a150d9f-ca4a-4a0c-af96-cdc94808ac41
locale: en-us
summary: OWASP A01 in OutSystems Developer Cloud (ODC) explains access token validation, roles, IP filters, and your duty to define a role model.
figma:
coverage-type:
  - understand
topic:
  - check-role-actions-odc
  - ip-filter-groups
  - token-lifecycle
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Authentication
  - Authorization
  - IP Filters
  - OWASP
  - Roles
  - Screens
  - Security
outsystems-tools:
  - none
helpids:
isautopublish: true
---

# OWASP A01 broken access control in ODC

Broken Access Control happens when users can act outside their intended permissions. Examples include opening a screen that you meant to restrict, reading another user's data, and calling server logic without a role check. The OWASP Top 10:2025 report keeps this category at rank #1.

This article covers A01 in OutSystems Developer Cloud (ODC). It lists the protections that apply by default, the ones you configure, and the work that remains yours. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Access protections that ODC applies by default {#covered-by-default}

The following protection applies to every ODC app in cloud stages without any action from you.

### Access token validation {#access-token-validation}

ODC validates the access token of every request before the request reaches the target service. The validation checks the following conditions:

1. The access token hasn't expired.
1. The access token is active, which means its start time has passed.
1. The access token was issued in the past.
1. The cryptographic signature of the access token is authentic and valid.

If any condition fails, ODC rejects the request before it reaches the service.

This validation checks the identity and integrity of the token. It isn't a permission check. After the validation succeeds, the service checks the permissions of the user.

For more information, refer to [Architecture of authentication and authorization mechanism](../manage-platform-app-lifecycle/platform-architecture/identity.md).

## Access controls that you configure or apply {#you-configure}

ODC provides the following mechanisms. The protection depends on you adding and configuring them.

### End-user roles {#end-user-roles}

You create end-user roles in ODC Studio and assign them to users. You then use the roles to control access in your app in the following ways:

* **Screens**: Allow only users with a certain role to open a screen.
* **Server-side logic**: Check the role of the user with the `Check<ROLENAME>Role()` function before the logic runs.
* **Data**: Use the same function in an expression, for example in an aggregate filter, so that the aggregate returns data only to users with the role.

Verify roles in server-side logic, because client-side checks depend on a client that a user can manipulate. Permissions are a separate step that runs on the roles that you define.

For more information, refer to [Secure your app with end-user roles](../user-management/secure-app-with-roles.md).

### Code Quality findings for insecure access patterns {#code-quality}

The **Code quality** dashboard in the ODC Portal reports security findings in your apps. The following findings relate to access control:

* A screen that any user can access, including anonymous users.
* Insecure use of the `GetUserId` function in client logic, where a user can change the identity that the client passes to the server.

For more information, refer to [Working with Code quality](../monitor-and-troubleshoot/manage-technical-debt/working-with-code-quality.md), [Avoid setting screens as accessible by everyone](../monitor-and-troubleshoot/manage-technical-debt/security/avoid-setting-screens-accessible-everyone.md), and [Insecure usage of GetUserId function on client context](../monitor-and-troubleshoot/manage-technical-debt/security/insecure-usage-of-getuserid-on-client-context.md).

### IP filters {#ip-filters}

IP filters restrict network access to your apps. You create IP filter groups and rules in the ODC Portal to define which IP addresses can reach the apps in a stage. IP filters require a Sentry for ODC subscription.

IP filters are available only for stages in the OutSystems Cloud. For self-hosted stages, you apply equivalent network controls in your own infrastructure.

For more information, refer to [Manage IP filters](../manage-platform-app-lifecycle/filter-ip.md) and [Sentry for ODC](sentry.md).

## Access control work that remains your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build and the access and permissions of their users. For this category, define a role model that matches your business rules.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about how OutSystems secures ODC, refer to the following articles:

* [Security of OutSystems Developer Cloud](security.md)
* [OWASP A02 security misconfiguration in ODC](owasp-a02-security-misconfiguration.md)
