---
layout: base
title: Connected Publications
permalink: publications.html
summary: Our work has produced a number of publications
tags: ['PUBLICATIONS']
---

List of pre-releases and publications connected to our work

[13] [https://www.nature.com/articles/s42256-025-01116-5](https://www.nature.com/articles/s42256-025-01116-5)

**Towards deployment-centric multimodal AI beyond vision and language**

Xianyuan Liu, Jiayang Zhang, Shuo Zhou, Thijs L. van der Plas, Avish Vijayaraghavan, Anastasiia Grishina, Mengdie Zhuang, **Daniel Schofield**, Christopher Tomlinson, Yuhan Wang, Ruizhe Li, Louisa van Zeeland, Sina Tabakhi, Cyndie Demeocq, Xiang Li, Arunav Das, Orlando Timmerman, Thomas Baldwin-McDonald, Jinge Wu, Peizhen Bai, Zahraa Al Sahili, Omnia Alwazzan, Thao N. Do, Mohammod N. I. Suvon, Angeline Wang, Lucia Cipolina-Kun, Luigi A. Moretti, Lucas Farndale, Nitisha Jain, Natalia Efremova, Yan Ge, Marta Varela, Hak-Keung Lam, Oya Celiktutan, Ben R. Evans, Alejandro Coca-Castro, Honghan Wu, Zahraa S. Abdallah, Chen Chen, Valentin Danchev, Nataliya Tkachenko, Lei Lu, Tingting Zhu, Gregory G. Slabaugh, Roger K. Moore, William K. Cheung, Peter H. Charlton & Haiping Lu

*Robust and comprehensive evaluation of large language models (LLMs) is essential for identifying effective LLM system configurations and mitigating risks associated with deploying LLMs in sensitive domains. However, traditional statistical metrics are poorly suited to open-ended generation tasks, leading to growing reliance on LLM-based evaluation methods. These methods, while often more flexible, introduce additional complexity: they depend on carefully chosen models, prompts, parameters, and evaluation strategies, making the evaluation process prone to misconfiguration and bias. In this work, we present EvalSense, a flexible, extensible framework for constructing domain-specific evaluation suites for LLMs. EvalSense provides out-of-the-box support for a broad range of model providers and evaluation strategies, and assists users in selecting and deploying suitable evaluation methods for their specific use-cases. This is achieved through two unique components: (1) an interactive guide aiding users in evaluation method selection and (2) automated meta-evaluation tools that assess the reliability of different evaluation approaches using perturbed data. We demonstrate the effectiveness of EvalSense in a case study involving the generation of clinical notes from unstructured doctor-patient dialogues, using a popular open dataset. All code, documentation, and assets associated with EvalSense are open-source and publicly available*

---

[12] [https://arxiv.org/abs/2602.18823](https://arxiv.org/abs/2602.18823)

**EvalSense: A Framework for Domain-Specific LLM (Meta-)Evaluation**

Adam Dejl, **Jonathan Pearson**

*Robust and comprehensive evaluation of large language models (LLMs) is essential for identifying effective LLM system configurations and mitigating risks associated with deploying LLMs in sensitive domains. However, traditional statistical metrics are poorly suited to open-ended generation tasks, leading to growing reliance on LLM-based evaluation methods. These methods, while often more flexible, introduce additional complexity: they depend on carefully chosen models, prompts, parameters, and evaluation strategies, making the evaluation process prone to misconfiguration and bias. In this work, we present EvalSense, a flexible, extensible framework for constructing domain-specific evaluation suites for LLMs. EvalSense provides out-of-the-box support for a broad range of model providers and evaluation strategies, and assists users in selecting and deploying suitable evaluation methods for their specific use-cases. This is achieved through two unique components: (1) an interactive guide aiding users in evaluation method selection and (2) automated meta-evaluation tools that assess the reliability of different evaluation approaches using perturbed data. We demonstrate the effectiveness of EvalSense in a case study involving the generation of clinical notes from unstructured doctor-patient dialogues, using a popular open dataset. All code, documentation, and assets associated with EvalSense are open-source and publicly available*

---

[11] [https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1761624/abstract](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1761624/abstract)

**Evaluating Privacy Leakages in LLM-driven Ambient Clinical Documentation**

Jenny Chim, **Jonathan Pearson**, **Dan Schofield**, Maria Liakata

*Automated documentation tools are being rapidly adopted in healthcare and clinical workflows. Among these are AI-enabled ambient scribing products, which transcribe conversations between patients and healthcare providers, then produce clinical records using automatic speech recognition (ASR) and generative AI such as Large Language Models (LLMs). While research suggests these technologies can reduce clinical burden, safe and responsible deployment requires that these tools determine what captured information is appropriate to record and under which circumstances. This presents a contextual privacy challenge distinct from PII leakage or data memorization and remains largely untested. We address this gap by operationalizing privacy leakage as the inappropriate inclusion of third-party personal information in LLM-generated clinical notes. We construct a benchmark of transcripts containing private information with gold standard clinical notes by enriching patient metadata from the aci-bench corpus and injecting third-party personal information across six relationship types and seven information topics. We evaluate open weight LLaMA 3.1 8B and 70B, Mixtral 8x7B and 8x22B, and proprietary Claude 3.5 Haiku and Sonnet models on note generation using prompts with varied privacy and structural requirements. Results reveal that all examined models leaked third-party information, and privacy instructions helped reduce leakage but proved neither complete nor robust as a solution. These results emphasize the need to build privacy-by-design systems and develop evaluation strategies that reflect emerging information synthesis and sharing practices.*

---

[10] [https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/privacy-enhancing-technologies/case-studies/g7-dpas-emerging-technologies-working-group-use-case-study-on-privacy-enhancing-technologies/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/privacy-enhancing-technologies/case-studies/g7-dpas-emerging-technologies-working-group-use-case-study-on-privacy-enhancing-technologies/)

**G7 DPAs' Emerging Technologies Working Group use case study on privacy enhancing technologies**

The IEEE Synthetic Data working group, Professor Khaled El Emam, University of Ottawa, Canada, **Dr Jonathan Pearson, NHS England Digital Analytics and Research, UK**, Professor Pierre-Antoine Gourraud, Université de Nantes, France, Dr Aurélien Bellet, National Institute for Research in Digital Science and Technology (Inria), France

*This hypothetical use case aims to demonstrate how synthetic data, generated from a real medical prescription dataset, can be used as part of a testing strategy for the development of a healthcare planning and resource allocation system, without jeopardising the privacy of real patients.*

---

[9] [https://www.researchsquare.com/article/rs-5701032/v1](https://www.researchsquare.com/article/rs-5701032/v1) 

**Constructing multicancer risk cohorts using national data from medical helplines and secondary care**

**Hadi Modarres**, Dimitris Pipinis, **Divya Balasubramanian**, **Rupert Chaplin**, **Scarlett Kynoch**, **Achut Manandhar**, Gursimran Thandi, Rebecca Cavilla, Emma Hirst-Williams

*Identification of cohorts at higher risk of cancer can enable earlier diagnosis of the disease, which significantly improves patient outcomes. In this study, we use machine learning to predict cancer diagnosis in the next year. We select nine cancer sites with high incidence of late-stage diagnosis or worsening survival rates, and where there are currently no national screening programmes. We use National Health Service (NHS) data from medical helplines (NHS 111) and secondary care appointments from all hospitals in England. We show that features based on information captured in NHS 111 calls are among the most influential in driving predictions of a future cancer diagnosis. Our predictive models exhibit good discrimination (AUC – 0.78 – SD 0.04), ranging from 0.69 (ovarian cancer) to 0.83 (oesophageal cancer). While our predictive modelling provides patient level risk predictions, our emphasis is on constructing cohorts of patients who may be at risk of cancer rather than individual risk scores. We present an approach of constructing cohorts at higher risk of cancer based on feature importance and considering possible bias in model results. These outputs can be used to develop highly targeted case finding services, which could help increase earlier detection rates and reduce health disparities. This approach is flexible and can be tailored based on the group the intervention targets (i.e. symptomatic or asymptomatic patients) and the data available to those charged with administering the intervention.*

---

[8] [https://arxiv.org/abs/2311.13978](https://arxiv.org/abs/2311.13978)

**Medisure: Towards Assuring Machine Learning-Based Medical Image Classifiers Using Mixup Boundary Analysis**

Adam Byfield, **William Poulett**, **Ben Wallace**, Anusha Jose, Shatakshi Tyagi, Smita Shembekar, Adnan Qayyum, Junaid Qadir, Muhammad Bilal

*Machine learning (ML) models are becoming integral in healthcare technologies, necessitating formal assurance methods to ensure their safety, fairness, robustness, and trustworthiness. However, these models are inherently error-prone, posing risks to patient health and potentially causing irreparable harm when deployed in clinics. Traditional software assurance techniques, designed for fixed code, are not directly applicable to ML models, which adapt and learn from curated datasets during training. Thus, there is an urgent need to adapt established software assurance principles such as boundary testing with synthetic data. To bridge this gap and enable objective assessment of ML models in real-world clinical settings, we propose Mix-Up Boundary Analysis (MUBA), a novel technique facilitating the evaluation of image classifiers in terms of prediction fairness. We evaluated MUBA using brain tumour and breast cancer classification tasks and achieved promising results. This research underscores the importance of adapting traditional assurance principles to assess ML models, ultimately enhancing the safety and reliability of healthcare technologies. Our code is available at [https://github.com/willpoulett/MUBA_pipeline](https://github.com/willpoulett/MUBA_pipeline).*

---

[7] [https://publichealth.jmir.org/2024/1/e46485](https://publichealth.jmir.org/2024/1/e46485)

**The Use of Online Consultation Systems or Remote Consulting in England Characterized Through the Primary Care Health Records of 53 Million People in the OpenSAFELY Platform: Retrospective Cohort Study**

**Martina Fonseca**, Brian MacKenna,  Amir Mehrkar, The OpenSAFELY Collaborative, Caroline E Walters, George Hickman,  **Jonathan Pearson**,  Louis Fisher,  Peter Inglesby,  Seb Bacon,  Simon Davy, William Hulme,  Ben Goldacre,  Ofra Koffman,  Minal Bakhai

*We aimed to explore general practice coding activity associated with the use of Online Consultations (OC) systems in terms of trends, COVID-19 effect, variation, and quality.  The OpenSAFELY platform was used to query and analyze the in situ electronic health records of suppliers The Phoenix Partnership (TPP) and Egton Medical Information Systems, covering >53 million patients in >6400 practices, mainly in 2019-2020.  We successfully queried general practice coding activity relevant to the use of OC systems, showing increased adoption and key areas of variation during the pandemic at both sociodemographic and clinical levels. The work can be expanded to support monitoring of coding quality and underlying activity. This study suggests that large-scale impact evaluation studies can be implemented within the OpenSAFELY platform, namely looking at patient outcomes.*

---

[6] [https://arxiv.org/abs/2403.19802](https://arxiv.org/abs/2403.19802)

**Developing Healthcare Language Model Embedding Spaces**

**Niall Taylor**, **Dan Schofield**, Andrey Kormilitzin, Dan W Joyce, Alejo Nevado-Holgado

*Pre-trained Large Language Models (LLMs) often struggle on out-of-domain datasets like healthcare focused text. We explore specialized pre-training to adapt smaller LLMs to different healthcare datasets. Three methods are assessed: traditional masked language modeling, Deep Contrastive Learning for Unsupervised Textual Representations (DeCLUTR), and a novel pre-training objective utilizing metadata categories from the healthcare settings. These schemes are evaluated on downstream document classification tasks for each dataset, with additional analysis of the resultant embedding spaces. Contrastively trained models outperform other approaches on the classification tasks, delivering strong performance from limited labeled data and with fewer model parameter updates required. While metadata-based pre-training does not further improve classifications across the datasets, it yields interesting embedding cluster separability. All domain adapted LLMs outperform their publicly available general base LLM, validating the importance of domain-specialization. This research illustrates efficient approaches to instill healthcare competency in compact LLMs even under tight computational budgets, an essential capability for responsible and sustainable deployment in local healthcare settings. We provide pre-training guidelines for specialized healthcare LLMs, motivate continued inquiry into contrastive objectives, and demonstrates adaptation techniques to align small LLMs with privacy-sensitive medical tasks.*

---

[5] [https://link.springer.com/chapter/10.1007/978-3-031-56107-8_21](https://link.springer.com/chapter/10.1007/978-3-031-56107-8_21) - Conference Paper

**Hypergraphs for Frailty Analysis Research Paper**

**Zoe Hancox**, Samuel D. Relton, Andrew Clegg, Philip G. Conaghan, and **Daniel Schofield**

*Inclusion of mortality to hypergraphs alongside the most prevalent combinations of frailty conditions.  This paper demonstrates that this technique enables us to determine the probability of acquiring another condition as well as understanding the connection and sequencing of acquiring comorbidities.*

---

[4] [https://doi.org/10.1101/2023.08.31.23294903](https://doi.org/10.1101/2023.08.31.23294903) - (Pre-Print)

**Representing Multimorbid Disease Progressions using directed hypergraphs**

**Jamie Burke**, Ashley Akbari, Rowena Bailey, **Kevin Fasusi**, Ronan A.Lyons, **Jonathan Pearson**, James Rafferty, and **Daniel Schofield**

*To introduce directed hypergraphs as a novel tool for assessing the temporal relationships between coincident diseases,addressing the need for a more accurate
representation of multimorbidity and leveraging the growing availability of electronic healthcare databases and improved computational resources.*

---

[3] [https://doi.org/10.1016/j.epidem.2022.100662](https://doi.org/10.1016/j.epidem.2022.100662)

**Large-scale calibration and simulation of COVID-19 epidemiologic scenarios to support healthcare planning**

**Nick Groves-Kirkby**, Ewan Wakeman, Seema Patel, Robert Hinch, Tineke Poot, **Jonathan Pearson**, Lily Tang, Edward Kendall, Ming Tang, Kim Moore, Scott Stevenson, Bryn Mathias, Ilya Feige, Simon Nakach, Laura Stevenson, Paul O'Dwyer, William Probert, Jasmina Panovska-Griffiths, Christophe Fraser

*... We adapted an agent-based model of COVID-19 to inform planning and decision-making within a healthcare setting, and created a software framework that automates processes for calibrating the model parameters to health data and allows the model to be run at national population scale on National Health Service (NHS) infrastructure. ... These simulations were used to support operational planning in the NHS in England, and we present the example of the use of these simulations in projecting future clinical demand during the rollout of the national COVID-19 vaccination programme. ...*

---

[2] [https://doi.org/10.1101/2023.01.25.23284428](https://doi.org/10.1101/2023.01.25.23284428)

**Primary care coding activity related to the use of online consultation systems or remote consulting: an analysis of 53 million peoples’ health records using OpenSAFELY**

**Martina Fonseca**, Brian MacKenna, Amir Mehrkar, The OpenSAFELY Collaborative, Caroline E Walters, George Hickman, **Jonathan Pearson**, Louis Fisher, Peter Inglesby, Seb Bacon, Simon Davy, William Hulme, Ben Goldacre, Ofra Koffman, Minal Bakhai

*We aimed to explore general practice coding activity associated with the use of online consultation systems in terms of trends, COVID-19 effect, variation and quality.*

---

[1] [https://doi.org/10.21203/rs.3.rs-2226531/v1](https://doi.org/10.21203/rs.3.rs-2226531/v1)

**Assessing the value of integrating national longitudinal shopping data into respiratory disease forecasting models**

**Elizabeth Dolan**, James Goulding, Harry Marshall, Gavin Smith, Gavin Ling, Laila Tata

*... We investigated the value of integrating sales of non-prescription medications commonly bought for managing respiratory symptoms, to improve forecasting of weekly registered deaths from respiratory disease at local levels across England, by using over 2 billion transactions logged by a UK high street retailer from March 2016 to March 2020. We report the results from the novel AI explainability variable importance tool Model Class Reliance implemented on the PADRUS model. ...*

---

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
