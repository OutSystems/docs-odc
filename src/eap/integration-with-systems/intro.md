---
summary: Explore how OutSystems Developer Cloud (ODC) facilitates integration with external systems.
tags: integration, external systems, cloud development, outsystems, api
locale: en-us
guid: BC301FD5-5457-4C74-BCE8-0DB525F9503B
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - none
coverage-type:
  - none
---

# Integration with external systems

OutSystems Developer Cloud (ODC) provides various options for integrating with your external systems. Depending on your specific requirements, you can choose the most suitable option for a seamless integration:

* [AI Integration](../building-apps/build-ai-powered-apps/intro.md) - Build intelligent apps by connecting your [AI models](../building-apps/build-ai-powered-apps/ai-models.md), [agentic apps](../building-apps/build-ai-powered-apps/agentic-apps.md), and [grounding data](../building-apps/build-ai-powered-apps/agentic-apps.md#grounding).

* [OutSystems Data Fabric](external-databases/intro.md) - Enables you to query your external data seamlessly and use [data mashup](../building-apps/data/fetch-data/data-mash.md) to combine data from different sources. Take the following into consideration:

    * Make sure ODC [supports your external data sources](../getting-started/system-requirements.md#supported-external-data-sources).

    * When data mashup is required, make sure Data Fabric [record limit](../building-apps/data/fetch-data/data-mashup-errors.md) complies with your app needs.

* [REST APIs](consume_rest/intro.md) - Enables you to retrieve or manipulate information from external systems that provide REST APIs for that effect.

* [Custom code](../building-apps/external-logic/intro.md) - Enables you to integrate with your external systems for use cases that can't be fully covered using the above integrations.
