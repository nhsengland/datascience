---
title: 'Investigating unknown ethnicity records in NHS emergency care data: patterns, predictors and missingness '
summary: 'Supporting the improvement of ethnicity recording in emergency care data by: (a) investigating variation in unknown ethnicity records, (b) exploring patterns of missingness between ethnicity and other variables, and (c) identifying the variables most important in the recording of an unknown ethnicity. '
tags: ['PUBLIC/POPULATION HEALTH', 'EMERGENCY CARE', 'CLASSIFICATION', 'MODELLING', 'STRUCTURED DATA', 'PYTHON', 'R', 'COMPLETE']
---
*This project was completed by Grace Dean, Senior Analyst, in the South East Data & Analytics Team Team, as part of the Data Science MRes at the University of Leeds.*

High quality ethnicity data is necessary for tackling health inequalities. This project looked at unknown ethnicity recording (where the ethnicity is either Null, Not Stated or Not Known) and was focused on three objectives: 

1.	Investigating variation in unknown ethnicity recording in ECDS across different organisation types, patient demographics and attendance characteristics.
2.	Looking at the patterns of missingness between ethnicity and other variables. 
3.	Identifying the factors which most contribute to ethnicity being recorded as unknown. 

## Main Findings

1.	Variation in unknown ethnicity recording was observed across demographics and attendance characteristics, with younger patients, those requiring low-level emergency care and those with fewer attendances more likely to have an unknown ethnicity record. Differences were also observed across organisation type, with higher rates of unknown ethnicity recording in independent sector organisations and community trusts compared to acute trusts. 
2.	Missing data in other ECDS variables was more common and more extensive when ethnicity was unknown. Increases in missingness were observed in variables relating to the investigations and treatments received by the patient, the severity of the patient’s condition, the chief complaint on arrival and place of discharge.
3.	Provider site code was identified as the most important variable in recording ethnicity as unknown, and a subset of acute trusts and independent sector organisations were identified as disproportionately contributing to unknown ethnicity records.

Output|Link
---|---
Code and Documentation - private while under development|[Link](https://github.com/nhsengland/ethnicity-coding-ECDS)

#