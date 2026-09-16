---
title: 'Supporting Dementia Diagnosis'
summary: 'Demonstrated the impact of COVID-19 on dementia diagnosis and the use of clinical codes within primary care patient records in high-performing machine learning classifiers and identified useful clinical code clusters for dementia diagnoses and the requirement to maintain and retrain classifiers due to changes in health care services.'
tags: ['PRIMARY CARE', 'CLASSIFICATION', 'FORECASTING', 'MODELLING', 'RESEARCH', PATIENT IDENTIFIABLE DATA, 'STRUCTURED DATA', 'PYTHON', 'COMPLETE']
---

*This project was completed by Emily Michelmore, Senior Data Product Manager, in the Data Product Team, as part of the Data Science MRes at the University of Leeds*

I worked in Primary Care analytical team and was the lead analyst for the monthly Dementia publication during the pandemic so had an interest in using the dataset to explore support post-pandemic recovery

Dementia affects one in 14 people aged 65 and over in the UK. However, early symptom detection in primary care settings can be challenging. NHS and PHE statistics indicated the detrimental impact of COVID-19 pandemic on dementia patients, but insight was limited to due to data availability. 

This study analysed 18,419 SNOMED codes from 60,247,062 patient records held in the GPES Data for Pandemic Planning and Research (GDPPR) dataset to further understand the impact of the pandemic. Of these patients, 308,801 patients were identified as having a dementia diagnosis between 1st January 2019 and 21st March 2022. 

A two-step machine learning approach was conducted, a random forest to determine features of importance which informed the features to be included in a decision tree. Two dementia cohorts, before COVID-19 and during COVID-19 and a control cohort without a dementia diagnosis were tested. The random forest classifiers had high performance (accuracy: 0.90 v 0.91) and similar clinical cluster features were identified as most important. The high-ranking features were selected for the decision tree classifiers that had lower performance and more variance (accuracy: 0.79 v 0.84). 

This methodology identified useful clinical code clusters for dementia diagnosis and the requirement to maintain and retrain classifiers due to changes in health care services; these results can be used to inform the implementation of machine learning in primary care settings to improve dementia diagnosis and thus support recovery from the COVID-19 pandemic.

#