---
layout: base
title: Adding a Clinical Focus to Evaluating Multi-Modal Data Representations
permalink: p31_txtrayalign2.html
summary: How to validate synthetic text generated from images for healthcare applications.
tags: ['SECONDARY CARE', 'NLP', 'UNSTRUCTURED DATA', 'MULTI MODAL', 'VISUAL DATA', 'PYTHON', 'COMPLETE', 'EXPERIMENTAL']
---

![Diagram of the proposed clinical workflow applications of ML to radiology, diagrams connected by arrows.](../images/p31fig1.png)
<p align="left">
    <em>Figure 1: Proposed clinical workflow applications of ML to radiology - using the CXR workflow as an example.  [CDSS = clinical decision support system, CXR = Chest x-ray, EHR = Electronic health record, PACS = Picture archiving and communication system]</em>
</p>

The use of Natural Language Generation (NLG) for the auto generation of radiology reports has the potential to provide multiple radiology workflow applications. Free text reports pose a challenging task from which to compare NLG outputs due to the "ambiguity, syntax, synonymy, medical abbreviations", use of negation, reference to "out of reach" information, linking of associated findings, and overall individual variation in reporting style seen between different
radiologists

An series of evaluation techniques were tested combining components from machine translation metrics (Bleu, Rouge, Meteor), Clinical metrics (CheXpert, Mirqi), and a suggested Clinical Scoring System.

## Results

Combinations of evaluation metrics were tested against three experiments which were trained on single sentence descriptions, multiple sentence descriptions and including the "impression and findings" section of the reports alongside the multiple sentence descriptions.

The metrics used to evaluate the performance of models for clinical tasks require further refinement to ensure clinical accuracy is captured. The effect on model performance from adapting model training as well as performance on external dataset was also conducted.

Three potential uses for NLG models in the clinical radiological workflow highlighted in this work include;

* use as a safety-net for radiologists to auto-fill positive findings if not included in the report by the radiologist,
* provide preliminary reports for acute CXRs to support junior doctors interpreting scans on the wards in the first instance whilst awaiting the radiologists
report communicating critical findings,
* automate follow up oncology scans, e.g. CT, reporting to provide a faster indication if a malignancy has progressed / quantifying response to therapy.

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [Github](https://github.com/nhsx/txt-ray-align) |
| Case Study | Awaiting Sign-Off |
| Technical report | [Here](https://github.com/nhsx/txt-ray-align/blob/main/report/TxtRayAlign_Report2_SH.pdf) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
