---
guid: f32afa36-2267-4007-9da2-1e70d277187d
locale: en-us
summary: OWASP A02 in OutSystems Developer Cloud (ODC) explains the WAF, infrastructure checks, enforced TLS, content security policy, and your settings.
figma:
coverage-type:
  - understand
topic:
  - odc-content-security-policy
  - outsystems-security-approach
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Infrastructure
  - OWASP
  - REST
  - Security
  - Settings
outsystems-tools:
  - none
helpids:
isautopublish: true
---

# OWASP A02 security misconfiguration in ODC

Security Misconfiguration happens when settings, defaults, or hardening leave an app or its infrastructure more exposed than necessary. Examples include insecure defaults, unneeded features left on, and missing security headers. The OWASP Top 10:2025 report moves this category up from rank #5 to rank #2.

This article covers A02 in OutSystems Developer Cloud (ODC). It lists the protections that apply by default, the ones you configure, and the settings that remain yours. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Configuration protections that ODC applies by default {#covered-by-default}

The following protections apply in cloud stages without any action from you. The WAF and the infrastructure checks cover the Platform and the Runtime. The container image hardening also covers the apps you deploy.

### Web application firewall {#waf}

A web application firewall (WAF) runs on the content delivery network (CDN). It protects the Platform and the Runtime from common web exploits and bots, as a first layer of defense. The OutSystems Security Office periodically reviews the WAF rules, and the firewall enforces them automatically.

In a self-hosted tenant, end-user traffic enters through your own ingress controller and load balancer.

For more information, refer to [Security of OutSystems Developer Cloud](security.md#web-application-firewall).

### Infrastructure checked for misconfigurations {#infrastructure-checks}

OutSystems plans and deploys the infrastructure of the Platform and the Runtime as code. A policy enforcement tool checks the infrastructure for potential misconfigurations and for policy issues that put the environment out of compliance with OutSystems or regulatory requirements. The OutSystems Security Office routinely reviews these policies.

In self-hosted stages, you provision and operate the infrastructure, including the Kubernetes cluster and the PostgreSQL databases.

For more information, refer to [Secure code and processes](security.md#secure-code).

### CIS benchmarks and hardened container images {#cis-hardened-images}

OutSystems applies the CIS benchmarks to all systems. OutSystems security engineers also continuously harden the base container image of each app to minimize the attack surface.

For more information, refer to [Secure code and processes](security.md#secure-code) and [Containers](security.md#containers).

### Enforced TLS for REST services {#enforced-tls}

In ODC cloud stages, SSL/TLS is always enforced for REST services, and you can't disable it.

In self-hosted stages, your load balancer terminates TLS with your domain certificates and forwards the traffic to the cluster over HTTP.

For more information, refer to [Exposed REST services without authentication](../monitor-and-troubleshoot/manage-technical-debt/security/exposed-rest-services-are-not-secured.md).

## Configuration mechanisms that you configure or apply {#you-configure}

ODC provides the following mechanism. The protection depends on you activating and configuring it.

### Content security policy {#csp}

A content security policy (CSP) controls which sources a browser can load scripts, images, frames, and other resources from. ODC doesn't activate a CSP by default, so no content or frames are blocked until you activate one.

In the ODC Portal, you do the following for each stage:

* Activate the CSP.
* Configure the directive values as an allow list, which blocks all other sources.
* Set the `frame-ancestors` directive to control which domains can embed your app pages in a frame.

Removing unsafe directives can affect some OutSystems components, so test your apps after you change the default values.

For more information, refer to [Content security policy](configure-csp.md), [Implement content security policy](implement-csp.md), and [Impacts of removing unsafe directives](impacts-removing-unsafe-directives.md).

## Configuration work that remains your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, keep the app and stage settings that you control aligned with your security requirements.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about how OutSystems secures ODC, refer to the following articles:

* [Security of OutSystems Developer Cloud](security.md)
* [OWASP A01 broken access control in ODC](owasp-a01-broken-access-control.md)
* [OWASP A03 software supply chain failures in ODC](owasp-a03-software-supply-chain-failures.md)
