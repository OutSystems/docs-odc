---
guid: 1800f41c-874c-4f6f-b91c-1db37aaab563
locale: en-us
summary: 'OutSystems Developer Cloud (ODC) and O11 connection troubleshooting: resolve common issues when connecting your ODC organization to an O11 infrastructure.'
figma: https://www.figma.com/design/epaiN2jasbbKgJA0iSYfZn/Extending-with-ODC?node-id=3053-409
coverage-type:
  - unblock
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Platform administrator
tags:
  - Authentication
  - Infrastructure
  - Troubleshooting
outsystems-tools:
  - lifetime
  - odc portal
helpids:
isautopublish: true
---

# Troubleshooting O11 and ODC connection issues

This page describes some common issues you may encounter when connecting your ODC organization to an O11 infrastructure, and how to solve them.

## Failure in validation of organization ID

When creating a new connection between your ODC and O11 infrastructure, the validation fails and you get the error OS-EBRG-40301, `The authentication token doesn't match the ODC organization ID`.

![The authentication token doesn't match the ODC organization ID](images/troubleshooting-org-id-error-pl.png "The authentication token doesn't match the ODC organization ID")

### Recommended action

If you are using a LifeTime service account that isn't bound to your ODC organization, create a new service account for O11-ODC interoperability with the following configuration:

* **Service account consumer** is set to **ODC**
* **ODC organization ID** matches the value in the ODC Portal

Refer to [Connect ODC to your O11 infrastructure](connect-o11-infrastructure.md#add-infrastructure) for further details.
