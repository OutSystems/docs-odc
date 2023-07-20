---
helpids: 30469
summary: From OutSystems Developer Cloud  you can enable authenticated IdP end-users to access ODC.
locale: en-us
guid: 84c9098b-c486-483f-9836-70b8faee63fa
app_type: mobile apps, reactive web apps
figma: 
platform-version: odc
---

# IdP and End-user group mapping

OutSystems Developer Cloud (ODC) enables you to accelerate onboarding end-users from your identity provider (IdP). End-users must exist in your IdP and it’s the IdPs responsibility to authenticate the users.

Using end-user group mapping, a person with manage end-user access permissions can connect  groups of end-users from their IdP to end-user groups and roles associated in ODC. With the Manage end-user access permission you  don’t need to invite end-users individually which speeds up the onboarding process.

You can only map end-users. You can’t map members who have organization roles, such as Admin or Developer.

According to the roles on the IdP, each end-user that exists in the IdP can login to ODC with the appropriate roles. When the mapping completes, end-users are automatically granted roles and access to apps for the ODC group. If an end-user already exists in ODC their permissions synchronize according to the existing group mapping if applicable. This happens every time an end-user logs into ODC.

You need the following before you can map an IdP end-user group to an ODC end-user group:

* Groups must exist in the IdP.
* Access to Identity Provider option. You must have permission to view, create, or delete the mapping on ODC.
* IdPs must already be configured in ODC. To learn how to configure your IdP for OutSystems, see [Configure authentication with external identity providers](intro.md).
* The end-user group in ODC must exist. To learn how to setup a group in ODC, see [User-management](../../user-management/intro.md).
* You must have the group claim (identifier) from your IdP. The claim enables ODC to access the end-user information from your IdP.

Most users can configure a group in ODC. But only users, with the appropriate permission can map end-user groups with IdPs. Typically, Admins have the permission to map IdPs.

Before mapping users from your IdP, create a group in ODC. To create a group, from the **ODC Portal Navigation** menu, select **End-user groups.** Then from the End-user groups summary page, click **Create group**, enter a Group name, and click **Save**. You now have a new group. No other information is required to create a group.
