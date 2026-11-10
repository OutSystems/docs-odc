---
summary: OutSystems Developer Cloud (ODC) First Notice of Loss setup loads sample data and tests the Claims Conversation Agent in Mobile Insurance.
tags:
  - Agentic
  - AI
  - Forge
  - Mobile app
  - Settings
  - Testing
  - Timers
locale: en-us
guid: a88b6944-604f-4906-a9ba-ba78cd7922f7
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - forge
  - odc portal
  - odc studio
content-type:
  - procedure
coverage-type:
  - apply
topic:
  - agentic-claims-modernization-setup
isautopublish: true
---

# Get started with the First Notice of Loss solution

After you install the [Agentic First Notice of Loss solution](claims-overview.md), set it up in your tenant and test it with sample data. The setup enables sign-in as a demo user, loads the sample data, and confirms that the app and the Claims Conversation Agent work together.

To set up and test the solution, complete the following tasks in order:

1. Open the main app.
1. Set the development domain.
1. Load the sample data.
1. Confirm the setup.
1. (Optional) Configure AI models.

## Prerequisites {#prerequisites}

Before you start, do the following:

* Make sure the [Agentic First Notice of Loss (ODC)](https://www.outsystems.com/forge/component-overview/25993/agentic-first-notice-of-loss-odc) solution is installed in your tenant.
* Make sure the trial AI model `TrialClaudeHaiku4_5` is available in your tenant. The agents use this model by default. If the model isn't in the list of AI models, [add it](../../build-ai-powered-apps/add-ai-models.md#add-ai-models).
* Find the hostname of your tenant. In the URLs on this page, replace `TENANT_HOSTNAME` with this hostname.

<div class="info" markdown="1">

If your tenant uses portfolios, install the solution in the same portfolio where the trial AI model is deployed.

</div>

## Open the main app {#open-the-main-app}

The main app of the solution is Mobile Insurance. To open it, go to `https://TENANT_HOSTNAME/CloneOfMobileInsurance` in your browser. The app shows its login page.

## Set the development domain {#set-the-development-domain}

Set the `DevelopmentDomain` setting so that the login page shows a button to sign in as a demo user.

1. In ODC Portal, open the Solutions Common Services app.
1. Edit the `DevelopmentDomain` setting and replace its value with the hostname of your tenant, which ends in `.app`.
1. Wait until the setting takes effect, and then refresh the app.

The login page shows the button **Log in as Matthew Shelton**. If the button doesn't appear, wait a little longer and refresh the app again, because the setting can take a short time to take effect.

<div class="warning" markdown="1">

Use the `DevelopmentDomain` setting only for testing in development and demo tenants. The setting adds a button that signs in as a demo user.

</div>

## Load the sample data {#load-the-sample-data}

Load the sample data so that the app has policyholders, policies, and claims to work with.

1. In ODC Portal, open Clone of Insurance Sync Services.
1. Find the `SyncScheduler` timer and run it. The timer imports the sample data, first for Solutions Common Services and then for Claims Services.

The first successful run imports the sample data, and later runs import only changed records. To reload the Claims sample data, run the `BootstrapData` timer in Clone of Claims Services. To remove the conversations and claims that you created while testing, run the `ClearAllConversationClaims` timer in the same app.

## Confirm the setup {#confirm-the-setup}

With the sample data loaded, check that the app and the Claims Conversation Agent work together.

1. Open the Mobile Insurance app in your browser.
1. Click **Log in as Matthew Shelton**.
1. Open the chat. The Claims Conversation Agent greets you and invites you to ask about your policy or report an incident.

## Configure AI models {#configure-ai-models}

The agents use the trial model `TrialClaudeHaiku4_5` by default, so you can try the solution without adding an AI model from a provider. Trial models work only in the development stage, and they stop working when their usage limit is reached.

Before you use the solution beyond development, replace the trial model in each of the four agents. For more information about the agents, refer to [AI agents in the First Notice of Loss solution](claims-agents.md).

1. In ODC Portal, [add an AI model](../../build-ai-powered-apps/add-ai-models.md) from a supported provider.
1. In ODC Studio, open the agent you want to configure.
1. Select your AI model for the agent.
1. Publish the agent.
1. Repeat the steps for each of the other agents.

## Next steps {#next-steps}

You've set up the solution and confirmed that a policyholder can start a conversation with the Claims Conversation Agent.

To learn how the solution is built, how a claim moves through it, and what each agent does, refer to:

* [Architecture of the First Notice of Loss solution](claims-solution-architecture.md)
* [Claim flow in the First Notice of Loss solution](claims-flow-and-status.md)
* [AI agents in the First Notice of Loss solution](claims-agents.md)
