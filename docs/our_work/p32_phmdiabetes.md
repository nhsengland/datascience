---
layout: base
title: Inequalities in Diabetes from PHM Data
permalink: p32_phmdiabetes.html
summary: How to extract inequalities information from linked population health management data
tags: ['POPULATION HEALTH', 'DISEASES', 'MACHINE LEARNING', 'ETHICS', 'STRUCTURED DATA', 'PYTHON', 'COMPLETE']
---

![Diagram with on the left a box containing the texts: "GP Services & Registration", "Deprivation IoD by LSOA", "Open Street Maps", "Postcode to Lat. Long", "Postcode to LSOA", "Population Demographics", and "Quality & Outcomes (QOF), each with a cartoon reflecting it next to it. This box points to "Process from source" which in turns points to "Save to remote host" and "Aggregate by GP and LSOA" which points to "Downstream analysis..." and a colored map. ](../images/p32fig1.png)
<p align="left">
    <em>Figure 1: Workflow in ESNEFT tools to process the data into Lower Super Output Area granularity for mapping and analysis</em>
</p>

A collaborations with East Suffolk and North Essex foundation trust (ESNEFT) to apply a suite of data science techniques to a large population health data including both primary and secondary care data.  The aim of the project was to identify inequalities in diabetes care whilst making reusable code bases which can now be applied for different conditions and in different organisations.

A small collection of code bases have been created to support the analysis of inequalities in diabetes services for a single locality based on linked population health data.

## Results

The project was able to both deliver new insights around drivers for inequalities as well as reproducible analytical pipelines in the code-bases.  This means the code and approach can be reused for other disease or could be adapted for different localities.

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [DNA Risk Predict](https://github.com/nhsx/dna-risk-predict) & [Diabetes Inequalities](https://github.com/nhsx/p24-pvt-diabetes-inequal) & [Morbidity Network](https://github.com/nhsx/morbidity_network_analysis)|
| Case Study | Awaiting Sign-Off |
| Technical report | [Here](https://github.com/nhsx/ESNEFT_diabetes_StephenRicher/blob/main/stephen-richer-report.pdf) |
| Project Slides | [Here](https://github.com/nhsx/ESNEFT_diabetes_StephenRicher/blob/main/stephen-richer-slides.pdf) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
