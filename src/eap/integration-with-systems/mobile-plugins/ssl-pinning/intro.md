---
summary: OutSystems Developer Cloud (ODC) uses SSL Pinning to secure mobile app communications by verifying server certificates.
locale: en-us
guid: 607a5bdb-b74e-4d53-88f6-a6ac8389873e
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4307-248&mode=design&t=LCxHTNNeg6HjzPVf-0
platform-version: odc
---
# SSL Pinning Plugin

<div class="info" markdown="1">

The SSL Pinning Plugin applies applies only to Mobile Apps.

</div>

In native mobile apps, SSL Pinning or HTTP Public Key Pinning (HPKP) provides an extra layer of security to HTTPS communications to avoid, for example, man-in-the-middle attacks. SSL Pinning works on the client-side. SSL Pinning verifies the client-server certificate by comparing the hashes of the public keys of the pre-bundled mobile app. 

By design, if there's a hash mismatch, calls to server actions stop working.  When there's a hash mismatch, you must add a new hash list in your app, build a new version of the app, and distribute it to your users. To prevent a hash mismatch, design the app to verify the certificate validity. To learn more about hash validity, see [Check the hash validity](#check-the-hash-validity) section.

OutSystems SSL Pinning Plugin uses a customized version of the SSL certificate validation and doesn't rely on the older SSL Pinning versions that may be in your browsers.

<div class="info" markdown="1">

To learn how to install and reference a plugin in your OutSystems mobile apps, and how to install a demo app, see [Installing a plugin](../intro.md/#installing-a-plugin-and-adding-a-public-element-to-your-app).

</div>

## More about certificates

To keep your stages secure, OutSystems continuously updates server certificates for their domains. This is important especially if your stages use OutSystems default domains and certificates.

<div class="info" markdown="1">

When certificates change, the stages using these certificates in their apps may stop working. To fix this problem, you must generate a new app and distribute the app. Due to any unforeseen circumstances, if OutSystems is unable to notify you every time there is a change or you miss a notification, everyone involved is at risk. 

OutSystems no longer supports the native Mobile apps generation when using SSL Pinning to pin your apps to OutSystems managed certificates. This change affects all stages, production and non-production. If this change affects your stages, get new domains and certificates, and provide their details to OutSystems.

</div>

## Implement SSL Pinning in OutSystems

To implement SSL Pinning, you must have two certificates on the server - one is the primary certificate and the second is a backup (if the primary certificate gets compromised).

To implement SSL Pinning in OutSystems, follow these steps:

1. Generate hashes for the public keys of the certificates.
1. Create a configuration file with the hashes.
1. Install the SSL Pinning plugin from Forge.
1. Add the configuration file to your mobile app.
1. Validate that the certificates are working only for the hashes in the mobile app.

<div class="info" markdown="1">

If you update the [configuration file](#create-the-configuration-file) of the SSL Pinning Plugin in new versions of your app, you need to manually run the app build creation. See: [Situations when the user must install a new build](../../../building-apps/mobile/apps-up-to-date.md#keeping-apps-up-to-date-for-your-users)

</div>

### Generate the hashes for public keys

To generate the hash of a public key in a certificate, get the certificate from server and use [OpenSSL](http://slproweb.com/products/Win32OpenSSL.html) commands to do the following:

1. Obtain the public key from the certificate.
1. Calculate the hash of the public key using the SHA-256 algorithm.
1. Encode the hash of the public key in Base64.

The following is an example of the openSSL commands to generate the hash of the certificate public key.

`openssl x509 -in my-certificate.crt -pubkey -noout | openssl rsa -pubin -outform der | openssl dgst -sha256 -binary | openssl enc -base64`

<div class="info" markdown="1">

To generate a hash with **openssl**, use Command Prompt on Windows or a console on Linux. Use PowerShell with caution as it may generate a different hash value.

</div>

For more examples of the openSSL commands, check out this [Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Public_Key_Pinning#extracting_the_base64_encoded_public_key_information) page or [this script](https://github.com/datatheorem/TrustKit/blob/master/get_pin_from_certificate.py) in GitHub.

### Create the configuration file

To create a JSON configuration file and populate it with hashes and the server addresses, use the following format:

    {

        "hosts": [{

            "host": "www.example.com",

            "hashes": [

                "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",

                "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB="

                ]

        }]

    }

When creating the JSON configuration file, verify your file adheres to the following requirements:

* The JSON file must follow the structure shown above.
* The file has a .json extension, for example, pinning.json.
* Include the full hostname of your server.
* Doesn't have any subdomains in the host.
* Each host has at least two hash keys.
* Hashes have the prefix `sha256/.`.
* For iOS, only unique hash keys are allowed.
  
<div class="warning" markdown="1">

If you change the SSL Pinning resource file **pinning.json**, you must manually run the app build creation. To learn more about when you must install a new build, see [Situations when the user must install a new build](../../../building-apps/mobile/apps-up-to-date.md#keeping-apps-up-to-date-for-your-users)

</div>

### Important note about certificate hashes for ODC

In ODC, you can continue to use custom SSL domains without using your own certificates. ODC utilizes the AWS Certificate Manager service and provides you all the required features to generate SSL certificates for your domains.

So, you must include all the hashes from the Amazon root certificates into your JSON configuration file (for example, pinning.json). To access all the hashes, see [Amazon root certificates](https://www.amazontrust.com/repository/).

The following is a configuration example generated in real-time for an application available on the domain my.custom-domain.com with the hashes from the Amazon root certificates:

    {
    
       "hosts":[
       
                  {
          
                     "host":"my.custom-domain.com",
             
                     "hashes":[
             
                        "sha256/++MBgDH5WGvL9Bcn5Be30cRcL0f5O+NyoXuWtQdX1aI=",
                
                        "sha256/f0KW/FtqTjs108NpYj42SrGvOB2PpxIVM8nWxjPqJGE=",
                
                        "sha256/NqvDJlas/GRcYbcWE8S/IceH9cq77kg0jVhZeAPXq8k=",
                
                        "sha256/9+ze1cZgR9KO1kZrVDxA4HQ6voHRCSVNz4RdTCx4U8U=",
                
                        "sha256/KwccWaCgrnaw6tsrrSO61FgLacNgG2MMLq8GE6+oP5I="
                
                             ]
                     
                  }
          
               ]
           
    }


### Install the SSL Plugin from Forge

Install the SSL Pinning Plugin from [Forge](https://www.outsystems.com/forge/) in your stage. For the plugin installation instructions, see [Installing a plugin](../intro.md/#installing-a-plugin-and-adding-a-public-element-to-your-app). 

### Add the configuration file to the app

Add the configuration file to the mobile app, so that the build service can bundle configuration in the native app build.

Go to the ODC Portal to complete the following steps in your mobile app. 

1. Open the ODC Portal or ODC Studio, and open your mobile app.
    * In the ODC Portal, navigate to the **Configuration tab**.
    * In ODC Studio, navigate to your app list > **Configure app** > **Configuration tab**.

1. Locate the **PinningConfiguration** setting.
    This setting automatically appears after you add a dependency to the SSL Pinning plugin in your mobile app.

1. Select the context menu, select **Edit**, and upload your **pinning.json** file.
 
### Implement additional verification of the server certificate

To add the SSL Pinning verification, ensure you have installed the SSL Pinning Plugin from [Forge](https://www.outsystems.com/forge/) in your stage. 

  ![Screenshot showing the process of adding SSL Pinning verification to a mobile app in ODC Studio](images/add-ssl-pinning-verification-odcs.png "Adding SSL Pinning Verification in ODC Studio")

In ODC Studio, complete the following steps in your mobile app:

1. Go to **Manage dependencies** (Ctrl+Q) and add the reference to SSLPinningPlugin.

1. Drag the **RequireSSLPinning** block to one of your screens. SSL Pinning works for all HTTPS requests in the mobile app. 

    You can add the block in the **Splash** screen.

### Check the hash validity

Calls to server actions stop working if there's a hash mismatch. It's a good practice to check for hash validity. If there's a mismatch, inform users that they must get the new version of the app. Use the client action **CheckCertificateForUrl** to check if a hash from the configuration list is valid or not. If the check doesn't pass, display a notification informing the users to install a new version of the app.

By default, the **CheckCertificateForUrl** action evaluates the current stage URL. Optionally, you can enter a value for the URL parameter. 

The action returns the following two values:

* Success: Boolean.
  True if the connection to the server was successful.

* Error: Error_structure.
  Message is displayed if there's an error during the request to the server. The values are the "SSLPinning found an issue with the configured certificate for the url!" (when there's a problem with the configured hash value) and "Message: SSLPinning found some problem with the request!" (a generic error that requires troubleshooting).

### Test the SSL Pinning

To test the mobile app with SSL Pinning, do the following:

1. Publish and generate the new version of your Mobile app with SSL Pinning.

1. Install and run the app on your smartphone. 

1. Verify that the app works (it has the right certificate and hash keys).

To test that the SSL Pinning rejects a certification, do the following:

1. Edit the configuration file and tamper with the hashes, for example, change one character in each hash.

1. In your mobile app:

    * Remove the resource with the old configuration file.

    * Add a resource with the new configuration file (remember to set the properties).

    * Publish and generate the new version.

1. Install and run the new version on your smartphone.

1. The Mobile app won’t work because the SSL Pinning displays an error due to an invalid certificate.

## SSL pinning for multiple servers

If you want your mobile app to perform the SSL Pinning validations when connecting to multiple servers, complete the following steps:

1. For each server, get its two certificates and generate their hashes.

1. Create the configuration file using the following JSON format:

    {

        "hosts": [{

            "host": "www.myserver1.com",

            "hashes": [

                "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",

                "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB="

                ]

        },{

            "host": "www.myserver2.com",

            "hashes": [

                "sha256/CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC=",

                "sha256/DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD="

                ]

        },

        ...

        ]

    }


1. Bundle the configuration file and implement the verification in your mobile app (as explained for a single server).

## Plan for the certificate renewal

If you're planning to update your certificate soon, release a new version of the app with the JSON configuration containing the hash values for both the current certificate and the new certificate. Do this before you update the certificate to give users enough time to update the app. This ensures that when you update the certificate, the app continues to work.

