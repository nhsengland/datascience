---
title: Building a Tool to Assess the Privacy Risk of Text Data
summary: Can we generate usable privacy scores for text data to support understanding of privacy concerns and the anonymisation process
permalink: c399_privfinger.html
tags: ['LLM','PYTHON', NLP, LLM, RESEARCH, DATA VALIDATION, UNSTRUCTURED DATA, TEXT DATA, PYTHON, ON PAUSE, SYNTHETIC DATA]
---

This work was undertaken as an external commission aiming to build a pipeline of components which firstly generated unstructured medical notes using a structured output from [Synthea:tm:](https://github.com/synthetichealth/synthea) and then running these through [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5) models to transform these into human readable notes.

These notes were then processed using named entity recognition to extract pre-defined identifiers and store these in a structured form.  The algorithm [pycorrect match](https://github.com/computationalprivacy/pycorrectmatch) was then implemented to give a privacy risk score of reidentification from the identifiers.

[Shap](https://github.com/slundberg/shap) analysis was then conducted to understand which components of an individual record and of the dataset as a whole had the highest risk of privacy leakage.

This pipeline could then be run before and after a de-identification process has taken place to understand the impact of the process on the risk score and to generate confidence that the dataset has been appropriately processed for use.

## Results

During the 10 week project the end-to-end code was developed, tested and delivered.  However, key components are dependent on commercial offerings and only the first (of three) levels of identifiers was tested in the setup.

Future work needs to replace some components with open source versions and a large number of experiments needs to be investigated to understand the limitations and where further development would be useful.

This is an ongoing piece of work.

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | Coming Soon |
| Case Study | Coming |
| Technical report | Coming Soon |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
