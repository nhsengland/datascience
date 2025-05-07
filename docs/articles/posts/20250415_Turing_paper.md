---
title: Driving Responsible Data Science: A Case Study of NHS England's Data Science Team
authors: [MiaNoonan]
date: 2025-04-15
categories:
    - Ethical AI
links:
    - https://zenodo.org/records/15053194
slug: driving-responsible-data-science
description: >
    Driving Responsible Data Science: A Case Study of NHS England's Data Science Team. This is a reproduction of the case study completed by the NHS England Data Science Team as a part of the Turing Experts in Residence programme.
---

# Driving Responsible Data Science: A Case Study of NHS England's Data Science Team

*This is a reproduction of the case study completed by the NHS England Data Science Team as a part of the Turing Experts in Residence programme. The original can be found [at this website](https://zenodo.org/records/15053194)*


The NHS is built on [values ](https://www.nhsconfed.org/what-we-do/our-values) of fairness, trust, compassion and safety. As artificial intelligence (AI) becomes a more prominent tool in healthcare – from automation of administrative processes to disease prediction and medical imaging analysis – NHS England’s data science team is working to ensure these values remain central to technological advancement.

This is much more than just a box-ticking exercise: it’s about shaping best practices, embedding those practices in projects right from the start, and being as transparent and open as possible throughout the development lifecycle. That way, patients can have confidence that their (often sensitive) personal information is being used safely, fairly and responsibly, and that the innovative use of data-driven technologies including AI can add genuine value to services and activities, improving outcomes for the tens of millions of people who rely on NHS England to support their healthcare needs.

Members of the NHS England data science team have been taking part in the 2024 cohort of The Turing Way Practitioners Hub’s Experts in Residence programme, giving them a platform to discuss with other professionals the opportunities, challenges and best practices of AI development and adoption within a large public-sector organisation.

This case study will explore some of the insights and ideas arising from those discussions, alongside a selection of NHS England’s ongoing projects. Particularly, we put a spotlight on ethical considerations in data science, from design to monitoring and evaluation, ensuring responsible decision-making at all stages.


## Ethics in AI Design: Open Source Framework of Data Hazards

We are all familiar with the symbols used to denote potentially harmful chemicals: fire for flammable, skull and crossbones for toxic, and so on. Misuse of data can also cause harm, which is why Dr Natalie Zelenka and Dr Nina Di Cara founded the community-driven, open source [Data Hazards project](https://datahazards.com/) in 2021. Data Hazards labels cover potential hazards such as automated decision-making, risk to privacy, and bias reinforcement. The project members, who have worked with *The Turing Way*, have now incorporated a chapter on this topic in *The Turing Way Guide* for Ethical Research.

NHS England’s data science team has been exploring the Data Hazards project as part of their own efforts to integrate structured, proactive, and accessible risk assessment into the team’s data science practice. By making use of Data Hazards, NHS England builds on a community-developed and customisable framework. This open source solution saves time and constitutes a concrete approach to the ethical evaluation of projects across the team and potentially the wider organisation. This strand of work evolved from an internal ‘white paper’ authored by the team, exploring ethical data science & AI  development in NHS England.

Mia Noonan, Principal Data Scientist at NHS England and Practitioners Hub Expert in Residence, says: “The Data Hazards project is about developing a common vocabulary to help creators of AI products become aware of, think about and critically engage with the ethical risks involved with their projects. Because Data Hazards is open source, we are able to easily adapt it to our needs using NHS-specific examples. It’s something that  people in many different roles, not just data scientists, can pick up and start using pretty quickly, and it’s applicable in different contexts.”

To increase engagement with the Data Hazards labels and normalise conversations around ethics the team has adopted a cross-project, interactive ‘show and tell’ approach with project leads and has sought to evaluate the success of the labels’ implementation through extensive feedback interviews. The feedback has been used to identify knowledge gaps in the team, for example, awareness of the environmental implications of their work, and led to work to create methods for environmental benchmarking to create a standardised approach for tracking CO2 emissions produced when training models.

Harriet Sands, AI Technical Specialist at NHS England and also an Expert in Residence, adds: “One of the reasons we decided to join the Practitioners Hub is that we were embarking on testing the Data Hazard labels at NHS England and felt there would be value in bringing that discussion to the broader community. That’s another benefit of the project being free and open source – we feel confident reaching out and having frank discussions about our experiences, which has been really helpful.”


## Ethics in AI Assurance: AI Quality Community of Practice

Ensuring AI systems in healthcare are safe, effective and ethically sound is a priority for NHS England. The AI Quality Community of Practice (AIQCOP) was established at NHS England to bring together technical assurers, data scientists and other stakeholders to explore collaboratively how AI assurance should be approached. Unlike traditional software assurance, AI presents unique challenges, including the need to evaluate not just whether a system functions as intended, but also its broader ethical and societal impacts, especially in healthcare– circling back to NHS principles of fairness, transparency and public trust.

Ben Wallace, Principal Data Scientist at NHS England and a founding member of the AIQCOP, helped develop the initiative using insights from *The Turing Way* handbook on AI ethics and responsible use. While the Data Hazards framework ensures ethical considerations from the outset, quality assurance tools and methods integrate these principles into the ‘embedosphere’—the ongoing processes of implementing, evaluating, and monitoring AI systems.

Ben says: “AIQCOP is about preparing for the reality in which AI is part of the systems we assure. We’re building a community of people who will encounter AI in their work and making sure they have the knowledge, skills and tools to assess it properly and ask the right ethical questions alongside the technical validation.” The AIQCOP community features a diverse range of voices and perspectives from across the organisation, fostering a dynamic, evolving approach to ongoing evaluation that is essential for AI assurance and which may be difficult to achieve through static compliance toolkits. In this way, ethical practice becomes more than simply a matter of adherence to existing standards.

To support this work, NHS England is establishing internal good practice guidance for assurance. Ben adds: “A big part of AIQCOP is recognising that traditional assurance methods don’t always work for AI. We need new ways of thinking, new tools, and an understanding that AI assurance isn’t just a checklist – it’s an ongoing process.”


## Ethics in AI Monitoring and Evaluation: An Approach to Large Language Models (LLMs)

Among the latest initiatives in the Data Science team at NHS England’s work towards a holistic approach to AI is the ongoing work to establish an approach to monitoring and evaluation for LLMs. A set of questions and corresponding evidence standards for projects that involve LLMs to meet (dubbed the LLM evaluation & monitoring framework), seeks to make sure LLMs are continued to be implemented and used safely.  

This work aims to help those involved evaluate the LLM components of systems in NHS England, and potentially more widely in health and care. It is designed to aid teams in generating the necessary evidence to ensure continued quality and to complement compliance, business cases and decision-making processes (including when an AI tool may need to be updated or decommissioned). A draft version is being tested on an AI product in development, in collaboration with an NHS trust acting as an incubator for the product and other teams from different functions of NHS England.


## Ethics in Transparency: Trialling the Algorithmic Transparency Recording Standard (ATRS)

The ATRS is a means by which public sector organisations can provide clear information about algorithmic tools they have made, or make use of, to support decision-making, ensuring transparency and accountability. The NHS was an early contributor to the Government’s Algorithmic Transparency Recording Standard; publishing a record of the QCovid Algorithm in July 2022.

More recently, the NHS Data Science Team has published an ATRS record of the NHS.UK Reviews Automoderation Tool. As documented in the [record](https://www.gov.uk/algorithmic-transparency-records/nhs-england-nhs-dot-uk-reviews-automoderation-tool), this tool automates the moderation of thousands of reviews of NHS services received each year. The tool uses natural language processing (NLP) techniques to meet efficiency & scalability needs while ensuring user safety. By openly sharing information about the algorithms that assist the delivery of public services, the record supports the mitigation of concerns the public may have about a so-called ‘black-box’ algorithm; ensuring that work is subject to scrutiny and helping to maintain the high standards of care and trust that patients and the public expect from the NHS.


## Key takeaways



* NHS England's data science team is proactively integrating responsible AI practices into its work to ensure fairness, trust, and safety in healthcare.
* Leveraging open-source resources like Data Hazards and The Turing Way, the team is adapting community-developed solutions to their projects.
* Recognising the limitations of traditional assurance methods for AI, the AI Quality Community of Practice (AIQCOP) has been established to collaboratively explore effective AI assurance approaches, addressing the unique challenges posed by AI compared to traditional software.
* The Data Science Team is working on a practical process to assist in the evaluation and monitoring of Large Language Models in products.
* The NHS.UK Reviews Automoderation Tool ATRS record is an exemplar of the team’s commitment to transparency and openness.


## Expert in Residence Spotlight: Harriet Sands & Mia Noonan

Harriet Sands is an AI Technical Specialist in the Joint Digital Policy Unit at NHS England, with a career in Data Science that includes roles at HM Treasury, 10 Downing Street, the Office for National Statistics (ONS), and dunnhumby (with a stint as a [Data Science for Social Good](https://www.datascienceforsocialgood.org/) fellow). Harriet's focus is on practically realising Responsible AI at NHS England, creating strategies to help design, evaluate, and deploy AI solutions ethically. She is also the co-founder and coordinator of a [public sector reading group](https://data-ethics-and-society.github.io/data-ethics-and-society-reading-group/) on the societal implications of data-driven technologies.

Mia Noonan joined NHS England as a graduate in 2021 after earning her MSc in Computer Science. Over the past three years, Mia has worked on projects involving data quality, regression, and data linkage. She focuses on operationalizing data science solutions, ensuring tools are deployed effectively and have meaningful impacts. Mia has been instrumental in implementing quality assurance frameworks for data science teams.

**Highlights from *The Turing Way* Practitioners Hub**

“Having access to The Turing Way and other open initiatives is really helpful for us because we can pick them up and work with them without feeling like we have to create our own resources from scratch. It’s a great way for us to experiment with what the research community is coming up with. We’ve also found having access to an open community of peers through the Practitioners Hub to be really beneficial in terms of discussing shared experiences and challenges.”


### Acknowledgements

This case study is published under [The Turing Way Practitioners Hub](https://www.turing.ac.uk/turing-way-practitioners-hub) 2024-25 Cohort - case study series. The Practitioners Hub is *[The Turing Way](https://the-turing-way.netlify.app/welcome)* project that works with experts from partnering organisations to promote data science best practices. In 2024, **Harriet Sands and Mia Noonan** jined the cohort as Experts in Residence to represent interests and opportunities to discuss, adopt and share their implementation approaches for data science and AI in the **NHS England Data Science Team** and Healthcare. 

This project is supported by [Innovate UK BridgeAI](https://iuk.ktn-uk.org/programme/bridgeai/). The Practitioners Hub has also received funding and support from the Ecosystem Leadership Award under the EPSRC Grant EP/X03870X/1 & [The Alan Turing Institute](https://www.turing.ac.uk/).

**Cite this publication**

Noonan, M., Sands, H., Wallace, B., Gillespie, S., Sharan, M., Bennett, A., & Demertzi, L. (2025). Driving Responsible Data Science: A Case Study of NHS England's Data Science Team. Zenodo. [https://doi.org/10.5281/zenodo.15053194](https://doi.org/10.5281/zenodo.15053194)


**Cite this publication**

Noonan, M., Sands, H., Wallace, B., Gillespie, S., Sharan, M., Bennett, A., & Demertzi, L. (2025). Driving Responsible Data Science: A Case Study of NHS England's Data Science Team. Zenodo. [https://doi.org/10.5281/zenodo.15053194](https://doi.org/10.5281/zenodo.15053194)
