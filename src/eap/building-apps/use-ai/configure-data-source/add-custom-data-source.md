---
helpids: 30547
summary: In this article you will learn how to add custom data source to the AI Agent Builder app.
tags: ai agent builder, custom data sources, database connectivity, data synchronization, api integration
guid: 58f21b67-9a0a-4636-8131-810ac77f6f8e
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - apply
---

# Add a custom data source to the AI Agent Builder app

Adding a custom data source to the AI Agent Builder enables connections to any database. You can leverage your custom data source to introduce capabilities that aren’t supported by other data sources, for example, vector search and text document chunking as well as, allowing for programmatic synchronization of documents.

This article explains how to add a custom data source. It is intended for administrators and DevOps engineers responsible for setting up the AI Agent Builder app.

## Prerequisites

Before you add a custom data source in the AI Agent Builder app, ensure you:

* [Build a data connector](#build-a-data-connector) in compliance with the [API Contract](aiab-api-contract.md) established by OutSystems.
* Gain access to the AI Agent Builder app with the Configurator role assigned in the ODC portal.

## Add a custom data source

To add a custom data source, follow these steps:

1. Log into the AI Agent Builder app.

1. Go to the **Configurations** tab.

    A list of all configured AI models and data sources is displayed.

1. Click **Add data source.**

1. Select **Custom connection**, and click **Confirm.**

1. Enter the data source details:

   * **Name** - An identifiable name for the data source.

   * **Description** - (Optional) Description of the data source.

   * **Endpoint** - URL of custom-built data connecter.
   
1. Click **Add header**

1. Enter the authentication header details:

   * **Name** - An identifiable name for the header.

   * **Value** - The authentication value of your custom-built data connector.

1. Click **Add data source**

The custom data source is added to your configurations.

## Build a data connector

1. Add your data to an AI search service provider of your choice. 

1. Build a data connector to that service in compliance with the OutSystems API contract

1. Authenticate and use your data connector in the AI Agent Builder.

For more information about the OutSystems API contract, refer to [OutSystems API Contract](aiab-api-contract.md).

## Next steps

* [Create an agent](../create-agent.md)

* [Integrate the agent into your app](../integrate-agent.md)
