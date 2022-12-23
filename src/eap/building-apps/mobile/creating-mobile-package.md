---
summary: How to create a mobile package for distribution in app stores.
tags:
locale: en-us
guid: 4e816fa7-fffc-48c4-b205-13f7165d3775
app_type: mobile apps
---

# Create mobile app package

After you can create a mobile app in ODC (OutSystems Developer Cloud) Studio, you can create a mobile app package in ODC Portal. The following list describes the overall process of making your app available for users: 

1. Develop your app. You can quickly preview your app in a browser as you develop. 
1. Try your app on a mobile device by creating a debug package for installation.  
1. Create your production mobile package.
1. Distribute your app by submitting it as a package to an app store or sharing it internally for a direct download.

<div class="warning" markdown="1">

Avoid changing the app name, due to [a know issue in the product](../../known-issues/intro.md#changing-app-name).

</div>

## Creating an iOS or Android Package

Go to ODC Portal and in the app details page, click **Mobile distribution**. To create a package click **Create package**. From the same screen, you can create an iOS or Android package. The two packages can process at the same time. Once you click the **Create Package** button, the ODC Portal displays a screen for you to provide configuration information. On first use, ODC Portal prefills some iOS and Android configuration fields for you.

Once the creation of the package completes, the display shows you the date and time it was last created, who created it, and a link to download the package. The page also shows the PWA QR code, information about the version, build type, and app identifier.  

To configure a package, you can use the default settings or enter information specific to your package. The required fields have an asterisk. The following sections contain a list of the fields to complete along with a short description.

## iOS package

Settings for creating an iOS package.

* **Build type** - the way you want to distribute this mobile package such as a stage, the app store or in-house for testing purposes
* **App identifier** - a unique identifier for your app in stores
* **Certificate** - authentication used in Apple’s iOS developer program
* **Certificate password** - the password to use for the authentication process
* **Provisioning profile** - the profile that matches the certificate
* **Mobile Apps Build Service (MABS) version** - a cloud service used by ODC to generate your packages
* **Version (Major, Minor, Patch)** - the ODC Portal suggests a version number, but you can enter any version number, that's equal to or higher than the previous version
* **Version code** - a number that increments by one every time MABS generates a new package. You can change this number, but it must be higher than the previous version

## Android package

Settings for creating an Android package.

* **Build type** - the way you want to distribute this mobile package such as a stage, a Google Play (app bundle), debug, or release
* **App identifier / Keystore details** - a unique identifier for your app in stores and Keystore details
* **Mobile Apps Build Service (MABS) version**  - a cloud service used by ODC to generate your package
* **Version (Major, Minor, Patch)** - ODC Portal suggests a version number, but you can enter any version number that's equal to or higher than the previous version
* **Version code** - a number that increments by one every time MABS generates a new package. You can change this number, but it must be higher than the previous version.

## App versions and MABS

ODC uses OutSystems **Mobile App Build Service (MABS)**. MABS is a cloud service that generates mobile packages. OutSystems continually improves MABS and makes new versions available. On the create package page, you can select the MABS version you want to use to create the mobile packages. ODC Portal records the MABS version you chose to generate the mobile package.  

The mobile package includes a version code field that's different from the app version. A version code is an internal number associated with the current code being used to create the mobile package. App stores use this number to determine whether one version is more recent than another version. By default, the version code increments by one every time MABS creates a mobile app package. The version of the app that gets created in ODC Studio isn't production-ready. This means it’s not ready for distribution, but you can use it to create a package.

<div class="warning" markdown="1">

There might be times when you need to change the default mobile app version number or the version code number. For example, if you are migrating an existing app from another provider to OutSystems, the current version number or version code of your app in the app store might be higher than the OutSystems version numbers. In this case, you need to set the OutSystems version number or version code number to a higher value than what's in the store.

</div>

______________________________________________________________
_QR CODE is a registered trademark of Denso Wave Incorporated._
