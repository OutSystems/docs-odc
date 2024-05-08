---
summary: Explore how to enhance accessibility in web applications using ARIA roles and attributes within OutSystems Developer Cloud (ODC).
tags:
locale: en-us
guid: 2dd1e5f8-9198-4f04-bc61-6a62073113e5
app_type: reactive web apps, mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=4582%3A521
platform-version: odc
---
# Accessible Rich Internet Applications roles and attributes

Accessible Rich Internet Applications (ARIA) is a set of accessibility standards that defines elements to use on top of HTML and OutSystems UI to provide additional information to assistive technology tools. ARIA is a valuable tool for addressing accessibility challenges that go beyond what native HTML handles. There are ARIA roles, states, and properties. ARIA roles define the type of element and its purpose, states indicate the current condition or status of an element, and properties provide additional information about an element. ARIA states and properties are also known as ARIA attributes.

Use ARIA to handle dynamic content or complex page structures:

* When you have several sections on a page, and setting a **role=main** tells the screen readers where the main content is.
* When you have a block that takes some time to load, to inform the screen readers by setting **aria-busy=true**.
* With a button that opens a popup window can warn users by **aria-haspopup=true**.

Adding ARIA attributes and roles requires familiarity with the concepts of ARIA and how ARIA works with HTML. An important thing to keep in mind is that **you shouldn't use ARIA to override the meaning that the HTML tags and the pages produced by the OutSystems UI provide by default**. Inspect the pages before deciding to add an ARIA role or attribute. OutSystems UI adds some ARIA attributes by default, for example in actions that handle menu visibility.

When developing OutSystems apps, add ARIA roles, states, and properties by editing the **Attribute** property of the widgets. There are also some actions that handle specific ARIA properties, such as **SetAriaHidden** or **SetAccessibilityRole**.

## Set ARIA as a static property

The ARIA property doesn't change when the app runs. To add the ARIA roles or attributes, select the widget, go to the **Properties** tab, and add the role or attribute in the **Attributes** section.

![Image showing how to set ARIA as a static property](images/aria-static-property-odcs.png "Setting aria as a static property")

Similarly, you can set an ARIA role.

![Image showing how to set an ARIA role](images/aria-role-odcs.png "Setting an aria role")

## Set ARIA dynamically

This ARIA property changes when the app runs, depending on a condition. To set an ARIA role or attribute dynamically, use the **If** keyword in the expression of the **Attribute** field. For example, the value of **aria-invalid** in the expression **aria-invalid=If(Form1.Valid, "false", "true")** changes depending on whether the **Form1.Valid** is true or false.

If the form is invalid, because one of the required fields is missing or a value isn't correct for a field, the form appears as marked with **aria-invalid="true"**. This is a signal to the screen readers to alert the users.

![Image showing how to set the ARIA property dynamically](images/set-aria-dynamically-odcs.png "Setting the aria property dynamically")

## Built-in ARIA actions

These are the built-in actions that support setting ARIA attributes. Use them to set the ARIA properties in your logic flows.

### Hide elements with SetAriaHidden

Use the **SetAriaHidden** action to hide an element and all content inside it from the assistive technology tools. It's equivalent to setting **aria-hidden="true"** explicitly for an element.

To find the **SetAriaHidden** action, go to the **Logic** tab > **OutSystemsUI** > **Accessibility.** 

### Change the role of the Alert pattern

To change the ARIA role of the Alert pattern, use the **SetAccessibilityRole** action. 
To find the **SetAccessibilityRole** action, go to the **Logic** tab > **OutSystemsUI** > **Accessibility** 
For more information, refer to [Alert pattern](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Accessibility#Alert_pattern).

<div class="info" markdown="1">

The **SetAccessibilityRole** actions work with the Alert pattern. Alternatively, you can test using SetAccessibilityRole for a child element of widgets.

</div>

## Examples of ARIA

This section shows some examples of how you can use ARIA to extend the functionality of the OutSystems UI.

### Status message

Status messages are pieces of text that assistive tools can read and inform the users about the state of each action. Enabling these messages lets screen readers tell the users about the status of the current action.

To enable the status message, do the following:

1. Select the UI Pattern.

2. On the **Properties** tab, go to the **Attributes** section.

3. Create a **role** attribute.

4. In the value field of the new **role** attribute, enter the status message.

The following figure shows an example of a status message:

![Image showing how to set a status message](images/status-message-odcs.png "Setting a status message")

### Create readable labels

This section describes how to create readable labels on UI Patterns, such as a button or a link.

To create a label, do the following:

1. Select the UI element on the screen.

2. On the **Properties** tab, go to the **Attributes** section.

3. Create a new **aria-label** attribute.

4. In the value field of the new **aria-label** attribute, enter the descriptive label.

5. Select the button label text, for example, **Cancel**.

6. On the **Properties** tab, create a new **aria-label** attribute.

7. Provide the descriptive text you want screen readers to say.

The following figure shows an example of a readable label on a **Delete** button. In this example, when the user selects this button, the screen reader says "Delete product".

![Image showing how to create readable labels](images/readable-labels-odcs.png "Creating readable labels")

### Hide text in buttons or links

This section describes how to hide text on the screen. If you have a link with a readable text description, for example, "View product in store", you can hide a portion of the text. All text set as hidden is invisible on the screen, but screen readers are able to read the full description.

To hide text in links, do the following:

1. In your application screen, select the Link you want to edit.

2. Select the portion of the link text you want to hide, for example, "product" in “View product in store”

3. [Add a CSS class](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Look_and_Feel/Cascading_Style_Sheets_(CSS)) that makes that part of the link invisible.

    ![Image showing how to hide text in buttons or links](images/hide-text-odcs.png "Hiding text in buttons or links")

### Add detailed descriptions for short labels

You can define what you want screen readers to say when you have short labels on buttons or links. For example, a **Cancel** button. The **aria-label** describes the purpose of the button or link. This enables screen readers to say full descriptions.

To add an **aria-label**, do the following:

1. Select the button label text, for example, **Cancel**.

2. On the **Properties** tab, create a new **aria-label** attribute.

3. Enter the descriptive text you want screen readers to say.

    ![Image showing how to add detailed descriptions to short labels](images/aria-labels-odcs.png "Adding detailed descriptions to short labels")
