---
title: 'Data Lens'
summary: 'Data Lens brings together information about multiple databases, providing a fast-access search in multiple languages.'
category: 'Projects'
origin: 'Skunkworks'
tags: ['NLP', 'SCRAPING','JAVASCRIPT','PYTHON', 'HTML','CSS']
---

![Data Lens screenshot](../images/data-lens.png)

As the successful candidate from a Dragons’ Den-style project pitch, Data Lens was first picked as a pilot project for the NHS AI (Artificial Intelligence) Lab Skunkworks team in September 2020.

The pitch outlined a common data problem for analysts and researchers across the UK: large volumes of data held on numerous incompatible databases in different organisations. The team wanted to be able to quickly source relevant information with one search engine.

## Results

A prototype website written in HTML/CSS/JavaScript (frontend), JavaScript (backend) and python (scrapers, search) implementing elasticsearch and natural language search across a number of NHS databases.

# Case Study

This is a backup of the case study published [here](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/data-lens-a-fast-access-data-search-in-multiple-languages/) on the NHS England Transformation Directorate website.

A pilot project for the NHS AI Lab Skunkworks team, Data Lens brings together information about multiple databases, providing a fast-access search in multiple languages

### Overview

As the successful candidate from a Skunkworks problem-sourcing event, Data Lens was first picked as a pilot project for the NHS AI (Artificial Intelligence) Lab Skunkworks team in September 2020.

The pitch outlined a common data problem for analysts and researchers across the UK: large volumes of data held on numerous incompatible databases in different organisations. The team wanted to be able to quickly source relevant information with one search engine.

### How Data Lens works

Following a 12-week development phase, a first-stage prototype of the Data Lens has been completed. Using Natural Language Processing (NLP) and other AI technologies, the Data Lens project is creating a universal search engine for health and social care data catalogues and metadata.

The Data Lens joins up data catalogues from NHS Digital, the Health Innovation Gateway, MDXCube, NHS Data Catalogue, PHE Fingertips and the Office for National Statistics.

By providing user-friendly access to previously time-consuming separate data catalogues, Data Lens aims to:

- present information about data from across the sector with one search
- give preview information and direct users to an original location (avoiding the need for another database)
- provide multilingual support and a user focused approach
- reduce workload and improve the quality of information available
- build up a picture of what data is collected and how it flows through the health and social care system.

The search tool not only increases data access and collaboration, it is learning to improve the results it provides by tracking what people search for, whether they click through and which dataset they use so that its results can be even more relevant over time.

Using Natural Language Processing (NLP), the engine is able to suggest relevant results that go beyond the scope of the search terms it is given. With the use of browser translation, it also supports searches and results in all 71 languages supported by Amazon Web Services (AWS), increasing the usability and inclusivity of the product.

The prototype is getting support through the NHS digital service development pipelines - part of the journey towards achieving a fully fledged AI product that is making a real difference to the delivery of health and social care.

### Why Data Lens is needed

The health and social care sector has huge amounts of data, spread across many NHS organisations and even more databases. When searching for information it can often be difficult to find out whether it exists, and where it is. Searching and cross-referencing multiple data catalogues can also be extremely time-consuming.

This project furthers the ‘Joining-Up Care Agenda’ by enabling cross-organisational views of data.

Using artificial intelligence to power this search engine reduces the time required to make the most of existing data sets, and answers the call from the Secretary of State for Health and Social Care to turbo-charge data responsiveness and ease the burden of data collection across the health and care system.

### Open source Data Lens code

Code and documentation from the development of this project is available for developers and AI enthusiasts. By making code freely available it is hoped that new search engines can be developed and that more organisations will engage with using AI.

With thanks to colleagues at NHSX Analytics Unit, Accelerated Capability Environment (ACE) and Naimuri - the ACE community member selected via competition - we undertook the following open approach over 12 weeks and 6 sprints:

1. NHSX Analytics Unit colleagues identified a number of openly licenced data sets from the healthcare world - forming the core of the proof-of-concept.
2. Partners at Naimuri built the platform on the community edition of ElasticSearch, a popular system for full-text search engines.
3. The team employed various Natural Language Processing (NLP) techniques in order to go further than providing simple keyword searches.
4. The AI was trained to understand better semantic similarities in searches, i.e. to suggest results for “smoking” alongside “cancer” using vector analysis and cosine similarity.
5. User feedback was built into the AI training, so the more users who give “thumbs up” (or down) to suggested results, the better the results will become over time.
6. Fuzzy matching was implemented to help with typos and misspellings.
7. A recommendation engine was developed to suggest related but not searched for sets.
8. Finally, around 9 published NHS acronyms and jargon busters were used to help unpick things like “A&E” and “IP”.

The team brought in metadata from NHS Digital, NHS England and Improvement, Public Health England, Office for National Statistics and Health Data Research UK in order to prove that Data lens could onboard from different organisations in different ways: APIs, scraping, even manual metadata files.

> Working with the AI Lab Skunkworks on this project was Agile in the truest sense of the word. We pitched an idea, had funding approved and were up and running in a very short amount of time. I sincerely hope it can be taken forward into production to help its users get value from the wealth of data and information that is produced by the Health and Social Care sector.
– Paul Ross, Data Engineer, NHSX Analytics Unit.
<!-- -->
> This project has shown the value of better data access using intelligent, domain specific search. The approach of creating a proof of concept and the freedom it's given us to apply advanced technology has really added value.
– Kieran Moran, Naimuri.
<!-- -->
> At ACE our overriding mission is to keep the public safe, so we welcomed the opportunity to work with NHSX, and help them tackle the challenges they and the wider healthcare sector face.
– Simon Christoforato, CEO of ACE’s Vivace supplier community.

Output|Link
---|---
Open Source Code & Documentation|[Github](https://github.com/nhsx/skunkworks-data-lens)
Case Study|[Case Study](https://www.nhsx.nhs.uk/ai-lab/explore-all-resources/develop-ai/data-lens-a-fast-access-data-search-in-multiple-languages/)

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
