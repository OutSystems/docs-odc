---
guid: 47f1d271-8016-4371-846c-49ed53bd4151
locale: en-us
summary: OWASP A04 in OutSystems Developer Cloud (ODC) explains encryption in transit and at rest, secret settings, and your data protection duties.
figma:
coverage-type:
  - understand
app_type: reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Data
  - OWASP
  - Security
  - Settings
outsystems-tools:
  - odc studio
  - odc portal
helpids:
isautopublish: true
---

# OWASP A04 cryptographic failures in ODC

Cryptographic failures expose sensitive data. Examples are traffic sent without encryption, data stored in plain text, and keys kept where others can read them. The OWASP Top 10:2025 report lists this category at rank #4, down from #2.

This article covers A04 in OutSystems Developer Cloud (ODC). It lists the encryption that applies by default, the mechanisms you set up, and the data protection that remains yours. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Encryption that ODC applies by default {#covered-by-default}

The following encryption applies to every ODC organization in cloud stages without any setup.

### Encryption in transit {#encryption-in-transit}

Requests to the Platform services and the Runtime terminate at an HTTPS endpoint. ODC applies HTTP Strict-Transport-Security (HSTS) as a native default, which forces browser communication over encrypted channels and prevents downgrade attacks. ODC supports TLS 1.3.

In self-hosted stages, your load balancer terminates TLS with your domain certificates and forwards the traffic to the cluster over HTTP.

For more information, refer to [Encryption in transit](security.md#encryption-transit).

### Encryption at rest {#encryption-at-rest}

ODC encrypts data at rest with the AES-256-GCM algorithm, including all backup instances. OutSystems stores and manages the keys in a Key Management Service.

All customer production runtime app data is encrypted with a per-customer encryption key that OutSystems manages. Encryption at rest protects stored data. The data that your custom logic and integrations handle remains your responsibility.

In self-hosted stages, app data is stored in PostgreSQL databases that you provision and operate.

For more information, refer to [Encryption at-rest](security.md#encryption-at-rest).

## Protection that you set up {#you-configure}

ODC provides the following protection for the sensitive values in your app settings. It protects only the settings that you mark as secret.

### Settings marked as secret {#secret-settings}

When you set the **Is Secret** property of an app setting to **Yes**, ODC stores the value in the Secrets Manager. ODC always encrypts the value and never shows it as plain text. You set the value for each stage in the ODC Portal.

If you change a secret setting back to a non-secret setting, ODC deletes the value when you publish the app.

For more information, refer to [Set as secret](set-as-secret.md).

## Data protection that remains your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, protect the sensitive data that your custom logic and integrations handle.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about how OutSystems secures ODC, refer to the following articles:

* [Security of OutSystems Developer Cloud](security.md)
* [OWASP A05 injection in ODC](owasp-a05-injection.md)
* [OWASP A06 insecure design in ODC](owasp-a06-insecure-design.md)
* [OWASP A07 authentication failures in ODC](owasp-a07-authentication-failures.md)
* [OWASP A10 mishandling of exceptional conditions in ODC](owasp-a10-mishandling-exceptional-conditions.md)
