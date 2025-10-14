---
title: 'Prediction of CVD Onset'
summary: 'Analysis and prediction of onset of first cardiovascular disease event in people with type 1 diabetes in England, using healthcare record data from the National Diabetes Audit.'
tags: ['SECONDARY CARE', 'DISEASES', 'POPULATION HEALTH', 'FORECASTING', 'RESEARCH', 'STRUCTURED DATA', PATIENT IDENTIFIABLE DATA, 'PYTHON', 'R', 'SQL', 'COMPLETE']
---

*This project was completed by David Connelly, Principal Information Analyst, in the Clinical Outcomes and Indicators Team, as part of the Data Science MRes at the University of Leeds*

Cardiovascular disease (CVD) is major source or morbidity and mortality in people with Type 1 Diabetes Mellitus (T1DM). Better understanding of the features associated with onset of CVD in people with T1DM can help support disease management. 

A logistic regression approach was used to investigate prediction of onset of first CVD event in people with T1DM. This cohort study of 142435 individuals utilised electronic health record data from the National Diabetes Audit (NDA) and Hospital Episode Statistics (HES) datasets in England. 

Dataset features were assessed for their association with onset of CVD and a logistic regression model was developed with the goal of predicting a first CVD event in 2018-19 audit year. Modifiable and non-modifiable variables were considered in the model. Non-modifiable variables included Age, Sex, duration of diabetes, ethnicity and deprivation. Modifiable variables included blood glucose, systolic blood pressure, BMI, blood cholesterol, smoking status, statin use and care process completion. 

## Conclusions
Prediction accuracy was low due to class imbalance. However, feature importance for variables such as IMD, smoking status and blood cholesterol levels, corresponds to findings in existing literature. One ambiguous result in terms of features importance was the role of sex in onset of CVD for people with T1DM.

#