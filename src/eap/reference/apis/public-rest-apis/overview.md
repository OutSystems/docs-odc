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

## Usage

The ODC API is a RESTful interface with predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

All API endpoints are relative to the following base URL.

`https://ODC_PORTAL_DOMAIN/api`

Where 

`ODC_PORTAL_DOMAIN` is the domain of your Organization

## API domains

### User and access management 

The user and access management REST APIs, enable you to programmatically manage user-related operations such as:

* Listing the current end-users of the apps to understand their status and modifying specific user information.

* Managing user access to specific resources or functionalities within the app. It includes granting or revoking access permissions, managing user groups, and defining access policies. 

For detailed information about the endpoints, refer to [User management API reference](../identity-v1.md).

### Portfolio management

The portfolio management REST APIs, enable you to view a list of deployed assets in each environment.

For detailed information about the different endpoints, refer to [Portfolio management API reference](../portfolio-v1.md).

## Terminology mapping between ODC portal and ODC APIs

A **stage** in ODC refers to the place where you deploy your apps, such as the Development stage and the Production stage. In ODC REST APIs, the **ODC stage** is represented as an **environment** resource.

An **end-user role** is a set of permissions assigned to users who interact with the ODC app. For detailed information about end-user roles, see [Secure your app with end-user roles](../../../user-management/secure-app-with-roles.md). In ODC REST APIs, an **end-user role** is represented as an **application role** resource. 

## Related resources

* [Getting started](getting-started.md)

* [Using OAuth 2.0 to access public REST APIs](authentication/using-oauth-access-api.md)

* [User management API reference](../identity-v1.md)




