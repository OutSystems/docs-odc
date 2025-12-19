---
summary: Learn about the process for streaming audit trail logs to Security Information and Event Management (SIEM) tools for real-time monitoring and compliance
tags: audit trail,siem integration,security monitoring,compliance,opentelemetry
guid: 000ca25b-a3c6-42d5-9ab9-8f3219f0a283
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=4011-50
outsystems-tools:
  - odc portal
coverage-type:
  - apply
content-type:
  - process
audience:
  - platform administrators
  - infrastructure managers
  - tech leads
  - architects
topic:
  - app-settings
  - app-configuration
  - debug-troubleshoot-logic
---

# Stream audit trail logs

With ODC's **audit trail streaming**, you can securely stream platform audit logs directly to your preferred security information and event management (SIEM) solutions or other security monitoring repositories. This enables continuous threat detection and anomaly analysis by integrating ODC with your existing monitoring tools, eliminating the need to manually export and upload audit logs.

## Benefits of audit trail streaming

Streaming audit trail logs to your SIEM tool provides several key advantages:

* **Real-time threat detection and alerting**: Detect and respond to security threats as they occur. Configure custom alerts to notify security teams immediately when suspicious activities or policy violations are detected.

* **Centralized security operations**: Integrate ODC audit logs with your existing security infrastructure and use advanced analytics to identify patterns, anomalies, and potential security incidents across all your systems.

* **Extended log retention**: Store audit logs beyond the 3-month retention period available in the ODC Portal, ensuring compliance with regulatory requirements that mandate longer retention periods.

* **Compliance reporting**: Generate comprehensive compliance reports by correlating ODC audit logs with data from other systems in your organization.

## Prerequisites

Before you start streaming audit trail logs, ensure you have:

* Subscription to Sentry. Contact your account manager for provisioning.

* **Manage audit trail streaming** permission in the ODC Portal.

* Tool-specific requirements for your chosen SIEM destination. For more information, refer to [Requirements for streaming audit trail logs](audit-trail-requirements.md).

## Create an audit trail stream

This example demonstrates the process of creating an audit trail stream. The steps might vary slightly depending on the SIEM tool you select.

1. In the ODC Portal, go to **Configure** > **Streams**.

1. Click **Create Stream** and select **Audit trail**.

    <div class="info" markdown="1">

    For any custom or 3rd-party tool, select **Other** as the destination tool

    </div>

   ![ODC Portal interface showing the Create Stream button highlighted in the Audit Trail Streaming section.](images/audit-trail-create-pl.png "Create Stream Button")

1. Select the destination SIEM tool and click **Choose**.

   ![ODC Portal interface for choosing the destination SIEM tool.](images/audit-trail-destination-pl.png "Choose Destination SIEM Tool")

1. Enter the destination details and click **Test stream**.

   ![ODC Portal interface for entering destination details, including authentication credentials and server URL.](images/audit-trail-test-stream-pl.png "Enter Destination Details")

    ODC attempts to establish a connection with the specified SIEM server.

    * **Successful connection:** If the connection is established successfully, a success message is displayed. The system also sends test data to your destination tool. You must validate that this test data has arrived and is visible in the SIEM tool.

        ![ODC Portal interface showing a successful connection message after testing the stream.](images/audit-trail-connection-success-pl.png "Successful Connection")

    * **Unsuccessful connection:** If the connection fails, an error message is displayed.

        ![ODC Portal interface showing an error message after a failed connection test.](images/audit-trail-connection-failure-pl.png "Unsuccessful Connection")

        In this case:

        * Review the destination information you entered to ensure its accuracy.
        * Verify that your SIEM tool is configured to accept incoming connections.
        * Check that any required firewall rules or network configurations are in place.
        * If the issue persists, consult the relevant troubleshooting documentation for the recommended action.

1. Click **Save**.

Your new audit trail stream is created, and audit logs can now be sent to the configured SIEM tool.

![ODC Portal interface showing the newly created audit trail stream with its status as Active.](images/audit-trail-stream-saved-pl.png "Stream Created")

## Stream status

A stream can have one of the following statuses:

* **Active:** The stream is currently running and successfully sending audit trail logs to the configured SIEM tool.

* **Active with errors:** The stream is currently running and attempting to send data, but encountering some errors. You should investigate these errors to ensure all logs are being delivered correctly. Check the stream details or logs for more information on the specific errors.

* **Inactive:** When you manually deactivate a stream, it transitions to an inactive state, and no audit logs are sent to the SIEM tool. You can reactivate an inactive stream. Once the stream is successfully reactivated, its status will change to **Active**.

## Related resources

* [Audit trail](audit-trail.md)

* [Requirements for streaming audit trail logs](audit-trail-requirements.md)

* [Allowlisting ODC public IP addresses](../../manage-platform-app-lifecycle/odc-public-ips.md)
