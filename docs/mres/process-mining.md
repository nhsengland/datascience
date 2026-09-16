---
title: 'Process Mining on Patient Pathways in Healthcare'
summary: 'Assessing the realism of synthetic patient pathways and proposing a taxonomy to grade usefulness'
tags: ['SYNTHETIC DATA', 'DISEASES','MODELLING', 'BEST PRACTICE', 'RESEARCH', 'STRUCTURED DATA', 'TIME SERIES', 'OPEN DATA', 'PYTHON', 'R', 'COMPLETE']
---

*This project was completed by Alistair Bullward, Head of Service, Data Product, in the Product Team, as part of the Data Science MRes at the University of Leeds*

Research on patient pathways is critical to identifying improvements in care and operational efficiencies. Process mining provides a rich set of methods to analyse a series of events that make up a patient pathway. However, patient event data is by its nature personal and sensitive thus accessing this data is often burdensome due to necessary information governance. In addition, there is often limited capacity of data producers to provide data. This is a barrier to researchers wishing to analyse data, especially in the early stages of a project where resource and time may be limited and a clear research question that can be linked to a legal purpose for accessing the data needs to be established via data discovery.  

Generating synthetic data that mimics the real data but does not disclose any confidential information is one way to address this challenge; this can mean the data is freely accessible on the internet for a global research audience. There is a growing number of openly available synthetic health datasets available however there is limited literature on process mining on synthetic data in health, especially when it comes to assessing the suitability of data sets for process mining.   

This paper proposes a taxonomy to assess usefulness of synthetic data for process mining in healthcare. It tests this taxonomy by developing a set of tests and applying them to the openly available synthetic Simulacrum Cancer data set that mimics data for cancer patients in England. It concludes that although this data set can be used for process mining, it is limited as it does not contain consistent information for events along a patient pathway and some key events do on not occur in a realistic order. 

In developing this taxonomy, it was identified that further research is needed on generating high fidelity synthetic data for process mining and that synthetic data fits alongside other privacy enhancing technologies. 

This study aims to save researchers time by proposing a simple taxonomy that producers of synthetic data can apply to their datasets. This will enable researchers and other users of the data to quickly assess if the data is relevant for their work on process mining in health.

Output|Link
---|---
Published Paper|[Link](https://link.springer.com/chapter/10.1007/978-3-031-27815-0_25)

#