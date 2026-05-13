---
guid: 11d2914f-e5e3-4c58-9334-fe4ae197ee1a
locale: en-us
summary: Configure secure Snowflake connections with key-pair authentication in OutSystems Developer Cloud (ODC), using OpenSSL keys and ODC Portal settings.
figma:
coverage-type:
  - apply
  - unblock
topic:
  - get-data-from-external-db
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Developer
  - Platform administrator
  - Tech lead
tags:
  - Authentication
  - External Databases
  - Private Gateway
  - Security
  - Troubleshooting
outsystems-tools:
  - odc portal
helpids: 30768
isautopublish: true
---
# Snowflake connections in ODC

<div class="info" markdown="1">

Snowflake connection is in Beta. For more information about Beta features, refer to [OutSystems product releases](https://success.outsystems.com/support/release_notes/outsystems_product_releases/#beta). If you want to try this new capability contact your OutSystems account team.

</div>

This guide walks you through connecting OutSystems Developer Cloud (ODC) to Snowflake using key-pair authentication — the recommended authentication method.

## Prerequisites

Before you start, make sure you have the following:

* [OpenSSL](https://www.openssl.org/) installed on your machine.
* Access to a Snowflake account with admin privileges to create users and assign keys.
* Access to the ODC Portal.

## Overview

Snowflake connections in ODC use **key-pair authentication**, which relies on a private/public key pair instead of a username and password. The setup involves three main tasks:

1. Generate a private and public key pair using OpenSSL.
1. Configure a Snowflake user and assign the public key.
1. Enter the connection details in the ODC Portal.

## Step 1: Generate a private key

Open your terminal and run the following command to generate an encrypted private key:

```bash
openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out rsa_key.p8
```

Enter and confirm a **passphrase** when prompted. Save this passphrase securely — you need it when configuring the ODC connection.

## Step 2: Generate a Public Key

Generate the public key from the private key:

```bash
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
```

Store both `rsa_key.p8` (private key) and `rsa_key.pub` (public key) in a secure location, such as a password manager.

## Step 3: Assign the public key to the Snowflake user

In the Snowflake web interface, open `rsa_key.pub` and copy the key content between the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` lines, **excluding** those header/footer lines themselves.

Then run the following SQL, replacing `<public-key-content>` with the copied content:

```sql
ALTER USER <your_user> SET RSA_PUBLIC_KEY='<public-key-content>';
```

## Step 4: Configure the connection in ODC

In the ODC Portal, navigate to your app's connection settings and open the **Setup by stage** panel. Fill in the following fields for each stage (Development, QA, Production):

| Field | Description |
| --- | --- |
| **Host** | Your Snowflake account host, e.g. `<account_id>.snowflakecomputing.com` |
| **Username** | The Snowflake username created in Step 3 |
| **Private key** | The full contents of your `rsa_key.p8` file, including the `-----BEGIN ENCRYPTED PRIVATE KEY-----` and `-----END ENCRYPTED PRIVATE KEY-----` lines |
| **Passphrase** | The passphrase you set when generating the private key in Step 1 |
| **Database** | The name of the Snowflake database to connect to |
| **Schema** | The schema within the database (e.g. `PUBLIC`) |
| **Warehouse** | The Snowflake warehouse to use for query execution |
| **Role** | The Snowflake role assigned to the user |
| **Additional parameters** | Optional. Any extra JDBC connection string parameters |

Once filled in, click **Test connection** to verify the connection is working, then click **Apply to all stages** if you want the same configuration across all environments.

## Known limitations

These are the current limitations when using Snowflake connections in ODC:

* Currently CreateOrUpdateSome operations aren't supported in Snowflake connections.

    This means that when using Snowflake as an external database, you won't be able to use CreateOrUpdateSome to insert or update records in bulk. You can still perform individual Create or Update operations, but bulk insert/update functionality isn't available.

* Private Gateway isn't supported for Snowflake connections.

    This means that you can't use ODC Private Gateway to connect to Snowflake. All connections must be made directly over the internet, so ensure that your Snowflake instance is configured to allow connections from ODC's IP ranges.

## Troubleshooting

| Issue | Possible Cause |
| --- | --- |
| Connection test fails | Incorrect host format, wrong username, or the public key was not assigned correctly in Snowflake |
| Passphrase error | The passphrase entered does not match the one used when generating the private key |
| Permission denied on query | The Snowflake role does not have the required `GRANT` permissions on the target schema or tables |
| Private key format error | Ensure the full PEM content is pasted, including the header and footer lines |

## Further reading

* [Snowflake Key-Pair Authentication Documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth)
* [Snowflake Authentication Methods](https://docs.snowflake.com/en/developer-guide/node-js/nodejs-driver-authenticate)
* [ODC Libraries & Security](https://success.outsystems.com/documentation/outsystems_developer_cloud/outsystems_language_and_elements/libraries/security/)
