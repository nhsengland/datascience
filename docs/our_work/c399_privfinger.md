---
layout: base
title: Building a Tool to Assess the Privacy Risk of Text Data  
permalink: c399_privfinger.html
---

> | "Can we generate usable privacy scores for text data to support understanding of privacy concerns and the anonymisation process "   

<p align="center">
    <img src="assets/img/c399fig1.png" alt=""  width="100%"/>
</p>
<p align="left">
    <em>Figure 1: The methodology works in the following way: generated structured data for an individual record, transform this into unstructured medical notes, encode identifiers through named entitiy recognition, evaluate privacy, perform deidentification, repeat process.</em>
</p>

This work was undertaken as an external commission aiming to build a pipeline of components which firstly generated unstructured medical notes using a structured output from [Synthea:tm:](https://github.com/synthetichealth/synthea) and then running these through [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5) models to transform these into human readable notes.

These notes were then processed using named entitiy recognition to extract pre-defined identifiers and store these in a structured form.  The alogrithm [pycorrect match](https://github.com/computationalprivacy/pycorrectmatch) was then implemented to give a privacy risk score of reidentification from the identifiers.  

[Shap ](https://github.com/slundberg/shap) analysis was then conducted to understand which components of an individual record and of the dataset as a whole had the highest risk of privacy leakage.  

This pipeline could then be run before and after a deidentification process has taken place to understand the impact of the process on the risk score and to generate confidence that the dataset has been appropriately processed for use. 

## Results 

During the 10 week project the end-to-end code was developed, tested and delivered.  However, key components are dependent on commercial offerings and only the first (of three) levels of identifiers was tested in the setup.   

Future work needs to replace some components with open source versions and a large number of experiments needs to be investigated to understand the limitations and where further development would be useful. 

This is an ongoing piece of work.


| Output | Link | 
| ---- | ---- |
| Open Source Code & Documentation | Coming Soon |
| Case Study | Coming |
| Technical report | Coming Soon |

|:-|:-|:-|:-|
|<img src="assets/img/machine_learning_badge_S.png" alt  width="80"/>|<img src="assets/img/Synthetic.png" alt  width="80"/>|<img src="assets/img/data_science_badge_S.png" alt  width="80"/>|<img src="assets/img/statistics_badge_S.png" alt  width="80"/>|
