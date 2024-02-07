---
title: 'Exploring how to create mock patient data (synthetic data) from real patient data'
summary: 'The generation of safe and effective synthetic data to be used in technologies that improve health and social care.'
category: 'CaseStudies'
origin: 'Skunkworks'
tags: ['SYNTHETIC DATA','VAE','PRIVACY','QUALITY','UTILITY','AI']
---

## Info
This is a backup of the case study published [here](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/exploring-how-to-create-mock-patient-data-synthetic-data-from-real-patient-data/) on the NHS England Transformation Directorate website.

## Case Study
The NHS AI Lab Skunkworks team has been releasing open-source code from their artificial intelligence (AI) projects since 2021. One of the challenges faced with releasing code is that without suitable test data it is not possible to properly demonstrate AI tools, preventing users without data access from being able to see the tool in action.

One avenue for enabling this is to provide “synthetic data”, where new “fake” data is generated from real data using a specifically designed model, in a way that maintains several characteristics of the original data. In particular, synthetic data aims to achieve:

- Utility - the synthetic data must be fit for its defined use.
- Quality - it must be a sufficient representation of the real data.
- Privacy - it mustn’t ‘leak’ or expose any sensitive information from the real data.

**The challenge**  
This project aimed to provide others with a simple, re-usable way of generating safe and effective synthetic data to be used in technologies that improve health and social care.

### The challenge
Using real patient data for research and development carries with it safety and privacy concerns about the anonymity of the people behind the information. Various anonymisation techniques can be used to turn data into a form that does not directly identify individuals and where re-identification is not likely to take place. However, it is very difficult to entirely remove the chance of re-identification. Wide release of anonymised data will always carry some risks. Synthetic data aims to remove the need for such concerns because there is no “real patient” connected with the data.

There are many ways to generate synthetic data. One common challenge with synthetic data approaches is that they are usually configured specifically for a dataset. This is a problem because it means a significant amount of work is needed to update them for use with a different data source.

Additionally, once data has been produced, it can be difficult to know whether it is actually useful.

In a partnership project, the NHS Transformation Directorate’s Analytics Unit and the NHS AI Lab Skunkworks team sought to further improve an existing synthetic data generation model (called [SynthVAE](https://nhsx.github.io/nhsx-internship-projects/synthetic-data-exploration-vae/)) and develop a framework for generating synthetic data that could be shared for others to re-use.

### The teams explored how SynthVAE could be used to generate synthetic data, how that data would be evaluated and how the whole process could be documented for others to re-use.

If you would like greater technical detail about this project, please read the version on the [Skunkworks Github website](https://nhsx.github.io/skunkworks/synthetic-data-pipeline).

They sought to:

- increase the range of synthetic data types that SynthVAE can generate
- create a standard series of checks that can be carried out on the data produced, so that people can better understand its characteristics
- implement a structure to allow users to run the full functionality with a single piece of code.

To be able to increase SynthVAE’s range of capabilities, the teams needed an input dataset containing a number of different data types in order to broaden the range of the data produced.

The teams chose to work from a starting dataset that was already in the public domain. This meant people wishing to use the code after release could access and use the same dataset with which the project was developed. MIMIC-III was selected because the size and variety of its data would enable them to produce an input file that would closely match the broad range of typical hospital data.

From the raw [MIMIC-III](https://physionet.org/content/mimiciii/1.4/) files, they produced a single dataset containing treatment provided by a hypothetical set of patients. It looked similar to datasets that might be encountered in a real hospital setting, helping to keep this project as relevant as possible to anyone wishing to explore the use of synthetic data for health and care.


#### 1. Adapting SynthVAE
SynthVAE was originally written primarily to generate synthetic data from both continuous data (data with an infinite number of values) and categorical data (data that can be divided into groups). The inclusion of other data types (like dates) in the new input dataset meant SynthVAE needed to be adapted to take the new set of variables.

#### 2. Producing synthetic data
Having sourced suitable data and created a useful input file, it was possible to use the input file to train a SynthVAE model that could generate synthetic data. The model was used to generate a synthetic dataset containing several million entries, a substantial increase on volumes previously produced using SynthVAE.

This wasn’t without challenges, as SynthVAE hadn’t been substantially tested using dates or large volumes of data. However, SynthVAE was successfully adapted to produce a synthetic version of the input data from MIMIC-III.

#### 3. Creating a checking process
In order to evaluate the privacy, quality and utility of the synthetic data produced, a set of checks were needed. There is currently no industry standard, so the teams chose a range of evaluation approaches designed to provide the broadest possible assessment of the data.

The process aimed to check whether the synthetic data was a good substitute for the real data, without causing a change in performance (also known as the utility). The additional checks that were added aimed to make the evaluation of utility more robust, for example by checking there are no identical records in the synthetic and real datasets, but also to provide visual aids to allow the user to see what differences are present in the data.

These checks were combined and their results collected in a web-based report, to allow results to be packaged and shared with any data produced.

#### 4. Creating a pipeline
Finally, the teams pulled these steps into a single workflow process for others to follow.

The input data generation, SynthVAE training, synthetic data production and output checking processes were chained together, creating a single flow to train a model, produce synthetic data and then evaluate the final output.

To make the end-to-end process as user-friendly as possible, a pipelining library called [QuantumBlack’s Kedro](https://medium.com/quantumblack/introducing-kedro-the-open-source-library-for-production-ready-machine-learning-code-d1c6d26ce2cf) was employed. This allowed each step in the workflow to be linked to the next, meaning users can run all parts of the process with a single command. It also gives users the ability to control the definitions within the pipeline and change it according to their needs.

### Outcomes and lessons learned
The resulting code (click here to see the code) enables users to see how:

- an input dataset can be constructed from an open-source dataset, MIMIC-III
- SynthVAE can be adapted to be trained on a new input dataset with mixed data-types
- SynthVAE can be used to produce synthetic data
- synthetic data can be evaluated to assess it’s privacy, quality and utility
- a pipeline can be used to tie together steps in a process for a simpler user experience.

By using the set of evaluation techniques, concerns around the quality of the synthetic data can be directly addressed and measured using the variety of metrics produced as part of the report.

The approach outlined here is not intended to demonstrate a perfectly performing synthetic data generation model, but instead to outline a pipeline that enables the generation and evaluation of synthetic data. Things like overfitting to the training data, and the potential for bias will be highlighted by the evaluation metrics but will not be remedied.

It’s important to emphasise that concerns around re-identification are reduced by using synthetic data but not completely removed. Looking at privacy metrics for the synthetic dataset will help the user to understand how well privacy has been preserved, but re-identification may still be possible.

### What next?
The Analytics Unit is continuing to develop and improve SynthVAE, with a focus on improving the model’s ability to produce high quality synthetic data.

To better understand the privacy of any patient data used to train a synthetic data generating model, the Analytics Unit has undertaken a project exploring the use of ‘adversarial attacks’ to prove what information about the original training data might be gained from a model alone. The project focussed on a particular type of adversarial attack, called a ‘membership attack. It explored how different levels of information would influence what the attacker could learn about the underlying dataset, and therefore the implications to any individuals whose information was used to train a model.

Who was involved?
This project was a collaboration between the NHS AI Lab Skunkworks and the Analytics Unit within the Transformation Directorate at NHS England and Improvement.

The NHS AI Lab Skunkworks is a team of data scientists, engineers and project leaders who support the health and social care community to rapidly progress ideas from the conceptual stage to a proof of concept.

The Analytics Unit consists of a team of analysts, economists, data scientists and data engineers who provide leadership to other analysts who are working in the system and raise data analysis up the health and care system agenda.

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#