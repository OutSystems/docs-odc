---
summary: Learn how to create multilingual Reactive Web and Mobile App with OutSystems.
tags:
locale: en-us
guid: ab798636-66c7-4ca9-88df-313bfa5cf8ef
app_type: mobile apps, reactive web apps
---

# Multilingual apps

With Multilingual web and mobile apps you can translate an app to other languages. Once the translations are available in the app, you can switch the language automatically or let users do it.

When translating apps, note the following important information about language codes:

* The default language code is **en-US**.
* The current language is bound to the user session and when the user logs out, the language code automatically changes to the default language code.
* All language codes are in the [RFC 1766](https://tools.ietf.org/html/rfc1766) standard format.
* Language codes are **case sensitive**.

## Getting started

Here's how to get started:

* For instructions on how to translate your app directly in ODC Studio, see [Translate your app](translate-your-app.md).
* If you want to extract text for sending it to a translation service, see [Translation management](translation-management.md).

You can translate the following elements of your app:

* Screen titles
* Text in buttons, links, and screens
* Text literals in expressions
* Instructions in human activities
* Validation messages, widget confirmation messages, and empty state messages
* Static entities. Check [Working with Static Entities](translate-your-app.md#working-with-static-entities) for important notes.

