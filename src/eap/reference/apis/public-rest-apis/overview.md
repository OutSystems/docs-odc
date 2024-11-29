---
summary: This article provides an overview of the OutSystems Developer Cloud (ODC) REST APIs.
tags: 
outsystems-tools: 
guid: be12dc22-fd28-4edb-af36-1edda72bddc3
locale: en-us
app_type: reactive web apps, mobile apps
content-type: 
    - conceptual
audience: 
platform-version: odc
figma: 
---

# ODC REST APIs

The OutSystems Developer Cloud (ODC) REST APIs allow you to create scripts, automation, and applications that leverage the resources of your ODC tenant, such as Users, Groups, App Roles, etc. You can use these APIs to automate and extend the built-in functionality provided with ODC.

The ODC REST APIs uses the [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) protocol for authorization and authentication, which is based on the [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) framework. For detailed information about the authentication process, refer to[Using OAuth 2.0 to access public REST APIs](authentication/using-oauth-access-api.md).

## API domains

### User and access management 

Enables you to programmatically manage user-related operations such as:

* Listing the current end-users of the apps to understand their status and modifying specific user information.

* Managing user access to specific resources or functionalities within the app. It includes granting or revoking access permissions, managing user groups, and defining access policies. 

### Portfolio management

Enables you to view a list of deployed assets in each stage.

## Further reading

* [Getting started](getting-started.md)

* [Using OAuth 2.0 to access public REST APIs](authentication/using-oauth-access-api.md)

* [User management API reference](../identity-v1.md)




