---
guid: d59f8e04-0de0-43f9-8933-8b5e739c0fd8
locale: en-us
summary: Create multimodal prompts using AI models with image input requirements in OutSystems Developer Cloud (ODC) to build advanced agentic apps.
figma:
coverage-type:
  - remember
  - understand
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - full stack developers
tags: ai models, image processing, multimodal ai, outsystems developer cloud, agentic apps
outsystems-tools:
  - odc studio
helpids:
---

# Image input for AI models

In ODC, you can create multimodal prompts combining text and visual data using AI models  that support image inputs. When you build your agentic app, you must select a multi-modal AI models, as text-only models don’t support this functionality and return an error. For supported models, your agentic apps can process images to build advanced AI solutions.

## Image requirements

Input images must meet the following requirements.

<div class="info" markdown="1">

These are general guidelines. For the most up-to-date and detailed requirements, consult the documentation for your specific AI model provider.

</div>

| Requirement | Detail |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Supported formats | PNG (.png), JPEG (.jpeg, .jpg), WebP (.webp), GIF (.gif, non-animated) |
| File size | Up to 20MB per image. |
| Resolution | **Minimum:** 512px x 512px  **Maximum:** 768px on the shortest side and 2000px on the longest side. |
| Content | <ul><li>No NSFW (not safe for work) content.</li><li>Must be clear enough for a person to understand.</li></ul><br/>**Note**: Images containing watermarks, logos, or embedded text are accepted, but the AI model may not always interpret or identify them accurately. |

The corresponding MIME types for these formats are **image/png**, **image/jpeg**, **image/webp**, and **image/gif**. If you use a file format the AI model does not support, it returns an error.

## Model-specific behavior {#behavior}

Different AI models may have unique requirements or behaviors when processing images.

<div class="info" markdown="1">

This is a summary of common behaviors. For a complete list of features and requirements, consult the official documentation for your specific AI model provider.

</div>

| Model | Behavior |
| --- | --- |
| Claude 3 Sonnet | <ul><li> In addition to standard image formats, this model supports other file types, like PDF, as image inputs.</li><li>The **FileFormat** input is **required** when you pass an image URL.</li><li>The **FileFormat** input is **not required** when you pass a Base64-encoded image.</li></ul> |
| OpenAI | <ul><li>Supports standard image formats.</li><li>The **FileFormat** input is ignored, even if specified.</li></ul> |

## Build prompts with images

To process an image, your app's logic must pass it to the agentic app as part of the message prompt. This typically involves an end-user uploading a file, which is then passed into the agentic app's logic.

In your consumer app's logic, you pass the required data to the agentic app. The agentic app uses this data to populate the **UserMessage content** structure. You must provide the required data- the text prompt, the image URL, or its Base64-encoded binary data.

You can pass the image in one of two ways:

1. **By URL:** Pass the public URL of the image in the **ContentUrl** input parameter.

1. **By Binary Data:** Pass the Base64-encoded image data in the **ContentBinaryData** input parameter.

When building the message, use the following inputs within the **UserMessage.Content** structure:

* **ContentText**: The text part of your prompt.

* **ContentUrl** OR **ContentBinaryData**: The image you want to send.

* **FileFormat**: The MIME type of the image (for example, **image/png**). Refer to [Model-specific behavior](#behavior) to know when this is required.

<div class="info" markdown="1">

In the **BuildMessages** Server Action flow of your agentic app, you must append each content item separately to construct a message with multiple parts. For example, to send a text prompt with an image, you first append the text content, and then append the image content. Don't try to combine different data types, like passing Base64-encoded data in the **ContentText** field.

</div>

## Example in practice

For a detailed step-by-step guide on how to build a multimodal agent, refer to the [Build the Intake Agent Exercise](https://www.outsystems.com/tk/redirect?g=c0209c24-b5d1-45b3-ade3-56412b832c90). This exercise demonstrates how to:

* Pass multiple document types including PNG and PDF to a Claude Sonnet model.
* Use the **ContentBinaryData** input to upload files from your app.
* Implement a common business use case: extracting and validating data from documents to automate a process.

## Common errors

If there's an issue with the image input, the AI model typically returns a runtime error. Here are some common causes:

| Error cause | Description |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unsupported model | The selected AI model doesn't support image inputs. |
| Missing fields | A required field is missing. For example, not passing the **FileFormat** for a URL image when using Claude 3 Sonnet. |
| File limits exceeded | The image is larger than the maximum file size or exceeds the resolution limits. |
| Invalid file format | The image isn't one of the supported file types. |
| Payload limit exceeded | The total size of the request payload (including the Base64-encoded image and text) is too large. This can cause a runtime error from the platform or the AI model. |
