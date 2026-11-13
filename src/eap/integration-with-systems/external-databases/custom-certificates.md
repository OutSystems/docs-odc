---
summary: Upload private CA or self-signed certificates in ODC Portal so external database connections in OutSystems Developer Cloud (ODC) trust your database server.
tags:
  - Data
  - External Databases
  - SQL
  - Security
  - Troubleshooting
guid: 45e1a707-813e-4651-87ee-2141f62cec76
locale: en-us
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
outsystems-tools:
  - odc portal
content-type:
  - procedure
  - reference
audience:
  - Platform administrator
coverage-type:
  - remember
  - apply
  - unblock
isautopublish: true
---

# Use custom certificates in external database connections

If your database server uses a certificate issued by a private certificate authority (CA) or a self-signed certificate, ODC can't validate the certificate, and the connection fails. To fix this, upload the certificate to the stage in ODC Portal. External database connections in that stage then trust your database server. You don't need to bypass certificate validation with parameters such as `trustServerCertificate=true`.

## Prerequisites

Before you upload a certificate, make sure you have the following:

* The `ManageCertificates` permission for the stage.
* The public certificate of the private CA, or the self-signed certificate of the database server, in PEM format. If the CA uses intermediate certificates, include the full chain.

## Certificate requirements

ODC Portal validates each file when you upload it. The file must meet the following requirements:

* The file is in PEM format.
* The certificate hasn't expired.
* The file doesn't include a private key.
* The file is smaller than 20 KB.

<div class="warning" markdown="1">

Never upload a private key. ODC Portal rejects files that include one.

</div>

## Upload a certificate

To let the external database connections in a stage trust your database server, upload the certificate to that stage. Do the following:

1. In ODC Portal, navigate to **Management** > **Configure** > **Certificates**.
1. Select the stage where the database connections run.
1. Select **Add certificate**.
1. Select the PEM file.
1. Select **Save**.
1. Open the external database connection.
1. Select **Test connection** to confirm that ODC connects to the database.

The certificate applies to all external database connections in the stage. Upload it to each stage that connects to the database server.

## Certificate expiration

The **Certificates** section shows the name and the expiration date of each uploaded certificate. Upload the renewed certificate before the expiration date to avoid connection failures.

## Use the CA bundle of a cloud database provider

Some cloud database providers use their own CA certificates, which ODC doesn't trust by default. For example, Amazon RDS uses a certificate bundle for each AWS Region. Download the bundle from your provider and upload it to the stage like a private CA certificate. For more information about the Amazon RDS certificate bundles, refer to [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html).

## Troubleshoot certificate errors

If a connection fails with a certificate error, check the following:

* The certificate for the database server's CA, or the self-signed certificate, is uploaded to the same stage as the connection.
* The certificate chain is complete, including intermediate certificates.
* The certificate hasn't expired.

## Self-hosted stages

Self-hosted stages support custom certificates in the same way as ODC cloud stages. Upload the certificate in ODC Portal.

## Related resources

For more information about creating the connections that use these certificates, refer to [Create connections to external data sources](create-connection-external-data.md).
