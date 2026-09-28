---
summary: OutSystems Developer Cloud (ODC) considerations for connecting to Azure SQL Managed Instances and non-Managed Instances, including Microsoft Entra ID authentication.
tags:
  - Active Directory
  - Authentication
  - External Authentication
  - External Databases
  - Private Gateway
  - Security
  - SQL
guid: 3c907276-4328-4beb-987b-6883ac087fff
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - odc portal
content-type:
  - reference
  - procedure
audience:
  - Developer
  - Platform administrator
coverage-type:
  - apply
isautopublish: true
---

# Azure SQL connection considerations

Review the following considerations for an Azure SQL connection, including Managed Instances, non-Managed Instances, and authenticating with Microsoft Entra ID. For information about creating or editing the connection, refer to [Create connections to external data sources](create-connection-external-data.md).

## Managed instances

Consider the following when you connect to an Azure SQL Managed Instance.

* As a prerequisite, you might need to create a user database following this format: `username@instance-name`. The username can be any value of your choosing. The `instance-name` can be found in your Microsoft Azure SQL environment. The `host` property contains the `instance-name`.

    As an example, if your `host` is `example12345.exampledns.database.windows.net`, the `instance-name` is `example12345`.

* When creating the Azure SQL connection in ODC Portal, insert the same username format (`username@instance-name`) in the username input.
* When creating the Azure SQL connection in ODC Portal, in the Additional Parameters input, you might need to add `encrypt=true;trustServerCertificate=true;`.

## Non-managed instances

Consider the following when you connect to an Azure SQL non-Managed Instance.

* When creating the Azure SQL connection in ODC Portal, use the format `username@instance-name` in the username input.
* When creating the Azure SQL connection in ODC Portal, in the Additional Parameters input, you might need to add `trustServerCertificate=true;`.

## Authenticate with Microsoft Entra ID

The Azure SQL connector supports Microsoft Entra ID (formerly Azure Active Directory) authentication using a Service Principal. This lets you use identity-based access to Azure SQL databases, aligned with your organization's security policies managed through Entra ID.

<div class="info" markdown="1">

This authentication method is not supported when connecting through a Private Gateway.

</div>

You need an active Microsoft Entra ID tenant with permission to register applications. Follow the steps below to set up a Service Principal and configure your connection in ODC Portal:

1. Register an application in Microsoft Entra ID. Follow the instructions in [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal).
1. Create a client secret for the registered application. In the Microsoft documentation, follow Option 3: Create a new client secret. Copy the Secret Value.
1. Note the Client ID of the registered application. You'll need it when configuring the connection in ODC Portal.
1. Link the Service Principal to your Azure SQL database. Follow the instructions in [Connect to Azure SQL with a Service Principal](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-service-principal?view=azuresql#connect-to-azure-%5B%E2%80%A6%5D-service-principal).
1. Configure the connection in ODC Portal. When creating or editing your Azure SQL connection in ODC Portal, set the Username to the Client ID of the Service Principal and the Password to the Secret Value of the client secret. In the Additional Parameters field, add `authentication=ActiveDirectoryServicePrincipal`.
