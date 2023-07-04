---
summary: Solving errors returned when testing a Server connection
tags:
guid: 8e453a94-9438-4613-ae63-ef702970fd77
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OS-INTC-60007

## SQL Server connection  

Testing a SQL Server connection can return these errors.

### Wrong Username or password

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username}' failed, details: Login failed for user '{username}'. ClientConnectionId:{id}"`

#### Recommended action

Enter the correct username and pasword.

### Wrong server/hostname

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={osdemo}' failed, details: The TCP/IP connection to the host {hostname:port}, port {port} has failed. Error: \"{hostname}. Verify the connection properties. Make sure that an instance of SQL Server is running on the host and accepting TCP/IP connections at the port. Make sure that TCP connections to the port are not blocked by a firewall.\"."`

#### Recommended action

Input the correct environment server/hostname without a protocol or path. Use the following examples as guidance.

* Correct: mydevenv.outsystems.com
* Incorrect: https://mydevenv.outsystems.com
* Incorrect: mydevenv.outsystems.com/XE

### Wrong database

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={osdemo}' failed, details: Cannot open database \"{DatabaseName}\" requested by the login. The login failed. ClientConnectionId:{id}"`

#### Recommended action

Enter the database name on the server. Make sure it's accessible to the user with the username.

### Unable to establish a connection to the server

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username}' failed, details: Connection reset ClientConnectionId:{id}"`

#### Recommended action

1. Verify the server address and port number are correct.
1. Verify the status of the server with your IT department. If the server is online, you may need to configure a secure gateway to allow connections from ODC to your server. For more information, see [secure gateways](https://success.outsystems.com/documentation/outsystems_developer_cloud/configuration_management/configure_a_secure_gateway_to_your_private_network/).

### No permissions

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username};database={DatabaseName}' failed, details: Cannot open database \"{DatabaseName}\" requested by the login. The login failed. ClientConnectionId:{id}"`

#### Recommended action

Ask a Server admin to give you access to the database.

### Invalid server certificate

`"errorMessage":"Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username};loginTimeout=15;trustServerCertificate=false' failed, details: The driver could not establish a secure connection to SQL Server by using Secure Sockets Layer (SSL) encryption. Error: "PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target". ClientConnectionId:{id}"`

#### Recommended action

1. Verify the server address and port number are correct.
1. If the address and port number are correct, an as a quick temporary fix, add `trustServerCertificate=true` to the **Additional parameters** input. It's important to contact your IT IT department to fix the server’s certificate.

### Invalid connection string syntax

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username}' failed, details: The connection string contains a badly formed name or value."`

#### Recommended action

The configuration added to the **Additional parameters** is not correct. To verify the syntax is correct, refer to [SQL Server connection strings](https://www.connectionstrings.com/sql-server/).

### Invalid connection string parameter value

#### When it's a boolean parameter

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username};trustServerCertificate=wrong' failed, details: The property trustServerCertificate does not contain a valid boolean value. Only true or false can be used."`

##### Recommended action

Set the value of a boolean parameter on the Additional parameters input as either “true” or “false”.

#### When it’s not a boolean parameter

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username};database=Restricte' failed, details: Cannot open database \"Restricte\" requested by the login. The login failed. ClientConnectionId:{id}"`

##### Recommended action

Assign valid values to the parameters entered on the **Additional parameters** input.

## Oracle Server connection

Testing an Oracle Server connection can return these errors.

### Wrong Username or password

`"errorMessage": "Connection to 'jdbc:oracle:thin:{username}/"******"@{hostname:port}/{ServiceName}?Pooling=false' failed, details: ORA-01017: invalid username/password; logon denied"`

#### Recommended action

Enter the correct username and password.

### Wrong server/hostname name

`"errorMessage": "Connection to 'jdbc:oracle:thin:{username}/"******"@{hostname:port}/{ServiceName}?Pooling=false' failed, details: IO Error: The Network Adapter could not establish the connection (CONNECTION_ID={id})"`

#### Recommended action

Enter the correct environment server/hostname without a protocol or path. Use the following examples as guidance.

* Correct: mydevenv.outsystems.com
* Incorrect: https://mydevenv.outsystems.com
* Incorrect: mydevenv.outsystems.com/XE

### Wrong database

`errorMessage: "Connection to 'jdbc:oracle:thin:{username}/"******"@{hostname:port}/{ServiceName}?Pooling=false' failed, details: Listener refused the connection with the following error: ORA-12514, TNS:listener does not currently know of service requested in connect descriptor (CONNECTION_ID={id})"`

#### Recommended action

Enter the database name on the server that's accessible to the user with the specified username.

### Unable to establish a connection to the server

`"errorMessage": "Connection to 'jdbc:oracle:thin:{username}/"******"@{hostname:port}' failed, details: IO Error: Connection reset by peer, connect lapse 10004 ms., Authentication lapse 0 ms."`

#### Recommended action

1. Verify the server address and port number are correct.
1. Verify the status of the server with your IT department. If the server is online, you may need to configure a secure gateway to allow connections from ODC to your server. For more information, see [secure gateways](https://success.outsystems.com/documentation/outsystems_developer_cloud/configuration_management/configure_a_secure_gateway_to_your_private_network/).

### Invalid connection string syntax

`"errorMessage": "Timed out waiting for test result"`

#### Recommended action

To verify the syntax is correct, refer to [Oracle connection strings](https://www.connectionstrings.com/oracle/).