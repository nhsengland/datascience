---
title: 'Predicting negligence claims with NHS Resolution'
summary: 'This project investigated whether it is possible to use machine learning AI to predict the number of claims a trust is likely to receive and learn what drives them in order to improve safety for patients.'
category: 'Projects'
origin: 'Skunkworks'
tags: ['CLASSIFICATION','PREDICTION', 'AI']
---

# Project

NHS Resolution provides expertise to the NHS on resolving concerns and disputes. The organisation holds a wealth of historic data around claims, giving insight and valuable data around the causes and impacts of harm.

The NHS Resolution team wanted to understand whether AI methods could be applied to their data to better understand and identify risk, preventing harm and saving valuable resources.

We aimed to prove the value of machine learning in determining insights from the available data. Automated machine learning was used to run repeated processes on the available data in order to select the AI models that uncovered the most relevant information.

# Case Study
This is a backup of the case study published [here](https://transform.england.nhs.uk/ai-lab/explore-all-resources/understand-ai/using-ai-to-support-nhs-resolution-with-negligence-claims-prediction/) on the NHS England Transformation Directorate website.

NHS trusts undertake an enormous number of activities each year (around 240 million in the year 2018 to 2019 according to the [Kings Fund](https://www.kingsfund.org.uk/projects/nhs-in-a-nutshell/NHS-activity)). The vast majority of people receive safe care, however [NHS Resolution](https://resolution.nhs.uk/) received over 15,000 claims for compensation last year on behalf of the NHS in England, which includes hospital trusts and GPs. Although many (almost half the claims in 2018 to 2019) get settled without damages, NHS Resolution figures show that claims can cost the health and care system up to £2.6 billion a year.

In early 2021, the NHS AI Lab Skunkworks team started a rapid feasibility study with NHS Resolution to investigate whether it is possible to use machine learning AI to predict the number of claims a trust is likely to receive and learn what drives them in order to improve safety for patients.

### Overview
NHS Resolution provides expertise to the NHS on resolving concerns and disputes fairly, shares learning to enable organisation-wide improvement and to preserve valuable resources for patient care.

The organisation holds a wealth of historic data around claims, giving insight and valuable data around the causes and impacts of harm.

Over a 10-week period, the project sought to:

- improve patient safety by reducing the time lag between incidents and the detection of claims, giving the opportunity for prevention
- create a risk profile for individual trusts by analysing a variety of NHS data
- better understand future costs to the NHS by predicting the volume of incidents that lead to a claim
- help reduce new claims arising by understanding the factors that drive the likelihood of a claim

The NHS AI Lab Skunkworks team worked with NHS Resolution and Accelerated Capability Environment (ACE) suppliers to provide a rapid delivery plan to:

- develop a machine learning model that could predict claims
- produce a code pipeline that could prepare input data, then train and run the chosen model.

### How the AI machine learning was developed
The project aimed to prove the value of machine learning in determining insights from the available data. Automated machine learning was used to run repeated processes on the available data in order to select the AI models that uncovered the most relevant information.

NHS Resolution provided multiple sources of data from the healthcare system spanning two years. This included claims, incidents, workforce, maternity, staff survey and publicly available population data sources.

The team applied automated machine learning methods to rapidly test multiple approaches. This testing:

- looked for correlations, or similarities, between the datasets and investigated effects associated with time lag
- used different modelling approaches including an XGBoost model and a Bayesian Hierarchical Model (BHM) to reach an end result that could both provide accurate predictions and actionable explanations
- identified the “decision tree” model as the best performing and most cost-effective to train because of its ability to cope with varied data quality (data variables and missing values)
- included a focus on “model explainability” - the need to understand how the model is making predictions so that we can explain what drives negligence claims
#### Constraints

There were a number of constraints that impacted the project including a lack of completeness and consistency across datasets. The data understandably showed a strong association between the number of claims and the size of the trust population, and it was necessary to eliminate the “size effect” so as not to hide other effects present in the data.

It was also not possible to try to predict the rate of claims per specialty (for instance the rate of claims specific to maternity), only by trust, because the data was not complete or granular enough to do so.

#### Data security
The data used for this testing process was pseudonymised by replacing any personal identifiable information with artificial data (pseudonyms). It was responsibly managed in accordance with General Data Protection Regulations (GDPR).

The project made use of ACE’s PodDev environment for the data. Using this bespoke environment meant that sensitive clinical data could be included securely and destroyed at the end of the project in a way that met the requirements of the NHS Resolution data controller.

### Impacts and outcomes
The completion of the “proof of concept” feasibility study led to some significant successes. Although claims prediction was not perfected, the results significantly outperformed baseline models when predicting rates of claims, by trust and by month.

Whilst useful for hospital trusts, predicting the rate of claims is not yet impactful in improving patient safety without further development of this project.

The project has provided an informative view of the data landscape across the wider health service, and its relevance to understanding medical negligence claims.

As a result of the work, it is possible to gain the following insights into what drives rates of claims, from wider health service data:

- The datasets for incidents, specialty, referral-to-treatment and hospital activities have the largest potential impact on the predicted rate of claims.
- The presence of specialties in a trust tends to have a correlation with the predicted rate of claims.
- The number of incidents, and specifically the percentage of incidents resulting in severe harm or death of the patient, also has a correlation with the predicted rate of claims.
- Longer waiting times also appear to correlate with the predicted rate of claims, although this varies with specialty.

The results are an indication that prediction of claims is possible but that large volumes of quality data are required to take the challenge further.

> NHSX Skunkworks was a perfect way for us to kickstart our AI journey. We were able to work with experts who guided us through the process and help us every step of the way. We’ve learned so much and are keen to take this forward for further investigation.  
– Niamh McKenna, Chief Information Officer, NHS Resolution

> This project highlighted not just that the data could broadly be used for better-than-baseline forecasts, but it also suggested a number of actionable ideas on how to improve data quality, something we really care about because without good data there cannot be good AI.  
– Giuseppe Sollazzo, Head of Skunkworks, NHS AI Lab, NHSX

### What next?
The resulting code base and methodology is a starting point for further machine learning exercises. The proof of concept has demonstrated how machine learning could increase NHS Resolution’s understanding of medical negligence claims.

In order to demonstrate a reduction in patient harm, more work will need to be done to select and engineer new features.

Ideally, improving the consistency of the claim reporting methodology across trusts would significantly improve the predictive power of the negligence claims data.

Future improvements to both the data and the model would provide a more accurate forecasting model and more insightful explanations.

Output|Link
---|---
Case Study|https://transform.england.nhs.uk/ai-lab/explore-all-resources/understand-ai/using-ai-to-support-nhs-resolution-with-negligence-claims-prediction/

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#