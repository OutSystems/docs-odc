---
summary: ODC emails use widgets for content and SMTP for sending. Build them with Mentor Studio or ODC Studio, and configure each stage in ODC Portal.
tags:
  - CSS
  - Logic
  - Mentor Studio
  - Settings
  - Timers
  - Triggers
  - Widgets
locale: en-us
guid: F826D84E-BF79-4287-9322-1E00E198A06E
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - odc portal
  - mentor studio
coverage-type:
  - understand
  - apply
  - evaluate
topic:
  - compose-and-send-emails
  - configure-email-settings-odc
  - email-css-compatibility
isautopublish: true
---

# Emails

In OutSystems Developer Cloud (ODC), email is a way to get information from your apps and send it to users. For example, you can send alerts to administrators or send a copy of a form to an end-user for submission. Before you can create emails and set up logic in your apps to send the emails, make sure you have the configuration for the SMTP server.

In OutSystems, email is a UI element that lets you design and manage the content of email messages. To create, send, and configure emails, you use both ODC Studio and ODC Portal. Emails are sent using SMTP. In ODC Portal, you can define the configuration and can create different configurations for each stage. At the app level you can change the test email addresses.

You can build emails and the logic that sends them by describing them to Mentor Studio and validating the result, or manually in ODC Studio. Whichever way you build, a correct result has the same characteristics. For more information, refer to [Correct email output](#correct-email-output).

In **ODC Studio** you define how you want to send emails. When working with the display of the content, you can use or define new templates. By default, ODC uses a light theme which is an industry standard and is automatically set for you.

To send emails from your app, you can do the following:

* Create a server action or a service action that runs the **Send Email** action.
* Add input parameters to the action to pass information to the Email.
* Call the action from your app logic, for example when a user clicks a button or submits a form.
* Call the action from a Timer to send an email at a specific time.

Developers can also use **widgets** (GUI elements to create and display the content) in an email to:

* Evaluate expressions and display values.
* Show or hide content based on a condition.
* Embed an image.
* Show information in columns and rows.

## Getting started

The following are the steps to get you started with creating and sending emails:

1. Configure ODC to send emails. See [Configure sending emails](../../manage-platform-app-lifecycle/configure-emails.md)
1. Create an email and add some content to it. See: [Working with emails](working.md)
1. Create logic that sends emails to users. See: [Sending emails](sending.md)
1. Optionally, add attachments in your emails. See: [Adding email attachments](attachments.md)

For more information about emails, see the following resources:

| If you want to... | Check out... |
| - | - |
| Describe an email to Mentor Studio | [Create an Email with Mentor Studio](working.md#create-an-email-with-mentor-studio) |
| Create a new email | [Creating a new Email](working.md#create-a-new-email) |
| Add content for an email | [Adding content to Email](working.md#add-content-to-an-email) |
| Add content based on user inputs | [Modify content in Emails](working.md#modify-content-in-emails) |
| Add attachment to emails | [Adding email attachments](attachments.md) |
| Create logic to send emails | [Sending Emails](sending.md) |
| See what widgets you can use | [Widgets available in Emails](widgets.md#widgets-available-in-emails) |
| See what data types you can use in inputs | [Available data types](../data/data-types.md), in particular [compound data types](../data/data-types.md#compound-data-types) |
| Validate or format email addresses | [Email built-in functions](../../reference/built-in-functions/email.md) |

## More about emails in ODC

The following sections cover the more technical details related to the emails in ODC.

### How emails work

In ODC Studio, you first define the structure of the email and the expressions the platform evaluates to generate the email content. Then, ODC turns the structure into a HTML template, evaluates the expressions, replaces the content, and creates the final HTML. Finally, ODC sends the email message using the configurations you provide in the ODC Portal.

### Email sending behavior {#email-sending-behavior}

How ODC sends emails determines where you place **Send Email** in your logic and how you handle its result. **Send Email** works like a call to any other integration, with the following behavior:

* **Synchronous call.** The flow waits while ODC sends the message to the SMTP server. When the SMTP server accepts the message, the flow continues to the next node.
* **Immediate sending.** ODC doesn't queue emails. ODC sends the email as soon as **Send Email** runs, and doesn't cancel the email if logic that runs after **Send Email** fails.
* **Exception on failure.** If sending fails, **Send Email** raises an exception. Handle the exception in your logic. For more information, refer to [Handling exceptions](../handling-exceptions/handle-exceptions.md). If your use case requires retries, build the retry logic in your app.
* **Sent means accepted.** Sending succeeds when the SMTP server accepts the message. ODC doesn't track delivery to the recipient or bounces, and doesn't keep a status, history, or message ID for sent emails.

### Data considerations

You can create content for emails by using input parameters, local variables and the scope of the Email widgets expressions. Elements like Aggregates, Data Actions, or Client Variables aren't available in the scope of an Email element.

Emails support compound data types.

### Email clients and CSS

There are many email clients and there's no consistent support for CSS. OutSystems recommends that you test your email content regularly in different clients. To check how different platforms support the CSS you want to use, you can use tools such as, [Can I email](https://www.caniemail.com/).

### CSS from producers

When your Email app (consumers) use CSS from other apps (producers), the emails show the latest styles that you published in the environment. When you publish the producer, continue using the consumer to get the latest styles from the producer. There's no need to republish the consumer.

### Clipped content in Gmail

Google Gmail clips messages if the HTML code is larger than 102 KB. OutSystems recommends you start with Emails that have only basic styles, without the CSS from OutSystems UI.

### SMTP server configurations

To send emails from your app, configure your SMTP server in ODC Portal. The policy of your SMTP server can limit sending and cause errors. For example, the policy can limit the number of addresses in the **To** and **From** fields, the port number, or the body message size, or prevent concurrent emails.

ODC doesn't apply sending quotas or throughput limits to your apps. The SMTP server defines any limits on how many emails your apps send.

## Correct email output

The platform guarantees that the model is valid, and you decide whether an email and its sending logic meet your requirements. The following checks are examples, not a complete list.

* **SMTP configuration.** The SMTP server is configured in ODC Portal, for each stage that sends emails.
* **Theme.** The Email uses a light theme, which is an industry standard for emails.
* **Data in scope.** The Email content uses input parameters, local variables, and the scope of the Email widgets. Aggregates, Data Actions, and Client Variables aren't available in an Email.
* **Size.** The HTML of the Email stays under 102 KB, because Gmail clips larger messages. The Email starts with basic styles, without the CSS from OutSystems UI.
* **CSS support.** The content displays correctly in the email clients that your users have, because CSS support differs between email clients.
* **SMTP policy.** The sending respects the policy of the SMTP server, such as limits on the number of addresses, the port, the body size, or concurrent emails.
* **Sending logic.** The **Send Email** action runs after the logic it depends on, because ODC sends the email as soon as **Send Email** runs. The logic handles the exception that **Send Email** raises when sending fails. For more information, refer to [Email sending behavior](#email-sending-behavior).

## Related resources

The following resource describes what the platform guarantees and what you check in a Mentor Studio proposal.

* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
