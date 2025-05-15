---
summary: Learn to implement self-registration flows in apps using OutSystems Developer Cloud (ODC), featuring user verification and logic creation tools.
tags: user registration, email verification, security, user experience, sms integration
locale: en-us
guid: cb22b88a-f8ec-416c-8f77-8ac814d58bd7
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - forge
coverage-type:
  - understand
topic:
  - self-registration
---

# Self-registration flow

The self-registration flow enables users to register and access your app without human intervention. This flow is specifically designed for cases where the *built-in identity provider* is used and is *not applicable for external identity providers* (e.g., Google, Facebook, or other third-party identity providers). Depending upon the type of app you create, users may find your app from your website through a Google search. If you have an app that requires users to register to log in, you may need to provide them with an email link to your app.

You might also want users to be validated as part of the sign-in process. Many apps use a verification process in which you provide users with a verification code. You can use verification codes to confirm the validity of the user using the email address.

<div class="info" markdown="1">

The OutSystems Developer Cloud (ODC) Portal provides access to the Forge. In Forge, you might want to review or use an unsupported component called “Vonage Messaging” that enables you to send a verification code using SMS.

</div>

You can also use the [provided OML](resources/SelfRegistrationSample.oml). The OML is an example app with the self-registration flow implemented. You can follow the steps in the OML directly to copy elements. The example app is a template for the self-registration flow.

Users then follow a self-registration process to gain access to the app. To personalize your users experience, you create screens, logic, emails, and validations in ODC studio.

You start by creating a **Signup** screen. A signup screen usually requires users to enter a username and an email address. Security of your app and systems is essential. If your company has security requirements for logging into an app, you can use ODC Studio to create logic to register a user. Writing business logic lets you define the actions. For example, using logic, you can:

* Create actions that send emails
* Generate a verification code that gets included in the email to the user
* Verify the verification code the user submits

Verification codes enable you to confirm that the person registering has access to that email. In ODC, you can **create an email to send the verification code**.

<div class="info" markdown="1">

To use email, you must have an email provider configured.

</div>

OutSystems provides a sample email that you can update, making the process easier and quicker. You can change the subject line, the message, the note text, and the body of the email.

Once users enter a validation code, you must verify the code. You create a form to validate the verification code. Using the Form widget, you create a form to capture the data. You can define the logic that:

* Sets the verification code
* Verifies the password follows the password policy
* Defines which screen to display once the user logs in

Use the following links in the order that they appear to learn how to:

* [Create a Signup screen, so users can register to use your app](screen.md)
* [Create logic to register a user](logic.md)
* [Create an email to send the verification code](email.md)
* [Create a form to validate the verification code](create-validation-form.md)
