---
guid: 3474ca87-eabb-44e5-bee0-f938e1f488d3
locale: en-us
summary: Optimize user management with OutSystems Developer Cloud (ODC) by applying best practices like least privilege, avoiding lockouts, and using APIs.
figma: 
coverage-type:
  - evaluate
  - unblock
topic:
  - lockout
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - infrastructure managers
  - tech leads
  - platform administrators
tags: user management,least privilege,api validation,api security,identity providers
outsystems-tools:
  - odc portal
helpids: 
---

# Best practices for user management in ODC

User management in OutSystems Developer Cloud (ODC) is essential for securing your organization’s resources, ensuring compliance, and streamlining access to apps and data. Following best practices helps prevent unauthorized access, reduces operational risks, and simplifies ongoing administration as your organization grows or changes. This article summarizes key recommendations for managing users, roles, permissions, and integrations with external identity providers (IdPs) and APIs.

## Test external IdPs before removing the built-in IdP

Switching authentication providers is a critical operation. Removing the built-in IdP assignment (to the organization for IT-users or to an app stage for end-users) without proper testing can result in a [lockout](../manage-platform-app-lifecycle/external-idps/intro.md#lockout), where no one can access either the ODC Portal and Studio, or the apps developed in ODC.

### Recommendations

Before removing the built-in IdP assignment, fully test your [external IdP configuration and assignments](../manage-platform-app-lifecycle/external-idps/intro.md).

### Benefits

Testing prevents accidental lockouts, ensuring continuous access to the ODC Portal and Studio or to the apps developed in ODC. Skipping this step can leave your organization without administrative access, requiring you to open a support ticket in the [Customer Portal](https://www.outsystems.com/support/portal/my-support-activity).

## Apply the principle of least privilege

Granting excessive permissions to a user increases the risk of accidental or malicious actions.

### Recommendations

Assign users only the minimum roles and permissions needed for their tasks.

### Benefits

Minimizing permissions reduces security risks and limits the impact of potential incidents. Over-privileged users can unintentionally or intentionally compromise data or system integrity.

## Use end-user groups for simplified access management

If you assign roles to end-users individually, it takes a long time and you can make mistakes.

### Recommendations

Organize end-users into [end-user groups](end-users/groups.md), and assign roles to groups instead of individual end-users to streamline end-user onboarding and permission changes.

### Benefits

By using groups, you can have standardized, scalable access control. If you follow this approach you assign roles only once (to the group) instead of multiple times (for each end-user), and you ensure consistent security policies. You can also make role changes more quickly and efficiently.

## Use end-user group mappings with external IdPs

If you integrate external IdPs with ODC, you can automate end-user onboarding and role assignment.

### Recommendations

When using an external IdP, if your IdP allows it, create groups and restrict access in the provider's side so that only specific groups can log in. Then, [map IdP groups to end-user groups in ODC](../manage-platform-app-lifecycle/external-idps/end-user-group-mapping.md), and assign roles to the group.

### Benefits

This approach helps prevent unauthorized access and speeds up the onboarding process of end-users. When end-users are created automatically in ODC after their first login using an external IdP, ODC automatically assigns roles to them according to the end-user group you mapped.

## Use APIs for user management

Manual user management does not scale for large organizations or frequent changes.

### Recommendations

Use the [User and access management API](../reference/apis/identity-v1.md) to automate user and role management tasks. Make sure to validate API input to prevent misuse or security vulnerabilities.

### Benefits

The [User and access management API](../reference/apis/identity-v1.md) enables you to:  

* Manage users in bulk or automate user management tasks, and reduce manual errors. Proper validation ensures security and data integrity.  

* View all users with permissions for a specific app. Currently, this functionality isn't available in the ODC Portal.

## Related resources

* [Roles and permissions for members (IT-users)](roles.md)
* [Secure your app with end-user roles](secure-app-with-roles.md)
* [Configure authentication with external identity providers](../manage-platform-app-lifecycle/external-idps/intro.md)
* [ODC REST APIs](../reference/apis/public-rest-apis/overview.md)
* [User management](intro.md)
* [Grant and revoke user roles](grant-and-revoke-user-roles.md)
* [Managing authorization and authentication for end-users](end-users/intro.md)
* [Managing authorization and authentication for members (IT-users)](it-users/intro.md)
