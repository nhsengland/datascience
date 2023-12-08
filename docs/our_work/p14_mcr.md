---
layout: base
title: Using Model Class Reliance to Understnad the Impact of Commerical Data on Predictions
permalink: p14_mcr.html
---

# {{page.title}}
> | "How to asses the value that commercial sales data of over-the-counter prescriptions has on respiratory death predictions"   

<p align="center">
    <img src="assets/img/p14fig1.png" alt=""  width="100%"/>
</p>
<p align="left">
    <em>Figure 1: Schematic of the difference between other variable importance tools and the Model Class Reliance approach to explaining the value of a sinlge input variable in a prediction</em>
</p>

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

|:-|:-|:-|
|<img src="assets/img/statistics_badge_S.png" alt  width="80"/>|<img src="assets/img/data_science_badge_S.png" alt  width="80"/>|<img src="assets/img/forecasting_badge_S.png" alt  width="80"/>|
