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

Testing a SQL server connection can return these errors.

### Wrong username or password

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username}' failed, details: Login failed for user '{username}'. ClientConnectionId:{id}"`

#### Recommended action

Enter the correct username and password.

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

Enter the database name on the server accessible to the user with the specified username.

### Unable to establish a connection to the server

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username}' failed, details: Connection reset ClientConnectionId:{id}"`

#### Recommended action

1. Verify the server address and port number are correct.
1. Verify the status of the server with your IT department. If the server is online, you may need to configure a private gateway to allow connections from ODC to your server. For more information, see [private gateways](../../eap/configuration-management/private-gateway.md).

### No permissions

`"errorMessage": "Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username};database={DatabaseName}' failed, details: Cannot open database \"{DatabaseName}\" requested by the login. The login failed. ClientConnectionId:{id}"`

#### Recommended action

Ask a Server admin to give you access to the database.

### Invalid server certificate

`"errorMessage":"Connection to 'jdbc:sqlserver://{hostname:port};databaseName={DatabaseName};password={******};user={username};loginTimeout=15;trustServerCertificate=false' failed, details: The driver could not establish a secure connection to SQL Server by using Secure Sockets Layer (SSL) encryption. Error: "PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target". ClientConnectionId:{id}"`

#### Recommended action

1. Verify the server address and port number are correct.
1. If the address and port number are correct, as a quick temporary fix, add `trustServerCertificate=true` to the **Additional parameters** input. It's important to contact your IT department to fix the server's certificate.

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

### Wrong username or password

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

Enter the database name on the server accessible to the user with the specified username.

### Unable to establish a connection to the server

`"errorMessage": "Connection to 'jdbc:oracle:thin:{username}/"******"@{hostname:port}' failed, details: IO Error: Connection reset by peer, connect lapse 10004 ms., Authentication lapse 0 ms."`

#### Recommended action

1. Verify the server address and port number are correct.
1. Verify the status of the server with your IT department. If the server is online, you may need to configure a private gateway to allow connections from ODC to your server. For more information, see [private gateways](../../eap/configuration-management/private-gateway.md).

### Invalid connection string syntax

`"errorMessage": "Timed out waiting for test result"`

#### Recommended action

To verify the syntax is correct, refer to [Oracle connection strings](https://www.connectionstrings.com/oracle/).

## SAP OData connection

Testing an SAP OData connection can return these errors.

### Unable to establish a connection to the server

`"errorMessage": "Connection to 'jdbc:cdata:sapgateway:InitiateOAuth=GETANDREFRESH;ConnectOnOpen=true;DataFormat=JSON;URL={serviceUrl};User={username};Password=******;' failed, details: Cannot conclude ssl handshake. Cause: Connection reset."`

#### Recommended action

Verify the status of the SAP server domain with your IT department. If the server is online, you may need to configure a private gateway to allow connections from ODC to your server. For more information, see [private gateways](../../eap/configuration-management/private-gateway.md).

### Wrong username or password

`"errorMessage": "Connection to 'jdbc:cdata:sapgateway:InitiateOAuth=GETANDREFRESH;ConnectOnOpen=true;DataFormat=JSON;URL={ServiceURL};User={username};Password=******;Pagesize=1000;' failed, details: HTTP protocol error. 401 Unauthorized."`

#### Recommended action

Enter the correct username and password.

### Wrong API key

`"errorMessage": "Connection to 'jdbc:cdata:sapgateway:InitiateOAuth=GETANDREFRESH;ConnectOnOpen=true;DataFormat=JSON;URL={ServiceURL};APIKey=******;Pagesize=1000;' failed, details: HTTP protocol error. 401 Unauthorized."`

#### Recommended action

Enter the correct API key.

### Wrong SAP server domain

`"errorMessage": "Connection to 'jdbc:cdata:sapgateway:InitiateOAuth=GETANDREFRESH;ConnectOnOpen=true;DataFormat=JSON;URL={ServiceURL};User={username};Password=******;Pagesize=1000;' failed, details: Invalid HTTP response! System error: UnknownHostException - {SAPServerDomain}: Name or service not known."`

#### Recommended action

1. Enter the SAP server domain without a protocol or path. Use the following examples as guidance.

* Correct: mydevenv.outsystems.com
* Incorrect: https://mydevenv.outsystems.com
* Incorrect: mydevenv.outsystems.com/XE

1. Verify the status of the SAP server domain with your IT department. If the server is online, you may need to configure a private gateway to allow connections from ODC to your server. For more information, see [private gateways](../../eap/configuration-management/private-gateway.md).

### Wrong service URL

`errorMessage: "Connection to 'jdbc:cdata:sapgateway:InitiateOAuth=GETANDREFRESH;ConnectOnOpen=true;DataFormat=JSON;URL={ServiceURL};User={username};Password=******;Pagesize=1000;' failed, details: [/IWFND/MED/170] "en". No service found for namespace '', name '{Service}', version '{Version}'."`

#### Recommended action

Enter the correct Service URL. Make sure it's accessible to the server domain.

### Unable to find the service

`"errorMessage": "Connection to 'jdbc:cdata:sapgateway:InitiateOAuth=GETANDREFRESH;ConnectOnOpen=true;DataFormat=JSON;URL={ServiceURL};User={username};Password=******;Pagesize=1000;' failed, details: [/IWCOR/CX_OD_NOT_FOUND/005****************80FE] The server has not found any resource matching the Data Services Request URI."`

#### Recommended action

Verify the service URL address and port number are correct.

### Unable to retrieve data from the service

`"errorMessage": "Connection to 'jdbc:cdata:sapgateway:InitiateOAuth=GETANDREFRESH;ConnectOnOpen=true;DataFormat=JSON;URL={ServiceURL};User={username};Password=******;Pagesize=1000;' failed, details: [SY/530] "en". No data retrieved from {Service} for entity {EntityName}."`

#### Recommended action

Validate the Service configurations in SAP. Make sure it's available to respond to the request.