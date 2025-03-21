---
title: Investigating Annotation Tools for Named Entity Recognition
authors: [willpoulett]
date: 2024-07-08
categories: 
    - Privacy
    - LLMs
    - Python
    - Annotation Tools
links:
    - TBC
slug: annotation-tools
description: >
    There are various tools for annotating and exploring free text data for Named Entity Recognition. The author explores some of these tools and discusses his experiences. 
---

> We have been building a proof-of-concept tool that scores the privacy risk of free text healthcare data. To use our tool effectivly, users need a basic understanding of the entities within their dataset which may contribute to privacy risk. 

> There are various tools for annotating and exploring free text data. The author explores some of these tools and discusses his experiences. 

<!-- more -->

## Introduction

We have been building a proof-of-concept tool that scores the privacy risk of free text healthcare data called [Privacy Fingerprint (opens in new tab)](https://nhsengland.github.io/datascience/our_work/ds255_privacyfp/).

Named Entity Recognition (NER) is a particularly important part of our pipeline. It is the task of identifying, categorizing and labelling specific pieces of information, known as entities, within a given piece of text. These entities can include the names of people, dates of birth, or even unique identifiers like NHS Numbers.

As of the time of writing, there are two NER models fully integrated within the Privacy Fingerprint pipeline used to identify entities which may contribute towards a privacy risk. These are:

- [UniversalNER (opens in new tab)](https://universal-ner.github.io/): A prompted-based NER Model, where a language model has been finetuned with a conversation-style prompt to output a list containing all entities in the text corresponding to an input entity type.
- [GLiNER (opens in new tab)](https://github.com/urchade/GLiNER): A BERT-like bidirectional transformer encoder with a key benefit over UniversalNER in that it is a smaller model in terms of memory size.

Both NER models in our pipeline need to be fed a list of entities to extract. This is true for many NER models, although some like [Stanza (opens in new tab)](https://stanfordnlp.github.io/stanza/) from [Stanford NLP Group (opens in new tab)](https://stanfordnlp.github.io/) and [BERT (opens in new tab)](https://huggingface.co/docs/transformers/tasks/token_classification) token classifiers do not need an initial entity list for extraction. For our privacy tool to be effective, we want our list of entities to be representative of the real entities in the data, and not miss any important information.

<figure class="inline end" markdown>
![Cartoon of man trying to extract entities. He looks confused and frustrated. He has a speech bubble saying "Extract an entity? What does that mean?"](../../images/annotation_tools_blog/entity_extraction_cartoon.jpg)
<figcaption>Figure 1: A frustrated user trying to extract entites!. </figcaption>
</figure>

Let's consider a new user who wants to investigate the privacy risk of a large unstructured dataset. Maybe they want to use this data to train a new generative healthcare model and don’t want any identifiable information to leak into the training data. Or maybe this dataset is a large list of outputs from a similar model and they want to ensure that no identifiable information has found it's way into the data. They may ask:

_What does my data look like?_

_What entities within my data have a high privacy risk?_

_Wait a second, what even is an entity?_

We want to offer an easy and interactive starting point for new users of our tool, where they can easily explore their data, understand the role of NER and identify what risks lie in their data. If they miss certain entities, this could have large implications on the scoring aspect of our pipeline.

Of course, we want people to use our tool efficiently and effectively! So we asked:

**How can a new user efficiently explore their data to understand what entities exist within the data, and in particular, which entities may contribute to a privacy risk?**

## Annotation Tools

Interactive annotation tools offer a solution to the above problem. If we can include a tool which allows a user to manually label their dataset, alongside live feedback from the NER model, it would allow a user to very quickly understand the entities in their data.

Further to this, some NER models can be surprisingly affected by the wording of entities. The entity titled 'name' may extract both the name of an individual and the name of a hospital. The entity 'person' might only extract the name of the person. We have found that changing the entity 'person' to 'name' in UniversalNER reduced how often names were picked up by the model. If a user gets live feedback from a model whilst labelling, this will help them both finetune which entity names work best, alongside picking out which entities to use at all.

We want a tool that:

- Is easy for a user to setup and use.
- Allows users to label new entities.
- Gets live feedback from the NER model.

There were two approaches we took to develop an annotation tool.

### DisplaCy and ipyWidgets

<figure markdown>
![Example annotation gif using ipywidgets](../../images/annotation_tools_blog/ipywidgets_example.gif)
<figcaption>Figure 2: An example of the ipyWidgets and DisplaCy labelling application. All clinicial notes are synthetic. </figcaption>
</figure>

First, we used [DisplaCy (opens in new tab)](https://spacy.io/usage/visualizers/), [ipyWidgets (opens in new tab)](https://github.com/jupyter-widgets/ipywidgets/blob/main/docs/source/examples/Index.ipynb), and a NER model of choice to generate an interactive tool that works inside Jupyter notebooks. DisplaCy is a visualiser integrated into the SpaCy library which allows you to easily visualise labels. Alongside ipyWidgets, a tool that allows you to create interactive widgets such as buttons, we created an interface which allowed a user to go through reviews and add new entities.

One of the main advantages of this method is that everything is inside a Jupyter notebook. The entity names you want to extract come straight from the experiment parameters, so if you used this in the same notebook as the rest of your pipeline the entitiy names could be updated automatically from the labelling tool. This would allow easy integration into a user workflow.

There is also a button which allows for live feedback from the NER model which is useful given our previous comment on different entitity names having different effects on the NER model.

This approach was simple and resulted in a fully working example. However, highlighting entities manually was not possible, and this meant it was hard to correct predictions that the model got wrong. You are fully reliant on the labels given by the model, and can't add your own.

### Streamlit

<figure markdown>
![Example annotation gif using Streamlit](../../images/annotation_tools_blog/ipywidgets_example.gif)
<figcaption>Figure 3: An example of the Streamlit labelling application. All clinicial notes are synthetic. </figcaption>
</figure>

We explored a second option using [Streamlit (opens in new tab)](https://streamlit.io/). Streamlit is a python framework that allows you to build simple web apps. We can use it alongside a package called [Streamlit Annotation Tools (opens in new tab)](https://github.com/rmarquet21/streamlit-annotation-tools) to generate a more interactive user interface. As an example, a user can now use their cursor to highlight particular words and assign them an entity type which is more hands-on and engaging. Unlike our ipyWidgets example, users can select different labels to be displayed which makes the tool less cluttered, and you can easily navigate using a slider to separate reviews. Like the previous widget, there is a button which uses a NER model to label the text and give live feedback. Including this, the tool is more synergistic, easier to use and more immersive than the ipyWidgets alternative.

However, there were still a few teething issues when developing the Streamlit app. Firstly, Streamlit annotation tool’s has an inability to display `\n` as a new line and instead prints `\n`, resulting in the structure of text being lost. This is a Streamlit issue and we haven’t yet found a way to keep the structure of the text intact. There was an easy fix in which each `\n` was replaced with two spaces (this means the start and end character count for each labelled entity remains consistent with the original structured text), but the structure of the text is still lost which may cause issues for some future users.

Secondly, Streamlit involves a little bit more set up than ipyWidgets. Rather than interacting with the reviews in your notebook you run the app on a local port and access it through your browser. This also makes it harder to retrieve back into your pipeline the list of entities you have labelled. Whilst there is benefit to running all your analysis in one jupyter notebook, the Streamlit app gives a better user experience.

## Future Work and Conclusion

Both labelling tools we have identified have key advantages. DisplaCy and ipyWidgets fit well into your workflow, whilst Streamlit offers a nicer user experience. ipyWidgets and Streamlit are both versatile tools, and so users can edit the annotation tools in the future to fit their own use case.

Following the research and development of these two tools, we believe the ability to interactively annotate, explore and extract entities from your data greatly improves the user experience when using our privacy risk scorer pipeline.

We will publish working examples of annotation using both ipyWidgets and Streamlit, such that a future user can build on them or use them to improve their workflow. The code is available on our [github (opens in new tab)](https://github.com/nhsengland/privfp-experiments).
