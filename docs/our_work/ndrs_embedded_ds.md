---
title: 'Embedded Data Scientists in the National Disease Registration Service (NDRS)'
summary: 'We have datascientists that work with the National Disease Registration Service supporting various functions.'
tags: ['GENOMICS', 'POPULATION-HEALTH', 'RAP', 'SQL', 'R', 'TEXT DATA', 'LINKAGE']
---

## Aim

The aim of this collaboration is to support NDRS with implementing data science based projects and support the upskilling of staff. 

## Projects

We have supported NDRS with a range of projects.

### Clinical Measurement Extractor

This is an LLM pipeline to extract out clinical measurments from free-text data. This is using AWS services such as BedRock and SageMaker. For more information, please follow the link to this [project page](./clinical_measurement_extractor.md).

| Output                             | Link                                                                 |
| ---------------------------------- | -------------------------------------------------------------------- |
| Private repo | [Github Repo](https://github.com/NHSE-NDRS/clinical_measurement_extractor)|

### ONS Population RAP Pipeline

This is a gold-level RAP, R-based codebase that scrapes population data from the ONS website to produce three tables reporting population counts broken down by year, LSOA, gender, age, and age bands. This data is used by NDRS analysts to support the calculation of population-based metrics.

| Output                             | Link                                                                 |
| ---------------------------------- | -------------------------------------------------------------------- |
| Private repo | [Github Repo](https://github.com/NHSE-NDRS/ONS_Population_Download)|

### Germline Count RAP Pipeline

An R-based codebase was developed to create visualisations showing the monthly and yearly counts of specific germline tests, as well as the percentage change in counts over time. The goal is to help evaluate the data quality of germline test counts and assess appropriate timelines for data sharing.

| Output                             | Link                                                                 |
| ---------------------------------- | -------------------------------------------------------------------- |
| Private repo | [Github Repo](https://github.com/NHSE-NDRS/Germline_Testing_Counts)|

### Supporting the Cancer Genomics Improvement Programme

The aim of this project is to link multiple datasets to capture the cancer diagnosis-to-treatment pathway, specifically for cases where genetic testing is required. Support for this project involved writing a hybrid of SQL and R scripts to define the cohort of interest and to extract relevant dates and events from pathology testing.

| Output                             | Link                                                                 |
| ---------------------------------- | -------------------------------------------------------------------- |
| Private repo | [Github Repo](https://github.com/NHSE-NDRS/Cancer_Genomics_Improvement_Programme)|


#
