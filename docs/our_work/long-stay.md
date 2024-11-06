---
title: 'Long Stayer Risk Stratification'
summary: 'Machine learning using historical data from Gloucestershire Hospitals NHS Foundation Trust to predict how long a patient will stay in hospital upon admission.'
category: 'Projects'
origin: 'Skunkworks'
tags: ['LOS','NEURAL NETWORKS','PYTHON', 'GAN', 'SQL', 'HTML', 'CSS', 'JAVASCRIPT', 'STRUCTURED DATA', 'ACCURACY']
---

![Long Stayer Risk Stratification screenshot](../images/long-stay.png)

As the successful candidate from the AI Skunkworks problem-sourcing programme, Long Stayer Risk Stratification was first picked as a pilot project for the AI Skunkworks team in April 2021.

## Results

A proof-of-concept demonstrator written in Python (machine learning model and backend), and HTML/CSS/JavaScript (frontend).

# Case Study

## Info

This is a backup of the case study published [here](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/using-machine-learning-to-identify-patients-at-risk-of-long-term-hospital-stays/) on the NHS England Transformation Directorate website.

## Case Study

Studies show that many patients who stay in hospital for extended periods experience negative outcomes: According to the Journal of Gerontology, “Ten days of bed rest in hospital leads to the equivalent of 10 years ageing in the muscles of people over 80” (Kortbein et al 2004). Long stays also create problems for busy hospitals because beds stay occupied for longer and require extra resources to manage. In this context, a long stay is regarded as any stay longer than 21 days.

These longer length of stays are often avoidable, as one study showed 60% of immobile older patients had no medical reason that required bed rest (Graf 2006, American Journal of Nursing).

The Business Intelligence team at Gloucestershire Hospital (GHFT), supported by GHFT's CIO and senior clinical leaders, developed an idea to use AI to address the issue of “long stayers” and was awarded a rapid feasibility project as part of the Skunkworks’ third round of competition at the NHS AI Lab.

> Long stayers at the Gloucestershire Hospitals Trust occupy an average of 278 beds per day, which is around 4% of all admissions but accounts for 34% of bed use. The ability to identify and intervene early could make a real difference to these patients.

### Overview

Sarah Hammond, Gloucestershire Hospitals’ Associate CIO, and Joe Green, Deputy Head of Business Intelligence, report that more than 30% of bed days in all of the Gloucestershire Trust’s acute hospitals are used by long stayers. It has been observed that long stayers have an 11% mortality rate during their hospital stay (compared to 5% of all admissions). Of these long stayers, 23% became unwell after being deemed medically fit for discharge (compared to 1% overall).

Long stayers at the Gloucestershire Hospitals Trust occupy an average of 278 beds per day, which is around 4% of all admissions but accounts for 34% of bed use. The ability to identify and intervene early could make a real difference to these patients.

After the completion of a rigorous Data Protection Impact Assessment (DPIA) and resulting Data Protection Agreement (DPA), the “longstayers” project had access to a good volume of data from over 7 years’ worth of admissions information. By analysing this data using machine learning methods (computer algorithms that learn from data), the team hoped to understand whether it is possible to identify the patients most at risk of becoming “longstayers”.

The challenge was to discover whether AI can provide a useful prediction solution. The follow up is whether that solution could be effectively and safely put into production and the results shared for wider use.

The project sought to:

- predict which patients are most likely to become "long stayers" (stay in hospital for more than 21 days)
- provide hospital staff with a prototype tool that provides a visible long stay risk score on every electronic patient record as soon as a new patient arrives at the hospital
- maximise the learning opportunities from the project by working in the open and making the resulting source code available for continued - experimentation by other researchers and developers
- contribute to potential better outcomes for people staying in hospitals around the country.

### What we did

Over a 12-week period, the project investigated an experimental approach to using AI to better understand the admissions data at Gloucestershire Hospitals. This rapid innovation is intended to explore a proof of concept that could help predict which patient will be a long stayer.

Data from more than 1 million admissions, stored in a secure SQL warehouse, was joined to an electronic patient record system to link key patient demographic indicators to each admission. The data available included age, sex, deprivation level, geography, and admission history like a patient’s presenting complaints, their socio-economic status, emergency department investigations and care home admissions.

This provided a rich and ready dataset for the project using data that is owned and securely held by the trust. This therefore allowed the data to be used for research purposes when anonymised appropriately.

The team:

- worked with clinicians to understand the problem and possible uses for the tool
- developed an historical dataset for the project using patient admissions information
- opted to progress a machine learning Generative Adversarial Networks (GANs) solution using an innovative AI algorithm
- explained which factors contributed to the likelihood of a patient becoming a long-stayer (by building a parametric risk model)
- tested how well the model worked against the expectations from the initial data analysis.

### Why a GANs solution was chosen

GANs, first designed by [Ian Godfellow](https://arxiv.org/pdf/1406.2661.pdf), involves simultaneously training two models. This includes a generative model that captures the data distribution, and a discriminative model that estimates the probability that a sample came from the training data.

The Generative Adversarial Networks (GANs) was chosen because the use of the GANs to predict length of stay from a structured dataset offered a novel and experimental approach to a problem that may have been more commonly solved with models such as gradient boosted trees.

There are many types of GANs, for this project a deep-convolutional generative adversarial network (DC-GAN) was selected to predict the length of stay. This model architecture (which broadly followed the [approach outlined here](https://arxiv.org/abs/1511.06434)) allowed for flexibility with applications over a wide range of data processing problems and the ability to apply a convolutional methodology to mixed data.

Through training it was clear that the discriminator portion of DC-GAN was most effective and that, combined with heuristics that were learned during an initial data-analysis phase, a new hybrid model could be used. Once the DC-GAN model had produced the length of stay estimate, this was fed into a risk model that used a cumulative density function model to produce a risk score for each patient’s likelihood of becoming a long-term hospital stayer. The final output was a risk score for that patient, from 1 to 5, with 5 being the highest risk.

### The outcomes and lessons learned

The project succeeded in achieving:

- a “long stay risk” model that successfully detects two-thirds of long stayers and stratifies the risk in a useful way
- identification of the factors that were predictive of long-stayers (specific to Gloucestershire)
- a model performance accuracy within 1% at all stages when the model was tested on unseen data before, during and after the 2020 COVID waves.

This proof-of-concept risk identifier will enable hospital staff to look closely at whether the patients identified as having a high probability of a long stay could benefit from earlier interventions and changes to their care pathway.

The team at Gloucestershire Hospitals is keen to heed the lessons learned by working together, and taking the next steps to understand what technical, compliance, and logistical requirements are necessary to adopt it.

> Our aim was to develop a proof of concept for a “long stay risk” score algorithm. Would it be possible to predict a patient’s length of stay the minute they arrive at the front door? The initial “long stay risk” model successfully detects two-thirds of long stayers at time of arrival, or very soon after.
– Joe Green, Deputy Head of Business Intelligence, Gloucestershire Hospitals Trust

The results have been very positive. It is hoped the information will allow trust staff to carefully tailor a patient’s care pathway accordingly. Based on a well-established evidence base showing the negative impacts of unnecessary long stays, the AI tool has the potential to lead to decrease in the length of hospital stays overall, with corresponding reductions in patient deterioration and mortality during admission, and also lead to reduced readmission rates.

### What next?

Gloucestershire Hospitals Business Intelligence team reports: “We will soon begin taking the model output tables, which run every 15 minutes, into our electronic patient record system to test and evaluate with clinicians.“

The Skunkworks team will continue to support Gloucestershire Hospitals with how to further test and evaluate the model, and adopt it safely into wider hospital use. The team is also preparing to support other organisations considering a similar approach.

### Who was involved?

This project is a collaboration between NHSX, [Gloucestershire Hospitals NHS Foundation Trust](https://www.gloshospitals.nhs.uk/), [Polygeist](https://polygei.st/) and the Home Office’s [Accelerated Capability Environment](https://www.gov.uk/government/groups/accelerated-capability-environment-ace) (ACE). The AI Lab Skunkworks exists within the NHS AI Lab to support the health and care community to rapidly progress ideas from the conceptual stage to a proof of concept.

The NHS AI Lab is working with the Home Office programme: Accelerated Capability Environment (ACE) to develop some of its skunkworks projects, providing access to a large pool of talented and experienced suppliers who pitch their own vision for the project.

Accelerated Capability Environment (ACE) is part of the Homeland Security Group within the Home Office. It provides access to more than 250 organisations from across industry, academia and the third sector who collaborate to bring the right blend of capabilities to a given challenge. Most of these are small and medium-sized enterprises (SMEs) offering cutting-edge specialist expertise.

ACE is designed to bring innovation at pace, accelerating the process from defining a problem to developing a solution and delivering practical impact to just 10 to 12 weeks.

Polygeist, a software company specialising in state-scale analytics, builds world-leading AI technology for defence, national security, law enforcement, and healthcare customers. The team for this project was able to produce a live system, producing insights, from a standing start, in 12 weeks.

Output|Link
---|---
Open Source Code & Documentation|[Github](https://github.com/nhsx/skunkworks-long-stayer-risk-stratification)
Case Study|[Case Study](https://www.nhsx.nhs.uk/ai-lab/explore-all-resources/develop-ai/using-machine-learning-to-identify-patients-at-risk-of-long-term-hospital-stays/)
Technical report|On request: <a href='mailto:ai-skunkworks@nhsx.nhs.uk?subject=Request%20for%20NHS_AI_Lab_Skunkworks_Long_Stayer_Risk_Stratification_Technical_Report.pdf'>ai-skunkworks@nhsx.nhs.uk</a>

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
