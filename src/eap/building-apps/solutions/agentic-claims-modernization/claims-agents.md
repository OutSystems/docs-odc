---
summary: OutSystems Developer Cloud (ODC) claims agents handle intake, evidence analysis, claim summaries, policy questions, and fraud decision support.
tags:
  - Agentic
  - AI
  - Architecture
locale: en-us
guid: ddde04ce-fbce-4050-85dc-00d090024b7e
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Architect
  - Developer
  - Tech lead
content-type:
  - conceptual
coverage-type:
  - understand
topic:
  - agentic-claims-modernization-claims-agents
isautopublish: true
---

# AI agents in the First Notice of Loss solution

The claim flow uses four AI agents, each with a defined responsibility. Use this page to understand the role of each agent and when it runs. For more information about the phases and statuses a claim goes through in the solution, refer to [Claim flow in the First Notice of Loss solution](claims-flow-and-status.md).

## Claim intake conversation {#claims-conversation-agent}

The Claims Conversation Agent runs the conversation in which the policyholder reports a loss.

* **Role**: Customer-facing. The agent is the only one that talks to the policyholder. It proposes status changes, and the core services apply them.
* **Responsibility**: Guides the policyholder through a first notice of loss as a conversation, one message at a time, based on the current status of the claim. For each message, the agent returns one structured response.
* **When it runs**: From the first message in the Initiation phase, which can start before any claim exists, until the policyholder submits the claim in the Wrap-up phase. In every phase, the agent follows the rule for the current status of the claim.

## Photo and document analysis {#claims-document-and-evidence-agent}

The Claims Document and Evidence Agent analyzes the photos and documents that the policyholder submits.

* **Role**: Back-office. The agent reviews each submission without interacting with the policyholder.
* **Responsibility**: Classifies each photo and document individually, extracts its fields, assesses its quality, and returns a verdict of valid, invalid, waived, or pending. The agent assesses each submission, not the claim as a whole, and reports integrity concerns to the adjuster as observations.
* **When it runs**: In the Evidence phase, each time the policyholder adds a photo or document.

## Claim summary {#claims-damage-report-agent}

The Claims Damage Report Agent writes the claim summary that the policyholder reviews before submitting the claim.

* **Role**: Back-office. The agent runs in the background.
* **Responsibility**: Writes a short narrative for the policyholder that covers the incident and the interaction with the other party or the submitted documents. The agent bases the summary on the evidence collected in the conversation, reports only the facts that the evidence shows, and saves the summary as the loss description of the claim.
* **When it runs**: At the end of the Evidence phase, so the summary is ready for the **Claim summary** card in the Wrap-up phase.

## Policy questions and coverage checks {#claims-policy-and-fraud-agent}

The Claims Policy and Fraud Agent answers questions about the policy and, when enabled, reads the policy document to check coverage.

* **Role**: Back-office. The Claims Conversation Agent passes the policyholder's policy questions to this agent during the conversation.
* **Responsibility**: Answers the policyholder's questions about the policy from the policy document. If the Claims Services setting `GetCoveragesFromPolicyDoc` is `True`, the agent also reads the policy document and returns the coverages that the policy elects. The default is `False`, and the solution then reads the policy coverages synchronized from the core system instead.
* **When it runs**: When the policyholder asks a policy question. If the `GetCoveragesFromPolicyDoc` setting is `True`, also in the Triage phase, when the solution checks the policy.

### Full policy and fraud analysis {#full-policy-and-fraud-analysis}

The Claims Policy and Fraud Agent includes a full policy and fraud analysis for the decision support phase, which happens after the claim is submitted and outside this solution. No component of the solution calls the analysis, so the agent doesn't produce a fraud assessment while the policyholder files the claim. To add decision support to your claim handling, call the `CallFullPolicyAndFraudAnalysis` entry of the agent from your own logic, and pass the `ClaimsOccurrenceId` of the claim.

The analysis reads the claim data from Claims Services and returns one decision-support packet for the adjuster. The packet contains the following:

* Policy-in-force validation, and a coverage decision for each item with the deductible applied.
* A fraud-likelihood score from 0 to 100, built from observed indicators and mitigating factors.
* A severity tier from 1 to 4 and a reserve range from low to high.
* Anomalies and information gaps for the adjuster.

The analysis recommends and uses neutral wording, such as "warrants review", for fraud indicators. The adjuster decides the claim action, and your logic stores the packet.

## Cards in the conversation {#cards-in-the-conversation}

Mobile Insurance renders the structured response of the Claims Conversation Agent as a conversation, including the following cards:

* **Claim summary**: Shows the claim and its summary, and the **Submit** button.
* **Car rental**: Shows the rental options and books the reservation.
* **Roadside assistance**: Shows the tow details and books the tow.
* **Evidence gallery**: Opens the photo capture for the vehicle.
* **Call emergency**: Shows the emergency call screen when the safety override fires.
