---
summary: Reference information for Roles built-in function in OutSystems Developer Cloud (ODC).
tags: roles, user authentication, server actions, service actions, outsystems developer cloud
locale: en-us
guid: 4facff20-972f-477b-8b61-d2b64539ea1c
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - remember
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
---
# Roles

## CheckEndUserRole

Returns True when the logged in end-user has the specific role. The function allows you to check for any public role whether local or consumed from another app.

Available in:  

* Server action
* Service action

### Input

RoleId
:    Type: Role Identifier. Mandatory.  
The identifier of the role to be checked.

### Output

Type: Boolean

### Example

```
HumanActivityInstance.AssignedUserId = GetUserId() or CheckEndUserRole(HumanActivityRole.RoleId) 
```

## GetUserId

Returns the identifier of the user that is currently authenticated with the server or 'NullIdentifier()' if the user is not authenticated.

Available in:

Server action
Service action
Database aggregate

## Output

Type: UserId
