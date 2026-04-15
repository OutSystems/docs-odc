---
helpids: 30689
summary: Test and refine system and user messages in OutSystems Developer Cloud (ODC) easily using ODC Studio's Test area to ensure effective agent communication.
tags: ai agents, agentcore, outsystems developer cloud
guid: 554ca4b1-497a-48c9-8103-995f7552b3b0
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=8094-10&t=Y0y0hUAqxmoUyzXm-1
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - apply
content-type:
audience:
  - full stack developers
  - tech leads
  - backend developers
topic:
---
# Testing your messages

System and user messages are an essential part of making your Agentic app's response the best possible. To avoid a time-consuming process, ODC allows you to preview your messages before committing to them. This way, when you publish your agent, it has the right set of messages for your use case.

## How to test your messages in ODC Studio

You can test System messages, User messages, or both in the Test area. To test your messages on ODC Studio:

1. Inside your Agentic App, double-click on the Call Agent node within the Agent Flow. This opens the Call agent window:

    ![Screenshot of the Call Agent window in ODC Studio showing the AI model selection.](images/ai-model-odcs.png "Call Agent Window in ODC Studio")

1. Select the Test tab:

    ![Screenshot of the Test tab in ODC Studio where users can enter system and user messages to test.](images/test-prompt-odcs.png "Test Tab in ODC Studio")

1. In the Test, you can:

    1. Select from the AI model drop-down the model you want to use in your testing.
    1. Write the System Message you want to test.
    1. Write the User Message you want to test.
    1. Click Test to test your message(s).

**Tip:** You can copy any of your messages or test results by clicking the copy icon located next to the message or button in the answer. These are added to your clipboard.

<div class="info" markdown="1">

To [add a new AI model](add-ai-models.md), add it first in the ODC Portal. After, add it as a Public Element in your app.

</div>

## Testing example

In the following example, you can see a test for both a System message and a User message:

![Screenshot of a testing example in ODC Studio showing system and user messages with the AI model response.](images/test-example-odcs.png "Testing Example in ODC Studio")

Whenever you test messages, you'll get:

* The test response
* The time stamp of your request
* Information on the AI Model used on the test
* The number of input and output tokens used during the test
