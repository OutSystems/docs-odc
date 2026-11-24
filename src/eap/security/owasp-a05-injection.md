---
guid: 9d87598b-8b71-444c-8f01-3cb2a98626cd
locale: en-us
summary: OWASP A05 in OutSystems Developer Cloud (ODC) explains prepared statements, the WAF, encode and sanitize functions, and your input validation duties.
figma:
coverage-type:
  - understand
app_type: reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Front-end developer
  - Platform administrator
  - Tech lead
tags:
  - JavaScript
  - Libraries
  - OWASP
  - Security
  - SQL
  - Web
outsystems-tools:
  - odc studio
  - odc portal
helpids:
isautopublish: true
---

# OWASP A05 injection in ODC

Injection happens when an app sends untrusted input to an interpreter as part of a command or query. Examples are SQL injection and cross-site scripting. The OWASP Top 10:2025 report lists this category at rank #5, down from #3.

This article covers A05 in OutSystems Developer Cloud (ODC). ODC runs your SQL queries as prepared statements by default. For HTML and JavaScript, you use the encode and sanitize functions that ODC provides. The sections that follow describe each protection and what remains your responsibility. For the summary of all ten categories, refer to [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md).

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Injection protections that ODC applies by default {#covered-by-default}

The following protections apply to every ODC organization in cloud stages without any setup.

### Prepared statements for SQL queries {#prepared-statements}

ODC runs the SQL queries that you define in SQL elements as prepared statements. A prepared statement uses parameters, and a parameter holds a value of one type, not an SQL fragment.

This protection ends if you enable the **Expand Inline** property of a Query Parameter. ODC then adds the value to the SQL statement without turning it into a literal. The property is disabled by default.

For more information, refer to [SQL injection](../monitor-and-troubleshoot/manage-technical-debt/security/sql-injection.md).

### Web application firewall {#web-application-firewall}

A web application firewall (WAF) runs on the content delivery network and protects the Platform and the Runtime from common web exploits. Its policies cover SQL injection attacks. The WAF is an extra layer of defense. It doesn't replace input validation in your apps.

In a self-hosted tenant, end-user traffic enters through your own ingress controller and load balancer.

For more information, refer to [Web Application Firewall](security.md#web-application-firewall).

## Functions and checks that you use {#you-configure}

ODC provides the following mechanisms to handle untrusted input. Each one protects only the code where you apply it.

### Encode functions {#encode-functions}

The built-in functions **EncodeSql**, **EncodeHtml**, and **EncodeJavaScript** replace reserved characters in text, so that you can use the text in a SQL string literal, an HTML literal, or a JavaScript literal. Each function has limits.

* **EncodeSql** encodes string literals only. It doesn't protect you from SQL injection on its own, and you use it when **Expand Inline** is enabled.
* **EncodeHtml** encodes text for HTML literals only. On its own, it doesn't stop cross-site scripting (XSS) or JavaScript injection.
* **EncodeJavaScript** encodes text for JavaScript literals only. On its own, it doesn't stop XSS or JavaScript injection.

For more information, refer to [EncodeSql](../reference/built-in-functions/text.md#encodesql), [EncodeHtml](../reference/built-in-functions/text.md#encodehtml), and [EncodeJavaScript](../reference/built-in-functions/text.md#encodejavascript).

### Sanitization library {#sanitization-library}

The Sanitization library provides actions for HTML, JavaScript, and SQL snippets that include untrusted content. **SanitizeHtml** sanitizes the HTML that you provide. **VerifyJavascriptLiteral** checks that text contains only JavaScript literals and raises an exception if it contains anything else. **BuildSafe_InClauseIntegerList** and **BuildSafe_InClauseTextList** build values for an SQL `IN` clause.

For more information, refer to [Sanitization library](../reference/libraries/sanitization.md).

### SQL injection finding in Code quality {#code-quality-finding}

**Code quality** reports a finding if you enable **Expand Inline** on a Query Parameter. The finding explains the impact and how to fix it.

## Input validation that remains your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the security of the apps you build. For this category, validate the input that you add to queries, HTML, or JavaScript.

The shared responsibility model doesn't assign duties to individual OWASP categories, so this statement is an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about how OutSystems secures ODC, refer to the following articles:

* [Security of OutSystems Developer Cloud](security.md)
* [OWASP A04 cryptographic failures in ODC](owasp-a04-cryptographic-failures.md)
* [OWASP A06 insecure design in ODC](owasp-a06-insecure-design.md)
* [OWASP A07 authentication failures in ODC](owasp-a07-authentication-failures.md)
* [OWASP A10 mishandling of exceptional conditions in ODC](owasp-a10-mishandling-exceptional-conditions.md)
