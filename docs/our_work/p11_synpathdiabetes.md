---
layout: base
title: Applying our SynPath Simulator to a Diabetes Pathway
summary: Exploration work into incorporating learning into a pathway simulator for diabetes.  This work has fed our current SynPathGo project to create synthetic patient pathways and a foundation for agent based modelling in the NHS.
permalink: p11_synpathdiabetes.html
tags: ['DISEASES', 'SIMULATION', 'GENERATION', 'TIME SERIES', 'SYNTHETIC DATA']
---

<figure markdown>
![Image of a table that compares three types of simulation models. The first type is health economics simulation models in diabetes. Examples include UKPDS (2020), NIHR SPHR Diabetes prevention model (Squires et al., 2016), and the Day model of Diabetic retinopathy (2013). The learnings from these models are the key stages of model building, key elements to include in the pathway, and best practices for conceptualizing a pathway. The second type is simulation models in transport. Examples are bus networks (Xie, Ma et al., 2014) and developments in the field (review) (Kagho, Balac et al., 2020). The learnings include good modeling of timing, such as whether agents optimize their time leaving the house for a commute, and bottleneck and corridor modeling. The third type is evacuation models. An example is modeling evacuation using a neural network (Tkachuk, Song et al., 2018). The main learning is adapting agents to respond to their environment using a neural network.](../images/p11fig1.png)
<figcaption>Figure 1: Table of learning algorithms considered for the simulation intelligence layer </figcaption>
</figure>

Using the SynPath framework we created a diabetes simulation for 800 patients.  These patients could interact within a fictional local area with hospitals providing outpatient and inpatient services, GP practices and community healthcare services.

## Results

The project showed how to develop a set of environments, interactions and patients from academic literature, policy, and clinical resources. The model currently runs a simulation that prints outputs of patient records into the console.

Future collaboration around validation and how to apply learning algorithms are being pursued.

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [Github](https://github.com/nhsx/SynPath_Diabetes) |
| Case Study | Awaiting Sign-Off |
| Technical report | [Here](https://github.com/nhsx/SynPath_Diabetes/blob/main/t2dm/reports/Technical%20Report%20(SynPath%20Diabetes)%20v1.pdf) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
