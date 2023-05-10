---
summary: "The file name '<FileName>' provided for the element '<ElementName>' icon was not found."
tags:
guid: 2b02449a-aa62-4d65-9871-9113efa4c301
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OS-ELG-MODL-05009

## Error message

`The file name '<FileName>' provided for the element '<ElementName>' icon was not found.`

## Cause

The error occurs because the specified file name for the element's icon doesn't exist in the project.

## Impact

You must fix this error before you can publish the external library. Once you've fixed it, you must create and upload a new ZIP file.

## Recommended action

Make sure the icon file exists and the file name is correctly specified. 

For example, suppose you have the following code with an OSInterface-decorated interface (`IMyLibrary`), and the icon file name specified doesn't exist:

    [OSInterface(Name = "MyLibrary", Icon = "NonExistentIcon.png")]
    public interface IMyLibrary
    {
        int Add(int a, int b);
    }

To resolve the error, add the correct icon file to the project and update the `Icon` property in the `OSInterface` attribute:

1. Add the correct icon file, for example `MyLibraryIcon.png`, to your project.
1. Update the `OSInterface` attribute with the correct icon file name:

        [OSInterface(Name = "MyLibrary", Icon = "MyLibraryIcon.png")]
        public interface IMyLibrary
        {
            int Add(int a, int b);
        }

Now the correct icon file is specified and the error should be resolved.

If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ELG-MODL-05009).
