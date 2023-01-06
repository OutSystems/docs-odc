---
summary: Use Microsoft .Net and AWS Lambda to support SOAP in your ODC applications.
tags:
locale: en-us
guid: b44dc63b-99f3-4cc4-9cf0-9e915eddd4fa
app_type: mobile apps, reactive web apps
---

# Supporting SOAP in ODC

Simple Object Access Protocol (SOAP) lets programs that run on different systems to exchange information as XML over HTTP. OutSystems Developer Cloud (ODC) lets you use SOAP by creating a high-code solution. This document provides prerequisites and instructions for AWS.

## Prerequisites

To create a solution that consumes a SOAP web service, you need the following software and components.

On your Windows machine:

* .NET 6.0 SDK with **WCF dotnet-svcutil**
* The latest version of Microsoft Visual Studio Code with the extensions **C#** (ms-dotnettools.csharp) and **AWS ToolKit** (amazonwebservicesaws-toolkit-vscode) or Microsoft Visual Studio

In your AWS account:

* AWS IAM
* AWS Lambda

In your ODC organization:

* **AWS Signature** component from Forge (not supported)

## Resources

You can use the following resources to create a SOAP project.

* The PDF [Consume SOAP web services](resources/consume-soap-services.pdf), with instructions for ODC and AWS
* A [sample ODC file](resources/SOAP-example.oml), that shows how to consume the service 