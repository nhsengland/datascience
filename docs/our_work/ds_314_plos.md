---
title: 'DS314 PLOS: Predicting Length of Stay'
summary: 'Developing an approach to predict inpatient discharge timing to support operational decision-making, using data science methods within the NHS Federated Data Platform.'
origin: 'NHS England'
tags: ['SECONDARY CARE','PYTHON' ,'MACHINE LEARNING', 'FDP', 'CLASSIFICATION', 'EXPLAINABILITY' , 'MULTI-MODAL','MODELLING', 'WORK IN PROGRESS', 'IN DEVELOPMENT']
---

## About PLOS: Predicting Length of Stay

Hospitals face ongoing operational pressure related to bed capacity, patient flow, and discharge planning. Being able to anticipate when inpatients are likely to be discharged can support more effective planning across clinical, operational, and managerial teams.

The **Predicting Length of Stay (PLOS)** project is exploring how routinely collected healthcare data can be used to predict *discharge date buckets* for inpatients. The work is currently in progress and focuses on building an approach that is scalable, reusable, and aligned with NHS data standards.

The project team has worked closely with clinical and hospital staff to ensure the model output will be in a format that can fit into users work flows and provide actionable real benefit.

---

## Problem

Hospitals often rely on manual processes, local knowledge, and short-term heuristics to estimate when patients will be discharged. These approaches can be inconsistent and inaccurate, particularly in complex acute settings.

A lack of reliable, data-driven discharge predictions can contribute to:
- Challenges in bed and capacity planning  
- Inefficient patient flow  
- Increased operational burden on clinical and operational teams  

---

## Intended Benefit

The intended benefit of this project is to:
- Support **operational and bed management decision-making**
- Provide **early, indicative signals** about likely discharge timing
- Reduce reliance on manual or ad-hoc estimation processes
- Explore how advanced analytics can be embedded into routine operational workflows

The outputs are intended to be *supportive* rather than prescriptive, and to complement existing clinical judgement. This tool should not be used to decide if a patient *should* leave hospital, but rather indicate when they *might* be ready to leave hospital.

---

## Data

The project uses a trusts routinely collected secondary care data available within the trusts local tenant of the NHS Federated Data Platform (FDP). At this stage, the exact data inputs and feature sets are still being refined.

The approach is being designed to work with **canonical data model (CDM)** data, enabling consistency and portability across organisations.

---

## Methods

The work is being undertaken within a **local FDP tenant** and is exploratory in nature.

Current methods under consideration include:
- Use of **machine learning approaches**
- Integration of **multimodal data** (subject to feasibility and governance)
- Prediction of **discharge date buckets**, for example:
  - Discharge today  
  - Discharge tomorrow  
  - Discharge within 48 hours  
  - Discharge within 72 hours  

The precise modelling approach, features, and outputs are subject to change as the project progresses and learning develops.

---

## Key Exploitable Results

Although the project is still in progress, key anticipated exploitable results include:

- **Reusable analytical approach**  
  The solution is being designed with reuse in mind, enabling adoption at other trusts.

- **Scalability through FDP and CDM alignment**  
  By building on FDP infrastructure and canonical data model data, the approach is intended to scale across organisations with minimal rework.

- **Code and framework sharing**  
  There is an intention to share the codebase and analytical framework to support similar work elsewhere in the NHS, promoting transparency and reuse.

---

## Teams

This project is a collaboration between:
- The **NHS England Central Data Science Team**
- An **England hospital trust’s local data, clinical, and operational teams**

The collaboration brings together national data science expertise and local operational knowledge.

---

## Project Status

This project is currently **work in progress (WIP)**.

- **Minimum Viable Product (MVP):** Targeted around **April 2026**
- Methods, data inputs, and outputs may evolve as the project develops

Further detail will be added as the project matures and findings are validated.
``

#
