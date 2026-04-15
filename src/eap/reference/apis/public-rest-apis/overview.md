---
summary: This article provides an overview of the OutSystems Developer Cloud (ODC) REST APIs.
tags: rest apis, authentication, user management, automation, oauth 2.0
outsystems-tools:
  - odc portal
guid: be12dc22-fd28-4edb-af36-1edda72bddc3
locale: en-us
app_type: reactive web apps, mobile apps
content-type:
  - conceptual
audience:
  - backend developers
  - full stack developers
platform-version: odc
figma:
---

# ODC REST APIs

The OutSystems Developer Cloud (ODC) REST APIs allow you to create scripts, automation, and applications that leverage the resources of your ODC tenant, such as Users, Groups, App Roles, etc. You can use these APIs to automate and extend the built-in functionality provided with ODC.

The ODC REST APIs uses the [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) protocol for authorization and authentication, which is based on the [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) framework. For detailed information about the authentication process, refer to [Using OAuth 2.0 to access public REST APIs](authentication/using-oauth-access-api.md).

## Usage

The ODC API is a RESTful interface with predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

## API domains

These are the OutSystems REST APIs that you can use to access and manage information related to your ODC assets.

### User and access management

The user and access management REST API enables you to programmatically manage user-related operations, such as:

* Listing the current end-users of the apps to understand their status and modifying specific user information.

* Managing user access to specific resources or functionalities within the app. It includes granting or revoking access permissions, managing user groups, and defining access policies.

For detailed information about the endpoints, refer to [User management API reference](../identity-v1.md).

### Portfolio management

The portfolio management REST API enables you to view a list of deployed assets in each environment.

For detailed information about the endpoints, refer to [Portfolio management API reference](../portfolio-v1.md).

### Build Operations

The Build Operations REST API enables you to programmatically manage build processes for your ODC assets. You can use this API to:

* Start build operations for your assets.

* Monitor the status and progress of ongoing builds.

For detailed information about the endpoints, refer to [Build Operations API reference](../build-v1.md).

### Deployments

The Deployments REST API enables you to automate the deployment lifecycle of your assets across different environments. You can use this API to:

* Deploy assets to specific environments (stages) in your organization.

* Monitor deployment progress and retrieve deployment status information.

For detailed information about the endpoints, refer to [Deployments API reference](../deployment-v1.md).

### Dependency Management

The Dependency Management REST API enables you to analyze and understand dependencies between assets before making changes. You can use this API to:

* Launch impact analysis to identify dependencies before deploying or deleting assets.

* Retrieve detailed dependency information to understand how changes affect other assets.

* Make informed decisions about asset lifecycle management based on dependency analysis results.

For detailed information about the endpoints, refer to [Dependency Management API reference](../dependency-v1.md).

### Asset Repository

The Asset Repository REST API enables you to access information about your ODC assets and manage their revisions.

For detailed information about the endpoints, refer to [Asset Repository API reference](../asset-v1.md).

### Asset Configurations

The Asset Configurations REST API enables you to manage configuration settings for your ODC environments and assets. You can use this API to:

* Retrieve and update global environment settings that affect all assets in an environment.

* Manage configuration settings for individual assets.

For detailed information about the endpoints, refer to [Asset Configurations API reference](../asset-config-v1.md).

### External library generation

The External Library Generation REST API enables you to generate and manage external libraries from high-code packages. You can use this API to:

* Generate and manage external libraries from .NET packages to integrate high-code functionality into your ODC apps.

* Retrieve information about your external libraries.

For detailed information about the endpoints, refer to [External Library Generation API reference](../external-library-generation-api-v1.md).

### Code quality

The Code quality REST API enables you to analyze and monitor the technical debt of your ODC assets. You can use this API to:

* Submit code analysis requests.

* Retrieve detailed findings about architecture, security, performance, and maintainability issues.

* Monitor quality scores and track trends over time to improve code standards.

For detailed information about the endpoints, refer to [Code quality API reference](../code-quality-api-v1.md).

## Terminology mapping between the ODC Portal and ODC APIs

A **stage** in ODC refers to the place where you deploy your apps, such as the Development stage and the Production stage. In ODC REST APIs, the **ODC stage** is represented as an **environment** resource.

An **end-user role** is a set of permissions assigned to users who interact with the ODC app. For detailed information about end-user roles, see [Secure your app with end-user roles](../../../user-management/secure-app-with-roles.md). In ODC REST APIs, an **end-user role** is represented as an **application role** resource.

## Related resources

* [Getting started](getting-started.md)

* [Using OAuth 2.0 to access public REST APIs](authentication/using-oauth-access-api.md)

* [User management API reference](../identity-v1.md)

* [Portfolio management API reference](../portfolio-v1.md)
