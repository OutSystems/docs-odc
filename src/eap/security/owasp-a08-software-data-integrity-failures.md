---
guid: fd29f95d-8550-4540-938e-2175e40d2c57
locale: en-us
summary: OWASP A08 in OutSystems Developer Cloud (ODC) explains token signing, image integrity, CSP, AppShield, and your verification duties.
figma:
coverage-type:
  - understand
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Front-end developer
  - Platform administrator
  - Tech lead
tags:
  - Data Integrity
  - Deploy
  - Mobile app
  - Native App
  - OWASP
  - Security
  - Web
outsystems-tools:
  - none
helpids:
isautopublish: true
---

<!--
DRAFT for TK-24661. ODC copy. The O11 copy is created at the end of the plan.
Resolve and delete these notes before publishing.

* Non-blocking, not claimed (TK-24108 Q5): how ODC protects serialized data. The only
  source is a 2024 ChatODC answer and the ODC training lesson, with no product
  doc behind it.
* Non-blocking: the CSP section is sourced from the CSP articles only.
* Non-blocking: no doc describes access token signing or the CSP for
  self-hosted stages. The info box scopes the page to cloud stages.
* The OWASP 2025 name is "Software or Data Integrity Failures". The ticket and
  the 2021-based training lesson use "and".
-->

# OWASP A08 software or data integrity failures in ODC

Software or Data Integrity Failures happen when an app trusts code or data that an attacker can change without detection. Examples include tampered tokens, updates without an integrity check, and a build that changes between test and production. The OWASP Top 10:2025 report keeps this category at rank #8.

This article covers A08 in OutSystems Developer Cloud (ODC). It lists the protections that apply by default, the ones you configure, and the checks that remain yours.

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Integrity protections that ODC applies by default {#covered-by-default}

The following protections apply to every ODC app in cloud stages without any action from you.

### Signed access tokens {#signed-access-tokens}

The ODC Identity Service issues access tokens as JSON Web Tokens (JWTs). Each token carries a cryptographic signature from a public and private key pair. The signature protects the token from modification and shows where the token comes from.

Before a request reaches its target service, ODC validates the access token. One check confirms that the signature is authentic and valid.

For more information, refer to [Architecture of authentication and authorization mechanism](../manage-platform-app-lifecycle/platform-architecture/identity.md).

### The same app container image in every stage {#same-app-image}

When you publish an app, ODC builds a container image and stores it in a container registry. When you deploy the app from Development to other stages, ODC reuses that image. The app in Production is the same build that you tested earlier.

In a self-hosted tenant with a custom container registry, you provision and maintain that registry, including its credentials and retention policies.

For more information, refer to [Containers](security.md#containers).

### Container images verified at each pipeline stage {#platform-services-images}

Before a code change in a Platform service reaches production, it goes through a deployment pipeline. At each stage, admission control verifies that nobody modified the container image. The image released to production is identical to the one built.

For more information, refer to [Software supply chain integrity](security.md#supply-chain-integrity).

## Integrity mechanisms that you configure or apply {#you-configure}

ODC provides the following mechanisms. The protection depends on you adding and configuring them.

### Content security policy for web apps {#csp}

A content security policy (CSP) limits the sources that a browser can load scripts and other content from. For this category, a CSP restricts your web app to code from approved sources, which reduces the risk of running tampered or untrusted scripts.

In the ODC Portal, you activate a CSP and set its directive values, for example to allow a trusted third-party service.

For more information, refer to [Content security policy](configure-csp.md) and [Implement content security policy](implement-csp.md).

### Tamper detection for mobile apps with AppShield {#appshield}

AppShield is a licensed plugin that hardens native Android and iOS apps and works with the Mobile Apps Build Service (MABS). Its repackaging detection checks whether someone changed the app bundle or signed it with a different keystore.

If you re-sign the app with a different certificate after MABS builds it, repackaging detection treats the app as repackaged and the app crashes on startup. Some distribution channels re-sign the app, for example Google Play App Signing. To prevent the crash, add the certificate that re-signs the app to the AppShield list of accepted signing certificates. AppShield adds the certificate of the keystore that you provide to MABS automatically.

For more information about the `ApplicationSignerCertificate` setting, refer to [Whitelist signing certificates](app-shield/intro.md#whitelist-signing-certificates).

To use AppShield, you must have an AppShield license.

For more information, refer to [Harden the protection of mobile apps with AppShield](app-shield/intro.md) and [AppShield protection features](app-shield/protection-features-description.md).

## Integrity checks that remain your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, verify the code and data that your apps get from external sources.

The model doesn't assign duties to individual OWASP categories. This section is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about how OutSystems secures ODC, refer to the following articles:

* [Security of OutSystems Developer Cloud](security.md)
* [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md)
* [OWASP A09 security logging and alerting failures in ODC](owasp-a09-security-logging-alerting-failures.md)
