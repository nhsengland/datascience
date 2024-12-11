---
title: 'Renal Health Prediction'
summary: 'Identifying acute kidney injury (AKI) patients at higher risk of requiring ITU, needing renal support (dialysis), or likely to have a higher potential for mortality.'
category: 'Projects'
origin: 'Skunkworks'
tags: ['AKI','DEEP LEARNING', 'TIME SERIES', 'NEURAL NETWORKS', 'PYTHON']
---

![diagram showing the renal health prediction workflow. At the top there are three boxes that say "electronic observations", "medication data", and "blood test results". All three boxes flow into a box that says "time series data builders (with missing data handling)", which flows into "Machine learning model". This then flows out into a box that says "Time series prediction of: no change, ITU bed, dialysis, Death. At least 24h in advance."](../images/renal-health-prediction.png)

Renal Health Prediction was selected as a project in Spring 2022 following a successful pitch to the AI Skunkworks problem-sourcing programme.

## Results

A proof-of-concept demonstrator written in Python (machine learning models, command line interface (CLI), Jupyter Notebooks).

Output|Link
---|---
Open Source Code & Documentation|[Github](https://github.com/nhsx/skunkworks-renal-health-prediction/)
Technical report|[PDF](https://github.com/nhsx/skunkworks-renal-health-prediction/raw/main/docs/renal-health-prediction-technical-report.pdf)
Pre-print (MedRxiv)|[PDF](https://www.medrxiv.org/content/10.1101/2023.02.22.23286184v1)

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
