---
guid: ede44fa9-a8cb-4ba0-a0d5-309119fcdeef
locale: en-us
summary: Avoid having server calls in the client-side logic of a screen that is accessible to everyone.
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3782-12&t=OYSeAQqMMvonnHHO-1
coverage-type:
  - unblock
  - remember
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - frontend developers
  - mobile developers
  - platform administrators
tags: server calls, client-side logic, security issues, frontend security, authentication
outsystems-tools:
  - odc portal
helpids:
---
# Server call in the logic of a screen accessible to everyone

A server action or aggregate is consumed in the client-side logic of a screen that is accessible to everyone.

<div class="info" markdown="1">

Unlike other patterns that are only analyzed in new app revisions, Code Quality performs a full sync for this pattern, searching for the pattern in your whole portfolio. This means you might have findings in apps that haven’t had new revisions in a while.

</div>

## Impact

If a screen is available to everyone, server calls in its logic are publicly exposed, inviting malicious users to access the server without any authentication or authorization.

A malicious user might modify client-side logic (JavaScript), check the server requests, and manipulate input parameters to try to access your data or perform unauthorized actions.

## Why is this happening?

Your app has a server action or aggregate executed in the client-side logic of a screen that can be accessed by everyone.

![The properties of a screen showing the screen is accessible to everyone.](images/server-call-screen-accessible-everyone-odcs.png "The properties of a screen showing the screen is accessible to everyone.")

## How to fix

If you don't need the screen to be accessed by everyone, change it to be accessible only to authenticated users.

If you need the screen to be accessed by everyone:

* Ensure you perform extra validation on the server side for all data sent to the server to prevent unauthorized access to read or edit operations.
  
* Make sure the business information returned by the server to be presented on the screen is not sensitive or private.
