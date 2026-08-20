---
summary: "ODC mobile app performance optimization best practices: lightweight init actions, balancing client and server processing, and preconnect for low-end devices."
guid: fb9e58d0-99b2-4d59-b218-bc74b3ff1ebb
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
tags:
  - Best Practices
  - Front-End
  - Mobile app
  - Optimization
  - Performance
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - evaluate
isautopublish: true
---

# Best practices for keeping mobile apps responsive

Mobile apps running on low-end devices and unreliable networks are especially sensitive to how much work happens on the client, how many resources the app loads, and how many round trips it makes to the server. Not every practice fits every app: apply them based on your device and network profiles, and validate the impact with real device testing before rolling out changes broadly.

## Keep initialization actions lightweight {#lightweight-initialization}

Heavy logic in **On Initialize** or **On Ready** blocks the UI from rendering until it completes, which is especially noticeable on low-end devices.

### Recommendations

Avoid blocking the UI by keeping **On Initialize** and **On Ready** actions minimal. Don't access screen data or perform blocking operations in these actions, and defer non-critical fetches until after the initial render.

### Benefits

The UI renders faster and feels more responsive, since the app isn't waiting on unrelated logic before showing the screen.

For recommendations on fetching screen data itself instead of in **On Initialize** or **On Render**, refer to [Best practices for loading data on mobile screens](loading-data-mobile.md#common-pitfall).

## Balance client-side and server-side processing by device profile {#balance-processing}

Client-side logic runs in the device's webview, so heavy computation slows down low-end devices even on a fast network. Server-side logic runs on infrastructure with more consistent processing power, but shifting everything to the server increases server load and increases the app's dependency on network availability.

### Recommendations

Move computationally heavy logic, such as data aggregation, transformation, or filtering, from client actions to server actions when targeting a user base with a significant share of low-end devices. Don't apply this as a blanket rule: weigh it against your actual device and network profiles, since it doesn't benefit apps that need to work reliably offline or on a slow network.

### Benefits

Low-end devices handle the app more smoothly because expensive logic no longer runs on constrained device hardware. The trade-off is a slight increase in server processing time, which is typically outweighed by a more stable client experience.

## Preconnect to known domains before they're needed {#preconnect-domains}

Establishing a DNS, TCP, and TLS connection takes time. If that negotiation only starts when the first request is made, the user experiences a delay on that first call.

### Recommendations

Use [required JavaScript](../../../integration-with-systems/javascript/use-external-lib.md), client-side JavaScript declared in a screen or block to extend it beyond built-in widgets, to open a preconnect hint, for example by injecting a `<link rel="preconnect">` element or using the equivalent Resource Hints API, for domains the app already knows it will call, as early as possible in the app's startup sequence.

### Benefits

The connection handshake happens before it's needed, reducing initial network lag and preventing bottlenecks caused by delayed connection setup during actual usage.

## Related resources {#related-resources}

To learn more about optimizing data loading and rendering on mobile screens, refer to [Best practices for loading data on mobile screens](loading-data-mobile.md) and [Best practices for rendering data on mobile screens](rendering-data-mobile.md).
