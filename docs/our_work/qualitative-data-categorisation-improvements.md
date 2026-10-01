---
title: 'Qualitative Data Categorisation Improvements'
summary: 'LLM-based multi-label text classifier for NHS patient experience comments, replacing a legacy ML model with an LLM approach requiring no model training'
origin: 'Insight and Voice'
tags: ['CLASSIFICATION', LLM, 'MACHINE LEARNING', 'NATURAL LANGUAGE PROCESSING', 'MODELLING', 'UNSTRUCTURED', 'TEXT DATA', 'PYTHON', 'IN DEVELOPMENT']
---

## Overview

Patient experience teams across the NHS collect thousands of free-text comments via patient feedback surveys. These comments need categorising against themes from the [Qualitative Data Categorisation (QDC) Framework](https://the-strategy-unit.github.io/PatientExperience-QDC/framework/framework3.html) to identify patterns and drive service improvement.

This is a multi-label classification task — a single comment can be assigned several categories simultaneously. For example, "The staff were very kind but there was not enough seating in the waiting area." covers both "Staff manner & personal attributes" and "Environment, facilities & equipment".

![Diagram showing the classification pipeline: patient comments pass through a redaction process and the data has some columns removed. The prompt is built from the category descriptions, extra classification rules, static examples and RAG-retrieved examples and sent with the survey comments to the LLM. The output from the LLM is then processed and validated and the final output file is constructed. The output is then saved to the destination. An optional workbook is generated to visualise the data in a formatted excel document.](../images/qdc_improvements/QDC_diagram_v3.png)

## Method

The previous approach used a trained sklearn/BERT ensemble that achieved 0.71 macro F1 score. The code for that tool is published [here](https://github.com/The-Strategy-Unit/pxtextmining) and is documented [here](https://the-strategy-unit.github.io/PatientExperience-QDC/).

We replaced this with an LLM-based classifier using Claude Sonnet. The system uses retrieval-augmented few-shot prompting — for each comment being classified, it retrieves semantically similar examples from a corpus of 11,000 labelled comments and includes them as in-context calibration. Comments are processed in batches per API call for efficiency. This approach requires no model training, and making category changes is as simple as updating a prompt. As part of this work, three additional categories were added and evaluated.

Beyond classification, the LLM approach enables segmented sentiment highlighting — each comment is broken into its component clauses, where each assigned category is paired with the corresponding quote from the comment and the sentiment of that quote. This means "The staff were very kind but there was not enough seating in the waiting area." produces two segments: "The staff were very kind" (Staff manner & personal attributes &#8594; Positive) and "there was not enough seating in the waiting area" (Environment, facilities & equipment &#8594; Negative). This gives the NHS England patient experience team a much richer, more actionable view of feedback than flat category labels alone.

## Prompt

Each prompt sent to the LLM consists of the following elements:

1. **Category descriptions** - A list of each topic and a description of when that topic should apply to a comment
2. **Extra classification rules** - Some categories benefit from extra rules to help the model disambiguate topics that can sometimes overlap
3. **Static examples** - these examples contain comments and category labels and are passed into every prompt
4. **RAG examples** - Each comment is embedded and the top 20 most similar comments from the RAG corpus are added to the prompt with their topic labels
5. **The comments** - A batch of comments along with the survey question and service type (if provided)

Since large parts of this prompt are static, we use prompt caching in our API calls to reduce unnecessary computation.

## Results

The LLM approach achieves:

- **Macro F1: 0.77** (vs 0.71 for the legacy model)
- Multi-label classification across 33+ categories with no training requirement
- Per-topic sentiment and evidence extraction


[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
