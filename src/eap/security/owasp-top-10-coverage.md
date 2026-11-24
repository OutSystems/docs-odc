---
guid: e6ed68de-3480-4378-8b03-7bfa54ecbb5c
locale: en-us
summary: OWASP Top 10:2025 coverage in OutSystems Developer Cloud (ODC) maps default protections, configuration, and shared responsibility for all ten risks.
figma:
coverage-type:
  - understand
topic:
  - owasp-top-10-lists
  - outsystems-security-approach
  - shared-responsibility-overview
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Authentication
  - Authorization
  - Data Integrity
  - Logging
  - OWASP
  - Roles
  - Security
outsystems-tools:
  - none
helpids:
isautopublish: true
---

<!--
DRAFT for TK-24330. ODC copy of a page that is duplicated for O11 (docs-next
has no platform-agnostic content yet). Resolve and delete these notes before
publishing.

* Row links point to anchors such as #a012025-broken-access-control on the
  first-aid page. The anchors don't exist until PR #2232 merges. After it
  merges, confirm that each anchor resolves and that the tk/redirect link
  keeps the #fragment. Each ODC category PR switches its rows to the ODC page:
  A08 and A09 link to their ODC pages (PR #4025), and A01 to A03 link to
  theirs (PR #4069).
* TK-24108 SME review: Fred confirmed the "Your responsibility" statements
  (Q2). SSRF is left out of the page, including the A01 row in the
  2021 comparison table, until product documentation covers it. No product
  doc mentions SSRF, and the only statement is in the ODC training lesson.
  Don't link the shared responsibility article as SSRF support.
-->

# OWASP Top 10:2025 coverage in ODC

The OWASP Top 10 lists the most critical security risks to web applications. Security teams use it as an awareness baseline when they assess a platform. It isn't a security standard or a certification.

This article is a surface-level overview of how OutSystems Developer Cloud (ODC) addresses each of the ten categories in the OWASP Top 10:2025 report. For details about the mechanisms behind each category, refer to [How OutSystems helps you address OWASP Top 10](https://www.outsystems.com/tk/redirect?g=74924eac-d729-4c99-bcb4-09b40a483cfa).

## Shared responsibility

Security in OutSystems Cloud, which includes ODC, is a shared responsibility. OutSystems operates and secures the components from the platform down to the infrastructure. You're responsible for your apps, their data, and the access and permissions of their users.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## How to read the coverage matrix

The coverage matrix has three columns for each OWASP category:

* **Covered by default**: Protection that applies to an app without any action from the developer.
* **You configure or apply**: Mechanisms that ODC provides and that you set up, use, or subscribe to.
* **Your responsibility**: What remains with you under the shared responsibility model.

The shared responsibility model doesn't assign duties to individual OWASP categories, so the **Your responsibility** column is an interpretation of the model.

## What changed from the 2021 list

The following table shows each 2025 category and how it changed from the 2021 list.

| 2025 rank | Category | Change from 2021 |
| --- | --- | --- |
| A01 | Broken Access Control | Unchanged at #1. |
| A02 | Security Misconfiguration | Up from #5. |
| A03 | Software Supply Chain Failures | New. Extends Vulnerable and Outdated Components to how software is built, distributed, and updated. |
| A04 | Cryptographic Failures | Down from #2. |
| A05 | Injection | Down from #3. |
| A06 | Insecure Design | Down from #4. |
| A07 | Authentication Failures | Unchanged at #7. |
| A08 | Software or Data Integrity Failures | Unchanged at #8. |
| A09 | Security Logging and Alerting Failures | Unchanged at #9. |
| A10 | Mishandling of Exceptional Conditions | New. Covers how apps respond to errors and unexpected states. |

## Coverage matrix

The following table lists, for each category in the OWASP Top 10:2025 report, what ODC covers by default in cloud stages, what you configure or apply, and what remains your responsibility. Each category links to the matching section of the detailed article.

<div class="info" markdown="1">

This matrix describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, and some protections differ. For example, the OutSystems WAF and IP filters don't apply, and end users sign in through an external OIDC IdP. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

| Category | Covered by default | You configure or apply | Your responsibility |
| --- | --- | --- | --- |
| [Broken Access Control (A01)](owasp-a01-broken-access-control.md) | Validation of the identity and integrity of the access token before each request reaches the target service. This check doesn't decide what the user can access. | Role-based access control for screens, logic, and data, and role checks in server-side logic. Permissions are a separate step that runs on the roles you define.<br/>Static code analysis that flags insecure access patterns, such as screens open to anonymous users.<br/>IP filter rules, with a Sentry for ODC subscription. | Define a role model that matches your business rules. |
| [Security Misconfiguration (A02)](owasp-a02-security-misconfiguration.md) | A web application firewall (WAF) on the content delivery network that filters common web exploits and bots as a first layer of defense.<br/>Infrastructure that OutSystems deploys as code and checks for misconfigurations, applies CIS benchmarks to, and runs from hardened container images.<br/>Enforced TLS for REST services. | A content security policy, inactive by default, that controls where app pages load resources from and which sites embed them. | Keep the app and stage settings that you control aligned with your security requirements. |
| [Software Supply Chain Failures (A03)](owasp-a03-software-supply-chain-failures.md) | A vulnerability policy for OutSystems components.<br/>Admission control at each stage of the Platform services pipeline, and daily scans of container images.<br/>Automatic patching of vulnerable apps, scheduled by severity. | Patching an app sooner with 1-Click Publish in ODC Studio.<br/>Reviewing or dismissing library updates. | Assess the components that OutSystems doesn't support before you use them. |
| [Cryptographic Failures (A04)](https://www.outsystems.com/tk/redirect?g=74924eac-d729-4c99-bcb4-09b40a483cfa#a042025-cryptographic-failures) | Encryption in transit with HTTPS, HSTS as a native default, and TLS 1.3 support.<br/>Encryption at rest with AES-256-GCM, including backups, and a per-customer key for production runtime app data. | Marking settings as secret, which always encrypts them and never shows them as plain text. | Protect the sensitive data that your custom logic and integrations handle. |
| [Injection (A05)](https://www.outsystems.com/tk/redirect?g=74924eac-d729-4c99-bcb4-09b40a483cfa#a052025-injection) | SQL queries that run as prepared statements.<br/>The WAF, as an extra layer of protection from SQL injection attacks. | Functions that encode and sanitize input when you build code dynamically. | Validate the input that you add to queries, HTML, or JavaScript. |
| [Insecure Design (A06)](https://www.outsystems.com/tk/redirect?g=74924eac-d729-4c99-bcb4-09b40a483cfa#a062025-insecure-design) | A platform designed with the secure-by-design principles of the OWASP Developer Guide, such as defense in depth and least privilege.<br/>A separate network namespace for each stage. | Static code analysis that flags insecure patterns across your apps. | Design your apps for security, for example with threat modeling. |
| [Authentication Failures (A07)](https://www.outsystems.com/tk/redirect?g=74924eac-d729-4c99-bcb4-09b40a483cfa#a072025-authentication-failures) | A fixed password policy of at least 12 characters with a digit and an uppercase letter.<br/>Temporary lockout after five consecutive failed sign-in or password change attempts, which grows to about 5 minutes.<br/>Refresh token rotation, and a different session identifier on each sign-in. | Single sign-on and multi-factor authentication through your identity provider (IdP).<br/>The Authorization Code flow with Proof Key for Code Exchange (PKCE) for OIDC providers.<br/>The maximum and idle session duration for each stage. | Apply your organization's authentication policies through an external IdP. |
| [Software or Data Integrity Failures (A08)](owasp-a08-software-data-integrity-failures.md) | Signed access tokens.<br/>Production container images for the Platform services that are identical to the built images. | **Web apps**: A content security policy that restricts the app to code from approved sources.<br/>**Mobile apps**: AppShield detects modified app bundles, with an AppShield license. | Verify the code and data that your apps get from external sources. |
| [Security Logging and Alerting Failures (A09)](owasp-a09-security-logging-alerting-failures.md) | An immutable audit trail of significant platform actions and changes, including successful sign-ins, shown for 30 days in the ODC Portal and exportable for up to 3 months. Failed sign-ins aren't recorded.<br/>Monitoring of the ODC infrastructure, events, and availability by OutSystems, 24 hours a day, seven days a week. | Streaming the audit trail to your security information and event management (SIEM) tool, with a Sentry for ODC subscription.<br/>Streaming logs, traces, and metrics to your performance monitoring tool, with an Analytics Stream subscription. | Set up alerts and monitor your apps in your SIEM and performance monitoring tools. |
| [Mishandling of Exceptional Conditions (A10)](https://www.outsystems.com/tk/redirect?g=74924eac-d729-4c99-bcb4-09b40a483cfa#a102025-mishandling-of-exceptional-conditions) | Rollback of database changes when an exception isn't handled, and a default Global Exception Handler.<br/>HTTP status code 500 for unhandled exceptions in exposed REST APIs.<br/>Platform timeouts of 60 seconds for an exposed REST API method and 100 seconds for a service action. | Exception handlers in actions, UI flows, and modules or apps. | Handle errors in your logic, and control the messages that users see. |

<div class="info" markdown="1">

For Software Supply Chain Failures (A03), app and library revisions can't change after publish. Only the version label and publish message can change. This supports version management and traceability, and isn't a supply chain control.

</div>

## Related security content

For more information about how OutSystems secures ODC, refer to [Security of OutSystems Developer Cloud](security.md).
