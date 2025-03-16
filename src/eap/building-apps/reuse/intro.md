---
summary: OutSystems Developer Cloud (ODC) distinguishes between strong and weak dependencies based on how producers expose functionality to consumers.
locale: en-us
guid: 908a38d8-c72c-47c4-81e1-63bccbaa4d1d
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
tags: application architecture, dependency management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
topic:
  - dependencies
---

# Understand strong and weak dependencies

Strong and weak dependencies are related to how information is exposed and used in OutSystems by producers and consumers. Producers typically expose functionality for consumers to use. For example, a Producer might be a Library that implements and exposes functionality, and the consumer is an app using the exposed functionality.

Depending on the type of element exposed by a producer, OutSystems generates a **strong** or a **weak** dependency between the producer and its consumers.

## Strong dependencies

A strong dependency means a **strong relationship** between the consumer and producer where a consumer is directly dependent on the producer. If the producer is changed or updated, it may impact the consumer that depends on it. The producer's code is executed in the same runtime request as the consumer.

Dependencies between apps and libraries or between libraries are always strong dependencies. The producer's code is necessary for compiling the app. For example, you need the compiled code of a Server Action in a Library to call it from within the consumer app.

In runtime, the consumer needs to know both the **signature** and the **implementation** of the element exposed by the producer to reuse it. For this reason, when the [producer changes the signature or the implementation](handle-changes.md#change-functionality-in-the-producer-module) of the exposed element, the consumer needs to refresh the dependency on the producer and to be republished to start using the latest producer version.

## Weak dependencies

A weak dependency means a **weak relationship** between the consumer and producer, meaning that any new change on the producer becomes immediately available to all consumers without requiring a new compilation and deployment of the consumer.

Dependencies between apps are always weak dependencies, following a micro-services architecture pattern. The consumer app does not require the producer's code for building purposes. Still, it requires knowing the signature of the reusable app elements (Service Actions and Entities) to reuse those elements.

In runtime, the consumer only needs to know the **signature** of the element to reuse it. For this reason, when the [producer changes only the implementation](handle-changes.md#change-functionality-in-the-producer-module) of the exposed elements, the consumer immediately starts using the latest producer version in runtime.