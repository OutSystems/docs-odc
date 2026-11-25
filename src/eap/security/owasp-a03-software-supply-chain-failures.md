---
guid: 45906b55-d961-484c-900b-3653eaa9e5c2
locale: en-us
summary: OWASP A03 in OutSystems Developer Cloud (ODC) explains the vulnerability policy, pipeline checks, patching, library updates, and your update reviews.
figma:
coverage-type:
  - understand
topic:
  - automatic-app-patching
  - odc-container-image-integrity
  - review-accepted-library-updates
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - 1-Click Publish
  - CI/CD
  - Deploy
  - Libraries
  - OWASP
  - Security
outsystems-tools:
  - none
helpids:
isautopublish: true
---

# OWASP A03 software supply chain failures in ODC

Software Supply Chain Failures happen when the components, tools, or pipelines that build and deliver software are vulnerable or compromised. Examples include a vulnerable library, a tampered build pipeline, and a malicious update. The OWASP Top 10:2025 report adds this category at rank #3. It extends the 2021 category Vulnerable and Outdated Components to how software is built, distributed, and updated.

This article covers A03 in OutSystems Developer Cloud (ODC). It lists the protections that apply by default, the ones you configure, and the checks that remain yours. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Supply chain protections that ODC applies by default {#covered-by-default}

The following protections apply to every ODC app in cloud stages without any action from you.

### Vulnerability policy {#vulnerability-policy}

OutSystems publishes a vulnerability policy that gives guidance about vulnerabilities reported in OutSystems products. OutSystems rates the severity of each vulnerability with the Common Vulnerability Scoring System (CVSS), an open industry standard.

For more information, refer to [Vulnerability policy](security.md#vulnerability-policy) and [Automatic patching](security.md#automatic-patching).

### Code scanning for Platform services {#code-scanning}

A static code analysis tool scans the code of the Platform services for vulnerabilities and weak security practices. The scan covers first-party and third-party code, and runs before the system builds the code as a container image.

For more information, refer to [Vulnerability patching](security.md#vulnerability-patching).

### Admission control in the deployment pipeline {#admission-control}

A code change in a Platform service goes through a deployment pipeline before it reaches production. At each stage, admission control verifies that the previous stage completed and that the container image is unmodified since it entered the pipeline.

For more information, refer to [Software supply chain integrity](security.md#supply-chain-integrity). For how this protection supports integrity, refer to [OWASP A08 software or data integrity failures in ODC](owasp-a08-software-data-integrity-failures.md).

### Daily scans and automatic patching {#scans-and-patching}

OutSystems scans the container registry daily. The scan covers the current Platform service images and the images of all apps deployed to all customer Runtime stages. When a scan detects a vulnerability, OutSystems security engineers fix it and release a new version of the affected Platform service or app base container image.

ODC then patches the affected apps automatically. The schedule depends on the severity of the vulnerability, and apps don't have downtime. Users with the Administrator built-in role in your organization receive emails about the process. Malware detection is part of the scanning.

For more information, refer to [Vulnerability patching](security.md#vulnerability-patching) and [Automatic patching](security.md#automatic-patching).

## Supply chain mechanisms that you configure or apply {#you-configure}

ODC provides the following mechanisms. They give you visibility or control. OutSystems patches your apps automatically even if you don't use them.

### Known vulnerabilities in the ODC Portal {#app-security-tab}

In the ODC Portal, go to **Management** > **Maintain** > **Platform updates**, then select the **App security** tab. The tab lists the apps with known vulnerabilities, the classification of the vulnerabilities, and the fixing schedule. Use the list to plan patching.

For more information, refer to [Vulnerability patching](security.md#vulnerability-patching).

### Earlier patching with 1-Click Publish {#one-click-publish}

You don't have to wait for the automatic patch. To patch an app sooner, open it in ODC Studio and select **1-Click Publish**. This patches the app in the development stage. Promote the app to the other stages so that all stages run the patched version. Patching manually also gives you control over when timers that run **When published** run.

For more information, refer to [Manual patching](security.md#manual-patching).

### Library updates {#library-updates}

When you open an app or library in ODC Studio, ODC Studio updates the dependencies of the asset. If a library has an update, ODC Studio asks you to review or dismiss it. Review the update for breaking changes before you accept it. You decide when a library update enters your app.

For more information, refer to [Libraries](../building-apps/libraries/libraries.md).

## Supply chain checks that remain your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, review the known vulnerabilities in your apps and the updates to the libraries that they use, and decide when to apply them.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about how OutSystems secures ODC, refer to the following articles:

* [Security of OutSystems Developer Cloud](security.md)
* [OWASP A02 security misconfiguration in ODC](owasp-a02-security-misconfiguration.md)
