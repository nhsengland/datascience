---
layout: base
title: NHSSynth
permalink: p41_nhssynth.html
summary: Continuation from the two previous synthevae projects with the aim to create a full experiment pipeline for production
tags: ['SYNTHETIC', 'VARIATIONAL AUTOENCODER', 'DIFFERENTIAL PRIVACY', 'PIPELINE']
---

![Structure of the workflow incorporating user configuation, data preprocessing, model selection, evaluation, and visualisation](images/nhssynthmodules.png)

This project seeked to take the learning from our previous work on variational autoencoders with differentail privacy for single table tabular data generation, and turn the code into a pipeline where experiments could be rigourously undertaken including comparison with other architectures (e.g. GANs), applicaiton to other datasets with comparable metrics, and experiments around constraining the direct acylic graph to deal with biases in the data.  

## Results

The pipeline is contained within the open code and allows for both config files to be run or a simplar command line interface.   Models can be switched in and out with a moderate amount of effort allowing for consistent comparisons and taking our synthetic generation work from a single investigation of a model to exploring how the latest models compare to our current workflows. 

Further work is needed to fix a bug when applying constraints and to enforce the mixed guassian model to include higher modes. 

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [Github](https://github.com/nhsengland/NHSSynth) |
| Case Study | Awaiting Sign-Off |
| Technical report | [io page documentation](https://nhsengland.github.io/NHSSynth/) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
