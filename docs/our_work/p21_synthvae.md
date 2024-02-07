---
layout: base
title: Developing our SynthVAE code
permalink: p21_synthvae2.html
---

> | "Improving our variational autoencoder to consider fairness and to run on non-gaussian distributions"   

Continuation of the previous development of our variational autoencoder (VAE) to correct for an error discovered since the last project finished.  This error appears when trying to generate data for continuous variables which follow non-Gaussian distributions.  Previously, standard scaling had been used to normalise these variables which was causing the non-gaussian variables to be synthesised poorly.  This was replaced with a Guassian mixture model from the RDT python library to scale and transform these variables into ones with a Gaussian distribution. 

The second phase of this worked focussed on understanding the different ways of measuring and implementing fairness within the synthetic data.  
## Results 

The gaussian mixture model was able to cope with non-gaussian variables thus extending the range of datasets which we can generate from greatly.  Additional hyper-paramter tuning and general coding improvements have increased the reusability and performance of the code. 

Regarding fairness, there are many metrics to choose from and to make the situation more complex, not all metrics are compatible with one another, i.e. you might be able to satisfy an equal odds metric for a group but not an equal prediction for the same group. This means that the level of fairness required is project specific and has to be re-evaluated depending on the research needs. 

Further work will expore the adaption of direct acylic graphs to control for fairness and the impact this has on quality and privacy. 

| Output | Link | 
| ---- | ---- |
| Open Source Code & Documentation | [Github](https://github.com/nhsx/SynthVAE) |
| Case Study | Awaiting Sign-Off |
| Technical report | [Here](https://github.com/nhsx/SynthVAE/blob/main/reports/NHSXSynthVAE%20(2).pdf) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#