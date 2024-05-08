---
summary: OutSystems Developer Cloud (ODC) enables secure and encrypted storage of sensitive app settings configured as secrets.
locale: en-us
guid: 3a5f56e7-2515-4e97-914e-b8a503f82c7f
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Set as secret

A secret is a private piece of information that gives access to protected resources or sensitive information. In OutSystems Developer Cloud (ODC), you don't need special skills to protect sensitive settings. You configure an app setting during development as a secret. Once you set a setting as secret, the value is hidden and stored securely. You can't see the value of the secret. 

As you develop apps, keep in mind that every application, script, automation tool, and other non-human identity relies on some form of a privileged credential. This credential gives access to other tools, applications, and data. These secrets can unlock protected resources or sensitive information in tools.

Sensitive information such as tokens and passwords are usually saved in a secret storage solution. A secret storage solution is an identity-based encryption management system. You use a secret storage solution to secure, store, and tightly control access to passwords, certificates, API keys, and other items you want to control.

Depending upon the app you build you can have several fields that should be set as secret. When you set a field value as a secret, the actual value is masked with asterisks (*****). The values are custom and you can define them for each stage.

Benefits of using this approach include:

* Secrets are stored in the Secrets Manager/vault.
* Secrets are always encrypted.
* Secrets never show as plain text.

## Setting as secret

There are two relevant parts to setting and using a field as a secret:

* In ODC Studio, you set a field as a secret.
* In the ODC Portal, you set the value of secret for each stage.

Following is an overview of the process for setting a secret:

1. In ODC Studio, under **Data** > **Settings**, set the property **Is Secret** to **Yes**. ODC Studio hides the value. Also, there is no default value for the field set as secret.
1. Publish the app to make the field available for editing in the ODC Portal.
1. In the ODC Portal, from the app details page in a stage, look for the settings section and insert the value for the field.

## Reverting from secret to non-secret

To change a setting from non-secret to secret, follow the same process you used when you initially set the secret in ODC Studio. Note that changing a secret to a non-secret deletes the value of the setting once you publish the app.
