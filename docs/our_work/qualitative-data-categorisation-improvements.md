---
title: 'Qualitative Data Categorisation Improvements'
summary: 'LLM-based multi-label text classifier for NHS patient experience comments, replacing a legacy ML model with a RAG-augmented approach requiring no model training'
origin: 'Insight and Voice'
tags: ['CLASSIFICATION', LLM, 'MACHINE LEARNING', 'NATURAL LANGUAGE PROCESSING', 'MODELLING', 'UNSTRUCTURED', 'TEXT DATA', 'PYTHON', 'IN DEVELOPMENT']
---

![Diagram showing the classification pipeline: patient comments pass through RAG retrieval of 20 similar examples from 13,000 labelled comments, then to Claude Sonnet in batches of 50, producing categories, segments and sentiment. Below, an example shows the comment "The staff were great but I couldn't get parked" split into two segments: "The staff were great" labelled Staff manner and Positive, and "I couldn't get parked" labelled Parking and Negative. Performance metrics show Macro F1 of 0.776 versus 0.70 for the legacy model.](../images/our_work/qualitative-data-categorisation-improvements/ee4e9491-3f3b-43f9-b25c-c46d5c22c6d2.png)

Patient experience teams across the NHS collect thousands of free-text comments via the Friends and Family Test (FFT). These comments need categorising against 31 themes from the Qualitative Data Categorisation (QDC) Framework to identify patterns and drive service improvement.

This is a multi-label classification problem — a single comment can be assigned several categories simultaneously. For example, "The staff were great but I couldn't get parked" covers both "Staff manner" and "Parking".

The legacy approach used a trained sklearn/BERT ensemble that required manual retraining and achieved ~0.70 weighted F1.

We replaced this with an LLM-based classifier using Claude Sonnet. The system uses retrieval-augmented few-shot prompting — for each comment being classified, it retrieves semantically similar examples from a corpus of 13,000 labelled comments and includes them as in-context calibration. Comments are processed in batches of 50 per API call for efficiency. This approach requires no model training, and making category changes is as simple as updating a prompt.

Beyond classification, the LLM approach enables segmented sentiment highlighting — each comment is broken into its component clauses, with each segment assigned its own category and sentiment. This means "The staff were great but I couldn't get parked" produces two segments: "The staff were great" (Staff manner, Positive) and "I couldn't get parked" (Parking, Negative). This gives patient experience teams a much richer, more actionable view of feedback than flat category labels alone.

## Results

The LLM approach achieves:

- **Macro F1: 0.776** (vs ~0.70 for the legacy model)
- **Weighted F1: 0.777**
- Multi-label classification across 31 categories with no training data pipeline
- Per-segment sentiment and evidence extraction

## Outputs & Links

Output | Link
---|---
Open Source Code & Documentation (Currently Private) | [Link](https://github.com/nhsengland/QDC_LLM)
Technical Methodology (Currently Private) | [Link](https://github.com/nhsengland/QDC_LLM/blob/main/docs/methodology.md)
Original Framwork Documentation | [Link](https://github.com/The-Strategy-Unit/PatientExperience-QDC)

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
