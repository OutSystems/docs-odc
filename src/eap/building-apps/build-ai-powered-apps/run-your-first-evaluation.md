---
guid: 9c4e1f2a-7b6d-4c8e-a1f3-5e9d2c8b0a14
locale: en-us
summary: Run an agent evaluation in OutSystems Developer Cloud (ODC) in development using your agentic app, service action, and saved dataset, then review runs, overall scores, and judge criteria scores on the Evaluations tab.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9564-1916&p=f&t=Eg8vOD7VJBTISsgI-0
coverage-type:
  - apply
topic:
app_type: reactive web apps, mobile apps
platform-version: odc
audience:
  - Tech lead
  - Developer
tags:
  - Agentic
  - AI
  - Quality Assurance
  - Testing
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---
# Run your first evaluation

This article describes how to run an **agent evaluation** in the ODC Portal after you have a dataset saved for your agentic app and service action. The evaluation runs each test case in the dataset through your service action, then scores the outcomes against the criteria you defined. You can also cancel a run that is in progress and review the history of all runs for an evaluation, including how scores change as you refine your agent and dataset over time.

## Availability

Evaluation runs and the scores you review in the ODC Portal are available only in development. Agent evaluations are available for cloud, hybrid, and on-premises setups.

## Prerequisites

Before you run an evaluation, confirm the following:

* **Dataset**: A dataset saved in the ODC Portal for the agentic app and service action you plan to evaluate. If you still need to create or upload one, refer to [Create and manage datasets](construct-dataset.md).
* **Agentic app** and **service action**: The same pair linked to that dataset. The service action is the executable unit the evaluation runs against.
* **Published after feature release**: The target agentic app must be republished at least once after agent evaluations are enabled for your organization.

### Concurrency

You can run only one evaluation at a time per agent. If an evaluation is already running, wait for it to complete before starting another run.

### Permissions {#permissions}

Agent evaluations use the following permissions at the Organization scope: **View evaluations** and **Manage evaluations**. For more information about permissions, refer to [Roles and permissions for members](../../user-management/roles.md#permissions-registry).

## Judge criteria {#judge-criteria}

When you configure an evaluation, you choose which **judge criteria** the scoring models apply to each test case in your dataset. The following table summarizes each criterion.

| Judge criterion | Description |
| --- | --- |
| **Correctness** | Validates that responses match the expected outcome semantically using LLM-as-judge. For example, when the expected outcome is that a customer order is shipped, an answer that the package is in transit passes if it matches that fact. An answer that claims the order is canceled fails. |
| **Safety** | Checks for harmful, toxic, or inappropriate content in the response. For example, if the user prompt tries to elicit insults or instructions to cause harm, a response that refuses or stays neutral passes. A response that supplies hate speech or dangerous instructions fails. |
| **Guidelines** | Evaluates the response against custom guidelines defined per test case. |
| **Relevance to Query** | Measures how relevant the response is to the input query. |
| **Tool Trajectory** | Validates that the agent called the expected tools during execution. |

## Create and save an evaluation

Use this procedure to create an evaluation in the ODC Portal, attach your **dataset**, and choose **judge criteria** so the platform scores agent outputs against your expectations.

To create and save an evaluation, follow these steps:

1. In the **ODC Portal**, navigate to **CREATE** > **Analyze** > **Agent evaluations**.
1. Select **Create evaluation**.
1. Enter the **Name** and the **Description** (optional) of the evaluation.
1. Select the **Dataset** for this evaluation.
1. Select the **Judge criteria** to use. Refer to [Judge criteria](#judge-criteria) earlier in this article for what each option measures.
1. Click **Save**.

![ODC Portal screen showing the Create evaluation form with highlighted fields for name, dataset, judge criteria, and the Save button.](images/create-evaluation-pl.png "Create evaluation form in ODC Portal")

After you save, the evaluation is stored with your dataset and judge criteria selections. When you run it, the platform uses those choices to score each test case. You can run the same evaluation again whenever you need to. Each run appears in the run list with its own scores.

## Start a run

To start an evaluation run, open the evaluation and select **Run evaluation**. The run appears in the **Runs** tab with a **Running** status, a progress indicator, and a **Started on** timestamp.

If the dataset has a **setup** action configured, the platform executes it before any test cases run. If setup fails, the entire run is aborted — refer to [Run failure states](#run-failure-states) for details.

## Cancel a run

If you triggered a run with the wrong dataset, or a run is taking longer than expected, you can stop it before it finishes.

To cancel a run in progress:

1. Open the evaluation that's running and you want to cancel, in the **Evaluations** tab.
1. In the evaluation details screen, you can see a card for each run for that evaluation.
1. Click **Cancel** on the card corresponding to the evaluation that's running and you want to cancel.

The run stops and transitions to **Cancelled** status. A **Finished on** timestamp appears on the card.

**What happens when you cancel:**

* If setup was still executing, it is aborted.
* Test case execution stops as soon as possible for any cases still in progress.
* If the dataset has a **teardown** action configured, it runs even after cancellation — to leave the environment in a clean state.
* No test case scores are returned for a cancelled run.

## Review evaluation results {#review-evaluation-results}

To review scores, select the **Evaluations** tab in the **ODC Portal**. Each evaluation lists its runs, the **overall score**, and the **judge criteria** scores.

To review scores, go to the **Runs** tab inside an evaluation. Each run card shows the run status, the **Started on** timestamp, and — once the run has ended — a **Finished on** timestamp alongside the status badge. Completed runs show the **overall score** and the **judge criteria** scores. Select a run to open the full report and review per-test-case results.

### Run statuses

Each run can move through the following statuses.

| Status | What it means |
| --- | --- |
| **Running** | The run is in progress. Setup, test cases, or judging may be executing. |
| **Completed** | All test cases executed and were scored. Results are available. |
| **Failed** | The run did not complete. This can happen if setup failed, if test case execution encountered an error, or if the judging step failed. The run report explains which stage failed. |
| **Cancelled** | The run was stopped by the user. No scores are returned. |

You can filter the Runs tab by status, including **Cancelled**, to focus on a specific subset of runs. Use the date presets at the top of the tab to narrow the view by time window. Run data is stored for 30 days.

### Comparing runs across dataset versions

Each run card shows the **dataset name** and the **dataset version** — the timestamp of the last time the dataset was modified before that run was triggered. This lets you see at a glance whether two runs used the same test cases.

If you edited the dataset between runs, the version timestamps differ and the runs aren't directly comparable. Adjust expected outputs in the dataset only when the correct agent behavior has intentionally changed, so that version differences stay meaningful.

## Run failure states {#run-failure-states}

A run can fail at different stages. The run card and expanded run details explain which stage failed so you know where to investigate.

### Setup failed

When the setup action could not complete:

* The run shows as **Failed**.
* No test cases executed and no scores are available.
* Expanding the run shows an alert and **Setup: Failed** in the details.
* Teardown still ran after the setup failure to clean up any partial environment state.

To investigate, check the logs for the app that contains the setup service action.

### Teardown failed

When the evaluation completed but the teardown action could not complete:

* The run shows as **Completed**. Test case scores are valid and available.
* Expanding the run shows an alert and **Teardown: Failed** in the details.
* The cleanup step did not finish. Test data or environment state from this run may still be present in your external system.

To investigate, check the logs for the app that contains the teardown service action, and clean up the environment manually if needed.

## Related resources

* For more information about how the run and the **platform judge** fit together, refer to [Agent evaluations](about-agent-evaluations.md).
