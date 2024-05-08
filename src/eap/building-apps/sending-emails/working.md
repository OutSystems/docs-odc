---
summary: OutSystems Developer Cloud (ODC) enables email design and management through its ODC Studio interface.
tags:
locale: en-us
guid: 4DB954E5-AD44-43A3-9FE0-1D29C5FBE109
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A11323&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Working with emails

In ODC Studio, Email is a UI element that lets you design and manage the content of email messages. Like Screens, you can find and create Emails in the UI Flows. However, unlike Screens that usually use the OutSystems UI, Emails require lightweight styles to follow the industry best practices for email sizes.

## Create a new Email

To create a new Email, go to ODC Studio and follow these steps:
 
1. Go to **Interface** > **UI Flows** and do one of the following:

    * If this is the first email you're adding in an app, right-click any UI Flow and select **Add Email**.
    * If you already have an email in your app, right-click the **Emails** UI Flow and select **Add Email**.
   
    ![Screenshot showing the UI Flow context menu with the 'Add Email' option highlighted.](images/add-email-ui-flow-ss.png "Adding a New Email in ODC Studio")

    <div class="info" markdown="1">

    Emails require a light theme. When you add your first email, ODC Studio creates the UI Flow with  a light theme, and then adds your email.

    </div>

2. Select the Email below  the UI Flow, and enter the following details:

    * In the **Name** field, enter a name to identify this email.
    * In the **Subject** field, enter `"No subject"` as a temporary subject. 

    ![Screenshot of the Email properties panel in ODC Studio with fields for Name, Description, and Subject.](images/email-properties.png "Email Properties Interface")

## Add content to an Email

To add content to your email, follow these steps in ODC Studio:

1. From  **Interface** select **UI Flows** > **your Emails UI Flow**  double-click the Email you want to edit. The Email opens for editing. The widget list on the left displays the available widgets that you can use in Emails.
    
    ![Screenshot of an open Email in edit mode within ODC Studio, showing the widget list.](images/edit-email-open-ss.png "Email Editing Interface")

2. From the widget display, drag the **Text** widget to the Email and enter some text.

    ![Screenshot demonstrating the process of dragging a Text widget into an Email's content area in ODC Studio.](images/edit-email-add-text.png "Adding Text to an Email")

3. Optionally, you can edit the **Text** widget properties from the **Styles** tab and,modify the text look and feel.

## Modify content in Emails

You can customize the content of your emails by adding information to the corresponding Email. Emails support compound data types and can use the data from the client scope of Email.

To add an **Input** to your Email and display the value in the email body, follow these steps:

1. Add an [Email to your app](#create-a-new-email) and optionally add [some text](#add-content-to-an-email).

1. From the **Interface** tab, right-click the Email and from the menu, select **Add Input Parameter**. ODC Studio adds an Input Parameter.

    ![Screenshot highlighting the 'Add Input Parameter' option in the context menu for an Email in ODC Studio.](images/adding-input-param-email-odcs.png "Adding Input Parameter to Email")

1. Set the following Input Parameter properties:

    * **Name** - enter `Handle`
    * **Description** enter information to identify the input parameter.
    * **Data Type** - select **Text**
    * **Is Mandatory** - Select **Yes** to make the **Handle** a required value in the Email

    ![Screenshot showing the input parameter properties for an Email with fields for Name, Description, Data Type, and Is Mandatory.](images/inputs-for-emails-ss.png "Configuring Email Input Parameters")

1. From the **Interface** tab, double-click the Email to open it for editing.

1. From the widget list, drag the **Expression** widget to the Email. The expression editor opens.

1. Enter `"Hello, " + Handle + "!"` and click **Done**.

    ![Screenshot of an Email in ODC Studio displaying a personalized greeting using the 'Handle' expression.](images/expression-preview-ss.png "Email Expression Preview")

When you open this email in the email client, the expression displays "Hello, John!" when the value of **Handle** is `"John"`.

## Clipped content warning { #clipped-content-warning }

If the content of an email is too big, some email readers clip the content. For example, Gmail displays **[Message clipped] View entire message** for all emails larger than 102KB. This can happen if you're generating content in your emails with a Theme that has a lot of CSS not designed for emails.

To reduce the size of the email content, use a blank Theme or a dedicated email Theme. You can also create UI Flow without styles and then add your emails under this UI Flow.

