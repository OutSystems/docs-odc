---
guid: 347db70f-fd6d-4274-ad86-1a79d3f8ce4d
locale: en-us
summary: OWASP A09 in OutSystems Developer Cloud (ODC) explains audit trails, SIEM and APM streaming, app logs, and customer alerting duties.
figma:
coverage-type:
  - understand
topic:
  - delayed-breach-detection
  - shared-responsibility-overview
  - understand-analytics-stream
app_type: reactive web apps
platform-version: odc
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Logging
  - Monitoring
  - OWASP
  - Security
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# OWASP A09 security logging and alerting failures in ODC

Security logging and alerting failures delay the detection of an attack. Logs that nobody reviews, and events that trigger no alert, give an attacker time to stay in a system and reach more data. The OWASP Top 10:2025 report keeps this category at rank #9 and adds alerting to its name. Recording events isn't enough. Someone must receive an alert and act on it.

This article covers A09 in OutSystems Developer Cloud (ODC). It lists the logging and monitoring that apply by default, the mechanisms you set up for alerting, and what remains yours.

<div class="info" markdown="1">

This article describes stages that run in the OutSystems Cloud. In a self-hosted tenant, the Test and Production stages run in your own infrastructure, so some protections differ. Each section notes the documented differences. For more information, refer to [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md).

</div>

## Logging and monitoring that ODC applies by default {#covered-by-default}

The following logging and monitoring apply to every ODC organization in cloud stages without any setup.

### Immutable audit trail {#audit-trail}

The audit trail is an immutable record of significant actions and changes in your organization. The audit trail shows who did what, where, and when.

The ODC Portal shows a rolling 30-day history. To get logs up to three months old, export the audit trail to a CSV file. To view or export the audit trail, users need the **Audit Trail View** role.

For more information, refer to [Audit trail](../monitor-and-troubleshoot/audit-trail/audit-trail.md).

### App logs, traces, and metrics {#app-logs}

ODC generates some app logs automatically, for example when a timer fails to run. ODC also collects metrics such as requests and errors. Exceptions in your app logic and calls to the **LogMessage** system action add more logs.

The ODC Portal gives access to logs, traces, and metrics up to four weeks old.

In self-hosted stages, OpenTelemetry and FluentBit stream the logs and traces of your apps to an observability destination that you host and operate.

For more information, refer to [Monitoring and troubleshooting apps](../monitor-and-troubleshoot/monitor-apps.md).

### Infrastructure monitoring by OutSystems {#infrastructure-monitoring}

OutSystems monitors the ODC infrastructure, events, and availability 24 hours a day, seven days a week. An unexpected alert, whether detected automatically or found in a log review, triggers the OutSystems Security Incident Response.

In self-hosted stages, OutSystems collects telemetry about platform health only. OutSystems doesn't monitor your Kubernetes cluster or hardware infrastructure.

For more information, refer to [OutSystems security operations center](security.md#security-operations-center).

## Alerting and logging that you set up {#you-configure}

ODC provides the following mechanisms. Alerting depends on you setting up these mechanisms and the tools that receive the data.

### Audit trail streaming to your SIEM tool {#audit-trail-streaming}

With a Sentry for ODC subscription, you can stream the audit trail to your security information and event management (SIEM) tool. In the SIEM tool, you configure custom alerts that notify your security team when suspicious activity or a policy violation happens. Streaming also keeps the audit logs for longer than the ODC Portal does.

For more information, refer to [Stream audit trail logs](../monitor-and-troubleshoot/audit-trail/audit-trail-streaming.md).

### Intrusion detection with Sentry for ODC {#intrusion-detection}

Sentry for ODC also adds intrusion detection, which monitors for anomalous patterns and activities. Intrusion detection applies to the shared platform infrastructure. It doesn't cover the app runtime.

For more information, refer to [Sentry for ODC](sentry.md).

### App observability streaming to your APM tool {#analytics-stream}

With an Analytics Stream add-on subscription, you can stream logs, traces, and metrics from your apps to your application performance monitoring (APM) tool. ODC uses the OpenTelemetry standard, and supports tools such as Datadog, Dynatrace, Elastic Cloud, New Relic, Splunk, and Amazon S3. Streaming keeps the data for longer than the four weeks in the ODC Portal.

The APM tool must expose an ingestion endpoint that's reachable from the public internet. Private connectivity options, such as a private gateway, aren't supported for this endpoint.

For more information, refer to [Streaming observability data](../monitor-and-troubleshoot/stream-app-analytics/stream-app-analytics-overview.md).

### Exception logging in your app logic {#exception-logging}

When you handle an exception, the **Log Error** property of the Exception Handler element sets whether ODC logs the exception. ODC always logs exceptions in integrations, whatever the value of **Log Error**.

For more information, refer to [Exception logs](../building-apps/handling-exceptions/handle-exceptions.md#exception-logs).

## Alerting and monitoring that remain your responsibility {#your-responsibility}

Under the OutSystems Cloud shared responsibility model, you own the monitoring of your apps. For this category, set up alerts and monitor your apps in your SIEM or APM tool. If you suspect a privacy or security incident, report it through the Support Portal.

The shared responsibility model doesn't assign duties to individual OWASP categories, so these statements are an interpretation of the model.

For more information, refer to [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47).

## Related resources

For more information about how OutSystems secures ODC, refer to the following articles:

* [Security of OutSystems Developer Cloud](security.md)
* [OWASP Top 10:2025 coverage in ODC](owasp-top-10-coverage.md)
* [OWASP A04 cryptographic failures in ODC](owasp-a04-cryptographic-failures.md)
* [OWASP A05 injection in ODC](owasp-a05-injection.md)
* [OWASP A06 insecure design in ODC](owasp-a06-insecure-design.md)
* [OWASP A07 authentication failures in ODC](owasp-a07-authentication-failures.md)
* [OWASP A08 software or data integrity failures in ODC](owasp-a08-software-data-integrity-failures.md)
* [OWASP A10 mishandling of exceptional conditions in ODC](owasp-a10-mishandling-exceptional-conditions.md)
