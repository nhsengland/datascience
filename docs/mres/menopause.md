---
title: 'Menopause-Related Diagnosis Coding'
summary: 'An analysis of menopause-related diagnosis coding in secondary care electronic health records using machine learning'
tags: ['SECONDARY CARE', 'MACHINE LEARNING', 'LINKAGE', 'EXPLAINABILITY', 'RESEARCH', 'MODELLING', 'STRUCTURED DATA', 'PYTHON', 'COMPLETE']
---

This project was completed by Jane Winter, Senior Analytical Lead in the Insight & Voice Team, as part of the Data Science MRes at the University of Leeds

## Objective
The menopause can be an important factor in determining the most appropriate treatment pathways for women, but there is a lack of awareness. We analyse clinical coding of menopause in secondary care electronic health care records in order to understand the current use of diagnosis codes. This can help improve the potential for supporting better treatment pathways and also for using routinely collected data to support future research in this area.

## Study Design
Age-matched analytical study of menopause related diagnosis codes within inpatient electronic health records for patients in English hospitals in 2019-20.

## Methods
Data from the Hospital Episode Statistics (HES) administrative dataset, covering all NHS hospitals in England, shows that c.40,000 primary or secondary diagnosis codes related to the menopause are recorded. Three cohorts of inpatient episodes from 2019-20 were defined: 
**Group 1:** episodes with a menopause code; 
**Group 2:** episodes without a menopause code from the same patients; 
**Group 3:** an age-matched cohort of episodes without a menopause code from different patients, selected at a ratio of 4:1 compared to Group 1. 

These were linked to outpatient records from the previous year. Machine learning classification techniques, including decision trees, were used to model and explain the differences between Group 1 and the comparison groups, Groups 2 and 3.

## Results
We analysed episodes of care from 147,897 patients. The analysis was successful in identifying whether a menopause-related diagnosis code is present on a HES inpatient record. The most important features of our chosen models, decision trees, were consistently where the patient is being treated under a gynaecology-related specialty. Models performed with an accuracy of 0.83 and 0.94 when tested on previously unseen data.

## Conclusion
This study has identified the circumstances under which menopause coding is currently utilised and reported in HES. This highlights that there may be gaps, which if addressed could improve the potential for future research and possibly lead to improved treatment pathways for women. 

# 