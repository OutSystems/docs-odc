---
guid: c04f069a-8ed4-45c5-bc1c-47b7def683d8
locale: en-us
summary: Understand the security and operational responsibilities you own as an ODC customer, as listed in the OutSystems SOC 2 Type II report.
figma:
coverage-type:
  - understand
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Platform administrator
  - Tech lead
  - Architect
tags:
  - Authentication
  - Authorization
  - Data
  - Monitoring
  - Roles
  - Security
  - SSO
outsystems-tools:
  - none
helpids:
isautopublish: true
---

# SOC 2 customer responsibilities in ODC

As an OutSystems Developer Cloud (ODC) customer, you own security and operational controls that OutSystems can't run for you. These controls depend on decisions that only you can make within your organization and the apps and agents you build on ODC. Use this article to identify your responsibilities and plan the controls your organization needs.

Auditors call these responsibilities Complementary User Entity Controls (CUECs). OutSystems lists them in the "User Entity Responsibilities" section of its SOC 2 Type II report for ODC. This article restates each responsibility in plain language.

**Note:** This article is a companion to the SOC 2 Type II report and doesn't replace it. For questions about these responsibilities, or to request the report, contact your OutSystems account team or the Security, Strategy and Assurance (SSA) department.

## Change management

Change management covers how you manage changes to the apps, agents, and data you build on ODC. You're responsible for the following:

* Own the security of the apps and agents you build on ODC, in line with the [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47). This includes managing your data, following secure development practices, reviewing your code for security issues, and identifying and fixing vulnerabilities in your apps and agents.
* Run your own process to review, approve, and track changes to the apps and data in your environment. OutSystems doesn't manage this process for you.
* Deploy and install the updates you make to your apps and agents.

## Monitoring and communication

Monitoring and communication covers how you keep OutSystems informed and watch over your own environment and people. You're responsible for the following:

* Tell OutSystems whenever your technical or administrative point of contact changes, so OutSystems can always reach the right person.
* Monitor the apps and agents you build for issues. OutSystems doesn't monitor them on your behalf.
* Oversee how your employees use the apps and systems you build, and make sure their usage is appropriate.
* Contact OutSystems Support right away if you know of or suspect a security incident, including a compromised user account used for integrations or secure file transfers.
* Tell your account representative if a change in your organization affects the service OutSystems provides to you.
* Maintain sound, consistent internal controls over who accesses your IT systems and how your organization uses them.

### Security event monitoring and reporting

Monitoring, alerting, and investigating security events within the apps and agents you build is your responsibility. OutSystems doesn't do this for you.

If you believe one of your apps or agents has been involved in a security event, contact OutSystems Support right away. For more information about reporting incidents, refer to [Security of OutSystems Developer Cloud](security.md#monitoring-and-support).

## Business continuity and disaster recovery

Business continuity and disaster recovery covers how you plan for service interruptions. You're responsible for the following:

* Maintain your own business continuity and disaster recovery plan that defines what your organization does if you can't access or use ODC services temporarily.

## Data management

Data management covers how you protect data as it moves to and from ODC. You're responsible for the following:

* Use secure transmission methods when you send data to or from ODC, and set your own security requirements for that data.

## Access

Access covers how you manage who can get into your own environment. You're responsible for the following:

* Set up single sign-on (SSO) or another appropriate authentication method for signing in to your environment.
* Review regularly who on your team has access to your environment, to confirm the access levels still make sense. Use ODC role-based access control to set permissions at the granularity your organization needs. For more information, refer to [User management](../user-management/intro.md).
* Manage your own user accounts. Grant access to new employees, update access as roles change, and remove access promptly when someone leaves your organization.

## Next steps

Use the following articles to learn more about security and responsibilities in ODC:

* [Security of OutSystems Developer Cloud](security.md) describes the security measures that OutSystems provides.
* [Sentry for ODC](sentry.md) describes the add-on that provides advanced security and compliance capabilities.
* [Self-hosted ODC shared responsibility model](../manage-platform-app-lifecycle/self-hosted/sh-shared-responsibility.md) describes the responsibility split for self-hosted ODC stages.
