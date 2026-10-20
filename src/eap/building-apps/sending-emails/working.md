---
summary: Create Emails in OutSystems Developer Cloud (ODC) with Mentor Studio or in ODC Studio.
tags:
  - Screens
  - Themes
  - Widgets
locale: en-us
guid: 4DB954E5-AD44-43A3-9FE0-1D29C5FBE109
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A11323&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
  - evaluate
topic:
  - app-email-sending
  - email-widgets
  - use-input-parameters
isautopublish: true
---

# Working with emails

In ODC Studio, Email is a UI element that lets you design and manage the content of email messages. Like Screens, you can find and create Emails in the UI Flows. However, unlike Screens that usually use the OutSystems UI, Emails require lightweight styles to follow the industry best practices for email sizes. You create an Email by describing it to Mentor Studio and validating the result, or by building it manually in ODC Studio.

## Create an Email with Mentor Studio

Create an Email, its input parameters, and its content by describing them in Mentor Studio, and validate the Email before you use it in logic that sends it.

In your prompt, include the following:

* The Email
* Its subject
* Its input parameters with their data types
* The content to display

For example, the following sentences form one prompt:

* "Create an Email named WelcomeEmail with the subject Welcome."
* "Add a mandatory input parameter named Handle of type Text."
* "Add a Text widget and an Expression widget that displays \"Hello, \" + Handle + \"!\"."

### Validate the Email

The platform guarantees that the model is valid, and you decide whether the Email displays the content you need. In the **Interface** tab of ODC Studio, check the following:

* The Email is in a UI Flow with a light theme, a blank Theme, or a dedicated email Theme. A Theme with a lot of CSS that isn't designed for emails can push the content over the 102 KB at which Gmail clips messages. For more information, refer to [Clipped content warning](#clipped-content-warning).
* The **Subject** property has the subject you want, not the temporary `"No subject"`.
* Each input parameter has the **Data Type** you need, and **Is Mandatory** is **Yes** for the values that the Email requires.
* Expressions use only input parameters, local variables, and the scope of the Email widgets. Aggregates, Data Actions, and Client Variables aren't available in an Email. For more information, refer to [Data considerations](intro.md#data-considerations).
* The Email uses only the widgets in [Widgets available in Emails](widgets.md#widgets-available-in-emails), and uses no JavaScript or custom actions.
* Each expression displays the expected value. For example, the greeting displays `Hello, John!` when **Handle** is `"John"`.

## Create a new Email manually in ODC Studio {#create-a-new-email}

To create a new Email manually, go to ODC Studio and follow these steps:

1. Go to **Interface** > **UI Flows** and do one of the following:

    * If this is the first email you're adding in an app, right-click any UI Flow and select **Add Email**.
    * If you already have an email in your app, right-click the **Emails** UI Flow and select **Add Email**.

    ![Screenshot showing the UI Flow context menu with the 'Add Email' option highlighted.](images/add-email-ui-flow-ss.png "Adding a New Email in ODC Studio")

    <div class="info" markdown="1">

    Emails require a light theme. When you add your first email, ODC Studio creates the UI Flow with  a light theme, and then adds your email.

    </div>

1. Select the Email below  the UI Flow, and enter the following details:

    * In the **Name** field, enter a name to identify this email.
    * In the **Subject** field, enter `"No subject"` as a temporary subject.

    ![Screenshot of the Email properties panel in ODC Studio with fields for Name, Description, and Subject.](images/email-properties.png "Email Properties Interface")

## Add content to an Email manually in ODC Studio {#add-content-to-an-email}

To add content to your email, follow these steps in ODC Studio:

1. From  **Interface** select **UI Flows** > **your Emails UI Flow**  double-click the Email you want to edit. The Email opens for editing. The widget list on the left displays the available widgets that you can use in Emails.

    ![Screenshot of an open Email in edit mode within ODC Studio, showing the widget list.](images/edit-email-open-ss.png "Email Editing Interface")

1. From the widget display, drag the **Text** widget to the Email and enter some text.

    ![Screenshot demonstrating the process of dragging a Text widget into an Email's content area in ODC Studio.](images/edit-email-add-text.png "Adding Text to an Email")

1. Optionally, you can edit the **Text** widget properties from the **Styles** tab and,modify the text look and feel.

## Modify content in Emails manually in ODC Studio {#modify-content-in-emails}

You can customize the content of your emails by adding information to the corresponding Email. Emails support compound data types and can use the data from the client scope of Email.

To add an **Input** to your Email and display the value in the email body, follow these steps:

1. Add an [Email to your app](#create-a-new-email) and optionally add [some text](#add-content-to-an-email).

1. From the **Interface** tab, right-click the Email and from the menu, select **Add Input Parameter**. ODC Studio adds an Input Parameter.

    ![Screenshot highlighting the 'Add Input Parameter' option in the context menu for an Email in ODC Studio.](images/adding-input-param-email-odcs.png "Adding Input Parameter to Email")

1. Set the following Input Parameter properties:

    * **Name** - enter `Handle`
    * **Description** enter information to identify the input parameter.
    * **Data Type** - select **Text**
    * **Is Mandatory** - Select **Yes** to make the **Handle** a required value in the Email

    ![Screenshot showing the input parameter properties for an Email with fields for Name, Description, Data Type, and Is Mandatory.](images/inputs-for-emails-ss.png "Configuring Email Input Parameters")

1. From the **Interface** tab, double-click the Email to open it for editing.

1. From the widget list, drag the **Expression** widget to the Email. The expression editor opens.

1. Enter `"Hello, " + Handle + "!"` and click **Close**.

    ![Screenshot of an Email in ODC Studio displaying a personalized greeting using the 'Handle' expression.](images/expression-preview-ss.png "Email Expression Preview")

When you open this email in the email client, the expression displays "Hello, John!" when the value of **Handle** is `"John"`.

## Clipped content warning {#clipped-content-warning}

If the content of an email is too big, some email readers clip the content. For example, Gmail displays **[Message clipped] View entire message** for all emails larger than 102KB. This can happen if you're generating content in your emails with a Theme that has a lot of CSS not designed for emails.

To reduce the size of the email content, use a blank Theme or a dedicated email Theme. You can also create UI Flow without styles and then add your emails under this UI Flow.

## Related resources

The following resources describe prompt examples, the steps to prompt Mentor Studio, and what the platform guarantees.

* For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#ui).
* For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).
* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
