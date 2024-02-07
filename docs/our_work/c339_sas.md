---
title: Creating a Generic Adversarial Attack for any Synthetic Dataset 
summary: Can the privacy of a generated dataset be assessed through downstream adversarial attacks to highlight the risk of reidentificiation 
permalink: c339_sas.html
---

An extensible code was developed to apply a suite of adversarial attacks to synthetically generated single table tabular data in order to assess the likely success of attacks and act as a privacy indicator for the dataset.  Using this information then informs the generation and information governance process to ensure the safety of our data. 

## Results 

The code-base was successfully developed with code injection points for extensibility.  Unfortunately, as the code could be used as an active attack on a dataset, we have decided not not to make the codebase public but instead aiming to both extend the number of attacks and incoproate the code in our synthetic generation process.  

| Output | Link | 
| ---- | ---- |
| Open Source Code & Documentation | restricted |
| Case Study | Awaiting Sign-Off |
| Technical report | [Blod](https://nhsx.github.io/AnalyticsUnit/SynthAdvSuite.html) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#