---
summary: OutSystems Developer Cloud (ODC) offers built-in accessibility features to help developers create apps that comply with WCAG guidelines.
tags: accessibility, wcag, aria, ui design, ethical design
locale: en-us
guid: 62770c36-d307-4a3a-ba01-acf10299454a
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4574%3A135&mode=design&t=Jvfv9vJci8R8xd4n-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - none
coverage-type:
  - apply
topic:
  - design-for-accessibility
---

# Accessibility

<div class="info" markdown="1">

Applies to Mobile Apps and Web Apps only

</div>

To ensure the availability of accessible apps that everyone can use is crucial for ethical, practical, and often legal reasons. OutSystems has developed user interface (UI) features with accessibility in mind, allowing you to create apps that comply with the [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21) (WCAG). Additionally, you have the flexibility to tailor both the UI and app logic to meet your specific accessibility goals.

A general recommendation is to start thinking about accessibility **early in the development phase**, test often, identify the issues, and fix the issues or provide workarounds.

Here are some guidelines to consider for meeting your accessibility needs:

1. Ensure that your app meets the basic accessibility requirements. For more information, refer to [Enable the built-in accessibility features](#enable).

1. Early in development, test your app against the accessibility success criteria for the level you are targeting and fix the issues. For more information, refer to [Testing and fixing accessibility issues](testing-fixing-accessibility-issues.md).

1. Pay close attention to complex interactions and dynamic content. Fix the critical issues immediately. Use ARIA to  provide more information to the assistive technology tools and improve the structure of your pages. For more information, refer to [ARIA roles and attributes](aria-roles-and-attributes.md).

1. See [UI Patterns accessibility reference](ui-patterns-accessibility-reference.md) for special notes about patterns you may be using on a page.

## Enable the built-in accessibility features { #enable }

OutSystems has many built-in accessibility features, such as creating applications with the right contrast ratio, focus, and skip-to-content settings. To develop accessible apps, you must activate the accessibility feature in ODC Studio. Suppose your app uses complex interactions or design. In that case, you may need specific customization and development, covered in [ARIA roles and attributes](aria-roles-and-attributes.md) and [UI Patterns accessibility reference](ui-patterns-accessibility-reference.md).

To enable the built-in accessibility features in ODC Studio, do the following:

1. Go to **UI Flows** and click on **Layouts**
1. Expand the layout you're using.
1. Select the **EnableAccessibilityFeatures** input parameter.
1. On the parameter properties, set the **Default Value** to **True**.

    ![Screenshot of enabling accessibility features in OutSystems ODC Studio with EnableAccessibilityFeatures parameter set to True](images/enabling-accessibility-features-odcs.png "Enabling the built-in accessibility features in ODC Studio")

By setting the **EnableAccessibilityFeatures** to true, you activate the following features for all screens using the layout:

* **Focus states** - allows you to set and highlight the focus on the current element.

* **Skip to content** - allows the user to skip the navigation elements on the screen, and tab directly to the content.

* **Accessible links** - generates link with high color contrast.

* **Enhanced contrast** - allows displaying the content on the screen using a contrast ratio perceivable to people with visual impairments.

### Page title

Screen readers use page titles to inform users of the name of the page they're on. To define the page titles for accessibility, do the following steps:

1. On the **Interface** tab, go to **UI Flows**
1. Select the screen to add the title from the list of screens
1. On the **Properties**, enter the screen title (for example, "Main page") in the **Title** field.

<div class="info" markdown="1">

The default page title of the log-in page is blank. Navigate to **UI Flows** > **Common** > **Login** and enter the title.

</div>

### Page language settings for screen readers

The locale of the app defines the language of the page. For more information, refer to [Multilingual Reactive Web and Mobile Apps](https://success.outsystems.com/documentation/11/developing_an_application/design_ui/multilingual_reactive_web_and_mobile_apps/).

### Image text alternatives

Image text alternatives, also known as alt text or alternative text, is a string of text that describes what's in the image. Adding image text alternatives allows screen readers to read the description of the images.

To add an alternative text for an image, do the following:

1. Select your image, and go to the  **Properties**.
1. In the **Attributes** section, create an **alt**.
1. Enter the description. When an image is for decorative purposes, set **alt=""**.

    ![Screenshot showing how to add alternative text to images in OutSystems ODC Studio](images/image-text-alternatives-odcs.png "Adding text alternative to images")

After adding alt-text to an image,  you can test the image text alternatives using a screen reader.

### Text headings

Text headings are a valuable visual aid for users to understand the page structure. Incorporating varying text sizes, especially larger ones, enhances visual guidance on the page and benefits users with cognitive disabilities. Moreover, text-to-speech readers rely on headings to assist users in navigating through a page.

To ensure proper content organization within your app, establish a clear heading structure. Add [a heading element](https://www.w3.org/WAI/tutorials/page-structure/headings/), for example, **h1**, by enclosing the text in the HTML widget and specifying **h1** as the tag.

To set the text headings, do the following steps:

1. On the toolbox, search for the **HTML Element** widget (1)
1. Drag it to the screen (2).
1. To add an **h1** element to the screen, go to the **HTML Element** widget properties, and in the **Tag** field (3), enter **h1**.
1. Enter some text into the HTML Element.
1. Check the widget structure to verify that the text is within the **h1** element (4).

    ![Screenshot illustrating how to set text headings using the HTML Element widget in OutSystems ODC Studio](images/text-headings-odcs.png "Setting text headings")

On setting the headings, you can test them using a screen reader.

### Text color contrast

By default, OutSystems UI provides the correct text contrast ratio to comply with the color contrast accessibility requirements. The built-in accessibility features once turned on, improve the contrast. If you edit the colors in your app, make sure the contrast is still valid by referring to the [minimum contrast criteria](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum).

### Text spacing

Improve the text readability by letting the users increase the text spacing in your application. To increase the text spacing, create an action that runs the accessibility **ToggleTextSpacing** action

To increase the text spacing, do the following:

1. In your app screen, select the page element that triggers the increased text spacing. For example, a button.

1. To create a new client action, in the **Events** section of the **Properties**, go to the **OnClick** event and select **(new client action)**.

    ![Screenshot of creating a new client action for text spacing in OutSystems ODC Studio](images/new-client-action-odcs.png "Creating a new client action")

1. Set the action name as **TextSpacing**, for example.

    ![Screenshot showing the setup of a text spacing client action in OutSystems ODC Studio](images/text-spacing-client-action-odcs.png "Setting the text spacing client action")

1. On the **Logic** tab, click on **OutSystemsUI**
1. Click on the **Accessibility** Client Actions folder.
1. Drag the **ToggleTextSpacing** action into the flow.

    ![Screenshot demonstrating how to set the accessibility ToggleTextSpacing action in OutSystems ODC Studio](images/set-accessibility-role-odcs.png "Setting the accessibility")

### Form labels

Labels provide captions to the input fields, describing the information requested from the user. You have to bind the Label widget to inputs in forms to allow screen readers to read each input field caption.

To bind labels with the forms fields, do the following steps:

1. Select the **Label** widget in the preview (1)
1. On the **Properties**, go to the **Input Widget** drop-down, and select the widget to associate the label (2).
1. To see a demo of a form, create a screen based on a **Detail** Screen Template.

    ![Screenshot of associating labels to form fields in OutSystems ODC Studio for better accessibility](images/form-labels-odcs.png "Associating labels to form fields")

 On binding labels with form fields, you can test reading the input field captions using a screen reader.

<div class="info" markdown="1">

Use the `aria-labelledby` attribute for more control when setting up relationships between objects and their text labels. For more information, refer to [Examples of ARIA](aria-roles-and-attributes.md#examples-of-aria).

</div>

### Form validation on screen readers

To learn how to validate the input fields of a form, refer to [Validate the fields of a form](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Forms/Validate_the_fields_of_a_form#Examples_of_the_client-side_validation_with_accelerators).

To learn how to signal to screen readers and users that the form isn't valid, refer to the example in [Set ARIA dynamically](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Accessibility/Accessible_Rich_Internet_Applications_roles_and_attributes#Set_ARIA_dynamically).

### Highlight selected elements

To enable the built-in accessibility features provides a visual indicator for selectable items on the page. As the user moves between various selectable elements using the tab key, they see the currently selected item as highlighted.

#### Select an element with the SetFocus action

You can explicitly select an element by using the **SetFocus** action. For example, you can highlight an input field when a user enters a page that contains a form.

![Screenshot showing how to set focus to an element using the SetFocus action in OutSystems ODC Studio](images/element-in-focus-odcs.png "Setting the focus to an element")

To explicitly select an element on a screen, do the following steps:

1. On the **Interface** tab, select the screen that contains the widget you want to highlight and open it.
1. On the screen **Properties**, go to **Events**, and select the **OnReady** action from the drop-down menu. The **OnReady** action logic opens.
1. On the **Logic** tab, click on **OutSystemsUI** and open the **Accessibility** Client Actions folder.
1. Select the **SetFocus** action and drag it into the logic, as shown in the figure below.
1. On the **Properties**, go to **WidgetId** and select the Id of the widget you want to highlight.

    ![Screenshot of adding the SetFocus action into an OnReady action in OutSystems ODC Studio](images/element-in-focus-setfocus-odcs.png "Adding the setfocus action into an Onready action")

After following these steps and publishing, you can test the highlighting of the element.

### Skip to specific content on a page

By default, text readers skip repetitive elements, such as headers and menus, and jump to the main content of a page for reading it. You might want text readers to skip to a specific page section other than the main content.

To change the default main container, do the following steps:

1. On the **Interface** tab, go to **UI Flows** and expand the **Layouts**.
1. Select and expand the layout you're using.
1. Double-click the **SkipToContentOnClick** action.
1. Select the **SkipToContent** node in the flow and edit the **TargetId** in the action properties.

    ![Screenshot showing how to set the Skip To Content target ID in OutSystems ODC Studio](images/skip-to-content-target-id-odcs.png "Setting the Skip To Content target ID")

<div class="info" markdown="1">

You must enter the name in the widget properties before you can use that widget in the **SkipToContent** action. For example, if you name your element **MainContent**, the identifier is **MainContent.Id**.

</div>

The default content Container is the **MainContentWrapper**. To find it, go to **UI Flows** > **Layouts**, and click on the layout you use in your app.

To find the  **SkipToContent** action, go to **Logic** > **OutSystemsUI** > **Accessibility**.

## Modal dialogs

<div class="info" markdown="1">

Applies to Platform Server 11.11 and later.

</div>

Use the **Popup widget** to create accessible modal dialogs. Popup adds the following attributes to the widget:

* `role="dialog"`
* `aria-modal="true"`

Additionally, you must add the class `"has-accessible-features"` manually in the Style Classes of the Popup Widget to enable the accessibility features.
