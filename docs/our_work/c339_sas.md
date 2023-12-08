---
layout: base
title: Creating a Generic Adversarial Attack for any Synthetic Dataset 
permalink: c339_sas.html
---

# {{page.title}}
> | "Can the privacy of a generated dataset be assessed through downstream adversarial attacks to highlight the risk of reidentificiation "   

<p align="center">
    <img src="assets/img/c339fig1.png" alt=""  width="100%"/>
</p>
<p align="left">
    <em>Figure 1: Attack diagrams for the currently incorporated scenarios.  Scenario 1: Access to the synthetic dataset and a description of the generative model’s architecture and training procedure.  Scenario 2: Access to a black box model that can provide unlimited synthetic data, with data realistic of the training distribution gathered by the attacker, which may be an example synthetic dataset released by the researchers.</em>
</p>

An extensible code was developed to apply a suite of adversarial attacks to synthetically generated single table tabular data in order to assess the likely success of attacks and act as a privacy indicator for the dataset.  Using this information then informs the generation and information governance process to ensure the safety of our data. 

## Results 

The code-base was successfully developed with code injection points for extensibility.  Unfortunately, as the code could be used as an active attack on a dataset, we have decided not not to make the codebase public but instead aiming to both extend the number of attacks and incoproate the code in our synthetic generation process.  

| Output | Link | 
| ---- | ---- |
| Open Source Code & Documentation | restricted |
| Case Study | Awaiting Sign-Off |
| Technical report | [Blod](https://nhsx.github.io/AnalyticsUnit/SynthAdvSuite.html) |

|:-|:-|:-|
|<img src="assets/img/Synthetic.png" alt  width="80"/>|<img src="assets/img/statistics_badge_S.png" alt  width="80"/>|
