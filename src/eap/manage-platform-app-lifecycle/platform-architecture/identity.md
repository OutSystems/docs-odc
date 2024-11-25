---
summary: Explore the architecture of the Identity Service in OutSystems Developer Cloud (ODC), focusing on authentication and authorization mechanisms.
tags: identity service, authentication, authorization, openid connect, security policy
locale: en-us
guid: 5f50a67f-d8c9-444a-9615-090062255870
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/wMgr3GDiuAdkPics5gzXx9/Cloud-native-architecture-of-OutSystems-Developer-Cloud?type=design&node-id=3001%3A1809&t=wS2nDUn4cr9EORu8-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - architects
  - platform administrators
outsystems-tools:
  - odc studio
  - odc portal
content-type:
  - conceptual
---

# Architecture of authentication and authorization mechanism

This article provides an overview of the architecture of the Identity Service of OutSystems Developer Cloud (ODC).

The Identity Service is the built-in identity provider (IdP) of the Platform and the Runtime. The IdP verifies that each HTTPS request comes from an authenticated and authorized user for the Platform services and your apps.

You can also use an external, self-managed OpenID Connect (OIDC) IdP as the authentication provider for the Platform services and your apps. There are several benefits of this approach. You can use a:

* Centralized authentication method (ODC and non-ODC) across your organization.
* Custom password policy for the Platform services and your apps that aligns with your organization's security policy.
* Multi-factor authentication (MFA) process for the Platform services and your apps.

## Authentication and authorization

**Authentication** is the process of verifying a user's identity. Once authenticated, **authorization** is the process of verifying what a user can access.

Your organization's developers, DevOps engineers and architects are granted **organization permissions** to use ODC Studio and ODC Portal to access the Platform services.

Users of your apps are granted **app permissions** to access secured screens, data and logic flows. Developers create app roles in ODC Studio and assign them to users in ODC Portal. 

Go to [User management](../../user-management/intro.md) for more information on user permissions and roles.

## Secure endpoints

The Platform uses microservices based on REST API. When ODC Studio and ODC Portal send **HTTPS requests**, the requests reach the **secure endpoints** the Platform exposes. An example of a request is when a developer clicks the 1-Click Publish button in ODC Studio. The request accesses a secure endpoint in Build Service.

Apps run in containers in the Runtime and expose secure REST API endpoints. For example, when a user submits a form in an app it's sent as a HTTPS request to the corresponding endpoint.

## Token technology

The Identity Service uses JSON Web Token (JWT) technology, an open standard the Identity Service uses to define identity information as a JSON object. The key benefits of this technology include: 

* JWTs are cryptographically signed using a public/private key pair which safeguards them from being modified by an attacker and ensures their authenticity.
* JWTs are self-contained, meaning they're quick to validate as they don't require a server database lookup. This means quick access to the Platform services and apps.

The Identity Service follows the OIDC standard: an identity layer on top of the OAuth 2 protocol.

### Secure sessions

ODC includes built-in protection against session fixation attacks, where an attacker tries to hijack a valid user session. ODC ensures that the session identifier is transparently changed on each login and validates this on every request, preventing session fixation attacks.

ODC also serializes and deserializes session data using a built-in anti-tampering JSON deserialization mechanism. 

## User flow

The following diagram shows an example of a user authentication and authorization flow. It shows what happens when a developer using **ODC Studio** (client) accesses a REST API endpoint exposed by **Service 1** (a Platform service).

![Diagram illustrating the user authentication and authorization flow in OutSystems Developer Cloud, including token validation and permission checks.](images/identity-flow-authorization-diag.png "User Authentication and Authorization Flow Diagram")

The Identity Service or external IdP checks the following conditions to **validate access token**:

1. User information is valid.
1. Client information is valid.
1. Token hasn't expired.
1. Current time is after the token's valid from time.
1. Issue time of the token is in the past.
1. Cryptographic signature is valid.

If any of the conditions (1)-(6) fail, the Identity Service or external IdP rejects the HTTPS request and revokes the ID and access tokens. Users must authenticate again by logging in to the client.

If the token validation is successful, the edge of the service checks the user's permission. If the permission check fails, the service rejects the HTTPS request and returns an error to the client.

The **ID** token contains information about the identity of the authenticated user, such as name and email. The **access** token contains information about the user's permissions. Transfer of JWTs between the client and service is over the OAuth 2 protocol.

When a user logs out, the tokens are invalidated. The tokens have a maximum lifespan of 12 hours. When the tokens expire, the user has to re-authenticate.

In the diagram, a user working in ODC Portal to access a REST API endpoint in a second Platform service is a valid example. Another valid example is a user working in a browser to access a REST API endpoint on a protected screen in an app.
