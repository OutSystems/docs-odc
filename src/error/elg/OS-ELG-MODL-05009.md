---
summary: The resource name '<FileName>' provided for the element '<ElementName>' IconResourceName was not found.
tags: c# development, embedded resources
guid: 2b02449a-aa62-4d65-9871-9113efa4c301
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - unblock
---

# OS-ELG-MODL-05009

## Error message

`The resource name '<FileName>' provided for the element '<ElementName>' IconResourceName was not found.`

## Cause

The error occurs because the specified resource name for the element's icon doesn't exist in the project. The `IconResourceName` must be the name of an available embedded resource element in the project.

## Impact

You must fix this error in your C# project before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make sure the icon file exists and the embedded resource name is correctly specified.

For example, suppose you have the following code with an `OSInterface`-decorated interface (`IMyLibrary`), and the icon file name specified doesn't exist:

    [OSInterface(Name = "MyLibrary", Icon = "NonExistentIcon.png")]
    public interface IMyLibrary
    {
        int Add(int a, int b);
    }

To resolve the error, add the correct icon file to the project and update the `IconResourceName` property in the `OSInterface` attribute:

1. Add the correct icon file, for example `MyLibraryIcon.png`, to your project.
1. Set the file's `BuildAction` to `EmbeddedResource`. In Visual Studio, for example, see the [Builds actions documentation](https://learn.microsoft.com/en-us/visualstudio/ide/build-actions?view=vs-2022) for guidance on how to do this.

1. The icon resource name is typically `<default namespace>.<extended namespace>.<filename>`. You can use a decompiler tool to check this.

1. Update the `OSInterface` attribute with the correct icon resource name:

        [OSInterface(Name = "MyLibrary", Icon = "MyNamespace.MyLibraryIcon.png")]
        public interface IMyLibrary
        {
            int Add(int a, int b);
        }

The correct icon resource name is now specified, and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05009).
