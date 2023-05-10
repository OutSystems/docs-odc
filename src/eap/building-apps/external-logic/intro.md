---
summary: The article describes how to use the External Logic feature in OutSystems Developer Cloud (ODC) to extend apps with custom code, specifically C#.
tags:
locale: en-us
guid: 656e14cb-27b2-433f-835b-2535636e053b
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Extend your apps with external logic

You can use External Logic when you need to extend OutSystems Developer Cloud (ODC) apps with custom code (C#). This lets you extend apps to cover use cases that can't be fully covered using the built-in functions and out-of-the-box libraries bundled with ODC. Along with writing your own C# code in IDEs such as Visual Studio or Jet Brains Rider, you can use open-source .NET libraries.

Your apps consume logic built in C# the same way they consume logic from libraries built in the OutSystems visual language or [out-of-the-box libraries](../../reference/libraries/intro.md). This means OutSystems developers consuming those libraries don't need to understand the underlying C# code to use external logic in their apps. The C# code becomes available in libraries as server actions and structures.

When you want to create new external logic or update existing external logic, follow these steps:

1. Build the logic in C# using the External Libraries Source Software Development Kit (SDK).
2. Upload and publish the logic as an external library using the ODC Portal.
3. Consume the logic in your apps and libraries built in OutSystems using ODC Studio.

![External Logic steps](images/extend-apps-with-external-logic-diag.png "External Logic steps")

## Build the external logic

The OutSystems External Libraries SDK is a stand-alone kit for building logic in C# that you can expose to ODC apps.

Because it's a stand-alone kit, the C# developer doesn't need an ODC organization account to use it.

The [documentation for the SDK](README.md) guides the C# developer through from creating the project to packaging the built logic into a ZIP file ready to upload to the ODC Portal. The C# developer can upload the ZIP file to the ODC Portal themselves (if they have an ODC organization account) or share it with a colleague.

## Upload and publish the external logic

<div class="info" markdown="1">

To complete this step you need permission to create and change libraries in the ODC Portal. To get the necessary permissions, speak to an administrator from your ODC organization.

</div>

Once you have the ZIP file of the logic created using the OutSystems External Libraries SDK, you need to upload and publish it as an external library.

To do this, select **External Logic** from the left nav menu in the ODC Portal to open the External Logic screen. You see a list of pending uploads and published external libraries. Now follow this procedure.

1. Click the:

    * **Create library** button to create a new external library. 
    * **Upload new revision** button within the detail page of the external library to update an existing external library. You access the detail page by clicking the library name in the list of published external libraries.

    In both cases the **Upload file** screen displays.

1. Click the **Upload file** button to browse for the ZIP file or drag and drop it to the labeled area. The ZIP file must be less than 90MB. Then click **Continue**.

    A spinning wheel shows the status of the file upload and inspection process. You can continue working on other tasks in the ODC Portal during the process.

    <div class="info" markdown="1">

    If there are errors in the code, the **View errors** button displays. Click the button to see the full list of errors. You must fix the errors in the C# code before you can proceed. Use the [error page documentation](../../../error/elg/intro.md) for guidance. Once you've fixed all the errors, click **Upload other file** button to upload the revised ZIP file.

    </div>

1. When the C# code is error-free, the **Review file contents** button displays. Click the button to see a full list of all the server actions and structures exposed through the generated external library. When ready to start the publish process click the **Publish library** button (displays for new library) or **Publish revision** button (displays for updated library).

1. The deployment status screen displays. The deployment status of the external library is one of the following:

    * **Running**: the deployment is in progress; please wait for it to finish.
    * **Finished with errors**: the deployment has finished, but it wasn't successful. Review the errors. Use the [error page documentation](../../../error/elg/intro.md) for guidance.
    * **Finished successfully**: the deployment finished successfully. The external library is available to consume in your apps and libraries built in OutSystems.

The external library is initially deployed to the Development stage. When an app or library that consumes the external library is deployed to another stage, the external library is automatically deployed to that stage as well.

## Consume the external logic

Once successfully published, the external logic becomes available in a library to consume across your ODC organization's apps and existing libraries. To learn how to consume the exposed server actions in your apps and libraries using ODC Studio, see [Use public elements](../use-public-elements.md#libraries).

<div class="info" markdown="1">

The server actions and structures exposed through external libraries are read-only and can't be edited in ODC Studio.

</div>

## Share the external logic

You can share an external library outside your organization by submitting it to Forge. You follow the same process to [submit or update](../../forge/submit.md) an external library to Forge as for an asset developed in OutSystems.

Users outside your organization follow the same process to [install](../../forge/install.md) an external library as for an asset developed in OutSystems. As with users in your organization, users who consume the external library from Forge can't edit the external logic in ODC Studio.

## Delete external logic

Before an external library is published, it should be deleted using the **External Logic** screen:

1. Access the detail page of the library by clicking its name in the list of published libraries.
1. Click the ellipsis icon to the right of the library name, then click the **Delete library** button.

Once published, you must delete an external library like an app or library developed in OutSystems. See [Deleting apps and libraries](../../building-apps/deleting-apps/intro.md) for guidance.
