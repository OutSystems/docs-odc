---
summary: An action that isn't used in an app or library and is also not exposed to other apps or libraries (non-public action).
tags: code maintenance, security risks, unused actions, non-public actions, mobile apps
guid: 395ec5da-9a47-4849-9a22-cbaffa541e8e
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
  - frontend developers
  - architects
  - tech leads
outsystems-tools:
  - odc studio
  - odc portal
---
# Unused action in app or library

An action that isn't used in an app or library and is also not exposed to other apps or libraries (non-public action).

## Impact

Unused actions can enlarge your code, make maintenance difficult, and increase security risks.

## Why is this happening? 

The app or library does not utilize the defined action anywhere.

## How to fix

Consider deleting the action if it isn't strictly necessary.
