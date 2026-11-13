---
summary: Chunk methods in ODC set which passages a semantic search returns. Learn how to choose a method and how chunk size and overlap affect results.
tags:
  - AI
  - Best Practices
  - Optimization
guid: fdfda10e-c4af-49f4-a8ad-1b7fab45a6ac
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
isautopublish: true
outsystems-tools:
  - odc studio
  - odc portal
audience:
  - Architect
  - Developer
  - Tech lead
coverage-type:
  - remember
  - understand
  - evaluate
topic:
  - choose-chunking-strategy
---

# Chunk methods in ODC

A semantic search returns chunks of your content, so the way the platform splits the content sets which passages an agent or app receives. A chunk method defines how the platform splits content into chunks before it generates embeddings, and each chunk becomes one search result. You set a chunk method for each searchable attribute in ODC Studio, where the setting is labeled **Chunking Method**, and for each knowledge base in the ODC Portal.

This page describes how to choose a method for your content, and how chunk size and overlap affect the results.

## Choose a chunk method

Match the method to the structure of your content and to the questions that users ask. For text attributes and File attributes, you can change the method later, and the platform reindexes every existing record. For a knowledge base, you set the method when you create the knowledge base and can't change it afterward, so choose it before you create the knowledge base.

The following table shows the content that each method fits, how it splits content, its parameters, and the search options where it applies.

| Method | Fits | How it splits content | Parameters | Available for |
| --- | --- | --- | --- | --- |
| **Smart** (default in ODC Studio) | Documents with mixed or inconsistent structure | For text attributes, uses recursive chunking with default separators. For files, follows the structure of the document, such as headings and tables. | None | Text attributes, File attributes, knowledge bases |
| **Fixed-size** | Large, uniform documents where a chunk can end mid-sentence | Splits at a fixed number of characters, with an overlap between adjacent chunks. | **Chunk Size**, **Chunk Overlap** | Text attributes, File attributes, knowledge bases |
| **Recursive** | Large documents where chunks end at separators, such as paragraph breaks | Splits at a prioritized list of separators until each chunk fits the chunk size, with an overlap between adjacent chunks. | **Chunk Size**, **Chunk Overlap**, **Separators** | Text attributes, File attributes, knowledge bases |
| **Sentence-based** | Text where individual sentences carry a complete meaning | Groups a set number of sentences into each chunk, within a maximum number of characters and an overlap. | **Sentences per Chunk**, **Chunk Size**, **Chunk Overlap** | Text attributes |
| **By page** | Documents where each page stands alone, such as slide decks | Creates one chunk for each page. | **Chunk Size** | File attributes, knowledge bases |
| **By paragraph** | Documents where each paragraph carries a complete idea | Creates one chunk for each paragraph or other content item, such as a table. | **Chunk Size** | File attributes, knowledge bases |
| **By section-header** | Documents with a clear heading structure | Creates one chunk for each section, from one section header to the next. | **Chunk Size** | File attributes, knowledge bases |
| **None** | Documents shorter than the maximum chunk length | Keeps the text as a single chunk, up to 8192 characters. The platform discards the text beyond that maximum. | None | Text attributes, File attributes, knowledge bases |

## Chunk size and overlap

The chunk size and the overlap set how much text each search result carries, and they affect the relevance of the results in the following ways:

* **Chunks that are too large** return broadly relevant content that includes noise, which makes it harder for an AI model to identify the precise answer.
* **Chunks that are too small** return precise content that can lack the context needed for a coherent answer.
* **Overlap** between adjacent chunks keeps content at chunk boundaries from being lost.

Size the chunks to hold the passage that answers a typical question about your content. In ODC Studio, these settings are the **Chunk Size** and **Chunk Overlap** properties, both measured in characters.

The Fixed-size and Recursive methods start with a chunk size of 1000 characters and an overlap of 200 characters. Keep the defaults for a first test with your own content and queries, then adjust them based on the results:

* If results contain the answer together with unrelated text, reduce the chunk size.
* If results cut off an answer or miss the context around it, increase the chunk size or the overlap.

The overlap must be smaller than the chunk size.

The By page, By paragraph, and By section-header methods split content at the structure of the document, and the chunk size sets an upper limit for each chunk. The platform splits a page, paragraph, or section that's longer than the chunk size into several chunks, without overlap. To keep each section in one result, set the chunk size above the length of your typical section. In a file format without pages, such as plain text, By page treats the whole document as one page, so the chunk size alone sets where the chunks split.
