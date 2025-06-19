---
summary: This article describes the User and Access Management REST API endpoint details.
locale: en-us
guid: e3d4a88f-3610-42a0-ada5-cd2eaf425343
app_type: mobile apps, reactive web apps
platform-version: odc
content-type:
  - reference
audience:
  - backend developers
  - full stack developers
  - platform administrators
figma:
api-render: true
tags: user management api, access control, rest api, odc platform, api documentation
outsystems-tools:
  - odc studio
  - odc portal
---
# User and Access Management API

<style>
#b3-b4-b1-InjectHTMLWrapper {height: auto!important}
.image-zoom div div{height: auto!important}
rapi-doc::part(section-overview-title) {display: none}
</style>

<rapi-doc spec-url = 'resources/user-access-management-api-v1-public.json'  theme = 'light' nav-bg-color = '#fff' show-header = 'false'  show-info = 'true'  allow-authentication ='false'  allow-server-selection = 'true' default-api-server = 'https://{odc-portal-domain}/api/identity/v1'  allow-api-list-style-selection ='false' render-style = 'view' layout = 'column' show-method-in-nav-bar = 'as-plain-text' use-path-in-nav-bar = 'true' allow-spec-file-download = 'true' show-side-nav = 'true' allow-try='false' regular-font = 'NotoSans' primary-color = '#242320' bg-color = '#fff' text-color = '#4D4D49' mono-font = 'monospace' allow-schema-description-expand-toggle = 'false' schema-style = 'tree' schema-description-expanded = 'true' default-schema-tab = 'schema'>
<div slot="operations-top" class ="info">
<p>When you use POST, PUT, or PATCH APIs in ODC Studio, you must:</p>
<ul><li>Set the <strong>Send Default Value</strong> to <strong>Yes</strong> for all the request fields in the API.</li>
<li>Send data for all the fields in the request body and not only for the fields that you want to update. For example, if you use <code>PATCH /users/{key}</code> API in ODC Studio to update the name of a specific user, you must also send the relevant data for both <code>photoUrl</code> and <code>isActive</code>.</li></ul>
</div></rapi-doc>
