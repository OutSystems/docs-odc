---
summary: Availability of each semantic search option by runtime region, and the language support for text attributes, File attributes, and knowledge bases.
tags:
  - AI
  - Infrastructure
  - Multi-language
guid: be29f8af-1a71-4b21-a6a6-5d35649e2d1d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - remember
  - understand
topic:
  - semantic-search-regional-availability
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# Regions and languages for semantic search

The runtime region of each stage determines which semantic search options are available in that stage and where the platform processes the requests. The language of your content determines how accurate the results are. This page lists the regional availability and the language support of semantic search over text attributes, semantic search over File attributes, and knowledge bases.

## Find the runtime region of a stage

Semantic search runs in the runtime region of the stage where your app runs, so look up the region of each stage before you read the availability table. In the ODC Portal, go to **Management** > **Organization**. The **Stages** table shows the **Runtime region** of each stage.

## Regional availability for semantic search

The runtime region determines where the platform runs the two components that semantic search depends on:

* **Embedding model**: Generates an embedding for each chunk during indexing and for each query during search.
* **Vector store**: Stores the embeddings of File attributes and knowledge bases. Text attributes store their embeddings in the app database, so they don't depend on the vector store.

The following table lists the availability of each search option by runtime region. In the cells marked **Available, processed in Europe**, the region doesn't host the embedding model. The platform sends the text of the content and the queries to the European region (`eu-central-1`) to generate the embeddings, and then returns them. Your content and its embeddings stay stored in your region, and the text leaves the region only for processing.

| Runtime region | Text attributes | File attributes | Knowledge bases |
| --- | --- | --- | --- |
| Cape Town (`af-south-1`) | Available, processed in Europe | Available, processed in Europe | Available, processed in Europe |
| Hong Kong (`ap-east-1`) | Available, processed in Europe | Available, processed in Europe | Available, processed in Europe |
| Jakarta (`ap-southeast-3`) | Available, processed in Europe | Available, processed in Europe | Available, processed in Europe |
| Singapore (`ap-southeast-1`) | Available, processed in Europe | Available, processed in Europe | Available, processed in Europe |
| Tel Aviv (`il-central-1`) | Available, processed in Europe | Not available | Not available |
| All other regions | Available | Available | Available |

In `il-central-1`, the vector store that File attributes and knowledge bases use isn't available, and the platform doesn't send these requests to another region.

If your data must stay in one region during processing, use semantic search in a region where the table shows **Available**.

## Language support for semantic search

The language of your content determines how accurate the results are. File attributes and knowledge bases extract the text of files in the same way, so they share the same language support. A scanned PDF contains images of pages instead of selectable text. The following table compares the language support of each search option.

| Aspect | Text attributes | File attributes and knowledge bases |
| --- | --- | --- |
| Indexed languages | Most languages | Any language, when the file has a supported type and selectable text |
| Most accurate results | The languages with dictionaries, listed in the following section | English |
| Text extraction from images in PDF files that also have selectable text | Not applicable | English, Chinese, and languages that use the Latin script |
| Text extraction from scanned PDFs | Not applicable | English and Chinese. For text in other scripts, the extracted text can be empty or unreadable. |

For images in a PDF file that also has selectable text, the platform chooses the text recognizer from the language of the selectable text. If the images use a different script than the selectable text, the extracted text can be empty or unreadable.

### Language dictionaries for text attributes

Semantic search over text attributes has dictionaries for the following languages:

* Czech
* Danish
* Dutch
* English
* Estonian
* Finnish
* French
* German
* Italian
* Norwegian
* Polish
* Portuguese
* Slovene
* Spanish
* Swedish

These dictionaries address language-specific nuances, such as acronyms and cultural context, which improves how the platform interprets phrases. In all other languages, punctuation divides sentences, which leads to less accurate results. The platform detects supported languages automatically and defaults to English for the rest.
