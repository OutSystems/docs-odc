---
summary: OS-ABRS-CONN-50000 is a generic internal error from the OutSystems Developer Cloud (ODC) service that runs AI agent connections. It appears when testing or running an MCP server or A2A connection fails unexpectedly.
tags:
  - AI
  - Agentic
  - MCP
  - Troubleshooting
guid: ac2f6ac8-a547-4f2f-afe5-28062601fc8f
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Tech lead
outsystems-tools:
  - odc portal
coverage-type:
  - unblock
isautopublish: true
---

# OS-ABRS-CONN-50000

## Error message

```
Internal Server error
```

The message can also appear as `Unexpected error occurred`, sometimes followed by technical details from the connection attempt.

## Cause

The service that runs AI agent connections hit an unexpected, unhandled error while testing or running a connection to an MCP server or an external agent (A2A). This is a generic code that the service returns when the failure doesn't match a more specific error, so the exact cause isn't reported to you.

## Impact

The connection operation doesn't complete. You can't test the connection, import its tools, or call the connected MCP server or external agent.

## Recommended action

This error reports a server-side failure, so the actions available to you are limited.

1. Select **Test connection** again, because the error can be transient.
1. Confirm the basics of the connection in ODC Portal under **Integrate** > **Connections**: the server URL starts with `http://` or `https://`, the authentication method and credentials are correct, and, for a server on a private network, the **Private Gateway** toggle is on with the port that matches your Cloud Connector.
1. If the error persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-ABRS-CONN-50000). Include the trace ID from the ODC Console if you have one.
