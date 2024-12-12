---
title: 'Bed allocation'
summary: 'Machine learning to effectively aid bed management in Kettering General Hospital.'
category: 'Projects'
origin: 'Skunkworks'
tags: ['HOSPITAL','FORECASTING', 'PYTHON', 'WEBDEV']
---

![Browser showing the dashboard for Kettering General Hospital that shows the forecasting of their bed occupancy.](../images/bed-allocation.png)

Bed allocation was identified as a suitable opportunity for the AI Skunkworks programme in May 2021.

## Results

A proof-of-concept demonstrator written in Python (backend, virtual hospital, models) and HTML/CSS/JavaScript (frontend).

# Case Study

This is a backup of the case study published [here](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/improving-hospital-bed-allocation-using-ai/) on the NHS England Transformation Directorate website.

Kettering General Hospital approached the NHS AI Lab Skunkworks team with a request for support exploring artificial intelligence (AI) to improve bed management. Their vision was to use AI to achieve the “right patient, in the right bed, receiving the right care, at the right time.”

This 14-week project investigated the AI techniques that could be used to generate options for moving patients in a way that supports the human team to make the best decisions. The project aimed to provide a proof of concept tool that uses historic data to predict demand and make bed allocation suggestions to the bed management team - providing the open source code for further experimentation at the end of the project.

### Overview

Admitting patients into hospital is like a game of Tetris, or chess, where the allocation of each patient and bed can have a huge knock-on effect to the smooth-running of admissions and the welfare of patients. This scheduling of beds is managed by a human team who rely on individual expertise to deliver a system not unlike air traffic control, calculating the best arrangement with a continually changing set of demands and numbers of patients.

The main challenges for managing hospital admissions were reported to be:

- Demand and capacity is complex. Not all patients are the same. Not all beds are the same.
- Staff are overwhelmed with options. Managing hundreds of beds and people presents too many choices.
- Expertise of staff, and therefore needs, varies.

The NHS AI Lab Skunkworks funded and supported an AI investigation with the team at Kettering General Hospital, alongside Faculty, an AI specialist supplier provided through the Home Office’s [Accelerated Capability Environment](https://transform.england.nhs.uk/ai-lab/explore-all-resources/develop-ai/improving-hospital-bed-allocation-using-ai/#ace) (ACE).

The work looked at whether AI could support better, faster decision-making, using a tool that would predict patient flow and provide bed allocation options for a human team to consider. The potential benefits being:

- high-quality, consistent bed allocation decisions
- improved patient experience
- improved workforce efficiency and staff satisfaction
- a reduction in the average number of patient moves per admission (and after-hours moves)
- reductions in inpatient length of stay
- improved problem solving capability within the team.

### What we did

We ran a discovery phase in which the project team sought to understand the problem, the existing process and the constraints. We talked to others who are trying similar projects. The team also researched existing attempts to use AI for demand management and scheduling.

#### Creating a virtual hospital

Following a robust information governance process, the team had access to 5 years’ worth of historic pseudonymised data from the patient admission system (PAS) and 1 to 2 years of patient flow data. Pseudonymisation is a technique that separates data from direct identifiers (for example name, surname, NHS number) and replaces them with a pseudonym (for example, a reference number), so that identifying an individual from that data is not possible without additional information.

Having assessed the data quality and analysed pre- and post COVID changes, they engineered training and test sets for modelling. This provided a virtual hospital environment with which to explore the use of AI.

#### Choosing a technical approach

For the forecasting component of the project, the team used a Bayesian modelling approach which used historical data to predict how many patients with specific characteristics would present at the hospital over time.

The team then compared three approaches to allocating a bed: greedy allocation, Monte Carlo Tree Search (MCTS) and reinforcement learning.

Greedy allocation allocates beds based on the best bed at the point of admission thereby making it a fast and less resource intensive method.

The MCTS model operates by considering future events such as the number and nature of patients who are likely to arrive for admission within the next couple of hours, along with constraints of available beds, and then uses that information to allocate the best bed to a patient at the point of admission. This makes the model resource intensive and requires significant computing power to operate.

Finally, a reinforcement learning approach was considered, which uses “agents” to maximise a reward over time, but this was not developed within the constraints of this 14 week project.

#### Building a user interface

In order to provide staff with a usable and understandable front end, the team developed and tested a web-based user interface (UI) and integrated the allocation models.

The team implemented the greedy allocation method in the user interface as it was the least resource intensive approach and able to provide an explainable allocation suggestion.

The resulting proof of concept was then tested and reviewed by Kettering General Hospital.

### Outcomes and lessons learned

The result is a proof of concept, created in 14 weeks, with a user interface that provides staff with the following:

- The ability to visualise a virtual hospital, showing current occupancy rates and forecasted demand for beds.
- A demonstration of what a fully developed allocation model could provide, making suggestions to the user along with an explanation.
- The ability to test the model on a wide range of patients with different attributes and associated constraints and validate the performance.

> This tool will help the likes of myself and others by supporting decision making. Support is the key word here, machine learning will support us to make these difficult bed allocation and patient decisions.
– Digital Director, Kettering General Hospital NHS Foundation Trust

> I regularly hear that a bed is a bed and I know it’s not ... But when you have those front door pressures, you can’t get ambulances offloaded and I have beds in the wrong place - this is the time I need the real support, real time data, an automatic risk assessment that is generated for each patient.
– Member of bed management staff, Kettering General Hospital

There have been significant challenges with this project.

#### Data quality

Attempting to get a total view of the trust’s capacity and demand is complicated. In this example with Kettering General Hospital, there is no centralised patient flow information. Admission data would be needed for all specialties across the trust for the allocation algorithm to produce the best results.

#### Complexity of patient needs

The unique nature of patients’ needs means taking into consideration a large number of complex combinations in order to achieve the best allocation decision.

#### Adapting quickly to change

In a real-world setting, the technology would need to be easily reconfigured by staff with new information about increased beds, changed ward layouts or flu admission peaks. There is currently limited ability to see the impact of changes like these.

### What next?

Kettering General Hospital will be working with Faculty to bid for further funding to develop and operationalise the bed allocation system. This will aim to build connections to patient data in real-time, refining the algorithm, and understanding how the allocation tool can be integrated into site management practises.

### Who was involved?

This project is a collaboration between NHSX, [Kettering General Hospital NHS Trust](https://www.kgh.nhs.uk/), [Faculty](https://faculty.ai/) and the [Home Office’s Accelerated Capability Environment](https://www.gov.uk/government/groups/accelerated-capability-environment-ace) (ACE). The AI Lab Skunkworks exists within the NHS AI Lab to support the health and care community to rapidly progress ideas from the conceptual stage to a proof of concept.

The NHS AI Lab is working with the Home Office programme: Accelerated Capability Environment (ACE) to develop some of its skunkworks projects, providing access to a large pool of talented and experienced suppliers who pitch their own vision for the project.

Accelerated Capability Environment (ACE) is part of the Homeland Security Group within the Home Office. It provides access to more than 250 organisations from across industry, academia and the third sector who collaborate to bring the right blend of capabilities to a given challenge. Most of these are small and medium-sized enterprises (SMEs) offering cutting-edge specialist expertise.

ACE is designed to bring innovation at pace, accelerating the process from defining a problem to developing a solution and delivering practical impact to just 10 to 12 weeks.

Faculty is an applied AI company that helps build and accelerate an organisation's AI capability. They offer a range of software and services solutions. Faculty works with a number of high-profile brands globally as well as government departments and agencies.

Output|Link
---|---
Open Source Code & Documentation|[Github](https://github.com/nhsx/skunkworks-bed-allocation)
Case Study|[Case Study](https://www.nhsx.nhs.uk/ai-lab/explore-all-resources/develop-ai/improving-hospital-bed-allocation-using-ai/)
Technical report|[PDF](https://github.com/nhsx/skunkworks-bed-allocation/blob/main/docs/NHS_AI_Lab_Skunkworks_Bed_Allocation_Technical_Report.pdf)

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
