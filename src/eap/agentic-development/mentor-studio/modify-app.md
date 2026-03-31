---
summary: Modify an existing app in ODC Studio using Mentor to generate and update logic, screens, and data structures through conversation.
tags: agentic development, code generation
guid: 8d4c9f3e-a521-4b8f-9e7a-6f2d8c1b5a09
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9351-10
topic:
  - creating-apps
  - outsystems-overview
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
audience:
  - frontend developers
  - full stack developers
helpids:
isautopublish: true
---

# Modify an app with AI in ODC Studio

In this tutorial, you use Mentor Studio to enhance an existing app. You transform a basic "Hello, world!" greeting into a personalized experience that asks for the user's name.

For background on how Mentor Studio works, refer to [AI development in Mentor Studio](how-it-works.md).

## Prerequisites

To complete this tutorial, you need:

* ODC Studio installed and connected to an ODC organization.
* The [Hello World app](../../getting-started/hello-world.md). If you haven't created it yet, follow that tutorial first.

## Use prompts to modify your app

With your "Hello, world" app open in ODC Studio, follow these steps to edit the app with AI:

1. Select the Mentor icon to open the Mentor panel.

    ![Mentor icon in ODC Studio interface.](images/toggle-mentor-ai-odcs.png "Toggle Mentor Studio in ODC Studio")

1. In the Mentor panel, enter the following prompt: "Add an input field for the user's name and change the greeting to say Hello followed by the name they entered". Press **Enter** to confirm and Mentor starts working on the code.

    ![Entering a prompt in the Mentor panel to edit the app.](images/enter-prompt-edit-app-odcs.png "Enter prompt in Mentor Studio")

1. Review the response and optionally select **View changes** to see what Mentor edited.

    ![View changes panel showing AI-generated code modifications.](images/review-ai-gen-code-odcs.png "View AI generated code in Mentor Studio")

    <div class="info" markdown="1">

    AI-generated code is non-deterministic, meaning Mentor may produce different results each time you send the same prompt. Your app's code and layout may differ from the examples shown in this tutorial.

    </div>

1. Select the **1-Click Publish** button to publish the app, then open the app in the browser.

    ![Updated app running in browser with personalized greeting.](images/ai-updated-app-browser-sa.png "AI Updated App in Browser")

## Next steps

You've successfully used Mentor to modify an existing app. To continue building with AI, describe your goals in the Mentor panel, review the generated changes, and iterate as needed.

For more information:

* [AI development in Mentor Studio](how-it-works.md) - Learn about the Mentor interface, workflow, and how to send feedback.
* [Capabilities and patterns for Mentor Studio](capabilities.md) - Review detailed examples and use cases for what Mentor generates.
* [Effective prompts for Mentor](../effective-prompts.md) - Strategies for writing prompts that produce accurate results.
