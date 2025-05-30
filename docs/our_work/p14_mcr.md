---
layout: base
title: Using Model Class Reliance to Understand the Impact of Commerical Data on Predictions
permalink: p14_mcr.html
summary: How to assess the value that commercial sales data of over-the-counter prescriptions has on respiratory death predictions
tags: ['PRESCRIBING', 'DISEASES', 'MACHINE LEARNING', 'CLASSIFICATION', 'MODELLING', 'STRUCTURED DATA', 'COMPLETE', 'EXPERIMENTAL']
---

The primary aim of the project was to apply the novel variable importance technique, [model class reliance](https://papers.nips.cc/paper/2020/hash/fd512441a1a791770a6fa573d688bff5-Abstract.html), to machine learning models which could predict registered respiratory deaths in the UK. The objective was to assess the value of commercial health data in healthcare predictions compared to other available datasets.

## Results

In order to apply MCR, a set of optimal models had to be created which can successfully make the required predictions. The project managed to achieve this outcome with the machine learning model PADRUS (Predicting the amount of deaths by respiratory disease using sales). PADRUS is a random forest regressor which makes accurate weekly predictions of respiratory deaths in 314 local authorities across England 17 days in advance. The models’ features are created from the following dataset types:

* week number,
* commercial sales,
* weather,
* indices of multiple deprivation,
* age and population,
* demographics,
* housing, and
* land use.

MCR was applied to PADRUS showing the highest and lowest impact variables had on predictions across all instances of the model. Grouped MCR was also employed in order for variables to be evaluated in concert as a collection of features created from a dataset type.

The MCR results implied model instances of PADRUS were using variables in different ways to achieve the same predictive results, and suggested where variables could be interchangeable or critical to predictions.

The addition of commercial data show a significant increase in predictive power.  Further results are closed whilst a publication is being reviewed.

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [Github](https://github.com/nhsx/commercial-data-healthcare-predictions) |
| Case Study | Awaiting Sign-Off |
| Technical report | [Here](https://github.com/nhsx/commercial-data-healthcare-predictions/blob/main/report/NHSX%20Report_ValueofCommercialProductSalesDatainHealthcarePrediction_V2.pdf) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
