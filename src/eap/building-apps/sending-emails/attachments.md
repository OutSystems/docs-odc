---
summary: Attach one or more files to an email in ODC with Mentor Studio or manually in ODC Studio.
tags:
  - Aggregates
  - Data
  - Entities
  - Logic
  - Mentor Studio
locale: en-us
guid: b03f90a8-d437-4f61-a08b-dda12e8ebbfe
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A11325&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
  - remember
  - evaluate
topic:
  - attach-file-to-email
isautopublish: true
---

# Adding email attachments

An email attachment is a file users can open and save to their devices. For example, you can send a PDF file in the email for users to view and print the content.

You can send email attachments by providing the list of files in the **Attachments** section of the **Send Email** node. Define the file name, content, and media type of an attachment as the [Attachment data structure](#attachment-data-structure).

In the **Attachments** section of the **Send Email**, you can add:

* One or more inline attachments. Do this to attach a static file that changes rarely, like a PDF embedded in the app resources. See: [Attaching a single file](#attaching-a-file).

* A list of attachments. Do this when, for example, you want to send multiple files from a database, such as images from a product catalog. See: [Attaching multiple files](#attaching-multiple-files)

## Attach files with Mentor Studio

Attach one file or a list of files by describing the attachment in Mentor Studio, and validate the **Send Email** node before you publish.

In your prompt, include the following:

* The action that sends the email
* The source of the files
* The file name and media type

For a list of files, also name the entity and the attributes that hold the file name and the file content.

For example, the following sentence attaches a single file:

* "In the SendOrderConfirmation server action, attach the PDF resource sample_pdf to the Send Email node with the file name sample.pdf and the media type application/pdf."

The following sentences attach a list of files:

* "In the SendProductCatalog server action, fetch five records of the Sample_ProductImage entity, and attach them to the Send Email node."
* "Use FileName as the file name and FileContent as the content."

### Validate the attachments

The platform guarantees that the model is valid, and you decide whether the email carries the files you intend. In the **Logic** tab of ODC Studio, open the action that sends the email, select the **Send Email** node, and check the following:

* Each attachment defines **FileName** and **FileContent**. For more information, refer to [Attachment data structure](#attachment-data-structure).
* **FileContent** is binary data, such as `Resource.sample_pdf.Content` for a file in the app resources, or the binary attribute of the fetched records.
* When you set **MimeType**, the value matches the file, such as `"application/pdf"` for a PDF file. When **MimeType** is empty, the email clients detect the media type.
* A file from the app resources exists in **Resources** in the **Data** tab.
* For a list of attachments, the Aggregate comes before the **Send Email** node, **Max. Records** returns the number of files you intend, and the **Attachments** list maps the binary content and the file name.
* The **Send Email** node shows no data type error for the **Attachments** list.

## Attach a file manually in ODC Studio {#attaching-a-file}

To attach a file to an email manually, complete the following steps in ODC Studio:

1. On the **Logic** tab, open the action that sends the email and select the **Send Email** node.

    <div class="info" markdown="1">

    To learn more about creating emails, see [Working with emails](working.md). To create logic that sends emails, see [Sending emails](sending.md).

    </div>

1. In the **Send Email** properties, locate the **Attachments** section and move your pointer over the **Attachments** list.

    ODC Studio shows a plus icon with the "add list item" tooltip.

    ![Screenshot showing the 'Add list item' tooltip and plus icon in the Attachments section of the Send Email action in ODC Studio.](images/add-list-item-attachment.png "Adding Attachments in Send Email Action")

1. Click the plus icon next to the **Attachments** list to add a new item.

    ODC Studio adds a new Attachment item and labels it with zero.

1. Move your mouse over the item you added in the **Attachment** list and click the plus icon to expand.

    ![Image depicting the process of adding a new attachment item in ODC Studio, with the plus icon and item labeled as zero.](images/email-attachment-add-list-odcs.png "Attachment Properties Expansion")

1. Enter the information to define the file name, content, and media type of the email attachment.

    For more information about the Attachment properties, see [Attachment data structure](#attachment-data-structure).

    ![Screenshot illustrating the input fields for FileName, FileContent, and MimeType in the email attachment properties within ODC Studio.](images/email-attachment-properties-odcs.png "Defining Email Attachment Properties")

    The following are example properties to attach a PDF file from the resources:

    * **FileName**: `"sample.pdf"`.
    * **FileContent**: `Resource.sample_pdf.Content`.
    * **MimeType**: `"application/pdf"`

    <div class="info" markdown="1">

    To add a file to the app resources, go to the **Data** tab, right-click **Resources**, and select **Import Resources**.

    </div>

## Attach multiple files manually in ODC Studio {#attaching-multiple-files}

To attach several files to an email manually, create a List with the Attachment data structure and then pass the list to the **Attachments** property of the **Send Email** action.

<div class="info" markdown="1">

The following example references the **Sample_ProductImage** Entity from **OutSystemsSampleData**, a standard sample data app in the OutSystems cloud. The text attribute **FileName** is the file name of the image attachment. The binary attribute **FileContent** is the content of the image.

</div>

In the following example, ODC Studio fetches images from a database with an Aggregate and then sends it in an email:

1. On the **Logic** tab, open the action that sends the email and drag an Entity before the **Send Email** node.

    ODC Studio places an Aggregate in the logic flow.

    ![Image showing an Aggregate in ODC Studio used to fetch data from a database for email attachments, with a focus on the 'Max. Records' property.](images/email-attachment-getting-from-database-odcs.png "Fetching Data from Database for Email Attachments")

    <div class="info" markdown="1">

    Enter a value in the **Max. Records** property. For example, enter `5` to get five records for five attachments in the email. Leave the field empty to get all the records.

    </div>

1. In the properties of the **Send Email** node, double-click the **Attachments** list.

    The expression editor opens.

    ![Screenshot of the expression editor in ODC Studio for selecting the output list from an Aggregate to be used as email attachments.](images/email-attachments-list-odcs.png "Email Attachments List in ODC Studio")

1. In the expression editor, select the output List from your Aggregate, for example, `GetSampleProductImages.List`. ODC Studio shows an error with a message that you need to use the Attachment List data type. Click **Close** to close the editor and move on to the next step to map the values and resolve the error.

1. In the Attachment section of Send Email, map the attributes so ODC Studio knows which values pass to the attachments. You must specify binary content and the file name. The MIME type is optional, but providing it lets more email clients handle the attachment.

    ![Image displaying the mapping of database attributes to the Attachment data structure in the Send Email action within ODC Studio.](images/email-attachment-mapping-odcs.png "Mapping Database Values to Email Attachment")

## Reference

More information related to attachments.

## Attachment data structure

Use the Attachment data structure to pass information about files between the logic elements that handle emails.

| Name | Data type | Notes |
| ----------- | ----------- | -------------------------------------------------------------------------------------------------------- |
| FileContent | Binary Data | Content that the platform embeds as the attachment. |
| FileName | Text | The file name of the attachment to show in the email. For example, `"image.png"`. |
| MimeType | Text | Media type identifier. For example, `"image/png"`. Enter to tell the email readers how to handle the content, as this can help prevent errors in some clients. Leave empty to let the email clients handle the detection. |

## Related resources

The following resources describe prompt examples, the steps to prompt Mentor Studio, and what the platform guarantees.

* For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#logic).
* For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).
* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
