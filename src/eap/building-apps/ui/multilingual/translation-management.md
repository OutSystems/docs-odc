---
summary: OutSystems Developer Cloud (ODC) supports translation management by allowing users to export and import translatable resources for apps.
tags: localization, translation editor, app development, multilingual support, globalization
locale: en-us
guid: 9eb50227-4f61-4cd7-809c-c290804c7e07
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - translating-apps
---

# Translation management

You can export translatable resources to files and send them to a professional translation service. Once you receive the translated files, import them into your app. You can also translate the resources yourself with the [translation editor](translation-editor.md).

<div class="info" markdown="1">

**Note:** If translatable text has no translation, the app shows the text in the default language of the app.

</div>

## Export the text for translation

To export the translatable text from your app follow these steps in ODC Studio:

1. Go to the **Data** tab, right-click **Multilingual Locales**, and then hover the move over **Export Language Resources** to show a new menu.

1. In the menu select one of the options to export in the format you want:

    * **To Excel**. Exports all translatable text to a single Excel file.

1. Select the export location and click **OK**.

For more information about the translation files, see [Translation resource file formats](#translation-resource-file-formats).

<div class="info" markdown="1">

To control which text ODC Studio exports, see more information about **translatable and non-translatable text** in [Translating with the translation editor](translation-editor.md).

</div>

## Import the translation

To import the translation back to the app, follow these steps in ODC Studio:

1. Go to the **Data** tab and right-click **Multilingual Locales** and select **Import Language Resources**. A dialog opens.

1. Select the file for import into ODC Studio.

    You can import files in one of the following formats:

    * **Excel file**. When you import an Excel file, you **update translations in all languages**.

## Translation resource file formats

What follows is more information about the file formats ODC Studio uses to export text for translation and import the translation.

### Excel

All translatable text is in a single Excel that consists of these columns:

* **Key**: a unique identifier
* **Location**: the location of the translatable text in the app
* **Text to be translated**: the text for translation
* **( Locale(s) )**: columns for each language locale in your app. Enter the translated text here. If you want to keep using the original text, leave the translation text empty.

The name of the Excel file is `<app name>` + `Language.xls`. For example, if your App name is **Recruitment** the file name is **RecruitmentLanguage.xls**.
