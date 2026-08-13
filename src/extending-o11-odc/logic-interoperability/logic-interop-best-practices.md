---
guid: d725b310-5f8b-48ed-9388-0a14a6fd3c02
locale: en-us
summary: "OutSystems platform logic reuse best practices: encapsulate REST APIs, secure endpoints with JWT, and version APIs to avoid breaking changes."
figma: https://www.figma.com/design/epaiN2jasbbKgJA0iSYfZn/Extending-with-ODC?node-id=2733-1204
coverage-type:
  - understand
  - evaluate
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
tags:
  - Authentication
  - Best Practices
  - Logic
  - Private Gateway
  - REST
  - Security
outsystems-tools:
  - service studio
  - odc studio
helpids:
isautopublish: true
---

# Best practices for reusing logic between O11 and ODC

This page describes development best practices to consider when [reusing logic between O11 and ODC apps](logic-interop.md).

## Encapsulate REST integrations into server actions {#encapsulate-rest}

To reuse business logic between O11 and ODC, encapsulate REST integrations for consumption by several apps. For example:

* When consuming the O11 exposed logic in ODC, encapsulate the REST integration within ODC libraries abstracting the API methods into server actions for consumption by web, mobile or agentic apps.

    ![Diagram showing ODC apps and an agentic app consuming O11 logic through ODC connector libraries that abstract the REST API](images/logic-interoperability-odc-o11-diag.png "ODC Consuming O11 Logic via Connectors")

* When consuming ODC exposed app or agent logic in O11, encapsulate the REST integration within O11 integration service modules abstracting the API methods into server actions for consumption by web or mobile apps.

    ![Diagram showing O11 apps consuming ODC agentic app logic through O11 connector service modules that abstract the REST API](images/logic-interoperability-o11-odc-diag.png "O11 Consuming ODC Logic via Connectors")

## Secure your REST APIs {#authentication}

When **consuming O11 logic in your ODC apps**, use a [secure connection](logic-interop-secure-connection.md) to route the REST API requests over a private gateway (this option is only supported when consuming O11 logic in your ODC apps).

Additionally, to maintain the integrity and confidentiality of your sensitive data, protect your endpoints from unauthorized access. Token-based authentication with [JSON Web Tokens (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token) provides a flexible way to authenticate callers and enforce authorization on every request.

See the following development patterns for guidance:

* Exposing O11 logic to ODC:

    * [Securing exposed REST APIs in O11 with JWT-based tokens](https://www.outsystems.com/tk/redirect?g=5f8c0c2b-41e0-4a0d-9b3b-2f5a6a1d9f11)
    * [Securing consumed REST APIs in ODC with JWT-based tokens](../../eap/integration-with-systems/consume_rest/token-based-auth-consume-dev-pattern.md)

* Exposing ODC logic to O11:
    * [Securing exposed REST APIs in ODC with JWT-based tokens](../../eap/integration-with-systems/exposing_rest/token-based-auth-expose-dev-pattern.md)
    * [Securing consumed REST APIs in O11 with JWT-based tokens](https://www.outsystems.com/tk/redirect?g=e475d7de-23dc-40ff-9308-0c64c3ae6c87)

## Minimize impacts of changes in exposed APIs {#minimize-impacts}

When reusing business logic between O11 and ODC, there are some scenarios where changing your exposed REST APIs can break the consumer logic. When this happens, minimize the breaking changes by creating a new API version and providing a transition period for consumers to migrate to the new version. A new version keeps the existing contract available to current consumers while the change ships separately, so nothing breaks until each consumer migrates on its own schedule.

Follows some examples of exposed API changes that impact consumers and how to minimize them:

* To **change the endpoint path or authentication**, create a **new API version with the same methods**.

    Consumers on the old version keep calling the original path and authentication until they migrate, so you avoid an immediate outage for every existing integration.

* To **change the name of a method**, create a **new API version with the new method name**.

    Consumers reference methods by name, so renaming a method breaks every existing calls. The old version keeps the original name available until consumers switch to it.

* To **remove or add a mandatory parameter or structure field**, create a **new API version** with the changed parameters.

    Existing consumers send or expect payloads shaped by the current contract, and a mandatory field change makes their requests fail validation. The previous version keeps that contract intact so current traffic isn't rejected.

* To **change the data type of a mandatory field**, create a **new API version** with the new data type.

    Consumers parse the field as its original type, so a type change causes parsing failures or silently wrong values. The previous version keeps the original type so existing consumers keep parsing correctly.
