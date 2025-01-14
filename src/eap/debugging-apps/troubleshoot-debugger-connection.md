---
summary: Explore common issues and solutions for mobile app debugging with OutSystems Developer Cloud (ODC) in this technical guide.
tags: mobile app debugging, connectivity issues, port configuration, android debugging, ios debugging
locale: en-us
guid: e482b9b0-c2f0-4636-8a9f-97aac1755ba6
app_type: mobile apps
figma: https://www.figma.com/file/8RLmb1pp1PYm5xqtrnq5O8/Debugging-apps?type=design&node-id=2901%3A74&t=sdGPdlxTkpCARchu-1
platform-version: odc
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - unblock
---

# Troubleshoot debugger connection

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

When trying to debug a mobile application using Google Chrome or a real device some issues can arise, like a firewall blocking local ports or a device not being discovered by ODC Studio.

Below you can find a list of the most common problems that you may find when you are starting a mobile app debug session, and suggestions for fixing them.

## Issues Related With Unavailable Local Ports

The mobile app debugger feature of ODC Studio requires one or two available local ports according to the debugging target:

When debugging on an Android device or in Google Chrome
:   One available port in the development machine starting at port 9222. If this port is unavailable, ODC Studio checks port 9223, and so on.

When debugging on an iOS device
:   Two available local ports in the development machine starting at port 9221. If this port is unavailable, ODC Studio checks port 9222, and so on.

If there are no available ports because they're in use or they're blocked (for example, by a firewall), you can't debug your mobile app in ODC Studio.

## Issues While Connecting an Android Device

Check the following sections for more information on how to solve these issues:

* [USB/Android Debugging not enabled in device](#usbandroid-debugging-not-enabled-in-device)
* [Device not recognized by Windows](#device-not-recognized-by-windows)
* [Incompatible USB mode selected in device](#incompatible-usb-mode-selected-in-device)
* [USB Debugging was not allowed in device](#usb-debugging-was-not-allowed-in-device)
* [More than one Android device is connected to your PC](#more-than-one-android-device-is-connected-to-your-pc)

### USB/Android Debugging not enabled in device { #usbandroid-debugging-not-enabled-in-device }

For the device to be detected by ODC Studio, you should start by having the USB debugging (or Android Debugging) option enabled.

1. Navigate to the **Developer options** section inside the **Settings** and enable the **USB debugging** option.

    ![Screenshot showing the USB Debugging option enabled in the Developer options section of an Android device settings](images/device-usb-debugging.png "USB Debugging Option")

    **Note:** If you don't have the **Developer options** section in **Settings**, check how to [enable **Developer options**](https://developer.android.com/studio/debug/dev-options.html#enable) on your device.

### Device not recognized by Windows { #device-not-recognized-by-windows }

After ensuring that the USB debugging option is enabled, you should check if the device is detected by Windows and its drivers are correctly installed:

1. Open **Control Panel**.

1. Navigate to the **Hardware and Sound** category.

1. Open **Device Manager**, located under **Devices and Printers**.

1. If your device is listed under **Other devices**, you need to install the correct drivers before proceeding:

    ![Device Manager window showing an Android device listed under Other devices indicating it is not recognized by Windows](images/device-unrecognized.png "Device Not Recognized by Windows")

To help Windows correctly detect the device, follow [this guide](https://developer.android.com/studio/run/oem-usb.html) to install the drivers provided by the manufacturer.

If after following the guide mentioned above Windows still fails to recognize the device properly, try using the drivers provided by Google by taking these steps:

1. Download the [Google USB Driver ZIP file](https://developer.android.com/studio/run/win-usb.html) and extract it (to the Desktop, for example).

1. Right-click on your device and select **Update Driver Software...**.

    ![Context menu with the option to Update Driver Software for an unrecognized Android device](images/device-update-driver.png "Update Driver Software")

1. Choose **Browse my computer for driver software**.

    ![Driver Software update window with the option to Browse my computer for driver software selected](images/device-browse-for-driver.png "Browse Computer for Driver Software")

1. Choose **Let me pick from a list of device drivers on my computer**.

    ![Window prompting to choose a device driver from a list on the computer](images/device-pick-driver-from-list.png "Pick from List of Device Drivers")

1. Select **Show All Devices** and click **Next**.

    ![Device Manager window with the Show All Devices option highlighted](images/device-show-all-devices.png "Show All Devices")

1. Choose the option **Have Disk...**, browse to the `usb_driver` folder located on the extracted folder and click **OK**.

    ![Install From Disk dialog box for selecting the driver to be installed for the Android device](images/device-install-from-disk.png "Install from Disk Option")

1. Select **Android ADB Interface** and click **Next**.

    ![List of device drivers with Android ADB Interface selected for installation](images/device-android-adb-interface.png "Android ADB Interface Selection")

1. Confirm the installation of the driver by pressing **Yes**.

    ![Windows Security warning dialog box during the driver installation process](images/device-driver-warning.png "Windows Security Warning")

1. Install the driver by choosing **Install**.

    ![Prompt window asking for confirmation to install the Android device driver](images/device-driver-install-prompt.png "Driver Installation Prompt")

When the installation completes, press **Close** and check that the device appears in Device Manager:

![Screenshot showing the Android device now recognized in Device Manager after successful driver installation](images/device-install-success.png "Successful Driver Installation")

### Incompatible USB mode selected in device { #incompatible-usb-mode-selected-in-device }

The USB mode which the device is configured to use when connecting to a PC can also cause issues in the device detection process.

Depending on the version of Android and the manufacturer of the device, this option can be in different places.
First of all, check if you have any notification referring to the USB mode, like the ones below:

![Notification on an Android device indicating the current USB mode](images/device-usb-mode-1.png "USB Mode Notification")

![Selection menu for USB mode on an Android device with options such as MTP, PTP, and Camera](images/device-usb-mode-2.png "USB Mode Selection")

![USB configuration options on an Android device with different connection modes](images/device-usb-mode-3.png "USB Configuration Options")

If you find these options, try to switch between them (`MTP`, `PTP` and `Camera` modes), disconnecting and reconnecting the device to the PC, and retrying the device discovery in ODC Studio.


### USB Debugging was not allowed in device { #usb-debugging-was-not-allowed-in-device }

Whenever an Android device is connected to a PC, a request to allow USB Debugging is shown on the device. This request should be accepted so that ODC Studio can communicate with the device.

If you get a pop-up on your device like the one below, just tap **OK** and try again on ODC Studio to detect the device:

![Pop-up on an Android device asking to allow USB Debugging with an OK button](images/device-allow-usb-debugging.png "Allow USB Debugging")

### More than one Android device is connected to your PC { #more-than-one-android-device-is-connected-to-your-pc }

Only one device from each platform (Android/iOS) can be connected to the PC for the device discovery process to run successfully. 

Ensure that you only have one Android device connected to your PC.

## Issues While Connecting an iOS Device

Check the following sections for more information on how to solve these issues:

* [Missing programs and/or libraries](#missing-programs-andor-libraries--missing-programs-andor-libraries)
* [Web Inspector is not enabled on your device](#web-inspector-is-not-enabled-on-your-device)
* [PC is not trusted for debugging](#pc-is-not-trusted-for-debugging)
* [More than one iOS device is connected to your PC](#more-than-one-ios-device-is-connected-to-your-pc)

### Missing programs and/or libraries { #missing-programs-and/or-libraries }

If you are running ODC Studio on Windows, one of the requirements for the debugger to work with iOS devices is to have iTunes installed.

[Download the latest version](https://www.apple.com/itunes/download/) from Apple's website.

**Note**: If you installed iTunes from the Microsoft Store, you must have iTunes running to be able to debug OutSystems mobile apps on iOS devices.

### Web Inspector is not enabled on your device { #web-inspector-is-not-enabled-on-your-device }

To ensure that your device is correctly detected you should make sure that the Web Inspector is enabled. 

Do the following:

1. On your iOS mobile device tap Settings > Safari > Advanced.

1. Make sure that the "Web Inspector" option is turned **on**.

    ![iOS settings showing the Web Inspector toggle turned on under Safari > Advanced](images/ios-web-inspector.png "Web Inspector Toggle")

### Cookies can't be set during a debug session

Server action cannot set cookies during a debug session. When configuring cookies in ODC Studio, ensure the debugger is turned off.

### PC is not trusted for debugging { #pc-is-not-trusted-for-debugging }

The final step to setup your device to be ready for debugging is to trust the PC so it can communicate with the device. To do so, tap **Trust** when the following pop-up appears on your device:

![Pop-up on an iOS device asking to trust the computer with a Trust button](images/device-trust-computer.png "Trust This Computer")

Check [Apple Support](https://support.apple.com/en-us/HT202778) for more information on trusted computers.

### More than one iOS device is connected to your PC { #more-than-one-ios-device-is-connected-to-your-pc }

You can only connect one device from each platform (Android/iOS) to the PC for the device discovery process to run successfully.

Ensure that you only have one iOS device connected to your PC.


## Issues During App Detection by ODC Studio

When starting a new debug session using a device, and after the device has been correctly detected, ODC Studio starts to actively look for the mobile app that you are debugging.

If you find issues during the app detection step (for example, the detection is taking too long), make sure you generated the mobile app with the `Debug` Build Type for Android and `Development` Build Type for iOS.

If your app is still not detected, try performing each of the following steps in your device and check if any of them solves your problem:

* Close all other running OutSystems mobile apps.
* Close any browser app that could be running.
* Close all running apps.
