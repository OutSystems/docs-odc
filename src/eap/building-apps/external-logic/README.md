---
summary: OutSystems Developer Cloud (ODC) External Libraries SDK enables the extension of ODC apps with custom .NET code.
tags: .net integration, custom code extension
locale: en-us
guid: 955feaca-cda0-492f-9b84-d5c89281692e
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3606%3A22095&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - evaluate
  - remember
  - unblock
topic:
  - legacy-systems-integration
---

# External libraries SDK README

The OutSystems External Libraries SDK allows you extend your ODC apps with custom C# code. The SDK supports modern .NET 8.0+ and integrates with your preferred IDE.

You decorate your C# code with SDK attributes that map directly to OutSystems visual language elements. This means you can expose your custom C# code as an ODC external library with reusable server actions and structures and use it across any ODC app. For detailed information, refer to [Extend your apps with custom code](intro.md).

For building your custom code, you can either start from [scratch](#build-external-logic-from-scratch) or accelerate development by using ready-made [templates](#build-external-logic-using-templates). 

Once you build and package your external code, you can upload it to the ODC Portal and make it available as an external ODC library.

## Prerequisites

* [.NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) installed.

* [NuGet](https://www.nuget.org/downloads) package manager installed.

* An IDE that supports building .NET projects. For example, Visual Studio, Visual Studio Code, or Jet Brains Rider.

* Basic knowledge of C# programming concepts.

## Build external logic using SDK

You can start developing external logic for an ODC app from scratch or using one of the provided templates.

### Build external logic from scratch

To build external logic with C# using Microsoft Visual Studio 2022 with .NET 8.0, follow these steps: 

1. From the **Create a new project** window select the **Class Library** template.

1. Give the project a name, for example `ClassLibrary1`. You must select **.NET 8.0 (Long-term support)** as the framework. Click **Create**.

1. From the **Solution Explorer** pane, right-click the project name and select **Manage NuGet packages...** Search for and install `OutSystems.ExternalLibraries.SDK`. If you want to enable logging in your C# code, install `Microsoft.Extensions.Logging` version 8.0.0. For tracing functionality, `System.Diagnostics` is part of the standard .NET library and is available by default.

1. Create a public interface containing the methods you want to expose as server actions to your ODC apps and libraries. Then decorate it with the `OSInterface` attribute. 

        using OutSystems.ExternalLibraries.SDK;

        namespace MyCompany
        {
            [OSInterface]
            public interface IMyLibrary
            {
                string SayHello(string name, string title);
                string SayGoodbye(string name);
            }
        }

1. Create a public class implementing that interface. Optionally for logging your code, use [Microsoft Extension ILogger Interface](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger?view=net-8.0-pp). These logs can then be accessed from the ODC portal. You can also create custom spans/activities for distributed tracing by using the current activity source to monitor the performance and behavior of your external logic.

Here's an example of a class that uses Microsoft Extension ILogger Interface to log the code and creates custom spans for tracing. 

        using Microsoft.Extensions.Logging;
        using System.Diagnostics;

        namespace MyCompany
        {
            public class MyLibrary : IMyLibrary
            {
                private readonly ILogger _logger;

                public MyLibrary(ILogger logger)
                {
                    _logger = logger;
                }

                public string SayHello(string name, string title = "Mr./Ms.")
                {
                    using var activity = Activity.Current?.Source.StartActivity("MyLibrary.SayHello");
                    _logger.LogInformation($"Saying hello to {name} with title {title}");
                    return $"Hello, {title} {name}";
                }

                public string SayGoodbye(string name)
                {
                    using var activity = Activity.Current?.Source.StartActivity("MyLibrary.SayGoodbye");
                    _logger.LogInformation($"Saying goodbye to {name}");
                    return $"Goodbye, {name}";
                }
            }
        }
 
The exposed methods can only have:

* Basic .NET types: `string`, `int`, `long`, `bool`, `byte[]`, `decimal`, `float`, `double`, `DateTime`.
* Structs decorated with the `OSStructure` attribute.
* Lists (any type inheriting from [IEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable)) of any of the previous two types.

<div class="info" markdown="1">

You can expose a server action using external code with optional parameters by adding a default value to the parameter in the action definition. In the above example, the `title` parameter is optional and has a default value "Mr./Ms.".

</div>

### Add tracing to your custom code

To create custom spans for distributed tracing in your external logic, use `Activity.Current?.Source.StartActivity()` to access the current activity source. This allows you to monitor the performance and behavior of your external logic operations within the ODC request trace.

When creating spans:

* Use descriptive names that indicate the operation being performed (e.g., "Iban.Parse", "MyLibrary.SayHello")
* Wrap the span creation in a `using` statement to ensure proper disposal
* The span will automatically be included in the distributed trace when your external logic is called from ODC apps

Here's an example based on the IBAN checker template:

        public Structures.Iban Parse(string value)
        {
            using var activity = Activity.Current?.Source.StartActivity("Iban.Parse");
            _logger.LogInformation("Parsing IBAN: {IbanValue}", value);
            return new Structures.Iban(_parser.Parse(value));
        }

This approach provides detailed tracing information that helps with monitoring and troubleshooting your external logic within the broader ODC application context.

For detailed information about errors, refer to [External libraries SDK errors](../../../error/elg/intro.md).

1. Once the code is successfully built, save the project and publish it. 

    To publish the code follow these steps:

    1. Right-click **{NAME_OF_SOLUTION}** and click **Open in Terminal**. 

    2. Execute `dotnet publish -c Release -r --no-self-contained`

        The published code runs in a Linux container. If your library has runtime-specific dependencies then you should publish it specifying the runtime: 
        `dotnet publish -c Release linux-x64 --no-self-contained`

1. Zip the contents of the publish output folder to the root of a ZIP file. 
     * For a cross-platform publish, the folder path is `./{NAME_OF_SOLUTION}/bin/Release/net8.0/publish/*`. 
     * For a `linux-x64` runtime-specific publish, the folder path is `./{NAME_OF_SOLUTION}/bin/Release/net8.0/linux-x64/publish/*`. 
          
1. Upload the ZIP file to the ODC Portal. For detailed information, refer to [Extend your apps with custom code](intro.md#upload-and-publish-the-external-logic).

Once the external code is published and uploaded in ODC portal, you must
create an external ODC library, publish, and release the library. For detailed information, refer to [Upload and publish the external logic](intro.md#upload-and-publish-the-external-logic). Once the external library is [released](intro.md#release-the-library), you can [consume the external logic](intro.md#consume-the-external-logic) across your ODC organization's apps and existing libraries.

For detailed information about best practices, refer to [Best practices for using external libraries](best-practices.md).

### Build external logic using templates

You can also get started building external logic for your OutSystems apps by using ready-made [templates](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates) that leverage the OutSystems External Libraries SDK. You can choose from a [basic](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/basic) or [advanced](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/advanced) template, both designed to help you implement custom C# code and expose it to your apps. 

The basic template covers simple use case for checking the validity of your International Bank Account Number (IBAN), while the advanced template includes complex use cases for IBAN validation. You can download a template, open it in your IDE, and adapt the code to fit your requirements saving you time and effort as you extend your app’s capabilities.

#### Using basic IBAN checker template 

1. Download and unzip the [basic template file from the SDK GitHub repository](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/blob/main/basic_template.zip).

1. Load the C# project file, `OutSystems.IbanChecker.csproj`, using a supported IDE.

    The following files are available in the project:

    * **IIbanChecker.cs**: Defines a public interface named `IIbanChecker`, decorated with the `OSInterface` attribute. The interface has a single method named `Parse`, which takes an IBAN string value as input and returns an `Iban` struct. `Parse` is exposed as a server action to your ODC apps and libraries.

    * **IbanChecker.cs**: Defines a public class named `IbanChecker` that implements the `IIbanChecker` interface. The class is a convenient wrapper for the `IbanNet` library, an [open-source library](https://github.com/skwasjer/IbanNet) that provides functionality for parsing and validating IBANs. The class has a private field named `_parser`, which is an instance of the `IIbanParser` interface.

    * **Iban.cs** Defines a struct named `Iban`, decorated with the `OSStructure` attribute. The struct has four public properties: `Country`, `Bban`, `BankIdentifier`, and `BranchIdentifier`. `Iban` is exposed as a structure to your ODC apps and libraries.

    UML diagram:

    ![Basic UML diagram](images/sdk-readme-basic-uml-diag.png "Basic UML diagram")

1. Edit the code to meet your use case. If your project requires unit tests, modify the examples found in `../OutSystems.IbanChecker.UnitTests/IbanCheckerTests.cs` accordingly.

1. Run the Powershell script `generate_upload_package.ps1` to generate `ExternalLibrary.zip`. Rename as required.

For detailed information about errors, refer to [External libraries SDK errors](../../../error/elg/intro.md).

2. Upload the generated ZIP file to the ODC Portal. For detailed information, refer to [Extend your apps with custom code](intro.md#upload-and-publish-the-external-logic).

Once the external code is published and uploaded in ODC portal, you must
create an external ODC library, publish, and release the library. For detailed information, refer to [Upload and publish the external logic](intro.md#upload-and-publish-the-external-logic). Once the external library is [released](intro.md#release-the-library), you can [consume the external logic](intro.md#consume-the-external-logic) across your ODC organization's apps and existing libraries.

For detailed information about best practices, refer to [Best practices for using external libraries](best-practices.md).


#### Using advanced IBAN checker template

1. Download and unzip the [advanced template file from the GitHub repository](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/blob/main/advanced_template.zip).

1. Load the C# project file, `OutSystems.IbanChecker.csproj`, using a supported IDE.

    Files in the project:

     * **IIbanChecker.cs**: Defines a public interface named `IIbanChecker` decorated with the `OSInterface` attribute. The interface has four methods:
    
        * `Parse`: Takes an IBAN string as input and returns an `Iban` struct.
        * `TryParse`: Attempts to parse an IBAN string as input and returns a boolean success indicator along with the parsed `Iban` struct.
        * `Validate`: Takes an IBAN string as input as checks it against a specific rule and a list of rejected countries.
        * `Format`: Takes an `Iban` struct and an optional format string as input and returns a formatted string representation of the IBAN.

        Each method is exposed as a server action to your ODC apps and libraries.

    * **IbanChecker.cs**: Defines a public class named `IbanChecker` that implements the `IIbanChecker` interface. The class is a convenient wrapper for the `IbanNet` library, an [open-source library](https://github.com/skwasjer/IbanNet) that provides functionality for parsing and validating IBANs. The class contains private fields `_parser` and `_validator`, which are instances of the `IIbanParser` and `IIbanValidator` interfaces. The constructor initializes these instances for use in the class methods.

    * **Structures/Iban.cs** Defines a struct named `Iban`, decorated with the `OSStructure` attribute. The struct has four public properties: `Country`, `Bban`, `BankIdentifier`, and `BranchIdentifier`. It's exposed as a structure to your ODC apps and libraries.

    * **Structures/IbanCountry.cs** Defines a struct named `IbanCountry`, decorated with the `OSStructure` attribute. The struct has five public properties: `TwoLetterISORegionName`, `DisplayName`, `NativeName`, `EnglishName`, and `DomesticAccountNumberExample`. It's exposed as a structure to your ODC apps and libraries.

    * **Structures/ValidationResult.cs** Defines a struct named `ValidationResult`, decorated with the `OSStructure` attribute. The struct has three public properties: `AttemptedValue`, `Country`, and `Error`. It's exposed as a structure to your ODC apps and libraries.

    * **CustomRules/RejectedCountriesRule.cs**: Defines a custom IBAN validation rule, `RejectCountryRule`, to reject specified country codes. It also defines an associated error result class, `CountryNotAcceptedError`, for handling rejected countries.

1. Edit the code to meet your use case. If your project requires unit tests, modify the examples found in `../OutSystems.IbanChecker.UnitTests/IbanCheckerTests.cs` accordingly.

1. Run the Powershell script `generate_upload_package.ps1` to generate `ExternalLibrary.zip`. Rename as required.

For detailed information about errors, refer to [External libraries SDK errors](../../../error/elg/intro.md).

2. Upload the generated ZIP file to the ODC Portal. For detailed information, refer to [Extend your apps with custom code](intro.md#upload-and-publish-the-external-logic).

Once the external code is published and uploaded in ODC portal, you must
create an external ODC library, publish, and release the library. For detailed information, refer to [Upload and publish the external logic](intro.md#upload-and-publish-the-external-logic). Once the external library is [released](intro.md#release-the-library), you can [consume the external logic](intro.md#consume-the-external-logic) across your ODC organization's apps and existing libraries.

For detailed information about best practices, refer to [Best practices for using external libraries](best-practices.md).

## Reference

The table below maps the .NET attributes exposed by the SDK to the corresponding OutSystems elements. Click the link embedded link for further information.

| .NET attribute | OutSystems element | .NET attribute property _(OutSystems element property)_ |
| --- | --- | --- |
| [`[OSInterface]`](REFERENCE.md#osinterfaceattribute-type) | External library | Name _(Name)_<br></br>Description _(Description)_<br></br>IconResourceName _(Icon)_<br></br>OriginalName _(Source name used for key calculation)_
| [`[OSAction]`](REFERENCE.md#osactionattribute-type) | Server action | Description _(Description)_ <br></br>IconResourceName _(Icon)_<br></br>ReturnType _(Output parameter type)_<br></br>ReturnName _(Output parameter name)_<br></br>OriginalName _(Source name used for key calculation)_ |
| [`[OSParameter]`](REFERENCE.md#osparameterattribute-type) | Input/output parameter | DataType _(DataType)_<br></br>Description _(Description)_<br></br>OriginalName _(Source name used for key calculation)_ |
| [`[OSStructure]`](REFERENCE.md#osstructureattribute-type) | Structure | Description _(Description)_<br></br>OriginalName _([Source Name used for the key calculation])_ |
| [`[OSStructureField]`](REFERENCE.md#osstructurefieldattribute-type) | Structure attribute | DataType _(DataType)_<br></br>Description _(Description)_<br></br>Length (Length)<br></br>Decimals _(Decimals)_<br></br>IsMandatory _(IsMandatory)_<br></br>OriginalName _(Source name used for key calculation)_ |
| [`[OSIgnore]`](REFERENCE.md#osignore-type)  |   | Use to decorate a public property/field within a .NET struct decorated with to specify that _it shouldn't be exposed as an OutSystems Structure Attribute._   |

## Troubleshooting

All validation of your external logic is done when [uploading the ZIP file to the Portal](intro.md#upload-and-publish-the-external-logic).

For detailed information about errors, refer to [External libraries SDK errors](../../../error/elg/intro.md).

## Related resources

* [Extend your apps with custom code](intro.md)

* [External libraries SDK Reference](REFERENCE.md)

* [Best practices for using external libraries](best-practices.md)
