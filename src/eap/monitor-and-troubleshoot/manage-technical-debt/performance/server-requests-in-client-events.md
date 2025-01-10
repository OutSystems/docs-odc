---
summary: Server actions being called in client events.
tags: server requests, client events, performance optimization, screen render time, mobile apps
guid: e23f04cc-761b-4d4c-8ef3-b639f4a80c83
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3627-10&t=GQOBWGLkIWVooPGi-1
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
---
# Server requests in client events

Avoid server calls in client events.

## Impact

Screen and block lifecycle events (On Initialize, Ready, Render, and After Fetch) are serialized in the request, and server calls can take time to get the response, which impacts the screen render time.

## Why is this happening?

You’re making a server call in a client event.

![An OnInitialize event flow with a server action node.](images/server-call-on-initialize-odcs.png "Server call on a client event")

## How to fix

Limit server requests to synchronization requests (typically performed on business events fired in screen actions, session start, or online events) and online transactions (typically performed in screen actions).
