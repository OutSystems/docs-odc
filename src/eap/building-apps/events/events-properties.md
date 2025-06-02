---
guid: b4aafec5-ef56-4f96-9359-0e30e838f07e
locale: en-us
summary: This article describes the properties of ODC events
figma:
coverage-type:
  - remember
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
tags: odc events, event payload, event delivery, event queue, event execution
outsystems-tools:
  - odc studio
  - odc portal
helpids:
---
# Properties of ODC events

| Properties      | Description     |
|---------------|---------------|
| Event payload  | The maximum payload size is 10KB per event. If the size exceeds the maximum, you must refactor the event to reduce the payload. Only primitive data types are supported as event parameters. Binaries, structures, lists, and entity records cannot be passed as event parameters. A maximum of 2000 characters are allowed for text parameters.|
| Event queue  | Each event has its own queue.The maximum number of events stored in a queue is 10000 per event type. |
| Event delivery  | Each event is delivered only once to consuming apps. A maximum of 10 retries is attempted per event. The intervals between retry attempts are determined by the backoff policy (2, 4, 8, 16, 32 min). The delivery order of the events is not guaranteed.
| Event execution  | Each app can concurrently handle 100 events. The maximum duration of each event execution is 2 minutes.  |

## Additional resources

* [Event-driven architecture in ODC](backend-events.md)

* [Implement events in ODC](implement-events.md)
