---
summary: An app containing too much disabled code.
tags: disabled code, code maintenance, app performance, code readability, production code
guid: c166aa05-26ca-48da-b80a-91ea20294bbc
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
  - full stack developers
  - tech leads
outsystems-tools:
  - odc studio
  - odc portal
---
# Too much disabled code

An app containing too much disabled code.

## Impact

Keeping a large amount of disabled code creates clutter and makes it difficult to read. It also increases maintenance costs and wastes time, as people tend to interpret disabled code to better understand its relevance.

## Why is this happening?

Too much disabled code results from deactivating code sections but not removing them.

## How to fix

Remove the code if you have disabled it for a while or if the app is in production and behaves correctly.
