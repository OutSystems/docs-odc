---
summary: OutSystems Developer Cloud (ODC) enables app interface translation and language switching capabilities for enhanced user accessibility.
tags:
locale: en-us
guid: 93f5315e-72fa-45f2-97ad-9e676da413a3
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Translate your app

Translate the interface of your app to other languages to let more users use your app.

## Quick start

Here's a quick start to help you translate your app. To let the users use your app in their language, you need to:

1. [Add a new language and translate the text in the app](#adding-a-new-language-and-translating-the-text) by using the ODC Studio translation editor.

1. [Create a language switcher](#creating-a-language-switcher) to let users change the language in the app.

1. If your app uses Static Entities, check [Working with Static Entities](#working-with-static-entities) for more information.

## Adding a new language and translating the text

To add a new language and translate your app, do the following in ODC Studio:

1. Go to the **Data** tab and right-click on the **Multilingual Locales**. Then, select **Add Locale**. The **Select Locale** window opens.

    ![Screenshot of the 'Add Locale' option in ODC Studio to add a new language for translation](images/add-new-language-translation-ss.png "Adding a New Language for Translation")

2. Select a locale and then click **OK** to open the **translations editor**.

    ![Screenshot showing the selection of a new language in ODC Studio](images/select-new-language-ss.png "Selecting a New Language")

    <div class="info" markdown="1">

    Make note of the language code, since you will need it later. For example, for **Portuguese (Brazil)** the code is **pt-BR**.

    </div>

3. In the translations editor, select the **Translate** option in the behavior list to see all text that needs translation.

    ![Screenshot displaying text items that need translation in the ODC Studio translations editor](images/show-translatable-text-ss.png "Translatable Text in ODC Studio")

    See [Translating with the translation editor](translation-editor.md) for more information on how to use the editor.

4. Translate the text in the **Translation in (language code)** column. Click **Done** when you are finished.

    ![Screenshot of the translation process in the ODC Studio translations editor](images/enter-translation-ss.png "Entering Translations in ODC Studio")
    
After you finish translating the text in your app, you then need to create a language switcher to show the available translations.

## Creating a language switcher

A language switcher lets your users change the language of the app. To create a language switcher, do the following:

1. Drag a Link widget to a screen and enter the language name in the **Text** part of the **Link**. 

    ![Screenshot showing a Link widget configured with a language name for switching languages in an app](images/link-with-language-name-ss.png "Link Widget with Language Name")

    The example shows how to use the Link widget to change the app language. You can create the same action with other widgets, including Button and Dropdown.

2. Select the Link widget to view its properties. In the **On Click** list, select **New Client Action**. New Client Action opens for editing.

    ![Screenshot of the process to create a new client action for a language switcher link in ODC Studio](images/new-client-action-for-link-ss.png "Creating a New Client Action for a Link")

3. With the logic editor open, go to the **Logic** tab and expand the **(System)** section in **Client Actions**. Locate the **SetCurrentLocale** client action and drag it to the logic flow.

    ![Screenshot of the SetCurrentLocale client action being added to the logic flow in ODC Studio](images/client-action-in-logic-tab.png "SetCurrentLocale Client Action in Logic Tab")

    <div class="info" markdown="1">

    If you can't find the **SetCurrentLocale Client Action**, you need to reference it first. Press **Ctrl+Q** to open the **Manage Dependencies** window and select **(System)**. In the right pane under **Client Actions**, select **SetCurrentLocale** and click **Apply** to confirm. You can now use **SetCurrentLocale Client Action** in your app logic.

    ![Screenshot of the SetCurrentLocale client action being selected in the Manage Dependencies window of ODC Studio](images/set-current-locale-in-manage-dependencies.png "SetCurrentLocale in Manage Dependencies")

    </div>

    <div class="warning" markdown="1">

    Keep in mind that SetCurrentLocale **Server** Action doesn't work offline. Use **SetCurrentLocale Client Action** whenever possible.

    </div>

4. In the **SetCurrentLocale Client Action**, enter the code of the language (for example, `"pt-BR"`) in the **Locale** property.

    ![Screenshot showing the Locale property being set in the SetCurrentLocale client action in ODC Studio](images/locale-in-client-action.png "Locale Property in SetCurrentLocale Client Action")

    <div class="info" markdown="1">

    If you have translations from **Static Entities**, add **Refresh Data** after **SetCurrentLocale**. For more information see [Working with Static Entities](#working-with-static-entities).

    </div>

5. Publish the app and select your link to change the language of the app.

## Editing existing translations

Use the [translation editor](translation-editor.md) to edit existing translations. You can also [export and import text for translation](translation-management.md). 

## Getting the identifier of the current language

You can get information about the current language with the [GetCurrentLocale built-in function](../../../reference/built-in-functions/organization.md#GetCurrentLocale).

![Screenshot of the GetCurrentLocale function being used in the expression editor of ODC Studio](images/get-current-locale-language-ss.png "GetCurrentLocale Function in Expression Editor")

## Working with Static Entities

Follow these steps to translate the text in Static Entities and show the translation in the app. 

1. In the [translation editor](translation-editor.md), search for the text you want to translate and set **Behavior** to **Translate**.

    ![Screenshot of the translation editor with a search for text to translate in ODC Studio](images/static-entity-search-ss.png "Searching in Translation Editor")

2. While still in the translation editor, enter the translation in the **Translation in (language code)** cell and click **Done**.

    ![Screenshot of the translation editor where translations for static entities are entered in ODC Studio](images/static-entity-translate-ss.png "Translating Static Entities in ODC Studio")
    
    <div class="info" markdown="1">

    Translations for static entity records are defined in the app or library that holds the static entity
    records. The static entity records and the translations can then be referenced in other apps.

    </div>

3. In the logic, to switch the locale, add **Refresh Data** just after the **SetCurrentLocale** action and select the Static Entity.

    ![Screenshot showing the refresh of static entity data after changing the locale in ODC Studio](images/static-entity-refresh-ss.png "Refreshing Static Entity Data")

## Switching back to the default language

To let users switch back to the default UI language, [create a language switcher](#creating-a-language-switcher) that sets the locale code to **en-US**.
