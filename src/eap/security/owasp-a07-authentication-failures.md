---
guid: bdf49dd6-69e9-4e1c-bd1b-9929706512d1
locale: en-us
summary: OWASP A07 in OutSystems Developer Cloud (ODC) covers password lockout, session fixation, token rotation, WAF protection, and IdP settings.
figma:
coverage-type:
  - understand
topic:
  - configure-session-timeout-odc
  - external-idp-system-limits
  - refresh-token-rotation
app_type: reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Authentication
  - End-user Authentication
  - External Authentication
  - IdP
  - OIDC
  - OWASP
  - Security
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# OWASP A07 authentication failures in ODC

Authentication failures let attackers sign in as other users or take over their sessions. Examples are weak passwords, unlimited sign-in attempts, and session identifiers that don't change at sign-in. The OWASP Top 10:2025 report keeps this category at rank #7, with a shorter name than in 2021.

This article covers A07 in OutSystems Developer Cloud (ODC). It lists the protection that applies by default, the settings you configure, and the authentication policies that remain yours. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Authentication protection that ODC applies by default {#covered-by-default}

The following protection applies to every app in cloud stages without any setup.

### Password policy {#password-policy}

Passwords must have at least 12 characters, including one numeric digit and one uppercase letter. Users who sign in through an external identity provider (IdP) manage their passwords in that IdP.

In a self-hosted tenant, end users of every stage, including Development, must sign in through an external OIDC IdP. The built-in IdP is available only for members who sign in to the ODC Portal and ODC Studio.

For more information, refer to [Passwords](../user-management/passwords.md).

### Lockout after failed attempts {#lockout}

ODC temporarily locks users out after five consecutive failed sign-in or password change attempts. The lockout starts at a few seconds. It grows with each failed attempt, up to about 5 minutes.

For more information, refer to [Lockout policy](../user-management/passwords.md#lockout-policy).

### Session fixation protection {#session-fixation}

In a session fixation attack, an attacker tries to hijack a valid user session. ODC changes the session identifier on each login and validates the identifier on every request.

For more information, refer to [Secure sessions](../manage-platform-app-lifecycle/platform-architecture/identity.md#secure-sessions).

### Refresh token rotation {#refresh-token-rotation}

Access tokens expire after five minutes, and ODC uses a refresh token to issue another one. Each refresh token works only once. If someone uses the same refresh token a second time, ODC invalidates the whole session.

When a user logs out, ODC invalidates the session and the refresh tokens. An access token issued shortly before logout stays valid until it expires, up to five minutes later.

For more information, refer to [Token lifecycle and logout](../manage-platform-app-lifecycle/platform-architecture/identity.md#token-lifecycle-and-logout).

### Web Application Firewall policies {#waf}

A Web Application Firewall (WAF) runs on the Content Delivery Network. The WAF protects the Platform and the Runtime from common web exploits and bots, including brute-force attacks. The WAF is an extra layer on top of the password and lockout policies.

In a self-hosted tenant, end-user traffic enters through your own ingress controller and load balancer.

For more information, refer to [Web Application Firewall](security.md#web-application-firewall).

## Authentication settings that you configure {#you-configure}

You configure the following settings for your stages and your identity providers.

### Session duration for each stage {#session-duration}

For each stage, you set the maximum session duration and the idle session duration. Both default to 12 hours, and the settings apply to all end-user apps in the stage. Member sessions in the ODC Portal and ODC Studio last 12 hours. You can't change that duration.

For more information, refer to [Session settings](../user-management/configure-user-session.md#session-settings).

### External identity provider {#external-idp}

ODC includes a built-in IdP. You can also use an external IdP for the Platform services and your apps. The external IdP applies multi-factor authentication (MFA) and a custom password policy. An external IdP also centralizes authentication across ODC and non-ODC apps. ODC supports IdPs that use the OpenID Connect (OIDC) or SAML 2.0 protocols.

In a self-hosted tenant, an external OIDC IdP is mandatory for end users. For the Test and Production stages, you register it as a public client without a client secret.

For more information, refer to [Configuring authentication with external identity providers](../manage-platform-app-lifecycle/external-idps/intro.md).

### Proof key for code exchange with OIDC providers {#pkce}

ODC supports proof key for code exchange (PKCE) with OIDC providers. PKCE adds a layer of security to the Authorization Code flow. ODC doesn't support the implicit and hybrid flows.

For more information, refer to [System considerations for OpenID Connect](../manage-platform-app-lifecycle/external-idps/intro.md#system-considerations-for-openid-connect).

## Authentication policies that remain your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, apply your organization's authentication policies through an external IdP.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about authentication and security in ODC, refer to the following articles:

* [Architecture of authentication and authorization mechanism](../manage-platform-app-lifecycle/platform-architecture/identity.md)
* [Security of OutSystems Developer Cloud](security.md)
* [OWASP A10 mishandling of exceptional conditions in ODC](owasp-a10-mishandling-exceptional-conditions.md)
