---
summary: OutSystems Developer Cloud (ODC) leverages event-driven architecture for real-time data processing and app automation.
tags:
locale: en-us
guid: 5bfd1452-1ff8-4180-a437-65603671437b
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=5324%3A590&mode=design&t=2ZbamW0IMDYxtZbC-1
---
# Events

In ODC Studio, an event represents a change within an app. Events help track app changes and trigger specific actions in response to these changes. For example, creating a new account(event) triggers generating a bank account number(response) in a finance app.

Events facilitate process automation without impacting the user experience and enable real-time data processing. For example, you can use back-end events to automate monthly billing for subscribers in a streaming app.

The Screens and Blocks follow a lifecycle composed of stages, allowing you to act upon those stages using event handler actions. These event handlers provide visibility into the lifecycle of screens and blocks, allowing you to implement logic when certain events occur.

In ODC, events follow the publish/subscribe (pub/sub) paradigm, allowing asynchronous communication. This model simplifies the development of highly functional and architecturally complex apps within cloud-native architectures.

## Event-driven architecture

Event-driven architecture (EDA) promotes app independence, with each component having minimal dependencies. EDA enhances team autonomy by enabling the development of apps with loosely coupled dependencies. EDA follows a reactive programming model, where decoupled components offer a dynamic approach to event handling.

![Diagram showing the flow of events from a producer app to a message broker and then to subscriber apps with event handlers.](images/events-architecture-diag.png "Event-Driven Architecture Diagram")

Publisher apps define events and triggers. When an event triggers, the publisher publishes the event in the message broker. Subsequently, subscribers interested in specific events can subscribe to them through the message broker.

Subscribers define event handlers to react to events asynchronously through server actions. The subscriber app consumes an event sent by the publisher app, creating a weak reference.

For example, in a finance app, you must generate a bank account number for each new account. In this example, creating a new account is an event trigger within the publisher app. A new account triggers an event, and the publisher publishes the event to a message broker. Subsequently, subscribers interested in specific events subscribe to them through the message broker. To respond to this event, subscribers use event handlers, such as generating a new bank account number.

<div class="info" markdown="1">

Publisher app can also subscribe to events from other apps.

</div>

Events are triggered, and event handlers execute them asynchronously, enabling subscribers to receive and process events independently without waiting for the publisher to finish processing them.
