---
guid: 7f2a9c01-8b4d-4e1f-9c3a-2d8e6f1a4b0c
locale: en-us
summary: Build a dataset as JSON that matches your service action interface so agent evaluations run consistent test cases and judge results against expected outputs and tool use.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9564-1843&p=f&t=Eg8vOD7VJBTISsgI-0
coverage-type:
  - apply
topic:
app_type: reactive web apps, mobile apps
platform-version: odc
audience:
  - tech leads
  - full stack developers
tags: agent evaluations, dataset, JSON, service actions, agentic apps
outsystems-tools:
  - odc portal
  - odc studio
helpids:
isautopublish: true
---
# Construct the dataset

A **dataset** is the benchmark you attach to an **agentic app** and a **service action** for agent evaluations. Each row is one test case. The dataset supplies values the platform passes into the service action during the run and the reference data the platform judge uses when it scores results.

## Prerequisites

Before you create a dataset, confirm the following:

* **Agentic app** and **service action**: The pair you plan to evaluate. You select the agent app and service action when you create the dataset in the ODC Portal, and the JSON you upload must match that service action's public interface.
* **Service action contract**: You know the service action input parameters, return structure, and tools in ODC Studio so the **`inputs`**, **`expectations`**, and tool entries in your JSON match the template from the **ODC Portal**.

### Dataset limits

Each dataset supports a maximum of **50 test cases**. The uploaded JSON file must not exceed **5 MB** in size. Whichever limit is reached first applies. You cannot delete a dataset while an evaluation that uses it is running.

### Permissions

Creating and uploading a dataset requires **Manage Evaluations** at the Organization scope (**View Evaluations** isn't enough). For more information, refer to [Run your first evaluation](run-your-first-evaluation.md#permissions).

For more information about how evaluations use a dataset during the run and during judging, refer to [Agent evaluations](about-agent-evaluations.md).

## Align the dataset with the service action

The dataset reflects the public contract of the service action you're evaluating, not the internal flow.

* **Inputs**: Values that match the service action input parameters for each test case.
* **Expected outputs**: Values the service action returns when behavior is correct (for example, the agent response your test expects).
* **Expected tool calls**: The tool behavior you treat as correct for that test case, when your scenario requires it.

The platform maps dataset fields to the **service action** interface. You don't configure column mapping yourself.

Because the **system prompt**, **user message**, and **grounding data** are produced inside logic at run time, they don't appear as separate fields you edit row-by-row in the dataset. You change those by changing the **service action** (or the elements it calls) in ODC Studio, then [run the evaluation again](run-your-first-evaluation.md) against the same or an updated dataset.

## Compare prompt or logic changes

The dataset holds **test cases and expected references**, not alternate prompt text.

For routine tuning, change **system prompts**, **user messages**, or **grounding** in **server actions** (or other logic) that your **service action** calls. That updates what the evaluation runs; you don't need to duplicate or rename the **service action**. After you publish in ODC Studio, [run the evaluation again](run-your-first-evaluation.md). Adjust **expected** outputs and **expected** tool calls in the dataset only when the correct behavior intentionally changes.

The **ODC Portal** ties each dataset to one **agentic app** and one **service action**. You keep using that same action across iterations; renaming is not required for prompt or inner-logic changes.

To compare two prompt strategies or two implementations **at the same time** without overwriting one another in code:

* Treat each executable variant as its own service action (or its own published logic) that the ODC Portal pairs with an evaluation and a dataset.
* Use datasets that exercise the same scenarios when you want a fair comparison, adjusting expected outputs and expected tool calls only when the new behavior intentionally changes the right answers.

## Design strong test cases

Strong datasets improve regression signal and make judge results easier to interpret.

* **Cover real scenarios** your users trigger, including typical and edge inputs.
* **Keep one intent per row** so a failed case points to a clear gap (wrong tool, wrong arguments, wrong final answer).
* **Stabilize expectations** when the correct answer is deterministic, use judgement-friendly expected text when the answer is naturally variable, per the judge options your organization enables.
* **Plan data dependencies** the service action needs (for example, records in a database or responses from dependencies). Setup and teardown of that data sit outside the evaluation feature scope. Your team supplies a consistent environment for the run.

## Example dataset JSON

The following example is for a fictional agentic app whose service action takes **`UserInput`** and **`SessionId`** and returns a text **`Response`**. The first test case expects the agent to call an order tool with specific arguments. The second expects a direct FAQ-style answer with **no** tool calls. Replace parameter names, response shape, **`expectedTools`** structure, and **`toolSet`** content with values that match your service action and the template you'll download from the ODC Portal.

```json
{
  "testCases": [
    {
      "name": "tc-order-status",
      "description": "Customer asks for shipment status using a known order number.",
      "inputs": {
        "UserInput": "Where is order SO-44192?",
        "SessionId": "sess-eval-001"
      },
      "expectations": {
        "expectedResponse": {
          "Response": "Order SO-44192 shipped on March 10 and is out for delivery. Tracking: https://example.com/track/SO-44192"
        },
        "guidelines": [
          "The answer must reference order SO-44192 and reflect that it's shipped or in transit.",
          "The answer must not claim the order was canceled unless fixture data says so."
        ],
        "expectedTools": [
          {
            "name": "FetchOrderStatus",
            "arguments": {
              "OrderNumber": "SO-44192"
            }
          }
        ]
      }
    },
    {
      "name": "tc-support-hours",
      "description": "General policy question that should not trigger order lookup tools.",
      "inputs": {
        "UserInput": "What are your support hours?",
        "SessionId": "sess-eval-002"
      },
      "expectations": {
        "expectedResponse": {
          "Response": "Support is available Monday through Friday, 9:00 to 18:00, GMT."
        },
        "guidelines": [
          "No order or account tools should run for this question.",
          "The answer must stay within the published business-hours policy."
        ],
        "expectedTools": []
      }
    }
  ],
  "toolSet": []
}
```

### Map to the template

* **`testCases`**: One object per row you want to run. Use **`name`** and **`description`** so humans know what each row validates.
* **`inputs`**: Values passed into the service action for that run. They must align with the service action's input parameters (here **`UserInput`** and **`SessionId`**).
* **`expectations.expectedResponse`**: The structured output the judge compares against the run (here a single **`Response`** field).
* **`expectations.guidelines`**: Free-text hints for the platform judge about what "good" looks like when the answer isn't an exact string match.
* **`expectations.expectedTools`**: The tool calls (or empty array) you treat as correct for that scenario. The exact JSON shape for each tool entry must match your product contract.
* **`toolSet`**: Reserved for tool metadata when your template requires it. The downloaded template defines usage.

## Upload the dataset in the ODC Portal

Use this procedure to create a dataset from a template file, upload your test cases as JSON, and save the dataset in the ODC Portal.

<div class="info" markdown="1">

Field names, nesting, and types for the JSON file follow the product contract for evaluations. Use the official schema or specification from engineering when you author files, and don't skip validating a small file before you upload a large benchmark set.

</div>

To create and save a dataset, follow these steps:

1. In the **ODC Portal**, navigate to **CREATE** > **Agents** > **Datasets**.
1. Select **Create dataset**.
1. Enter the **Dataset details**: **Name**, **Description** (optional), **Agentic app**, and **Service action**.
1. Download the template.
1. Edit the template JSON to add your test cases. For recommendations on coverage and expectations, refer to [Design strong test cases](#design-strong-test-cases) earlier in this topic.
1. Upload the completed JSON file.
1. Click **Save**.

![Create dataset screen displaying dataset details fields, the Download template button, file upload area, and the Save action highlighted.](images/create-dataset-pl.png "Create dataset form in ODC Portal")

After you save, the row data is read-only. To change test rows, prepare a new JSON file and follow your team's process for updating datasets (for example, creating a new dataset).

## Next steps

* To run an evaluation with your saved dataset, refer to [Run your first evaluation](run-your-first-evaluation.md).
