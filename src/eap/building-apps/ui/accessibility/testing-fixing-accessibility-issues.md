---
summary: OutSystems Developer Cloud (ODC) supports accessibility testing and fixing through tools like WAVE and Lighthouse, as demonstrated in ODC Studio.
tags:
locale: en-us
guid: 04bcfcb9-e575-4b01-9b03-0e755ea54fdb
app_type: reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4574-177&mode=design&t=mgggrWLg7VuE5pai-0
platform-version: odc
---
# Testing and fixing accessibility issues

While developing accessible apps, OutSystems recommends you test for accessibility issues and fix them early. This section shows a quick example of using the [WAVE accessibility evaluation tool](https://wave.webaim.org/) to identify and address issues in ODC Studio. WAVE shows issues as visual markers on the page, which lets you focus on the low-code approach of the app development. You can also audit your apps with Lighthouse, integrated with the Chrome DevTools.

## Build a page

In ODC Studio create a screen, publish the app, and open it in your browser. Here is an example of a simple screen with a title and an image.

![Image of a sample page in ODC Studio](images/a-sample-page-odcs.png "A sample page")

## Test for accessibility

To test your page for accessibility, do the following steps:

1. Load the page.
1. Click on the WAVE extension (1) to start testing. The existing issues show on top of the page elements.
1. Click an error marker (2) to open a pop-up box with the notes. In this example, a page title is missing.
1. Click the reference link (3) to see which success criteria the issue affects. In this example it's the "2.4.2 Page Titled" rule, which is the Level A success criteria (4).

    ![Image showing the process of testing accessibility in ODC Studio](images/test-for-accessibility-odcs.png "Testing the accessibility")

There are other issues with this page. There is no heading, and the image is missing the alternative text.

<div class="info" markdown="1">

The accessibility analysis shows page structural elements and ARIA annotation. These elements and annotations come from the OutSystems UI by default.

</div>

## Fix the accessibility issues

To fix all the issues from this example, follow the instructions in the [Basic accessibility settings](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Accessibility#Basic_accessibility_settings) section. After some quick edits, the page now has a title, the language definition, and the image has an alt text. If you check the page again, the report shows zero errors.

![Image showing the process of fixing accessibility issues in ODC Studio](images/fixing-accessibility-issues-odcs.png "Fixing the accessibility issues")
