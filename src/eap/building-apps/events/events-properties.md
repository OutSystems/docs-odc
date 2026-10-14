---
guid: b4aafec5-ef56-4f96-9359-0e30e838f07e
locale: en-us
summary: "OutSystems Developer Cloud (ODC) event properties: payload (10 KB), queue capacity (10,000), delivery retries, and execution limits."
figma:
coverage-type:
  - remember
  - evaluate
topic:
  - odc-event-limits
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
tags:
  - Events
outsystems-tools:
  - odc studio
  - odc portal
  - mentor studio
helpids:
isautopublish: true
---
# Properties of ODC events

The following table lists the limits that apply to every ODC event, whether you create the event with Mentor Studio or manually in ODC Studio.

| Properties | Description |
| --------------- | --------------- |
| Event payload | The maximum payload size is 10KB per event. If the size exceeds the maximum, you must refactor the event to reduce the payload. Only primitive data types are supported as event parameters. Binaries, structures, lists, and entity records cannot be passed as event parameters. A maximum of 2000 characters are allowed for text parameters. |
| Event queue | Each event has its own queue.The maximum number of events stored in a queue is 10000 per event type. |
| Event delivery | Each event is delivered only once to consuming apps. A maximum of 10 retries is attempted per event. The intervals between retry attempts are determined by the backoff policy (2, 4, 8, 16, 32 min), and the interval stays at 32 minutes for the 6th to the 10th retry. The delivery order of the events is not guaranteed. |
| Event execution | Each app can concurrently handle 100 events. The maximum duration of each event execution is 2 minutes. |

## Correct event property output

The platform guarantees that the model is valid, and you decide whether an event stays within these limits. The following checks are examples, not a complete list.

* **Payload.** The event input parameters use basic data types, and Text parameters hold at most 2000 characters. The payload stays below 10KB.
* **Queue.** The producer triggers events at a rate that the consumers handle, so the queue stays below 10000 events for each event type.
* **Delivery.** The handler tolerates the retry and backoff policy, because the platform retries delivery up to 10 times. The handler doesn't depend on the delivery order.
* **Execution.** Each handler completes within 2 minutes, and the handling load stays within 100 concurrent events for each app.

## Related resources

The following resources describe event architecture, event implementation, and what the platform guarantees and what you check in a Mentor Studio proposal.

* [Event-driven architecture in ODC](backend-events.md)

* [Implement events in ODC](implement-events.md)

* [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md)
