---
summary: Learn how to extend your code using mTLS APIs in OutSystems Developer Cloud (ODC) with a detailed guide on creating and consuming a mTLS service library.
tags: mtls, rest apis, .net development, c# programming, software development kits (sdks)
locale: en-us
guid: e7dd9dd2-dccf-4da1-8eb3-f94dd1982534
app_type: mobile apps, reactive web apps
figma: 
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Supporting mTLS in ODC

Mutual TLS (mTLS) is a way to authenticate the server and the client. It ensures that each side of the communication is what it claims to be verifying that both have the correct certificate information. mTLS is typically used in the zero-trust architecture (ZTA).

You can use mTLS to authenticate your code in OutSystems Developer Cloud (ODC). This document provides an example of creating a library to consume a mTLS REST API in ODC. This article assumes you know C#, .NET, and REST APIs.

For an example of a C# project designed to consume a mTLS rest API, go to [mTLS Project](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/mtls)

## Prerequisites

Ensure you have installed the necessary prerequisites to [extend your apps with external logic](README.md#Prerequisites). Next, launch an integrated development environment (IDE) that supports building .NET projects, such as Visual Studio or Visual Studio Code. Open the extensions marketplace within the IDE and search for the following extensions. Install them once you find them:

* C# (extension id: ms-dotnettools.csharp)
* NuGet Package Manager GUI (extension id: aliasadidev.nugetpackagemanagergui)

In this example, the external tool [NSwag](https://github.com/RicoSuter/NSwag) is used to generate the client code. This tool is used because it's built on C# but there are other tools that also generate C# client code. If you use any other tool please adapt the example instructions to the chosen tool.

### Install .NET tools to create a library

Select the folder in which you want to create your mTLS integration. Create a folder with a descriptive name, such as `how-to-mtls`. Then go to the IDE terminal and enter the following command: `cd path-to/<your-folder>`

1. To add the dependencies, use either the terminal or NuGet Package Manager GUI. Then install the following dependencies:

    * `dotnet add package OutSystems.ExternalLibraries.SDK`
    * `dotnet add package Newtonsoft.Json`

## Consume mTLS API as an external library in ODC

To create a library that consumes a mTLS API, follow this process:

1. [Create OutSystems external library](#create-outsystems-external-library)
1. [Upload the library to ODC Portal](#upload-the-library-to-odc-portal)

## Create OutSystems external library

To create an OutSystems external library that consumes a mTLS API in C#, follow this process:

1. [Set up the project](#set-up-the-project)
1. [Generate the API client code](#generate-the-api-client-code)
1. [Define the interface of the method](#define-the-interface-of-the-method)
1. [Implement the external library code](#implement-the-external-library-code)
1. [Import the image resources](#import-the-image-resources)
1. [Test the custom code](#test-the-custom-code)
1. [Release the mTLS API](#release-the-mtls-api)

### Set up the project

To set up your external library project, follow these steps:

1. To create your library using the class library template, run the following code. Give the project a name, such as `ConsumeMTLSExample`, and select **.NET 8.0 (Long-term support)** as the framework.

    `dotnet new classlib --language "C#" --framework "net8.0" -o ConsumeMTLSExample`

### Generate the API client code

To generate the client code using NSwag, follow these steps:

1. Next to the library project folder created in the last step, create a folder to generate the NSwag client code.

1. Download the swagger file and save it in the working folder. Typically, the swagger file is at the endpoint `https://api.endpoint/swagger/v1/swagger.json`

1. Create a folder named `templates` and download all the template files from this [github repo](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/mtls/resources/nswagtemplates)
    1. `Class.Annotations.liquid` - adds the OSStructure to the library structures.
    1. `Class.Property.Annotations.liquid` - adds the OSStructureField to the properties.
    1. `Class.Property.Annotations.liquid` - creates the properties class as a structure as required by the external logic library.

1. Generate the NSwag client running the following command:

    ```
    nswag openapi2csclient 
          /Input:<api swagger file location>.json 
          /Namespace:<client class namespace>
          /ClassName:<client class name> 
          /ClientBaseClass:<client base class name>
          /Output:<client file output location>.cs
          /UseHttpClientCreationMethod:true
          /GenerateClientInterfaces:true
          /InjectHttpClient:false
          /DisposeHttpClient:true
          /ClientClassAccessModifier:internal
          /ClassStyle: Record
          /DateType: System.DateTime
          /TemplateDirectory:<template files location>
          /AdditionalNamespaceUsages:OutSystems.ExternalLibraries.SDK
    ```

    Example:

    ```
    nswag openapi2csclient 
          /Input:swagger.json 
          /Namespace:MtlsClient
          /ClassName:MtlsClientExample 
          /ClientBaseClass:MtlsHttpClientBase
          /Output:MtlsClientExample.cs
          /UseHttpClientCreationMethod:true
          /GenerateClientInterfaces:true
          /InjectHttpClient:false
          /DisposeHttpClient:true  
          /ClientClassAccessModifier:internal 
          /ClassStyle: Record
          /DateType: System.DateTime
          /TemplateDirectory:templates
          /AdditionalNamespaceUsages:OutSystems.ExternalLibraries.SDK
    ```

1. Copy the generated client code to the external library project.

1. Next to the generated client code file, create a file for the client base class named `<client base class name>.cs`, and add the following code replacing the values used in the command above:

```
// This code needs to be adapted to do the correct mTLS
// validation of the server and authenticate the client
// (send the client certificate)

namespace <client class namespace> {
    internal class <client base class name> {
        private static bool ValidateServerCertificate(
            HttpRequestMessage request, 
            X509Certificate2? certificate, 
            X509Chain? chain, 
            SslPolicyErrors errors) {
                // Perform custom server certificate validation if required
                // Return true if the certificate is trusted, false otherwise
        }
        
        protected async Task<HttpClient> CreateHttpClientAsync(CancellationToken cancellationToken) {
            // Load the client certificate
            X509Certificate2 clientCertificate = new X509Certificate2("path/to/client_certificate.pfx", "certificate_password");
            
            // Create an HttpClient with MTLS authentication
            var httpClient = new HttpClient(new HttpClientHandler {
                ClientCertificateOptions = ClientCertificateOption.Manual,
                SslProtocols = SslProtocols.Tls12,
                ServerCertificateCustomValidationCallback = ValidateServerCertificate,
                ClientCertificates = { clientCertificate }
            });
            return httpClient;
        }
    }
}
```

<div class="warning" markdown="1">

The storage of the certificates and passwords in a secure way is the customer's responsibility.

</div>

<div class="info" markdown="1">

Alternatively, you can use the files [generate_clientcode.ps1](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/mtls/resources/generate_clientcode.ps1) and [MySwaggerConfig.nswag.template](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/mtls/resources/MySwaggerConfig.nswag.template) to run this NSwag command. The way the script generates the client is different as it creates an NSwag configuration file and runs the command with that configuration file. <b>The resulting code is the same</b>. This NSwag configuration file can be opened in the NSwag's GUI for more customizations.

</div>  

<div class="warning" markdown="1">

For more information about the NSwag CLI, go to the [NSwag documentation page](https://github.com/RicoSuter/NSwag/wiki/CommandLine).

</div>

<div class="warning" markdown="1">

At the [mTLS example project](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/mtls/resources) the NSwag templates and config files are examples that can be changed to better comply with any development guidelines. As long as it also complies with OutSystems' custom code [requirements](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_custom_code/external_libraries_sdk_readme/#from-scratch)

</div>

### Define the interface of the method

To define the method interface, follow these steps:

1. Rename the file from `Class1.cs` to `ConsumeMTLSExample.cs`.

1. Add an interface named `ImTLSClient` before the class in the namespace.

    ```
    namespace ConsumeMTLSExample 
    {
        public interface ImTLSClient
        {
            //Define the API's methods contract here
        }
        public class Class1
        {

        }
    }
    ```

1. Add the custom code attributes from the OutSystems External Libraries SDK before the interface.

    ```
    namespace ConsumeMTLSExample 
    {
        /* In this case, the OSInterface attribute provides information about the interface to the ODC,
            which uses this information to create an integration layer with a mTLS API. */
        [OSInterface(Description = "...", IconResourceName = "ConsumeMTLSExample.Resources.mTLSAPI.jpg", Name = "mTLSAPI")]
        public interface ImTLSClient
        {
        }
    }
    ```

1. Inside the interface, add the methods that represent the API's methods.

    ```
    // This method is exposed as a server action to your ODC apps and libraries.
    [OSAction(Description = "Get Weather Forecast for the next 5 days.", ReturnName = "WeatherForecast")]
    ICollection<WeatherForecast> GetWeatherForecast(
        [OSParameter(Description = "Service Base Url.", DataType = OSDataType.Text)] 
        string baseUrl);
    ```

<div class="info" markdown="1">

<ul>
    <li>For reference check the interface generated by NSwag.</li>
    <li>We suggest adding a parameter BaseUrl to all the methods.</li>
</ul>

</div>

### Implement the external library code

To glue the external library interface and the NSwag client code, rename the class `Class1` to `mTLSClient` and the inherit the interface `ImTLSClient`. Implement the methods by calling the NSwag generated client.

```
namespace ConsumeMTLSExample 
{
    ...
    public class mTLSClient : ImTLSClient
    {
        ...
    }
}
```

### Import the image resources

The interface includes icon resources located in the [resources folder of the provided project](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/soap/ConsumeSOAPExample/Resources). To import these resources, follow these steps:

1. After you download the icons into your project, create a new folder and name it `Resources`. Then upload the icons to the **Resource** folder.

1. To add these resources to the project, open **ConsumeMTLSExample.csproj** and add the following code inside the ItemGroup tag:

      ` <EmbeddedResource Include="Resources\SOAP.jpg" /> `

### Test the custom code

To test the custom code and create a C# test project, follow these steps:

1. Create a folder for the test project named `ConsumeMTLSExample.Tests`. The folder structure should look like the following:

    ```
    /your-folder
        ConsumeMTLSExample.sln
        /ConsumeMTLSExample
            Source Files
            ConsumeMTLSExample.csproj
        /ConsumeMTLSExample.Tests
    ```

1. Create the tests project inside the folder by running the following command:

    `dotnet new nunit`

1. On the file `UnitTest.cs` create a method to call each of the API endpoints and test its return (as shown in this example):

    ```
    [Test]
    public void TestGetWeatherForecast()
    {
        mTLSClientExample client = new();
        var weatherForecast = client.GetWeatherForecast(BaseUrl);
        Assert.IsNotNull(weatherForecast);
        Assert.IsTrue(weatherForecast.Count == 5, 
            $"Weather Forecast return the forecast for {weatherForecast.Count} days, expecting 5.");
    }
    ```

### Release the mTLS API

1. Once you finish the code, save the project and publish it. For example, right-click **ConsumeMTLSExample** and select **Open in Terminal**. Run the command,
    ` dotnet publish -c Release `

1. Zip the published output folder (for example, ConsumeMTLSExample > bin > Release > net8.0 > publish) to the root folder of a ZIP file. For example, `ExternalLibrary.zip` is the name of your external library.

## Upload the library to ODC Portal

Once you have the mTLS client zip file, [upload and publish the external logic](intro.md#Upload-and-publish-the-external-logic) in ODC.
