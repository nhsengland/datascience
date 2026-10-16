---
title: Building a Bias & Fairness Assessment Pipeline for NHS Predicted Length of Stay: What 8 Weeks as a Data Science Intern Taught Me
authors: [SofiaAlabi]
date: 2026-10-16
categories:
    - Fairness
    - Evaluation
    - Python
    - Professional Development
links:
    - PLoS project page: https://nhsengland.github.io/datascience/our_work/ds_314_plos/
    - Fairlearn: https://fairlearn.org/
slug: plos-bias-and-fairness-pipeline
description: >
    Sofia Alabi reflects on her internship at NHS England, where she built a pipeline to test whether the Predicted Length of Stay model performs fairly across sex, ethnicity, age group and BMI, and what it taught her about the limits of fairness metrics.
---

> Sofia Alabi reflects on her internship at NHS England, where she built a pipeline to test whether the Predicted Length of Stay model performs fairly across sex, ethnicity, age group and BMI, and what it taught her about the limits of fairness metrics.

<!-- more -->

During my internship at NHS England, I had the opportunity to work on something that genuinely matters: making sure an AI model works fairly for every patient, not just on average. Coming from a healthcare background as a former Healthcare Assistant, it was especially meaningful to work on a project focused on improving the understanding of patient pathways and outcomes through data.

The project centred on a Predicted Length of Stay (PLoS) model that classifies patients into one of four stay bands (0–1 day, 2–3 days, 4–7 days, 8+ days). My task was to build a bias and fairness assessment pipeline from scratch to evaluate whether the model performed equally across demographic groups.

## What I built

Using Python, I developed a fairness assessment pipeline that evaluated model performance across key demographic groups using established open-source tools and statistical methods, including Fairlearn. The pipeline assessed performance across four protected characteristics: sex, ethnicity, age group and BMI. It also used bootstrap confidence intervals (500 resamples) to help distinguish genuine disparities from statistical variation in smaller groups.

## What I found

Because the dataset was collected for clinical care rather than analytics, some demographic fields were recorded more consistently than others, which shaped how confidently we could compare model performance across groups. Linking to centrally curated datasets could strengthen future fairness assessments.

Confidence intervals told an equally important story. Some smaller demographic groups showed apparent differences in model performance, but limited representation meant those comparisons were statistically uncertain. This highlighted the importance of considering both data quality and sample size when interpreting fairness results.

## What I learned

Beyond the technical skills, including Git, Python, Fairlearn and statistical testing, this project taught me that fairness in AI is not a technical problem with a purely technical solution. The biggest differences were often linked to who was represented in the data, how completely demographic information was recorded and the realities of how clinical data is captured in practice. A model can only be as fair as the data and systems behind it. This changed how I think about AI. It is as much about understanding data as it is about writing code.

I also learned the importance of being honest about limitations. We found natural variation in how BMI and ethnicity were recorded across sources, which influenced how we interpreted results. Fairlearn measures association, not causation, and recognising these limitations is a critical part of responsible analysis.

Fairness work is about people, processes and data, not just algorithms. Being transparent about limitations is not a weakness in the work; it is an essential part of the work itself.

Grateful to NHS England and the PLoS Team for the opportunity to contribute to something with real clinical impact.
