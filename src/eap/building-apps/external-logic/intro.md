---
summary: OutSystems Developer Cloud (ODC) supports extending apps with custom .NET code through external logic integration.
helpids: 30485
tags: external libraries, .net integration, custom code, c# development, sdk
locale: en-us
guid: 656e14cb-27b2-433f-835b-2535636e053b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3325-22015&t=cNJuaJIMze8z5Tsy-0
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
  - understand
topic:
  - legacy-systems-integration
---

# Extend your apps with custom code

You can extend your ODC apps with external logic using custom C# code. This is useful for building capabilities in your app where ODC's standard functions and libraries don't fully cover. You can write your C# code in IDEs such as Visual Studio or JetBrains Rider, and use libraries of your choice, whether open-source or private.

Once you build the custom code, ODC apps can consume this C# logic just like [libraries](../../building-apps/libraries/libraries.md) built using OutSystems visual language or [out-of-the-box libraries](../../reference/libraries/intro.md). This means developers using your C# libraries don't need to understand the underlying C# code to use the external logic in their apps. The C# code becomes available in libraries as server actions and structures.

To create new external logic or update existing external logic using C#, follow these steps:

1. [Build the logic](#build-the-external-logic) in C# using the External Libraries Source Software Development Kit (SDK).
1. [Upload and publish the logic](#upload-and-publish-the-external-logic) as an external library using the ODC Portal.
1. [Release the library](#release-the-library) in ODC Portal.
1. [Consume the logic](#consume-the-external-logic) in your apps and libraries using ODC Studio.

<div class="info" markdown="1">

Ensure that you use .NET 8.0 framework to build your external logic in ODC.

</div>

The following diagram illustrates the steps to implement external logic in ODC.

![Diagram illustrating the steps to implement External Logic in OutSystems Developer Cloud](images/extend-your-apps-with-external-logic-diag.png "External Logic Implementation Steps")

## Build the external logic

To build the external logic using custom C# code, you must use the stand-alone tool kit [OutSystems External Libraries SDK](https://www.nuget.org/packages/OutSystems.ExternalLibraries.SDK). This external OutSystems SDK library allows you to decorate your C# code with SDK attributes that map to OutSystems visual language elements. For detailed information, refer to the [SDK documentation](README.md). The SDK documentation provides instructions that guide you through every step, from project creation to packaging your built custom C# code into a ZIP file for upload to the ODC Portal.

You don't need an  ODC organization account to use the SDK.

### Log your custom code

You can also add logging capabilities directly into your custom C# code. To log your custom code and generate detailed logs including informational messages and errors, you must use the [**Microsoft.Extensions.Logging**](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger?view=net-8.0-pp) ILogger interface in your C# code. Additionally, you can create custom spans/activities for distributed tracing to better monitor the performance and behavior of your external logic. For detailed information about how to log your custom code and create spans, refer to [External library SDK README](README.md#build-external-logic-using-sdk).

Once you build and publish the C# code as an ODC external library, the logs in your custom code can be accessed and viewed from the **ODC Portal** just like other [app logs](../../monitor-and-troubleshoot/monitor-apps.md). The logs help you monitor and troubleshoot your external logic effectively and ensure that your custom code behaves as expected.

<div class="info" markdown="1">

Don't use `Console.WriteLine` or similar methods for logging. Console logs aren't visible in the ODC Portal but can be accessed by OutSystems staff in lower level system logs.

Ensure also that logs don't expose sensitive information, such as personal data or credentials, to comply with data protection regulations.

</div>

## Upload and publish the external logic

<div class="info" markdown="1">

To upload and publish your custom code, you need permission to create and change libraries in the ODC Portal. Contact your ODC organization's administrator to obtain the necessary permissions.

</div>

Once you have the ZIP file of the logic created using the OutSystems External Libraries SDK, you must upload and publish it as an external library.

To upload and publish the custom code as an external library, follow these steps:

1. Go to **ODC portal**.

1. Click **Integrate > External Logic**.
A list of pending uploads and published external libraries is displayed.

1. Click **Create library** to create a new external library.

1. Upload the zip file and  click **Continue**.

    If there are errors in the code, click **View errors** to see the full list of errors. You must fix the errors in the C# code before proceeding. For detailed troubleshooting information, refer to [External Libraries SDK errors](../../../error/elg/intro.md). Once you've fixed all the errors, click **Upload other file** to upload the revised ZIP file.

    <div class="info" markdown="1">

    You can get a real-time list of errors while working on your C# code by using the **ODC Custom Code Analyzer**, a community asset (unofficial and unsupported by OutSystems). For detailed information about how to use the extension, refer to [CustomCode-Analyzer readme](https://github.com/jonathanalgar/CustomCode-Analyzer?tab=readme-ov-file#how-to-use). You can get help or share your feedback in the [Community Forum post](https://www.outsystems.com/forums/discussion/100963/odc-external-libraries-custom-code-analyzer/).

    </div>

    When the C# code is error-free, click **Review file contents** to view a list of all  server actions and structures exposed by the external library.

1. Click **Publish library** to publish the library.

    The deployment status screen displays one of the following statuses for the external library:

    * **Running**: The deployment is in progress; please wait for it to finish.

    * **Finished with errors**: The deployment finished, but it wasn't successful. Review the errors. Use the [error page documentation](../../../error/elg/intro.md) for guidance.

    * **Finished successfully**: The deployment finished successfully. Now you can consume the external library in your apps and libraries.

    The external library is initially deployed and published to the Development stage. Once published, it's recommended you test the library in an app before releasing the first stable version. To do this, open the **Version history** tab on the detail page for the library, click the ellipsis next to the release date, and select **Try library in an app**. This launches a test session in ODC Studio, see [Test a revision of a library](../libraries/libraries.md#test-a-revision-of-a-library) for best practices on what type of app to use.

<div class="info" markdown="1">

You can follow the same steps to update and publish an existing external library.

</div>

Once the library is published you must release the library to be used in other ODC apps and libraries.

## Release the library

Release the first version of your library. For detailed information, refer to [Release a new version of a library](../libraries/libraries.md#release-a-new-version-of-a-library).

When an app or library that consumes the external library deploys to another stage, the external library automatically deploys to that stage as well.

## Consume the external logic

Once the library is successfully published and released, the custom C# code becomes available as a library to be consumed across your ODC organization's apps and existing libraries. For detailed information about how to consume the exposed server actions in your apps and libraries using ODC Studio, refer to [Use public elements](../libraries/use-public-elements.md#libraries).

For detailed information about best practices for using the external libraries, refer to [Best practices for using external libraries](best-practices.md).

<div class="info" markdown="1">

The server actions and structures exposed through external libraries are read-only and can't be edited in ODC Studio.

</div>

## Share the external logic

To share an external library outside your organization, submit it to Forge. For detailed information, refer to [Submit assets to Forge](../forge/submit.md). The submission or update process is the same as for any asset developed in OutSystems.

Users outside your organization can [install](../forge/install.md) an external library from Forge the same way they would install any asset developed in OutSystems. Users inside and outside of your organization can use the library from Forge in their apps but can’t edit its external logic in ODC Studio.

## Delete external logic

To delete an external library before it has been published, follow these steps:

1. Go to the ODC Portal.

1. Select **External Logic** to display the list of pending uploads and published external libraries.

1. In the pending uploads list, click **X** next to the external library you want to delete. A confirmation popup appears.

1. Click **Cancel creation**. The list updates.

If you want to delete an external library after its published, the process is similar to deleting an app or library developed in OutSystems. Follow these steps:

1. Go to the ODC Portal.

1. Select **External Logic**  to display the list of pending uploads and published external libraries.

1. To access the library's detail page, click its name in the list of published libraries.

1. Click the ellipsis (3-dots) to the right of the library name, then click the **Delete library**. A confirmation popup appears.

1. Enter the library name and click **Delete library**.

<div class="info" markdown="1">

Deleting an external library impacts consumers that consume the library.

</div>

For more information about deleting published assets, refer to [Deleting apps and libraries](../../deleting-apps/intro.md) for guidance.

## Related resources

* [External libraries SDK README](README.md)

* [External libraries SDK Reference](REFERENCE.md)

* [External libraries SDK templates](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates)
