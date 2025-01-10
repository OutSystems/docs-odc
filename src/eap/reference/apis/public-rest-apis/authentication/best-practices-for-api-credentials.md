---
summary: Learn best practices for securing API credentials in OutSystems Developer Cloud (ODC), including safe storage, HTTPS usage, and access controls.
tags: 
outsystems-tools: 
guid: 7b0b7f02-8329-4f68-863c-041ba0e7a294
locale: en-us
app_type: mobile apps, reactive web apps
content-type: 
    - best practice
audience: 
platform-version: odc
figma: 
---
# Best practices for keeping API credentials secure

Here are some best practices for storing and using the OAuth client credentials.

* Securely store client credentials (client ID and client secret) in environment variables or a secure storage system. OutSystems recommends using a storage mechanism intended to store sensitive data on the platform that you are using. Avoid hardcoding them directly into the app code or configuration files.

* Limit access to API Clients to only those who require managing them. Use role-based access controls (RBAC) to restrict access within your organization.

* Limit the use of client credentials to only trusted and secure environments. Avoid sharing client credentials across multiple applications or services unless necessary.

* Educate developers about securing client credentials and following best practices for OAuth client authentication. Provide training on secure coding practices and guidelines for handling sensitive information.
