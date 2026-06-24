---
title: "Interview with a Data Scientist - The Fairness Enthusiast"
authors: [KonstantinGeorgiev]
date: 2026-03-30
categories:
- Data Science Interviews
slug: interview_with_konstantin_georgiev
description: >
  Welcome to another instalment of our “Interview with a Data Scientist” series, where we explore the careers and work of the talented data scientists across our healthcare organisations. We aim to showcase the fantastic individuals who contribute to Data Science within the healthcare sector and provide valuable insights for those considering a career in this field.
---

> Today we’re interviewing Konstantin Georgiev, a postdoctoral researcher at the University of Edinburgh’s Institute for Neuroscience and Cardiovascular Research and former NHS England Data Science Officer. Konstantin’s journey from software engineering in Bulgaria to using multimodal AI for cardiac diagnostics in NHS Scotland offers fascinating insights into the intersection of deep learning, fairness in AI, and real-world healthcare impact.

<!-- more -->

This interview orginally was published in the [March edition](https://nhsengland.github.io/datascience-pd-newsletter/posts/2026_03/newsletter.html) of the Data Science Community for Health and Care Newsletter. You can subscribe and join the community [here](https://forms.office.com/pages/responsepage.aspx?id=slTDN7CF9UeyIge0jXdO48pr_29hyJFKpCZ7SYYvjeFUNUVPMUk0STlDRlJMNklIWEI3V0NZVTZXVS4u&route=shorturl).


## How did you end up in data science in your healthcare organisation? What did you do before, and what really sparked your interest in this field?

My path into health data science felt both quite sudden and incredibly long at the same time, and it certainly wasn’t something I ever expected or dreamed of doing!

Everything started off at the Technical University of Varna in Bulgaria in 2015, where I barely passed the informatics entry exam to qualify for my bachelor’s degree! In my first year, the bar was set quite low, and I was highly unmotivated because, apart from programming, as ‘prospective engineers’, we were forced into taking courses in electrical and mechanical engineering, which were notoriously difficult to clear. Quite a few people in our group dropped out, but I just managed to scrape by and move on.

In my second year, I was quite frustrated with uni life, and I had already made up my mind that if I was going to learn anything meaningful in this life, I needed to reach out to people and find a ‘niche’ that I found genuinely interesting. So, I got in contact with senior developers, looked up their companies, and just started steamrolling through courses (free access to Coursera materials was a game-changer!).

I took courses on everything from full-stack web development to mobile apps, and then I finally came across my first taste of AI and machine learning. During that time, I completed a short internship in optical character recognition and computer vision, which really opened my eyes to what was possible with AI.

Fast-forward to 2019: I blinked twice and became a software engineering graduate with a competitive European scholarship, and was accepted to study an MSc in Artificial Intelligence at the University of Aberdeen. That’s where the healthcare sector came into play, and it really showed me how multi-faceted AI applications can be as products. As part of my dissertation and industrial placement, I collaborated with [Red Star AI](https://redstar.ai/), a Scottish healthcare startup, to develop an explainable AI tool for predicting patient outcomes from discharge notes. I built deep text classifiers using CNNs and then wrapped them with the LIME (explainability) framework to highlight which parts of discharge letters contributed most to predictions of mortality and readmission. That project made me realise how much impact AI could have on actual patient care, not just as an academic exercise but as something that could help clinicians make better decisions.

What really hooked me was seeing how routine healthcare data, the kind that’s being collected every day across NHS Scotland, could be transformed into actionable insights. After my MSc, it was an easy decision to join the Precision Medicine PhD programme at the University of Edinburgh, as I had already built a foundation in wrangling routine healthcare data and pitching risk prediction algorithms to stakeholders across NHS Scotland.

My PhD was essentially more of the same, but more focused on building decision-support tools that could drive better care for older people. I worked with some challenging, massive cohorts from NHS Lothian, developing machine learning models (shout-out to XGBoost!) to forecast everything from pre-symptomatic dementia risk up to predicting the exact number of healthcare contacts a patient would need during their hospital stay.

## Once you joined your healthcare organisation, what was that experience like? What different roles and teams have you been a part of, and how have they shaped your career?

My healthcare data science journey has been quite multifaceted, which I think has been one of my greatest strengths. Since October 2020, even while doing my PhD, I’ve been working part-time as a Health Data Scientist with Red Star AI. One of our standout projects was the [Fracture Liaison Service](https://redstar.ai/products/fracture-liaison-service/) for NHS Greater Glasgow & Clyde. We designed XGBoost models predicting fragility fracture risk and built a clinical dashboard that ended up reducing case processing time by 55% and saved physicians 28 hours per week: that’s about a full working week freed up to focus on actual patient care.

Between January and June 2025, I took on a role as a Data Science Officer with NHS England in Edinburgh and Leeds as part of their PhD Data Science Internships programme. This was actually on my second try and towards the end of my PhD, so never feel disheartened if you didn’t get the role! Overall, the job was a fantastic opportunity to dip my toes into NHS England practices and meet a whole network of new people from the NHSE engineering and data science teams.

I learned about measuring fairness and explainability in multimodal AI for risk prediction. With the mentorship of my wonderful colleague Sophie Martin (now a postdoctoral researcher at UCL, working on some exciting dementia research!), I developed the [MM-HealthFair](https://github.com/nhsengland/mm-healthfair) framework, an open-source PyTorch framework for understanding bias in deep multimodal fusion using the MIMIC-IV dataset. The toolkit turned out to be so comprehensive that it might’ve overcomplicated our narrative a bit! It incorporated fairness metrics (demographic parity, equalised odds), multimodal feature importance scoring (an extension of Shapley values for multimodal scenarios), and adversarial debiasing strategies.

For me, this opened up so many potential avenues for researching new methods in fairness-aware learning and the importance of this when we’re talking about applying AI algorithms across our whole population. With the excellent help of my supervisors, Dan Schofield, Jonny Pearson and Jonathan Hope, we showed the many implications this could have for validating AI algorithms across NHS trusts and ensuring equitable implementation of clinical AI, which is even more important now with the wide range of foundation models being developed to solve complex medical tasks.

## What are you currently working on? Are there any projects that you’re particularly excited about, or that you feel are making a real difference? What impact are you having?

Since October 2025, I’ve been a Postdoctoral Researcher at the University of Edinburgh, supported by a British Heart Foundation grant, and since then, I’ve shifted my focus to applying multimodal AI for improving the diagnosis of acute cardiac conditions in clinical practice. I am actively trying to bring together everything I’ve learned from multimodal fusion to fairness assessment into what I’m most excited about right now.

I’m currently developing a novel multimodal foundation model that fuses Electronic Health Records (EHR), electrocardiogram (ECG) waveforms, and chest X-ray (CXR) images to predict acute cardiac conditions in the NHS Lothian (Edinburgh) emergency departments. We’re working with a rich cohort of over 170,000 patients from our [DataLoch](https://dataloch.org/) Heart Disease Registry who experience acute coronary syndrome. The goal is to improve diagnostic precision for myocardial infarction, heart failure, and pulmonary embolism, all conditions that are becoming a major burden on our population, where early, accurate diagnosis is absolutely critical and where current diagnostic pathways can sometimes miss opportunities or order unnecessary tests.

What makes this particularly exciting is that we’re not just building another AI model. Using my experience from the MM-HealthFair project, I’m investigating how different multimodal fusion mechanisms affect both diagnostic performance and fairness across socio-demographic groups here in Scotland. Healthcare data notoriously contains biases: whether that’s underrepresentation of ethnic groups, age gaps, or socioeconomic deprivation. And if we don’t actively address these, our AI systems will perpetuate or even amplify them when we combine multiple modalities together.

The challenge is finding the optimal fusion strategy: do we fuse early at the feature level, late at the decision level, or somewhere in between? How do these choices impact fairness? And can we provide new helpful benchmarks for fairness that researchers can use in their own studies?

The impact I’m hoping to achieve with this project is threefold. First, streamline risk interpretation in complex cardiac presentations: that is, help clinicians quickly identify high-risk patients who need immediate intervention. Second, reduce unnecessary clinical tests by safely ruling out low-risk patients who don’t need them, such as an echo when symptoms are not suggestive. Every avoided unnecessary test means lower healthcare costs, reduced patient anxiety, and freed-up resources for those who truly need them. Finally, as you might’ve guessed: fairness!! And this will ensure that the patient population is not being systematically disadvantaged by the AI system.

## Looking back on your time in your healthcare organisations Data Science team, what were the most impactful moments? How do you reflect on that experience now?

One of the standout moments from my time with the NHS England Data Science team was seeing MM-HealthFair grow from a rough idea in a notebook to a fully fledged open-source framework that other people in the NHS could install, run, and critique. It was the first time I’d built a toolkit with so many complex components covering fairness, explainability, and multimodal performance, all treated as coequal design goals rather than add-ons, and watching colleagues stress-test it against real clinical questions made the work feel very concrete.

I also really valued the internal discussions around “what good looks like” for AI in the NHS: meaning not just AUROC, but questions about protected characteristics, deployment risk, and how to communicate limitations to non-technical teams. Those conversations, plus the chance to contribute something reusable to the wider NHSE GitHub ecosystem, were easily the most meaningful parts of the internship for me.

Professionally, the experience pushed me to level up my data science skills and critical thinking (especially important in academia). I became much more rigorous about reproducibility and engineering standards. I deepened my understanding of fairness methodology in a very practical sense: thinking carefully about model trade-offs and how to explain them to clinicians. Finally, I got better at stakeholder communication: translating fairly involved multimodal fusion explanations into something that clinical and policy colleagues could challenge, and ultimately see value in.

## If you could give someone just starting out in data science a few pieces of advice, what would they be? And what resources have you found particularly helpful along the way that you can share?

My first piece of advice would be not to focus too much on resources, but to build a mindset: build a strong foundation, sure, but also don’t forget to seek advice while you’re at it. Read papers, talk to healthcare professionals, talk to programme managers who lead initiatives you’re interested in, and even shadow clinicians in their work if you can. I think the best data science in healthcare happens at the intersection of technical excellence and collaboration.

Also, try to put everything you do out in the open (I need to take this advice as well, as it’s not so easy with closed research environments!). Build projects, contribute to open source, and make your code available on GitHub. I feel that this often encourages you to write clean, well-documented code and to think carefully about how others will use your work.

Try to think about the full project lifecycle and not just the exciting modelling bit. Yes, XGBoost and PyTorch are powerful tools, but you’ll spend far more time on data extraction, cleaning, feature engineering, and validation than on tuning hyperparameters. Learn to work with messy real-world data. My experience setting up big data pipelines (e.g., MLOps), whether it’s extracting features from MIMIC-IV or working with real Scottish Morbidity Records from multiple NHS health boards, has been just as valuable, if not more so, than my modelling skills.

We have unprecedented amounts of data, powerful computational tools, and growing recognition from healthcare systems that AI can genuinely improve patient outcomes. But we also need to do it responsibly, and that creates many opportunities to take on exciting projects.

___

We hope you have found Konstantin’s interview insightful! If you are interested in learning more about the Data Scientists working in healthcare, you can read our previous iterations of the ["Interview with a Data Scientist"](https://nhsengland.github.io/datascience/articles/category/data-science-interviews/){target="_blank"} on the NHS England Data Science Website.
