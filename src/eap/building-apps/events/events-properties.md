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

**Event payload**: The maximum payload size is **10KB** per event. If the size exceeds the maximum, you must refactor the event to reduce the payload. Only primitive data types are supported as event parameters. Binaries, structures, lists, and entity records cannot be passed as event parameters. A maximum of 2000 characters are allowed for text parameters.

**Event queue**: The maximum number of events that are queued for a producer app is 10000. The event always remain queued in the position it was created (FIFO).

**Event delivery**: Each event is sent at least once to consuming apps. If event is not delivered, a maximum of 10 retries is attempted per event. The intervals between retry attempts are determined by the exponential backoff policy (2, 4, 8, 16, 32 min).  Once the event is consumed by an app, it won't be sent again.

Here's how the delays are calculated:

Retry 1: Occurs after a 2-minute delay from the initial failure.

Retry 2: Occurs 4 minutes after Retry 1 (a total of 6 minutes from the initial failure).

Retry 3: Occurs 8 minutes after Retry 2 (a total of 14 minutes from the initial failure).

Retry 4: Occurs 16 minutes after Retry 3 (a total of 30 minutes from the initial failure).

Retry 5: Occurs 32 minutes after Retry 4 (a total of 62 minutes from the initial failure).

Retries 6 through 10: Each subsequent retry (from Retry 6 up to Retry 10) will also occur 32 minutes after the previous retry. This indicates that the exponential increase in delay caps at 32 minutes. The delivery order of the events is not guaranteed.

**Event execution**: Each consumer app compute instance can concurrently handle a maximum of 100 events. The maximum duration for each event execution is 2 minutes.

 Additional app compute instances are launched up to the [capacity limits](../../getting-started/capacity-limits.md) to accommodate more concurrent events when demand is high.

## Related resources

* [Event-driven architecture in ODC](backend-events.md)

* [Implement events in ODC](implement-events.md)
