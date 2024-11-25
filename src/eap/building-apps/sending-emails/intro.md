---
summary: OutSystems Developer Cloud (ODC) enables email management and configuration through ODC Studio and ODC Portal using SMTP.
tags: email configuration, smtp integration
locale: en-us
guid: F826D84E-BF79-4287-9322-1E00E198A06E
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
content-type:
  - conceptual
  - process
---

# Emails

In OutSystems Developer Cloud (ODC), email is a way to get information from your apps and send it to users. For example, you can send alerts to administrators or send a copy of a form to an end-user for submission. Before you can create emails and set up logic in your apps to send the emails, make sure you have the configuration for the SMTP server. 

In OutSystems, email is a UI element that lets you design and manage the content of email messages. To create, send, and configure emails, you use both ODC Studio and ODC Portal. Emails are sent using SMTP. In ODC Portal, you can define the configuration and can create different configurations for each stage. At the app level you can change the test email addresses. 

In **ODC Studio** you define how you want to send emails. When working with the display of the content, you can use or define new templates. By default, ODC uses a light theme which is an industry standard and is automatically set for you.

When defining how to send the email, developers can:

* Create server and service actions to send emails.
* Create parameters in actions to pass information.
* Define timers to send an email at a specific time.
* Define manual triggers by creating a send email button or automate the sending of emails such as a confirmation of registration. 

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

If you want to... | Check out... |
| - | - |
| Create a new email | [Creating a new Email](working.md#create-a-new-email) | 
| Add content for an email | [Adding content to Email](working.md#add-content-to-an-email)| 
| Add content based on user inputs  | [Modify content in Emails](working.md#modify-content-in-emails)| 
| Add attachment to emails  | [Adding email attachments](attachments.md)| 
| Create logic to send emails | [Sending Emails](sending.md)| 
| See what widgets you can use  | [Widgets available in Emails](widgets.md#widgets-available-in-emails)| 
| See what data types you can use in inputs  | [Available data types](../data/data-types.md), in particular [compound data types](../data/data-types.md#compound-data-types)  | 
| Validate or format email addresses | [Email built-in functions](../../reference/built-in-functions/email.md)  | 

## More about emails in ODC

The following sections cover the more technical details related to the emails in ODC.

### How emails work

In ODC Studio, you first define the structure of the email and the expressions the platform evaluates to generate the email content. Then, ODC turns the structure into a HTML template, evaluates the expressions, replaces the content, and creates the final HTML. Finally, ODC sends the email message using the configurations you provide in the ODC Portal.

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

To send emails from your app you need to configure your SMTP server on the ODC Portal. The SMTP policy of your server might limit sending of the emails that can cause errors. For example, you might have a maximum number of addresses in To / From, or policy may limit the port number, body message size, or prevent concurrent emails.

