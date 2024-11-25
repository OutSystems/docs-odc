---
helpids: 30469
summary: OutSystems Developer Cloud (ODC) facilitates efficient onboarding by enabling group mapping from identity providers to automate role assignments.
locale: en-us
guid: 84c9098b-c486-483f-9836-70b8faee63fa
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
tags: identity and access management, user onboarding, role management, identity providers, group mapping
audience:
  - platform administrators
  - full stack developers
  - mobile developers
  - frontend developers
outsystems-tools:
  - odc portal
content-type:
  - procedure
  - conceptual
---

# IdP and end-user group mapping

OutSystems Developer Cloud (ODC) enables you to accelerate onboarding end-users from your identity provider (IdP). End-users must exist in your IdP, and it’s the responsibility of the IdP to authenticate users.

Users must have permission to access the End-user group mapping option. With permission, you can map groups of end-users from your IdP to end-user groups in ODC. Once the group mapping is correctly configured, you don’t need to invite end-users individually. End-users are automatically granted the roles configured on the mapped end-user group when they log into your OutSystems, which speeds up the onboarding process.

<div class="info" markdown="1">

This ODC feature only works if your IdP supports groups. Check with your IdP to verify they support groups. Additionally, if your IdP does support groups, you might have to do some configuration work on the IdP to send the group information during authentication. You can only map end-users. You can’t map members with organization roles, such as Admin or Developer.

</div>

According to the roles on the IdP, each end-user that exists in the IdP can log in to ODC with the appropriate roles. When the mapping completes, end-users are automatically granted roles and access to apps for the ODC group. If an end-user already exists in ODC, their permissions synchronize according to the existing group mapping if applicable. This happens every time an end-user logs into ODC. For more informaiont about Roles, refer to [Roles](../../user-management/roles.md)

You need the following before you can map groups:

* Access to the **Create group** option in ODC.
* Groups must exist in the IdP.
* Access to **Identity Provider** option. You must have permission to view, create, or delete the mapping on ODC.
* IdPs must already be configured in ODC. To learn how to configure your IdP for OutSystems, see [Configure authentication with external identity providers](intro.md).
* End-user group in ODC must exist. To learn how to setup a group in ODC, see [User-management](../../user-management/intro.md).
* Group claim name (identifier) and value from your IdP. The claim enables ODC to access the end-user information from your IdP. Some IdPs send group identifiers, while others send group names. Before beginning, check it with your IdP.

Most users can configure a group in ODC. But only users, with the appropriate permission, can map end-user groups with IdPs. Typically, Admins have the permission to map IdPs.

To create a group, from the ODC Portal Navigation menu, select **End-user groups**. Then, from the End-user groups summary page, click **Create group**, enter a Group name, and click **Save**. You now have a new group. No other information is required to create a group.

You can access group mapping from the ODC portal by selecting **End-user groups** or **Identity providers**. Choose the option that works best for you. From the End-user group mapping, you can add several mappings to a group. From the Identity provider, you can add several mappings to a provider.

## Mapping from the End-user groups option

To map a provider to an End-user group, from the portal, select **End-user groups**. A summary page displays End-user groups. You can display groups for different stages. Click the **End-user group** you want to map to an IdP.

Click the **Group mappings** tab to display all group mapping for this group. In the Group mappings section, you can view all mappings, active mappings, or inactive mappings. An **Inactive** status indicates that the IdP and group aren't in the same stage. Hover over the Inactive status to learn what you need to fix to make the mapping active.

To add a new mapping, click **Add mapping**. All fields are required. From the Provider drop-down, select a provider. Enter a **claim name** and a **Claim value (provider group)**. Your IdP provides the claim value, which is the group claim (identifier) and the Claim Name.

<div class="info" markdown="1">

For Azure AD (or Microsoft Entra) the claim value should be the Object Id of the group and the claim name should simply be "groups".

</div>

## Mapping from the Identity providers option

To connect a provider to an end-user group, from the ODC Portal, select **Identity providers**. From the Identity provider summary page, click on the provider you want to map to an end-user group. If you have the correct permissions, a Group mappings tab displays.

The Group mappings summary page shows the current mappings for this Provider. The display shows the Provider group(s) and end-user groups that are mapped and the current status. An **Inactive** status indicates that the IdP and end-user group aren't in the same stage. Hover over the Inactive status to learn what you need to fix to make the mapping active.

To add a new mapping, click **Add mapping**. You must enter a **Claim name** and a **Claim value (provider group)**. Your IdP provides the claim value (identifier) and the group claim. In the End-user group section, click on the group(s) you want to map, select a stage, and then click **Save**. When the mapping completes, end-users can log into ODC and access the apps assigned to the group.

When an admin removes a user from an Okta group through the Okta dashboard, the user can no longer log in to the app. However, the user still appears as mapped in the ODC Portal.

If a user is added to Okta, it won't appear in the ODC Portal immediately. User is required to log in to the app for the first time for their mapping to appear in the ODC Portal. The admin must refresh the page in order to see the user added in the list.

For more information about setting up the claim in Azure, [click here](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/connect/how-to-connect-fed-group-claims).

For more information about setting up the claim in OKTA, [click here](https://help.okta.com/asa/en-us/content/topics/adv_server_access/docs/group-management.htm).

## Managing users in end-user groups

When viewing the users linked to the end-user group, you can link the users in the following ways:

* Mapped users are automatically assigned to the end-user group when they log in using the Identity Provider. These assignments are not managed on the ODC Portal and are done during login. 
* Assigned users are explicitly assigned to the end-user group on the ODC Portal. 
* Assigned & mapped users are both assigned and mapped to the end-user group. 

Assigned users can be unassigned anytime from the ODC Portal. However, mapped users can't be unmapped from the ODC Portal and remain mapped to the end-user group even if they get unassigned from the external provider group.
 
<div class="info" markdown="1">

Mapped users who haven't logged in using the Identity Provider are not displayed in the end-user group. 

</div>

You can manually add assigned users in the ODC Portal, follow these steps to add assigned users:

1. Go to the ODC Portal, and from the Navigation menu, select **End-user groups** to display the list of groups.
1. Select the group you want to add users to.
1. Click **Users** to display the list of users. 
1. Click **Assign users** to display a popup where you can assign or unassign users from the group.

If the user mapping is from an external IDP, access gets revoked after removing the mapping from the IDP. However, if you assign the users in the ODC portal, they retain access after the removal of mapping from the IDP.

To remove a user from a group, access the identity provider managing the user account and remove the user from the mapped provider group. However, the user still appears mapped in the ODC Portal. Although the user can't log in, the mapping remains visible until the next login attempt.

## After mapping IdPs and end-user groups

The saved configuration defines the landing page users see after logging into your App. The configuration assigns the provider that authenticates the organization and app users. This determines which redirect URLs you must add to the identity provider.

## Deleting group mappings

When you delete an IdP group mapping, all group claims are also removed. The associated end-user group links are also removed. This means if this was the only mapping for a particular end-user, then that user no longer has access to ODC.

You can also delete an end-user group. When you delete a group, all end-user linking and mapping entries are deleted. Any access to apps from this group is no longer available.
