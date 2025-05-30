---
layout: base
title: Parkinson's Disease Pathology Prediction
summary: Automatic segmentation and detection of Parkinson’s disease pathology using synthetic staining and deep neural networks
category: Projects
origin: Skunkworks
tags: ['DISEASES', 'NEURAL NETWORKS', 'DEEP LEARNING', 'MODELLING', 'UNSTRUCTURED DATA', 'VISUAL DATA', 'CLASSIFICATION', 'PYTHON', 'COMPLETE']
---

![Parkinson's prediction workflow diagram.](../images/parkinsons-detection.png)

"Parkinson's Disease Pathology Prediction" was selected as a project in 2022 following a successful pitch to the AI Skunkworks problem-sourcing programme.

## Results

A proof-of-concept demonstrator written in Python (machine learning models, command line interface (CLI), Jupyter Notebooks).

# Case Study

This is a backup of the case study published [here](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/identifying-and-quantifying-parkinsons-disease-using-ai-on-brain-slices/) on the NHS England Transformation Directorate website.

Identification of Parkinson’s Disease is carried out by neuropathologists who analyse post-mortem brain slices. This process is highly time intensive, and the neuropathologists are highly trained in their field. Being able to look at introducing automation to this process has potential to increase the speed at which Parkinson’s Disease can be diagnosed in a brain, as well as freeing up neuropathologists who are otherwise required to spend hours looking at the brain slices themselves.

**The challenge**
Develop an approach to enhance the identification of biomarkers which are indicative of Parkinson’s Disease, and explore whether automated identification of Parkinson’s Disease in these slices is possible.

### Overview

Parkinson’s UK Brain Bank, at Imperial College London, receives brains which are donated by people who have taken the decision to donate their brain prior to their passing. The Parkinson’s UK Brain Bank is the world's only brain bank solely dedicated to Parkinson's research1. Accurate identification and Parkinson’s Disease in post-mortem brain tissue is critical to ensure that the brain is as useful as possible in research studies. These research studies aim to help us to understand what causes Parkinson’s Disease and how drugs can be developed for Parkinson’s Disease.

Parkinson’s Disease can be diagnosed in a slice of the brain by looking for the presence of a type of protein, which is ‘stained’ (their colour is changed to a more contrasting one) using a chemical. This protein is important, as Lewy Bodies are up of these proteins, and the presence of Lewy Bodies can be indicative of Parkinson’s Disease.

Once the staining is undertaken, a digital image of the brain slice can be taken. A number of these images are produced for different parts of the brain, and it is from these images that the neuropathologist produces their diagnosis.

A significant benefit of working with the Parkinson’s UK Brain Bank was having access to images of a large number of brains, which have been consistently processed and recorded as images. This gave the AI tooling a strong starting point to be developed from.

In this project, a proof-of-concept solution was developed which had two key steps. First, brain slices were synthetically stained (i.e. staining was performed on the digital images using algorithms) to highlight the proteins of interest in bright, contrasting colours. This aimed to provide a view for neuropathologists that was less intensive to analyse.

Following this step, an automated classifier was developed which used the synthetically stained brain slices to produce a judgement as to whether or not the image contained evidence of Parkinson’s Disease. This classifier was able to do this with performance exceeding that of experts manually reviewing the images.

### What we did

Over a 12-week period, the project used the Parkinson’s UK Brain Bank images to explore the viability of using AI to identify Parkinson’s Disease.This rapid innovation is intended to explore a proof of concept that could help predict where Parkinson’s Disease was present in brain slice images.

Overall, about 400 brains were used for this project, split into those both with and without Parkinson’s Disease present. The images from these brains were very detailed as they were taken using microscopes capable of magnifying at 200x what an eye can normally see. This also meant that the images were very large files, so had to be processed using powerful computer hardware. This ensured that analysis could happen within a reasonable timeframe.

The project produced a solution which can be split into two key steps. The first of those was synthetic staining, where the existing images had an algorithm applied to them in order to highlight alpha-synuclein (also known as α-syn or αS) proteins more clearly. These are the proteins which are indicative of Parkinson’s Disease being present. The second step was to automatically classify images of brain slices into whether they contain evidence of Parkinson’s Disease or not.

### Synthetically staining the brain slices

Synthetic staining of the brain slice image refers to taking the original images of slices of brains, and applying an algorithm to them to highlight regions of interest. The benefit of this is to aid neuropathologists in being able to spot relevant material more quickly. This could speed up the overall process of diagnosing Parkinson’s Disease in an image of a brain slice.

The chosen algorithm was a pre-trained type of neural network which had been specifically designed to understand colour, texture and spatial elements of an image. The neural network is provided with hints as to the colours of certain elements in an image. Using this information, and the algorithm’s own understanding of colour, texture and space within images, the algorithm attempts to colour the entire image. The results produced were successful in highlighting α-syn proteins very clearly. Additionally, it was seen that in brain slices without any α-syn proteins, the synthetic staining tended to not incorrectly stain these images. More details on the approach used can be found in the technical report ([here](https://www.biorxiv.org/content/10.1101/2022.08.30.505459v1)).

![](../images/Parkinsons_synthetic_brain_slices.width-800.png)

***Figure 1**: An example of the synthetic staining process. a) the original slide, containing the α-syn proteins stained in a brownish colour b) a processed version of the original slide, filtered for the brownish colour c) the synthetically stained image after the algorithm has been applied to it. The α-syn proteins are now highlighted in a greenish colour.*

### Identifying presence of Parkinson’s Disease

With the ability to synthetically stain images, the next stage of the project could be attempted. This step aimed to classify images of brain slices into whether or not evidence of Parkinson’s Disease was present in the image. For this, a particular type of Neural Network which had previously been demonstrated to work quickly on large datasets. This was important, as while powerful computers were used, the selection of an inappropriate algorithm might have meant that no useful results could be obtained within the 12 week time frame.

The neural network model takes in the synthetically stained images and gives a classification for whether Parkinson’s Disease is present in the image. The results seen using this method were excellent and could match (and exceed) the performance of experts in some aspects.

#### Outcomes and lessons learned

In summary, the code from this project, released as open source on our Github (available to anyone to re-use, [link here](https://github.com/nhsx/skunkworks-parkinsons-detection)), demonstrates the viability of automation of identification of Parkinson’s Disease in post-mortem brain slices. This is achieved by synthetically staining the images, before applying a neural network to predict whether or not the disease is present.

The tool achieves cutting edge performance, and demonstrates ability which exceeds that of expert raters in some aspects. Despite this only being a proof of concept, results were promising, which is exciting for future further development of this work.

A key lesson learned was the importance of good data. This is particularly true in projects involving images where quality and way the image was captured can vary significantly. A key driver of success in this project was having lots of consistent and high quality images to work with.

### What’s next?

The NHS AI Lab Skunkworks team has released the code from the project on [Github](https://github.com/nhsx/skunkworks-parkinsons-detection) to allow anyone to try the methodology out using fake data which has a similar appearance to the images of brain slices.

A second phase is currently being planned to develop this work further, continuing to work in conjunction with Polygeist, Parkinson’s UK and the Parkinson’s UK Brain Bank at Imperial College London.

### Who was involved?

This project was a collaboration between the NHS AI Lab Skunkworks, within the Transformation Directorate at NHS England and NHS Improvement, Parkinson’s UK, Parkinson’s UK Brain Bank at Imperial College London, [Polygeist](https://polygei.st/) and the Home Office’s [Accelerated Capability Environment](https://www.gov.uk/government/groups/accelerated-capability-environment-ace) (ACE).

NHS AI Lab Skunkworks is a team of data scientists, engineers and project leaders who support the health and social care community to rapidly progress ideas from the conceptual stage to a proof of concept.

Accelerated Capability Environment (ACE) is part of the Homeland Security Group within the Home Office. It provides access to more than 250 organisations from across industry, academia and the third sector who collaborate to bring the right blend of capabilities to a given challenge. Most of these are small and medium-sized enterprises (SMEs) offering cutting-edge specialist expertise.

ACE is designed to bring innovation at pace, accelerating the process from defining a problem to developing a solution and delivering practical impact to just 10 to 12 weeks.

Polygeist, a software company specialising in state-scale analytics, builds world-leading AI technology for defence, national security, law enforcement, and healthcare customers. The team for this project was able to produce a live system, producing insights, from a standing start, in 12 weeks.

Output|Link
---|---
Open Source Code & Documentation|[Github](https://github.com/nhsx/skunkworks-parkinsons-detection/)
Technical report|[biorxiv.org](https://www.biorxiv.org/content/10.1101/2022.08.30.505459v1)
Case Study|[Case Study](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/identifying-and-quantifying-parkinsons-disease-using-ai-on-brain-slices/)

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
