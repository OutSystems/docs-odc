---
summary: OutSystems Developer Cloud (ODC) claim flow maps four phases, AI agent tasks, emergency handling, evidence review, and claim statuses.
tags:
  - AI
  - Agentic
  - Mobile app
locale: en-us
guid: 40f32dc6-3d8c-4bbe-b54e-df4f69073fde
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/qNvoQig5kGad2lkuAU7c0W/banking-solution?node-id=95-613
audience:
  - Architect
  - Developer
content-type:
  - conceptual
coverage-type:
  - understand
topic:
  - agentic-claims-modernization-claims-flow
isautopublish: true
---

# Claim flow in the First Notice of Loss solution

A claim starts when the policyholder reports a loss, and it ends when the policyholder submits the claim for review. In between, the policyholder works with the Claims Conversation Agent in Mobile Insurance, and the solution creates the claim, analyzes the evidence, and writes the claim summary. The claim process follows four phases.

## Claim phases {#claim-phases}

The following table describes what each phase represents and who acts in it.

| Phase | What it represents | Actors |
| --- | --- | --- |
| Initiation | The policyholder opens a claim and the solution checks for an emergency. | Policyholder, Mobile Insurance, Claims Conversation Agent |
| Triage | The solution collects the facts, creates the claim, and checks the policy. | Policyholder, Claims Conversation Agent, Claims Services, Claims Policy and Fraud Agent when enabled |
| Evidence | The policyholder provides photos and documents that support the claim. At the end of the phase, the solution writes the claim summary. | Policyholder, Claims Document and Evidence Agent, Claims Damage Report Agent |
| Wrap-up | The policyholder reviews the summary and submits the claim, which hands it over to your claim management system. | Policyholder, Claims Services |

Within each phase, the claim moves through statuses, such as `InTriage` or `EvidencePending`, and the Claims Conversation Agent follows a rule for each status.

The solution covers the claim up to its submission. The data model also defines the phases for decision support, adjuster review, and committing and closing the claim, which happen outside the solution. The wrap-up hands the claim over to them. For more information about the agents, refer to [AI agents in the First Notice of Loss solution](claims-agents.md).

## Claim steps {#claim-steps}

The following diagram shows the steps of a claim, including the route for an emergency.

![Diagram of the claim flow in four phases, with lanes for the policyholder and the solution. In Initiation, the policyholder starts a claim in Mobile Insurance, and the solution greets them and checks for an emergency, which leads to a safety hold and a follow-up task. In Triage, the solution looks up the policy, the policyholder describes the incident, the solution creates the claim, checks the policy, and offers assistance services, and the policyholder accepts or declines. In Evidence, the policyholder captures photos and uploads documents, the solution analyzes the evidence and flags concerns, and then the solution writes the claim summary. In Wrap-up, the policyholder reviews the summary and submits the claim, and the solution sets the claim status to InReview, so the claim is pending adjuster review.](images/claims-flow-diag.png)

The process has the following steps:

1. The policyholder opens a claim in Mobile Insurance through a crash alert, a general chat, or an explicit request to start a claim. The Claims Conversation Agent greets the policyholder and checks for an emergency. If emergency services are required, the solution pauses the flow and raises a follow-up task to reach the policyholder.
1. The solution looks up the policy once and keeps it for the rest of the conversation.
1. The policyholder describes the incident in their own words. The agent collects details such as the type of incident, the location, and the date and time, asks follow-up questions to fill gaps, and confirms the details.
1. The solution creates the claim with a claim number, and then checks that the policy was active at the time of loss. If the policy lapsed or doesn't apply to the claim, the agent warns the policyholder and flags the claim for the adjuster. The flow continues.
1. The agent offers assistance services, such as roadside assistance and a rental car, and the policyholder accepts or declines each offer.
1. The policyholder captures photos of the damage and of the overall scene. The Claims Document and Evidence Agent checks the quality of each photo.
1. The policyholder uploads supporting documents. The Claims Document and Evidence Agent extracts their data, and a check on the document metadata flags any suspicion for the adjuster without notifying the policyholder.
1. The agent surfaces any skipped details without blocking the policyholder. The claim summary card shows the claim and the summary that the Claims Damage Report Agent writes. The policyholder submits the claim, Claims Services sends it to your claim management system, and the claim is pending adjuster review with the status `InReview`.

## Crash detection entry {#crash-detection-entry}

A claim can also open from a crash alert. The solution doesn't integrate a crash detection service, so it simulates the alert with a push notification. You trigger the simulated alert from the Start screen of Insurance Sync Services.

When the alert reaches Mobile Insurance, the policyholder chooses one of three options: an emergency call, getting assistance and filing a claim, or dismissing the alert. Only getting assistance creates a claim. Before the chat opens, Mobile Insurance creates the claim with the crash time, the device location, and the safety flags. The conversation then starts with the crash facts already recorded.

## Claim statuses {#claim-statuses}

Each claim has a status that shows where it is in the flow. The following diagram shows the statuses that the solution sets and the paths between them:

![State diagram of the claim statuses that the solution sets. A claim moves from Draft to InTriage, IncidentDetailsPending, RoadsidePending, RentalPending, EvidencePending, DocumentsPending, WrapUp, and InReview, and is then handed over for adjuster review. From Draft, an injury, an unsafe scene, or an emergency moves the claim to AwaitingSafety. From InTriage and IncidentDetailsPending, distress moves it to AwaitingSafety, and a claim that is out of policy moves it to ManualHandling.](images/claims-status-diag.png)

A claim moves to `AwaitingSafety` when there is an injury, an unsafe scene, an emergency, or distress, and to `ManualHandling` when it is out of policy. When the claim reaches `InReview`, the solution hands it over for adjuster review.
