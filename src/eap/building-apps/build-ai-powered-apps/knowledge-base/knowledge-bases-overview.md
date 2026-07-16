---
summary: Knowledge bases in OutSystems Developer Cloud (ODC) store and semantically index documents so agents and apps retrieve relevant content using RAG at runtime.
tags:
  - Agentic
  - AI
guid: aa426959-c1c6-474e-b905-8d96e799a15f
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - understand
audience:
  - Tech lead
  - Developer
isautopublish: true
outsystems-tools:
  - odc portal
---
# Knowledge bases in ODC

<div class="info" markdown="1">

Knowledge bases are in Beta. For more information about Beta features, refer to [OutSystems product releases](https://success.outsystems.com/support/release_notes/outsystems_product_releases/#beta). If you want to try this new capability contact your OutSystems account team.

</div>

A **knowledge base** is a curated set of documents that you upload and manage in the ODC Portal. The platform ingests those documents, processes them into a searchable form, and exposes semantic search over those files so your agents and apps can retrieve relevant content at runtime.

That way, instead of relying only on a language model’s general knowledge, your agentic flows and apps can query a knowledge base and ground answers in your organization’s documents.

## How do knowledge bases work

When you upload a file to a knowledge base, the platform automatically runs it through an **ingestion pipeline** where:

1. Splits the document into smaller pieces called chunks.
1. Converts each chunk into a numerical representation called an embedding, a vector that captures the meaning of the text.
1. stores embeddings in a vector index that it uses to find the most relevant chunks for a given query.

At runtime, when a developer calls knowledge base search from an agent or app, the platform compares the query against the vector index and returns the most semantically relevant chunks. This process is called **retrieval-augmented generation (RAG)**.

## Supported file types and sizes

Knowledge bases accept the following file types:

| File type | Extension |
| --- | --- |
| PDF | `.pdf` |
| Microsoft Word | `.docx` |
| Microsoft PowerPoint | `.pptx` |
| Web pages | `.html`, `.htm` |
| Plain text | `.txt` |
| Markdown | `.md` |
| Comma-separated values | `.csv` |

Note that files can't be bigger than 20MB.

## Stage isolation

Each stage, Development, Quality Assurance, and Production, has its own files, storage area, and search index.

Documents uploaded in your Development stage never appear in Production stage search results and vice versa.
This stage isolation ensures that knowledge bases in each stage are independent and don't interfere with one another.

However, knowledge bases don't automatically copy between stages. To use the same knowledge base in multiple stages, create and upload files to each stage separately

Also, the data source configuration remains the same across stages. You set the chunking configuration during knowledge base creation, and you can't modify it afterward.

## Regional availability and limitations

Knowledge bases rely on cloud AI infrastructure. Due to regional differences in service availability, knowledge base functions differently in the way it handles data, depending on where your ODC environment is hosted.

<div class="info" markdown="1">

**Knowledge bases are available for all customers in all regions.** It's recommend that you read this section carefully, as there are some regional constraints.

</div>

### Unsupported regions

ODC semantic search triggers cross-region data transfers in the following regions:

* Cape Town (af-south-1)
* Hong Kong (ap-east-1)
* Jakarta (ap-southeast-3)
* Singapore (ap-southeast-1)
* Tel Aviv (il-central-1)
* UAE (me-central-1)

If you need to maintain data residency compliance, avoid deploying knowledge bases within these territories. In case you still want to use knowledge bases in one of these regions, note that the data is routed to the European region (eu-central-1) and then back to your region. However, no data is stored outside of your region. This constraint is due to the embedding model not being deployed in these regions.

<div class="info" markdown="1">

To determine your ODC environment's region, refer to the information provided when you purchased ODC or contact your account manager.

</div>
