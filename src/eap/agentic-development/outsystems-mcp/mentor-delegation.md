---
summary: With OutSystems MCP, the agent in your MCP host sequences the work and delegates the build to Mentor, which edits the app model on the OutSystems server.
tags: mentor, delegation, agent-to-agent, outsystems mcp, agentic development
guid: 57e403b6-6cec-458a-8abc-16db6321a3f0
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
  - mentor
coverage-type:
  - understand
content-type:
  - conceptual
audience:
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Delegation to Mentor

Mentor is the OutSystems AI that builds and changes apps from natural-language instructions. When you work with OutSystems MCP, the agent in your MCP host sequences the work and delegates the build to Mentor. Mentor edits the app model on the OutSystems server and returns the result to the agent. This division of work determines how you sequence inspection, edits, and publishing.

## The delegation model

The agent and Mentor have distinct roles in a single workflow:

* The agent interprets your request and calls OutSystems tools.
* For edits, the agent hands the work to Mentor, which loads and changes the app model on the server.
* The app model stays on the server. The agent inspects an app's structure through context lookups, and the MCP host never downloads the model.

## A session-backed conversation

Mentor runs as a multi-turn conversation backed by a server-side session that holds the loaded app model. Follow-up turns reuse the same session, so the model and the conversation history stay loaded between turns.

A session persists across turns. A turn that fails, or that you cancel, leaves the session and its conversation in place, so you continue in the same session rather than starting another. The session runs one turn at a time, so wait for a turn to finish before you start the next.

Editing inside a session stays scoped to the session. To make changes part of the app, you publish. To move them to another stage, you deploy.

## Session expiry

A session closes after a period of inactivity, and the edits you didn't publish are discarded. Publish before a long pause. To continue, start a new session and load the app again. The new session loads the app's most recent revision, so it includes changes that others published from ODC Studio.

Work on one app in one session at a time.

Close a session once its work is published, or once you no longer need it. An open session keeps server resources allocated until it times out. Publish before you close a session, so your changes become part of the app.

If a session returns wrong or empty results, or references something that doesn't exist, cancel the turn, close the session, and then start a new session. A new session loads the current app model.

## Task sequence for delegated edits {#why-this-matters-for-your-prompts}

The agent sends each edit to Mentor, which modifies the model. Treat each task as a sequence: inspect the app, delegate the edit to Mentor, then publish to persist the change. Across a multi-step change, publish between major steps to keep your changes.

When a turn reports success, confirm that the change was applied before you move on. A turn can finish without applying the edit, so read the result the turn returns, or inspect the app.

A Mentor turn runs for a couple of minutes, and complex UI work can take several turns, so expect a multi-step change to take time.

Before a publish, deploy, or rollback, the agent is instructed to restate the operation and wait for your confirmation. Reads, searches, and edits inside a session run immediately. For more information about how confirmation works, refer to [Governance in OutSystems MCP](governance.md#confirming-state-changing-operations).
