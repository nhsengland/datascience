---
title: 'Examining whether recruitment data can, and should, be used to train AI models for shortlisting interview candidates'
summary: 'Identify where bias has potential to occur when using machine learning for shortlisting interview candidates and mitigate it'
category: 'CaseStudies'
origin: 'Skunkworks'
tags: ['nlp', 'neural networks']
---

## Info
This is a backup of the case study published [here](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/examining-whether-recruitment-data-can-and-should-be-used-to-train-ai-models-for-shortlisting-interview-candidates/) on the NHS England Transformation Directorate website.

## Case Study
Recruitment is a complex process where many factors need to be considered and understood so that the right candidates can be shortlisted for an interview. As well as that, it is a time-consuming process. However, the information provided in a job application has the potential to lead to bias if not handled correctly. This can happen with human shortlisters, but extra care must be taken if a machine (e.g. AI) is involved that is entirely unaware of what is and is not sensitive.


**The challenge**  
Can we identify where bias has potential to occur when using machine learning for shortlisting interview candidates as part of the NHS England recruitment process? How does this manifest, and how can it be mitigated?


### Overview
Recruitment in the NHS involves identifying the best candidates for a wide array of jobs, where the skills typically vary significantly between roles. The process is very time consuming, with applications, CVs and other supporting documents reviewed to identify the best candidates. These candidates are then ‘shortlisted’ for an interview, which is the next step in the process. This shortlisting is done by often highly experienced hiring managers, who have a nuanced understanding of what makes a good candidate. However, the fact that humans are involved in this review process means decisions taken at this stage can vary, from person to person as well as between hiring rounds.

One way to gain some consistency might be to leverage artificial intelligence (AI), specifically machine learning, to undertake this process. The purpose of this project was to review the feasibility and consistency of this in the context of the NHS.

**What do we mean by bias?**
There are many ways to define bias depending on whether it is in relation to the data, design, outcomes or implementation of AI. In this piece of work, bias was investigated in the representativeness of the data set and the results of the predictive model using the distribution and balance of shortlisted candidates across groups of protected characteristics in those who applied.

When talking about bias by the predictive model, the model was determined to have shown ‘bias’ if the errors made in prediction were larger than an accepted error rate (which is defined by the person carrying out the work).

Bias can also be identified by looking at integrity of the source data (looking at factors such as the way it was collected) or sufficiency (see [here](https://en.wikipedia.org/wiki/Fairness_(machine_learning)#:~:text=of%20a%20model.%22-,Sufficiency,-%5Bedit%5D)) of the data

![Bed allocation screenshot](../images/Recruitment_graph.width-800.png)
> **Figure 1**: An example of the synthetic staining process. a) the original slide, containing the α-syn proteins stained in a brownish colour b) a processed version of the original slide, filtered for the brownish colour c) the synthetically stained image after the algorithm has been applied to it. The α-syn proteins are now highlighted in a greenish colour.

> I regularly hear that a bed is a bed and I know it’s not ... But when you have those front door pressures, you can’t get ambulances offloaded and I have beds in the wrong place - this is the time I need the real support, real time data, an automatic risk assessment that is generated for each patient.  
– Member of bed management staff, Kettering General Hospital

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#