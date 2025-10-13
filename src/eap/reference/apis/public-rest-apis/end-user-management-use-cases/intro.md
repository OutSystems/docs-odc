---
guid: e6cc2e02-ac14-4a8f-a6bc-accf84adf2b5
locale: en-us
summary: This articles provides a list of use cases for user and access management APIs.
figma:
coverage-type:
  - remember
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - mobile developers
tags: user management, access management, apis, rest api, user roles
outsystems-tools:
  - odc studio
  - odc portal
  - forge
helpids:
---
# User and access management API use cases

ODC provides a set of user and access management APIs that allow you to programmatically create, view, and manage users and their permissions at runtime. For detailed information on individual endpoints of these APIs, refer to [User and access management API](../../identity-v1.md). You can use these APIs to do the following:

* [Create a single user and assign a role to the user](create-user-assign-role.md)

OutSystems recommends that you consume all the user and access management APIs in a separate [library](../../../libraries/intro.md) and create individual server actions that invoke the corresponding REST API. This allows you to reuse the APIs across different ODC apps.  For detailed information about how to consume REST APIs, refer to [Consume one or more REST API methods](../../../../integration-with-systems/consume_rest/consume-a-rest-api.md).

To explore a sample user and access management ODC library, refer to the User Management Connector in the [User Management Forge component](https://www.outsystems.com/forge/component-overview/21016/users-management-odc).

## Related resources

* [User management in ODC](../../../../user-management/intro.md)
