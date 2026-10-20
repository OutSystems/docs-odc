---
summary: Email widgets in OutSystems Developer Cloud (ODC) create lightweight, secure emails that most email readers display.
tags:
  - JavaScript
  - Security
  - Table
  - UI
  - Widgets
locale: en-us
guid: 665cc9c6-00e6-44f9-91ba-04f6de8fa936
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A11326&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - remember
  - evaluate
topic:
  - email-widgets
isautopublish: true
---

# Widgets in emails

OutSystems designed widgets to help you create lightweight emails that most email readers can open. When you edit an email, ODC Studio shows the available widgets in the [available Email widgets](#widgets-available-in-emails) in the widgets tool bar.

![Screenshot of email widgets available in ODC Studio interface](images/email-neo-widgets-ss.png "Email Widgets in ODC Studio")

Use the Email widgets like you use the Screen widgets, with the following common differences designed to make the emails light and secure:

* Email widgets don't have features that require handling plenty of data. For example, Tables in Emails don't show a pagination section.
* You can't use JavaScript and custom actions in Email widgets. Most email clients don't support JavaScript due to security concerns.

## Widgets available in Emails

You can use the following widgets in Emails.

| Widget | Description | Notes |
| ----------- | --------------------------------------------------- | -------------------------------------------------------------- |
| Container | Lets you arrange other widgets. | |
| Expressions | Evaluates expressions and displays variable values. | |
| If | Shows content based on a condition. | |
| Images | Embeds an image. | Using binary content from a database |
| Link(*) | Adds a navigational element. | |
| List | Shows records as items in a list. | To quickly create a list in a Mobile App, drag an Entity to Email. |
| Table | Shows records in columns and rows. | To quickly create a table in a Web App, drag an Entity to Email. |

<div class="info" markdown="1">

(*) If your app uses a [custom domain](../../manage-platform-app-lifecycle/domains/custom-domains.md) and you want to link to an app screen, you must link to the URL of that screen. For example, to link to `Screen1` in `App1` using the custom domain `example.com`, set the **OnClick** property to **RedirectToURL** with the expression `"https://example.com/App1/Screen1"`. For guidance on building expressions, see [Expressions](../../building-apps/logic/expressions.md).

</div>

## Correct email widget output

The platform guarantees that the model is valid, and you decide whether the widgets in an Email suit your content. The following checks are examples, not a complete list.

* **Supported widgets.** The Email uses only the widgets in [Widgets available in Emails](#widgets-available-in-emails).
* **No scripts.** The Email has no JavaScript and no custom actions, because most email clients don't support JavaScript.
* **Light content.** The Email doesn't depend on features that handle plenty of data, because Tables in Emails don't show a pagination section.
* **Images.** An Images widget embeds an image from binary content in a database.
* **Links to screens.** When the app uses a custom domain, a link to an app screen sets **OnClick** to **RedirectToURL** with the URL of the screen.

## Related resources

The following resource describes what the platform guarantees and what you check in a Mentor Studio proposal.

* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
