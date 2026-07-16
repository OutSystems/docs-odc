---
summary: "ODC knowledge base chunking strategies reference: compare Smart, Fixed-size, Sentence-based, and more, with trade-offs to optimize retrieval quality."
tags:
  - AI
  - Best Practices
guid: fdfda10e-c4af-49f4-a8ad-1b7fab45a6ac
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
isautopublish: true
outsystems-tools:
  - odc portal
audience:
  - Tech lead
  - Developer
coverage-type:
  - remember
  - understand
---
# About chunking strategies in ODC

When you create a knowledge base in the ODC Portal, or use Semantic Search over app data, you need to select a chunking strategy that defines how the platform splits your data into chunks.
The chunking strategy affects how semantic search retrieves relevant content at runtime. When the platform ingests a file, it splits the content into smaller pieces called **chunks** before generating embeddings. The chunking strategy controls how that split happens.

## Chunking strategies

The table below shows the chunking strategies available in ODC Knowledge Bases, how each splits content, and the trade-offs between them.

| Strategy | How it splits content | Best for | Trade-off |
| --- | --- | --- | --- |
| **Smart** | Uses a mix of recursive chunking with default separators | Mixed or inconsistently structured documents where neither fixed size nor headers alone work well | May cut sentences mid-thought if overlap is too small |
| **Fixed-size** | Splits at a fixed token or character count, with optional configurable overlap between adjacent chunks | Large, uniform documents (reports, manuals) | May cut sentences mid-thought if overlap is too small |
| **Sentence-based** | Splits at paragraph boundaries | Documents with clear paragraph structure | Chunk sizes vary widely; very long paragraphs create oversized chunks |
| **Recursive** | Splits into chunks of a fixed token or character count, with optional overlap | Large, uniform documents (reports, manuals) | May cut sentences mid-thought if overlap is too small |
| **By Page** | Splits into chunks of a fixed token or character count, with optional overlap | Large, uniform documents (reports, manuals) | May cut sentences mid-thought if overlap is too small |
| **Recursive** | Splits into chunks of a fixed token or character count, with optional overlap | Large, uniform documents (reports, manuals) | May cut sentences mid-thought if overlap is too small |
| **By paragraph** | Splits at sentence boundaries | Documents where individual sentences carry complete meaning | Can produce very short chunks for dense technical text |
| **By section-header** | Splits at section header boundaries | Documents with clear section structure | May create very large chunks for sections with little content |
| **None** | Splits into chunks of a fixed token or character count, with optional overlap (Max characters: 8192) | Documents smaller than the max characters limits | May cut sentences mid-thought if overlap is too small. Also, if the document is larger than the max characters limit, the remainder of the characters is truncated. |

## Deciding on the chunking strategy

Although the chunking strategy is configured differently for Semantic Search, and in the Knowledge Bases, on during development in ODC Studio, the other one at the time of knowledge base creation in the ODC Portal, the same principles apply. Whatever chunking strategy you choose, should be based on the structure of your data and the type of queries you expect to run against it. The goal is to balance chunk size and context to optimize retrieval quality.

So, this should be part of your design considerations, and be accounted for in your app architecture when you are building your app, and you should test different chunking strategies to see which one works best for your specific use case.

## How chunking strategy affects retrieval quality

The chunking strategy has a direct impact on the relevance of search results:

* **Chunks that are too large** return broadly relevant content but may include noise, making it harder for the language model to identify the precise answer.
* **Chunks that are too small** return precise content but may lack the surrounding context needed to make the answer coherent.
* **Overlap** between adjacent chunks helps ensure that content at chunk boundaries isn't lost.

If search results are returning irrelevant content or missing expected matches, review the chunking strategy used for that knowledge base.
