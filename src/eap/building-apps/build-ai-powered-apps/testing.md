---
guid: c3d9116b-e78e-4c4f-95af-5953916950df
locale: en-us
summary: Test agentic apps in ODC Studio using an auto-generated test app for quick validation.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=8046-10&t=i5iZDDNuznYYyXBM-1
coverage-type:
  - understand
  - apply
  - evaluate
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - full stack developers
tags: agentic apps testing, quick validation, development lifecycle, odc studio, automated test app
outsystems-tools:
  - odc studio
helpids:
---
# Test agentic apps

Testing your [agentic app](agentic-apps.md) in OutSystems Developer Cloud (ODC) is a key part of the development lifecycle. ODC Studio streamlines this process by automatically generating a test app. With this app, you can validate your agentic app's behavior, see how it responds to prompts, and verify its functionality. This removes the need to manually create and deploy a separate app just for testing. Keep in mind that this test app is for validation only. To use your agentic app's capabilities, you must build a consumer app that integrates its logic.

Adopting a testing practice has direct advantages:

* **Accelerate development:** Quickly see how the agentic app performs, which speeds up development and iteration.

* **Confirm reliability:** Validate your agentic app's behavior directly in ODC Studio before deploying it to production.

* **Ensure performance:** Ensure the agentic app provides consistent, accurate, and relevant responses across various scenarios.

## Test your agentic app

This section guides you through the options for testing your agentic app in ODC. After you publish your agentic app, click the **Test agent** button in ODC Studio. This gives you two ways to validate its functionality: using a test app or using one of your own apps.

### Test app

ODC creates a temporary test app. This option is ideal for:

* Quickly validating an agent app's responses and logic.

* Simple to medium-complexity testing scenarios.

* Testing without needing to build a separate user interface first.

This test app is a shortcut for rapid validation, not for simulating complex, real-world use cases. For the generation to succeed, your Service Action must follow specific naming conventions. For more information about test app requirements, refer to [Test app prerequisites.](#prerequisites)

### Use your own app

If another app in the same stage already consumes your agent app's Service Action, you can use that app as your test environment. Use this approach for:

* Simulating real-world user interactions and complex scenarios.

* End-to-end testing within your existing app's context.

When using your own app, the Service Action parameters do not need to follow any specific naming convention.

## Test app prerequisites { #prerequisites }

* Ensure you have a configured and published agentic app in your ODC app.

* The exposed Service Action must include the following parameters for the test app to generate successfully. The names and data types must be an exact match.

|                   |             |           |
| ----------------- | ----------- | --------- |
| Type of Parameter | Name        | Data type |
| Input             | `SessionId` | Text      |
| Input             | `UserInput` | Text      |
| Output            | `Response`  | Text      |

You can include more parameters in your Service Action as needed.

## Choose a Service Action to test

After you select which app to use for testing, ODC determines which public Service Action to connect to.

* **If your agentic app has one public Service Action**: The selected app launches in a new browser tab, ready to test that action.

* **If your agentic app has multiple public Service Actions**: A dialog appears in ODC Studio prompting you to choose one. After your selection, the selected app launches in a new browser tab.

## Test your changes

ODC streamlines the process of testing iterative changes to your agentic app. If you already have a test running in a browser tab, you can quickly validate your updates.

1. Modify your agentic app in ODC Studio and publish the changes.

1. After publishing, click the **Test agent** button again.

Instead of repeating the initial setup, ODC sends you directly to the running app. The app is automatically refreshed with the latest changes, bypassing the selection dialogs and allowing you to test your modifications immediately.

## Understand the test app

The user interface of the test app changes depending on the input parameters of the Service Action you test. The app displays one of two views: a simple chat interface or a chat with structured inputs.

### Chat interface

If your Service Action has no input parameters beyond the required `SessionId` and `UserInput`, the app shows a chat window. Use this interface to type prompts and directly test your agent app's conversational abilities.

### Chat with structured inputs

If your Service Action includes additional input parameters, the app displays an input panel next to the chat window. First, fill in the fields in this panel with your test data, and then send your prompt through the chat. This layout helps you test more complex scenarios by simulating how the agentic app responds to specific data inputs, including edge cases and potential errors.

![ODC Studio test app interface showing input fields for AccountID, Input1, Input2, Structure 1, and Input4, alongside a chat window for user prompts.](images/chat-odcs.png "Chat with Structured Inputs Interface")
