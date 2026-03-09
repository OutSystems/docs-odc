---
guid: fda3c696-646f-4935-908f-cb175a85c55f
locale: en-us
summary: Implement AI-powered semantic search in ODC apps using LLMs and vector embeddings to understand user intent, context, and meaning for accurate search results.
figma:
coverage-type:
  - understand
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - tech leads
  - full stack developers
tags: semantic search, ai search, llm, vector embeddings, outsystems developer cloud
outsystems-tools:
  - odc studio
  - odc portal
helpids:
---
# Semantic search in ODC apps

<div class="info" markdown="1">

Semantic search is in Beta. For more information about Beta features, refer to [OutSystems product releases](https://success.outsystems.com/support/release_notes/outsystems_product_releases/#beta)

</div>

Semantic search is essential for many AI-powered apps. In ODC, you can implement semantic search using Large Language Models (LLMS) and search services, but relying on third-party tools often adds complexity to app development.

With the semantic search, you can, in **all** ODC apps, have semantic search over your app data. This means that you can have a semantic search on top of your entities. This is possible because ODC semantic search mechanism uses the power of LLMs to create vector embeddings of your data and then uses these embeddings to perform semantic search.

## What's semantic search?

Semantic search streamlines data exploration by eliminating the constraints of keyword-based queries. By transforming queries into vector embeddings, the system captures the underlying meaning of the text to identify and return the best conceptual matches.  

There are some core principles behind semantic search:  

* **Intent**: The specific goals or tasks users aim to achieve.
* **Context**: The situational relationships between words in a dataset.  
* **Meaning**: The deeper understanding of synonyms and linguistic associations.  

To accomplish this, semantic search uses the capabilities of LLMs together with a vector database to index chunked content.

## When should you use semantic search

Deciding to use semantic search depends on your business needs, but semantic search is particularly effective for:  

* **Chatbots**: Leverage natural language understanding to navigate user intent and context, overcoming the limitations of traditional keyword matching.  
* **Recommendation engines**: Excels at identifying conceptual relationships and synonyms to surface relevant products or content, particularly in e-commerce environments.  

Conversely, scenarios requiring absolute precision, such as serial numbers and error codes, aren't suitable for semantic search.
Also, note that semantic search in ODC supports only text attributes. If your search needs to include other types of data, semantic search isn't the best option.

## The importance of chunking in semantic search

To understand the importance of chunking, consider how semantic search processes data. Semantic search doesn't read text line by line; it converts text into vectors that represent its meaning.

To work effectively, don't turn large datasets into a single vector, as this obscures the meaning for the LLM. Chunking is fundamental as it allows you to break the data into smaller, meaningful pieces so the search engine can find what’s inside.

In ODC case, you are able to select the entities and their attributes that are subjected to semantic search and use different methods for the content chunking, namely:

* **Smart chunking (default)**: Adapts automatically to the specific content found within searchable fields.
* **Fixed-sized chunking**: Defines a specific maximum character count per chunk and a set overlap between them.  
* **Sentence-based**: With this chunking method, you explicitly define how many sentences your chunks are allowed to have, and also the maximum number of characters and overlap for your chunks.
* **Recursive chunking**: Defines character limits and overlaps while prioritizing a hierarchy of specific characters as delimiters.  

## Regional availability and limitations

Semantic search relies on cloud AI infrastructure. Due to regional service availability differences, semantic search varies depending on the region where your ODC environment is hosted.

### Usage of multiple languages

Semantic search over app data supports, in theory, most languages. The following languages have dictionaries that usually enable better results:

* English
* Czech
* Danish
* Dutch
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

These dictionaries address language-specific nuances, such as acronyms, cultural context, and other details, enabling the system to understand phrases better. In all other languages, punctuation is used to divide sentences, which might lead to less accurate results. Also, note that if the system doesn't identify the language, it defaults to English.

### Unsupported regions

ODC semantic search is currently unavailable in the following regions:

* Cape Town (af-south-1)
* Hong Kong (ap-east-1)
* Jakarta (ap-southeast-3)
* Singapore (ap-southeast-1)
* Tel Aviv (il-central-1)
* UAE (me-central-1)

In these specific regions, semantic search triggers cross-region data transfers. To maintain data residency compliance, avoid deploying semantic search within these territories. In case you still want to use semantic search in one of these regions, note that the data will be routed to the European region (eu-central-1) and then back to your region.

<div class="info" markdown="1">

To determine your ODC environment's region, refer to the information provided when you purchased ODC or contact your account manager.

</div>
