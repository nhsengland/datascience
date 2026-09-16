---
title: 'Exploring the relationship between psychotropic medication usage and Talking Therapies treatment outcomes: a retrospective cohort study'
summary: 'Exploring medication use as a predictor of reliable recovery following completion of a course of Talking Therapies, using logistic regression and causal analysis'
tags: ['PRIMARY CARE', 'MENTAL HEALTH', 'MACHINE LEARNING', 'MODELLING', 'RESEARCH', 'STRUCTURED DATA', 'R', 'PYSPARK', 'SQL', 'COMPLETE']
---
*This project was completed by CHRISTINE WELLS, Analyst, in the Modelling & System Analytics Team, as part of the Data Science MRes at the University of Leeds.*

NHS Talking Therapies (NHSTT) provide psychological support to people with anxiety and depressive disorders. The ideal outcome, following a completed course of treatment (minimum 2 sessions) is to achieve ‘reliable recovery’. Psychological therapy may sometimes be supplemented by prescribing psychotropic medication such as antidepressants. At each appointment patients are asked whether they are prescribed and taking any psychotropic medication, although no specific details of any medication is collected and responding is not mandatory. Whilst this information has sometimes been included as a predictor in machine learning-based analysis of therapeutic outcomes, there has been less focus on understanding how outcomes differ between medicated and non-medicated groups. 

## Objectives: 

* To use national NHSTT data to train and test a logistic regression model that included medication status (taking/not) as a predictor of the odds of achieving reliable recovery. 
* Use propensity score matching to undertake causal analysis of the impact of medication on reliable recovery. 

## Design: 
A retrospective cohort study of 2½ years’ worth of patients who had completed treatment. 

## Setting: 
Data was extracted from the NHS England NHSTT database for patients who had completed treatment between 1st January 2022 and 31st May 2025. 

## Participants: 
The cohort was N = 1,120,839 for the logistic regression (669,142 = taking medication, 451,697 = not taking medication) and N = 54,802 for the matching analysis (N = 27,401 per group). 

## Interventions: 
The exposure was whether patients were taking psychotropic medication during treatment or not, and whether they received high or low intensity therapy. 

## Primary outcome measure: 
Whether patients achieved reliable recovery by completion of treatment. Results: Logistic regression on the cohort showed that medication was associated with reduced odds of recovery. Logistic regression on the matched groups suggested:

1. a small but beneficial effect of medication, although this result was non-significant, and 
2. taking medication in combination with high intensity therapy was more beneficial than high intensity therapy alone. 

## Conclusions: 
The results support previous research regarding other predictors associated with increased odds of recovery, including number of treatment sessions and lower levels of deprivation. Whilst the medication information contained in the NHSTT dataset is limited, there is scope to expand this analysis through linkage to prescribing data. Enhancing our understanding of how medication status relates to therapeutic outcomes has important implications for interpretation of NHSTT recovery rates.

#