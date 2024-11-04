---
summary: OutSystems Developer Cloud (ODC) facilitates the creation and integration of AI agents through its AI Agent Builder tool.
tags:
locale: en-us
guid: 683e4fb2-5457-4952-8f98-0da719576379
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Using the AI Agent Builder 

With AI Agent Builder, you can combine AI model, instructions, additional data sources to create agents for a specific use case. You can then integrate the agent into your existing app to build generative AI applications. You also have the option to choose from a variety of [sample apps](intro.md#sample-apps) that closely matches your use case and download the OML. The OML file consists of entities, screens, call to an Agent, and an integration template for the external solutions in the app, such as Zendesk for Salesforce.

You can assign the following end user roles to manage the AI Agent Builder:

* **AIAgentBuilder**: Gives access to the AI Agent Builder and can create/manage agents but do not have permissions to create AI models and data sources.

* **Configurator**: Gives full access to the AI Agent Builder and can create/manage agents, AI models and data sources.

This article explains the overall process of using the AI agent builder to build generative AI applications.

## Prerequisites

Before using the AI Agent Builder, ensure you have:

* Access to the ODC portal.

* Access to the AI Agent Builder tool

## High-level process for using the AI Agent Builder

### Step 1: Install the AI Agent Builder app

1. Log into the ODC portal.

1. Install the AI Agent Builder app from the Forge. For detailed information on installing a Forge asset, refer to [Install or update a Forge asset](../forge/install.md).

1. Assign yourself the **Configurator** end-user role for the AI Agent Builder app. For detailed information about how to assign end-user roles in ODC portal, refer to [end-user roles](../../../eap/user-management/roles.md#end-user-roles)

1. Open the AI Agent Builder app in the ODC portal.
    
    1. From the home page of the ODC portal, Click **Apps**. A list of all apps display.

    1. Search for **AI Agent Builder**. 

    1. Click **AI Agent Builder** app. The AI Agent Builder app details page display.

    1. Click **View app**.

Now you are inside the AI Agent Builder app.

### Step 2: Configure the AI Agent Builder app

1. Log into the AI Agent Builder app. 

1. [Configure and add the AI model](configure-model/intro.md).

1. (Optional) [Configure and add the data source](configure-data-source/intro.md).

### Step 3: Choose and customize sample apps

1. Choose a sample app that closely matches your AI use case.

1. Preview the Gen AI feature of the app.

1. (Optional) Customize the agent template loaded on the app.

1. Test your agent in the playground and refine your instructions until the agent responds satisfactorily.

1. Save the agent and copy the Agent ID.

1. Download the app OML.

  (Or)

### Step 3b: Create your custom AI agent 

1. [Create an agent](create-agent.md) for your AI use case either from scratch or by using agent templates. Optionally, you can add a data source while creating the agent to improve the quality of the AI-generated response.

1. Test your agent in the playground and refine your instructions until the agent responds satisfactorily.

1. Save the new agent and copy the Agent ID.

### Step 4: Integrate the agent into your app 

For detailed information, refer to [Integrate the agent into your app](integrate-agent.md).

## Next steps

* [Configure AI model](configure-model/intro.md)

* [Configure data source](configure-data-source/intro.md)

* [Create an agent](create-agent.md)

* [Integrate the agent into your app](integrate-agent.md)
