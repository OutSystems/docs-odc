---
summary: Manage sensitive information by setting it as secret in Service Studio. Give the setting a value in Portal, different for each stage.
tags: 
locale: en-us
guid: 3a5f56e7-2515-4e97-914e-b8a503f82c7f
app_type: mobile apps, reactive web apps
---

# Set as secret

A secret is a private piece of information that gives access to protected resources or sensitive information. As you develop apps, keep in mind that every application, script, automation tool, and other non-human identity relies on some form of a privileged credential to access other tools, applications, and data. These secrets can unlock protected resources or sensitive information in tools.

Sensitive information such as tokens and passwords are usually saved in a secret storage solution. A secret storage solution is an identity-based encryption management system. You use a secret storage solution to secure, store, and tightly control access to passwords, certificates, API keys, and other items you want to control.

In Project Neo, you don't require special skills to protect sensitive settings. You configure an app setting during development as a secret. Once you set a setting as secret, the value is hidden and stored securely.

Depending upon the app you build you can have several fields that should be set as secret. When a field value is set as secret, the actual value is masked with asterisks (*****). The values are custom and you can define them for each stage.

Benefits of using this approach include:

* Secrets are stored in the Secrets Manager/vault.
* Secrets are always encrypted.
* Secrets never show as plain text.

## Setting as secret

There are two parts relevant to setting and using a field as a secret:

* In Service Studio, you set a field as a secret.
* In Portal, you set the value of secret for each stage.

Here is an overview of the process for setting a secret:

1. In Service Studio, under **Data** > **Settings**, set the property **Is Secret** to **Yes**. Service Studio hides the value. Also, there is no default value for the field set as secret.
2. Publish the app to make the field available for editing in Portal.
3. In Portal, from the app details page in a stage, look for the settings section and insert the value for the field.

## Reverting from secret to non-secret

To change a setting from non-secret to secret, follow the same process you used when you initially set the secret in Service Studio. Note that changing secret to non-secret deletes the value of the setting once you publish the app.
