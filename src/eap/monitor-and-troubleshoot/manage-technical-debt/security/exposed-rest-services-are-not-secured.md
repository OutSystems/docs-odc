---
summary: Exposed REST services should enforce authentication to protect against unauthorized access.
tags: authentication, rest services, security, vulnerability
guid: d669fc5b-08da-4bff-954f-cc007ade6174
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - unblock
  - remember
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - none
---
# Exposed REST services without authentication

Exposed REST services should enforce authentication to protect against unauthorized access.

<div class="info" markdown="1">

In ODC, SSL/TLS is always enforced for all REST services and you can't disable it, ensuring secure communication by default.

</div>

## Impact

Without authentication, REST endpoints are vulnerable to unauthorized access, data breaches, and misuse.

## Why is this happening?

The exposed REST API isn't protected. The authentication is set to **None**.

 ![Screenshot showing the authentication setting set to None in the REST service security options.](images/odcs-authentication-none.png "Authentication Setting in REST Service")

## How to fix

Change the authentication to **Basic** or **Custom** in the REST service.
