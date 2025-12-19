---
summary: Learn about the requirements for streaming audit trail logs to different SIEM tools including Datadog, Splunk, AWS Firehose, and other security monitoring platforms
tags: audit trail,siem integration,security monitoring,datadog,splunk,aws firehose,requirements
guid: 6b41adf6-f9aa-48c7-a3d2-70e39c0cb8e8
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
outsystems-tools:
  - odc portal
coverage-type:
  - apply
content-type:
  - reference
audience:
  - platform administrators
  - infrastructure managers
  - tech leads
  - architects
topic:
  - app-settings
  - app-configuration
---

# Requirements for streaming audit trail logs

Before you stream audit trail logs to your security information and event management (SIEM) tool, you must complete specific setup steps. The requirements vary depending on the destination tool you select.

## General requirements

Regardless of which SIEM tool you choose, you must have:

* An **ODC Sentry** subscription. Audit trail streaming is part of the ODC Sentry package. Contact your account manager for provisioning.

* The **Manage audit trail streaming** permission in the ODC Portal to create and configure streams.

* An active subscription and account with your chosen SIEM tool or other log retention repository (Datadog, Splunk, AWS Firehose, or other).

<div class="info" markdown="1">

AWS Firehose is a data ingestion tool that enables you to forward audit logs to S3 or other repositories.

</div>

* Administrative permissions in your SIEM tool to create API keys, configure data ingestion endpoints, and manage authentication credentials.

* Network connectivity that allows your SIEM tool to accept incoming HTTPS connections from ODC. Review any firewall rules or network security groups that might block traffic.

## Datadog requirements

To stream audit trail logs to Datadog, you must:

1. Get the API key from your Datadog account. This key authenticates the connection between ODC and Datadog.

1. Identify your Datadog site region (for example, US1, US3, US5, EU1, or AP1). The site determines the correct API endpoint, for example, `https://http-intake.logs.datadoghq.eu/v1/input` for EU1.

1. Configure log indexes in Datadog to effectively organize and manage your ODC audit logs.

Once you've completed these requirements, go to the ODC Portal and [configure the audit trail stream](audit-trail-streaming.md#create-an-audit-trail-stream).

## Splunk requirements

To stream audit trail logs to Splunk, you must:

1. Create an HTTP Event Collector (HEC) token in Splunk. This token authenticates incoming data from ODC.

1. Get the HEC endpoint URL from your Splunk instance (for example, `https://your-splunk-instance.com:8088/services/collector`).

    * Ensure your Splunk HEC endpoint uses a valid SSL certificate. Self-signed certificates may cause connection issues.

1. Verify that the HEC is enabled on your Splunk instance and configured to accept HTTPS connections.

1. Identify or create a Splunk index where you want to store the audit trail logs.

    * Verify that the HEC token has permission to write to the designated index.
    * Consider configuring a custom source type in Splunk to identify ODC audit logs (for example, `odc:audit:trail`).

Once you've completed these requirements, go to the ODC Portal and [configure the audit trail stream](audit-trail-streaming.md#create-an-audit-trail-stream).

## AWS Firehose requirements

To stream audit trail logs to AWS Firehose, you must:

1. Create an Amazon Kinesis Data Firehose delivery stream in your AWS account.

1. Configure the delivery stream destination (for example, Amazon S3, Amazon Redshift, Amazon OpenSearch Service, or a third-party service provider).

    * Ensure your Firehose destination (for example, S3 bucket or  OpenSearch domain) has the appropriate permissions and configurations to receive data.

1. Create an IAM role with permissions to put records into the Firehose delivery stream.

    * The IAM role must have the `firehose:PutRecord` and `firehose:PutRecordBatch` permissions for the delivery stream.
    * Configure the trust policy for the IAM role, using your tenant ID as the external key.

1. Get the Firehose delivery stream name and AWS region. Note the AWS region where your delivery stream is hosted (for example, `us-east-1` or `eu-west-1`).

Once you've completed these requirements, go to the ODC Portal and [configure the audit trail stream](audit-trail-streaming.md#create-an-audit-trail-stream).

## Other 3rd-party tools

To stream audit trail logs to other 3rd party SIEM or security monitoring tools, you must:

1. Identify the HTTP/HTTPS endpoint URL where your tool receives data.

1. Set up authentication credentials for your tool's endpoint. You can use one of the following authentication methods:

    * **API Key** - Provide the API key header name and the API key value

    * **Bearer token** - Provide the bearer token for authentication

    * **Username and password** - Provide basic authentication credentials

1. Verify that your tool supports receiving JSON data through HTTP/HTTPS endpoints and can process the JSON schema format that ODC uses for audit trail log streaming.

Refer to your tool's documentation for configuring HTTP/HTTPS data ingestion endpoints and authentication methods.

### JSON schema

The following JSON schema defines the structure of audit trail logs:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AuditLog",
  "type": "object",
  "properties": {
    "CustomerVisible": {
      "type": "string"
    },
    "Metadata": {
      "type": "object",
      "properties": {
        "Schema": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "Event": {
      "type": "object",
      "properties": {
        "Category": { "type": "string" },
        "EventId": { "type": "string" },
        "TenantId": { "type": "string" },
        "EnvironmentId": { "type": "string" },
        "EnvironmentName": { "type": "string" },
        "Ring": { "type": "string" },
        "DateTime": { "type": "string", "format": "date-time" },

        "Source": {
          "type": "object",
          "properties": {
            "ApplicationId": { "type": "string" },
            "Name": { "type": "string" },
            "Version": { "type": "string" },
            "OsVersion": { "type": "string" }
          },
          "additionalProperties": false
        },

        "Request": {
          "type": "object",
          "properties": {
            "SourceIp": { "type": "string" },
            "DestinationIp": { "type": "string" },
            "TraceId": { "type": "string" },
            "UserId": { "type": "string" },
            "UserName": { "type": "string" },
            "EntityType": { "type": "string" },
            "EntityId": { "type": "string" },
            "EntityName": { "type": "string" },
            "EntityOldValue": { "type": "string" },
            "EntityNewValue": { "type": "string" },
            "Action": { "type": "string" }
          },
          "additionalProperties": false
        },

        "Response": {
          "type": "object",
          "properties": {
            "Status": { "type": "string" },
            "StatusCode": { "type": "integer" },
            "StatusMessage": { "type": "string" },
            "OSErrorCode": { "type": "string" }
          },
          "additionalProperties": false
        },

        "Effect": {
          "type": "object",
          "properties": {
            "Message": { "type": "string" }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

### Sample JSON

The following example shows the structure of an audit trail log event:

```json
{
  "CustomerVisible": "true",
  "Metadata": {
    "Schema": "urn:os:comp:auditLog:begin:1.0.0"
  },
  "Event": {
    "Category": "UserManagement",
    "EventId": "evt-789654",
    "TenantId": "tenant-123",
    "EnvironmentId": "env-456",
    "EnvironmentName": "Production",
    "Ring": "R1",
    "DateTime": "2025-11-27T10:32:00Z",
    "Source": {
      "ApplicationId": "app-001",
      "Name": "UserService",
      "Version": "2.5.1",
      "OsVersion": "Ubuntu 22.04"
    },
    "Request": {
      "SourceIp": "10.1.2.3",
      "DestinationIp": "10.1.5.10",
      "TraceId": "tr-0e4845e7a483a1891d683addb5a3107b",
      "UserId": "user-999",
      "UserName": "user.name",
      "EntityType": "User",
      "EntityId": "u-648",
      "EntityName": "John Doe",
      "EntityOldValue": "{\"role\":\"viewer\"}",
      "EntityNewValue": "{\"role\":\"admin\"}",
      "Action": "UpdateRole"
    },
    "Response": {
      "Status": "Success",
      "StatusCode": 200,
      "StatusMessage": "Role updated successfully",
      "OSErrorCode": ""
    },
    "Effect": {
      "Message": "Visibility rules applied"
    }
  }
}
```

Once you've verified compatibility, go to the ODC Portal and [configure the audit trail stream](audit-trail-streaming.md#create-an-audit-trail-stream).

## Related resources

* [Stream audit trail logs](audit-trail-streaming.md)

* [Audit trail](audit-trail.md)

* [Allowlisting ODC public IP addresses](../../manage-platform-app-lifecycle/odc-public-ips.md)
