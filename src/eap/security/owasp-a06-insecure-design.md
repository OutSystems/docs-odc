---
guid: 806dc51c-bbbe-4390-8ab9-472df45a67b1
locale: en-us
summary: OWASP A06 in OutSystems Developer Cloud (ODC) explains the secure-by-design platform, stage isolation, Code quality findings, and your app design duties.
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
  - Architecture
  - Best Practices
  - OWASP
  - Security
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# OWASP A06 insecure design in ODC

Insecure design is a flaw in how an app is planned, not in how it's coded. A missing control or an unchecked assumption stays in the app even when the code is correct. The OWASP Top 10:2025 report lists this category at rank #6, down from #4.

This article covers A06 in OutSystems Developer Cloud (ODC). It lists the design principles and isolation that OutSystems applies to the platform, the analysis that you use for your apps, and the design work that remains yours. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Design protections that ODC applies by default {#covered-by-default}

The following protections apply to the platform and to every ODC organization in cloud stages without any setup. They describe the design of ODC. They don't review the design of your apps.

### Secure-by-design principles {#secure-by-design}

OutSystems designs ODC with the secure-by-design principles of the OWASP Developer Guide. These principles are defense in depth, least privilege, separation of duties, and complete mediation.

For more information, refer to [Security of OutSystems Developer Cloud](security.md).

### Isolation of stages {#stage-isolation}

A network namespace isolates each stage in each organization's Runtime, so the internal traffic of a stage stays within that stage. Each stage has its own relational database. A network policy defines the connection between the namespace and the database.

In a self-hosted tenant, the Test and Production stages each connect to a dedicated PostgreSQL database in your infrastructure.

For more information, refer to [Isolation of stages](security.md#isolation-of-stages).

## Analysis that you use {#you-configure}

ODC provides the following analysis for your apps.

### Security findings in Code quality {#code-quality-findings}

**Code quality** analyzes your apps and reports findings for security patterns. Each finding explains the impact, why it happens, and how to fix it.

The findings flag known code patterns. They don't evaluate whether the design of your app meets your security requirements.

For more information, refer to [Security findings](../monitor-and-troubleshoot/manage-technical-debt/security/security.md).

## Design work that remains your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, design your apps for security, for example with threat modeling.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about the other OWASP categories in ODC, refer to the following articles:

* [OWASP A04 cryptographic failures in ODC](owasp-a04-cryptographic-failures.md)
* [OWASP A05 injection in ODC](owasp-a05-injection.md)
* [OWASP A07 authentication failures in ODC](owasp-a07-authentication-failures.md)
* [OWASP A10 mishandling of exceptional conditions in ODC](owasp-a10-mishandling-exceptional-conditions.md)
