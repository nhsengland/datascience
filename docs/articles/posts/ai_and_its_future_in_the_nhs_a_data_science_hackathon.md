---
title: AI and it’s Future in the NHS – A Data Science Hackathon
authors: [willpoulett]
date: 2026-11-03
categories:
    - LLMs
    - Events
slug: ai_and_its_future_in_the_nhs_a_data_science_hackathon
description: >
    Many of our team recently attended a joint hackathon between NHS England, the Department for Health and Social Care, and and NHS Business Services Authority. This blog documents some of the highlights from the day!
---

> Many of our team recently attended a joint hackathon between NHS England, the Department for Health and Social Care, and and NHS Business Services Authority. This blog documents some of the highlights from the day!

<!-- more -->

# AI and it’s Future in the NHS – A Data Science Hackathon

On Thursday 22nd October, data scientists from NHS England, the Department of Health and Social Care, and NHS Business Services Authority came together to partake in a *'If I had a day'* themed hackathon. For participants, the aim for the day was to work with new AI solutions and methods which they had not yet had the time to explore; learning, developing, and sharing knowledge across organisations. 

Days like this allow our data scientists to stay up to date with modern AI techniques, ensuring we can always use the best and newest methods to improve patient safety, support clinical decision making and improve access to healthcare knowledge. 

Eight teams worked across 5 different projects. 

1. LLM Benchmarking investigated how to quantify differences in behaviour of different large language models, building bespoke benchmarks to evaluate LLMs on specific healthcare tasks. 
2. LLM Finetuning investigated whether fine-tuning small language models can improve their performance on specialised tasks, comparing them to base models and larger LLMs.
3. LLM Topic Modelling explored whether modern LLMs can be used for a high-quality topic modelling, without replying on traditional NLP techniques.
4. Geospatial Insight Assistant explored how LLMs and geospatial datasets can be combined to make agentic mapping tools, which can take a free text input and generate geospatial analysis.
5. Evidence-Based Ranking vs LLM-as-a-Judge explored how system one models (e.g. [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) or OpenAI’s decisions) compare to LLMs for tasks such as LLM as a Judge.

The feedback from the day was very positive. For many, the opportunity to spend such a large chunk of time on a task with colleagues from across the country was a real highlight. 

> “Being in management it is a rare pleasure to be able to spend a day with data and code, was fantastic to see how much can be done with AI coding tools and a good base knowledge of techniques. Really great to see the variety of solutions being applied to similar problems too, some really innovative approaches.” - Jonathan Hope, Lead Data Scientist

> “It was great to work with people I don't normally, and for us all to do it in person. Normally we are spread from London to Tyneside!” - Jen Struthers, Senior Data Scientist 

Many also enjoyed the opportunity to work with new AI technology. This included experimenting with agentic coding assistants.

> “My group investigated how system one models could be used in healthcare. These models are essentially generalised classifiers, which are far quicker at classifying tasks than LLMs, whilst still being able to generalise to multiple scenarios. 
Our team used Claude Code to rapidly prototype a series of OpenJev classifiers that ran in the background of a GP conversation being captured by ambient voice technology. The items it could flag included who is speaking and whether the GP is being dismissive. This was just a fun PoC to demonstrate the technology, but taught us lots about how system one models could be used in healthcare.
Additionally, rapidly prototyping with Claude as a group was a fun way to work with agentic coding tools. We debated the best way of displaying the tool, what data should be displayed to the user, and whether OpenJev was appropriate for different tasks.” - Will Poulett, Senior Data Scientist

> “My group was assigned the work on Geospatial Insights in Python. We were given a notebook to start us off which really helped direct us. We worked to assign land types (Urban/Developed, Water, Green Space, etc) and link this to NHS trust sites, and provide insights on the different types of land at different radii of sites.
We discovered how well the Databricks Genie (AI Assistant) worked, and how it could build across multiple files. It was incredibly quick to describe what you wanted done and set it going. In the end, I didn't even open app.py - the Genie built the whole thing. This meant that instead of bug fixing or Googling for syntax we could spend our time discussing extra features we wanted to implement or how a tool like this could be used in the future.
Learning how to use launch a Streamlit app in Databricks was great - as it means we will be able to build these dashboards without needing to make sure any data being shared is public.” - Jen Struthers, Senior Data Scientist 

> “The hackathon was an opportunity to learn about the advances in the healthcare. Our project involved in benchmarking LLM models. The work allowed us to understand the variation of models from different providers and understand the best way validate summary the open source dates of Reports to Prevent Future Deaths. I have learnt to implement API calls to a variety of LLMs and will be using this skill in future projects.” - Kenneth Quan, Senion Data Scientist

Overall, the day was a great success. By utilising these new methods and techniques with data collected by the NHS, we can continue to use data science to help people live healthier longer lives. 

We’d also like to thank Kainos, who took the lead in organising the event, which went incredibly smoothly and was enjoyed by all!

**Would you have liked to be involved?**

Our team is committed to helping individuals across the NHS improve their data science skills and techniques! If you’d like to get regular updates from our team, you can sign up to our community and read our newsletters [here](https://nhsengland.github.io/datascience-pd-newsletter/). Here, we regularly share development opportunities - could you be in a data science hackathon soon? If you’d like to learn more about our team, check out our past projects [here](https://nhsengland.github.io/datascience/our_work/).
