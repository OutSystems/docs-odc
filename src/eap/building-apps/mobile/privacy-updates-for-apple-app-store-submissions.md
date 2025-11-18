---
summary: Submit apps with a privacy manifest to Apple App Store with approved API justifications, ensuring compliance using OutSystems Developer Cloud (ODC).
tags: apple app store, privacy policy, app submission, api usage, sdk integration
guid: 61a1d08c-3607-4d70-8dcd-5b2e1f7da8a7
locale: en-us
app_type: mobile apps
platform-version: odc
figma: https://www.figma.com/file/B7ap11pZif6ZobXV6HC1xJ/Deploy-your-apps?type=design&node-id=3440%3A34&mode=design&t=sLtP6F4ZsrU6wCQB-1
audience:
  - mobile developers
outsystems-tools:
  - none
coverage-type:
  - apply
  - understand
---
# Privacy updates for Apple App Store submissions

Apps submitted to the Apple App Store must include a privacy manifest file outlining the APIs employed and their purposes. When uploading a new or updated app to App Store Connect, include approved justifications for the APIs used in your code. Furthermore, when integrating a new third-party SDK, follow the API, privacy manifest, and signature requirements specific to that SDK. You must verify that the version employed includes its privacy manifest and note that signatures are compulsory when incorporating it as a binary dependency.

Your app or third-party SDK must declare one or more approved reasons that accurately reflect your use of each of these APIs and the data derived from their use. Use these APIs and their data for the declared reasons only. Ensure that your app's functionality, as presented to users, aligns with these declared reasons and that you don't use the APIs or derived data for tracking.

## Privacy manifest file

You must provide a PrivacyInfo.xcprivacy file in your OutSystems app, where the APIs used are detailed. Provided is a default file that can be used. Ensure you've installed a new app build after adding the privacy manifest file.

     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
     <plist version="1.0">
     <dict>
     <key>NSPrivacyTracking</key>
     <false />
     <key>NSPrivacyTrackingDomains</key>
     <array />
     <key>NSPrivacyCollectedDataTypes</key>
     <array />
     <key>NSPrivacyAccessedAPITypes</key>
     <array>
     <dict>
     <key>NSPrivacyAccessedAPIType</key>
     <string>NSPrivacyAccessedAPICategoryFileTimestamp</string>
     <key>NSPrivacyAccessedAPITypeReasons</key>
     <array>
     <string>C617.1</string>
     </array>
     </dict>
     <dict>
     <key>NSPrivacyAccessedAPIType</key>
     <string>NSPrivacyAccessedAPICategorySystemBootTime</string>
     <key>NSPrivacyAccessedAPITypeReasons</key>
     <array>
     <string>35F9.1</string>
     </array>
     </dict>
     <dict>
     <key>NSPrivacyAccessedAPIType</key>
     <string>NSPrivacyAccessedAPICategoryDiskSpace</string>
     <key>NSPrivacyAccessedAPITypeReasons</key>
     <array>
     <string>E174.1</string>
     </array>
     </dict>
     <dict>
     <key>NSPrivacyAccessedAPIType</key>
     <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
     <key>NSPrivacyAccessedAPITypeReasons</key>
     <array>
     <string>CA92.1</string>
     </array>
     </dict>
     </array>
     </dict>
     </plist>

## Providing a privacy manifest file for a File plugin

When you use a File plugin, you must include a PrivacyInfo.xcprivacy file in your OutSystems app.

The following table contains the required key and recommended reason value for this plugin:

|Key | Recommended reason value | Recommended reason |
|----------|-------------|------|
| [NSPrivacyAccessedAPICategoryFileTimestamp](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api#4278393) | C617.1 | Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container. |
| | 3B52.1 | Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller. |
| [NSPrivacyAccessedAPICategoryDiskSpace](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api#4278397) | E174.1 | Declare this reason to check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users. Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to avoid downloading files from a server when disk space is insufficient. |

### Example privacy manifest file for a File plugin

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    <key>NSPrivacyAccessedAPITypes</key>
    <array>
    <!-- Add this dict entry to the array if the PrivacyInfo file already exists -->
    <dict>
    <key>NSPrivacyAccessedAPIType</key>
    <string>NSPrivacyAccessedAPICategoryFileTimestamp</string>
    <key>NSPrivacyAccessedAPITypeReasons</key>
    <array>
    <string>C617.1</string>
    <string>3B52.1</string>
    </array>
    </dict>
    <dict>
    <key>NSPrivacyAccessedAPIType</key>
    <string>NSPrivacyAccessedAPICategoryDiskSpace</string>
    <key>NSPrivacyAccessedAPITypeReasons</key>
    <array>
    <string>E174.1</string>
    </array>
    </dict>
    </array>
    </dict>
    </plist>

## Providing a privacy manifest file in ODC

To create a binary setting in the browser, follow these steps:

1. In ODC Studio, navigate to **App > Edit app properties > Extensibility**.

1. Right-click **Extensibility Settings**, click **Add Extensibility Setting**.
   For detailed information about using extensibility settings, refer to [Configuring mobile apps](../../building-apps/mobile/configuring-mobile-apps.md#configure-extensibility-settings-configure-extensibility-settings).

2. Name your file similar to "PrivacyInfoFile” and ensure the **Data Type** is set to `Binary Data` and **Publish**.

3. In the portal, navigate to **Apps,** and select your app.

4. Navigate to **Mobile distribution** and select **Extensibility settings**.

5. On the **"PrivacyInfoFile"** dropdown list, select **Edit**.

    ![Screenshot of the ODC portal highlighting the PrivacyInfoFile setting with an Edit option.](images/edit-privacy-setting-pl.png "Editing Privacy Info File in ODC Portal")

6. Upload your PrivacyInfo.xcprivacy file and **Save**.

In ODC Studio, to configure your Extensibility Configurations:

1. Select **Edit app properties** > **Extensibility**.

1. Add the following entry:

    ```
    {
        "buildConfigurations": {
            "resources": {
                "ios": [
                    {
                        "source": "$extensibilitySettings.PrivacyInfoFile",
                        "target": "PrivacyInfo.xcprivacy"
                    }
                ]
            }
        },
        "resources": {
            "ios": {
                "PrivacyInfoFile": {
                    "src": $extensibilitySettings.PrivacyInfoFile,
                    "target": "PrivacyInfo.xcprivacy"
                }
            }
        }
    }
    ```

1. The name of the object property inside `ios` and `src` must match the name of the setting. `Target` must be set to `PrivacyInfo.xcprivacy`.

1. Both `buildConfigurations.resources.ios` is necessary for building Capacitor applications and `resources.ios.PrivacyInfoFile` is necessary for building Cordova apps.  You can specify both, as in the example.
