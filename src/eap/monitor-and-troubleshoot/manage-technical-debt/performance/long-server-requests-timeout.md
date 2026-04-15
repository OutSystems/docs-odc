---
summary: The default timeout for server action requests is more than 10 seconds, or an explicit timeout in a server call is more than 10 seconds.
tags: server requests, timeout settings, user experience, data processing, connectivity issues
guid: d6a6ff38-316b-476d-a579-c9ac92b0079f
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3525-192&t=ZHJybqzEUX6B7aIU-1
coverage-type:
  - unblock
  - remember
audience:
  - full stack developers
  - backend developers
outsystems-tools:
  - none
---
# Long server requests timeout

The default timeout for server action requests is more than 10 seconds, or an explicit timeout in a server call is more than 10 seconds.

## Impact

Server requests should be efficient. 10 seconds is all it takes for a device to go to sleep mode or lose network connectivity. A high timeout can lead to poor user experience. If the server is slow or unresponsive, the user might have to wait indefinitely for the request to complete.

## Why is this happening

The default timeout for server action requests is set to more than 10 seconds, or an explicit timeout in a server call is set to more than 10 seconds.

![An action flow diagram with a Run Server Action node where the specified Server Request Timeout is set to 60 seconds.](images/odcs-server-request-timeout.png "Server Request Timeout set to 60 seconds")

If your server requests take too long, you might be processing too much data at the same time, or you might be trying to access data that's not prepared on server side.

## How to fix

Instead of increasing the timeout settings, prepare and cache data in advance on the server side so that it's available when required. You can also reduce the server request timeout to fail quickly (with a "retry later" message).  

Ensure that the default timeout has a short time defined (no more than 10 seconds), as this affects all the server action requests in the app. The same principle applies to each server action; if you increase a server action timeout after defining the default timeout to a lower number, a finding will be raised.
