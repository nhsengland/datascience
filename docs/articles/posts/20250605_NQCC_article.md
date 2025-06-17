---
title: NHS England Use-Cases at the National Quantum Computing Centre annual Hackathon
authors: [jpearson]
date: 2025-06-17
categories: 
    - Quantum
    - Optimisation
    - Python

links:
    - Project Github Repository: https://github.com/nhsengland/SynPathToy
slug: NQCCHack
description: >
    Quantum computing has the potential to dramatically change many aspects of healthcare analysis.   For our interests this mostly features around increased efficiency in optimisation and hybrid ML-Quantum approaches.  This article briefly describes our use-cases submissions to the annual NQCC Hackathon to showcase the emerging interests for healthcare using this technology.
---

> Quantum computing has the potential to dramatically change many aspects of healthcare analysis.   For our interests this mostly features around increased efficiency in optimisation and hybrid ML-Quantum approaches.  This article briefly describes our use-cases submissions to the annual NQCC Hackathon to showcase the emerging interests for healthcare using this technology.

<!-- more -->

## Introduction

The National Quantum Computing Centre (NQCC) - UK National Laboratory - was launched in 2020 spanning 5 years with a 93 million pound investment from the Uk Government as part of the national quantum technologies program.   

The NQCC’s annual UK Quantum [Hackathon](https://www.nqcc.ac.uk/uk-quantum-hackathon-2025/) aims to demonstrate how quantum computing can solve real-world problems by bringing together talented people from across the value chain, with the objectives to:

- Connect the UK quantum ecosystem through networking and collaboration throughout the event
- Understand the opportunities and limitations of quantum computing by demonstrating the current capabilities of the technology
- Explore a broad range of use cases for quantum computing
- Enable aspiring practitioners to develop their quantum computing programming and applications skills
- Showcase the breadth of technology available currently and enable a broad range of users to access these tools

Our team has been engaging with this event for the past few years through the submission of use-cases in order to connect and understand the possible roles of quantum computing in healthcare. 

## First Quantum Hackathon in 2022 - Bed Optimisation

At the first of these hackathons in 2022, we challenged the hackers to devise a strategy for allocating patients to beds whilst taking account of various individual and system constraints.  Currently, this is an extremely complex problem that is usually worked out by people on the ground with a lot of domain knowledge.   See the full event article [here]( https://www.nqcc.ac.uk/wp-content/uploads/2022/09/NQCC_Hackathon_article_July2022.pdf). 

## Second Quantum Hackathon in 2023 - Route Optimisation

The following year, we continued on the theme of optimisation but this time proposed a route optimisation problem around the transportation of both staff and time-sensitive materials to multiple locations.  The computation of optimal routes is of value and a common classical problem.   Owing to the nature of routing and scheduling problems being NP-complete, the application of quantum computing for problem solving in a healthcare setting is an exciting proposition.  

To make the problem tractable, the team used a hybrid method that combines classical compute for clustering (k-means-constrained) with quantum annealing. The clustering technique focuses on finding non-overlapping clusters, constraining the search space, and making the solution viable for existing hardware and at scale. 

Several clustering methods were attempted, and k-means-constrained proved most useful. Hospitals were clustered before using D-Wave to provide solutions for the optimal route based on the shortest path between clusters. The team had a limited number of qubits to use but were still capable of finding solutions for up to five health centres. See the full report [here](https://www.nqcc.ac.uk/wp-content/uploads/2024/04/NQCC_Quantum-Hackathon-2023_Technical-report.pdf).

## Third Quantum Hackathon in 2024 - A&E Forecasting

In 2024, we proposed quantum modelling for NHS forecasting as the use-case.  This built upon our current A&E forecasting tool which uses a Hierarchical Bayesian model trained using a particular kind of Markov-chain Monte Carlo (MCMC) algorithm.  Whilst this approach allows information to be shared between hospitals during training (helping improve quality and missingness of the data), this is computationally expensive.   By incorporating quantum random sampling algorithms into the model it was hoped that better training speed and efficiency could be achieved as well as increasing performance and reducing costs.  
A quantum-MCMC was attempted but proved to be unsuitable.  Instead a variational quantum circuit was implemented for the time-series forecasting with linear trends in the data detected using just 25 qubits.  See the full report [here](https://www.nqcc.ac.uk/wp-content/uploads/2025/04/NQCC_Quantum-Hackathon-2024_Technical-report.pdf).

### What's next?

We're aiming to submit a fourth use-case for the 2025 hack taking place in July.  Watch this space!.

The 2025 hackathon details can be found [here](https://www.nqcc.ac.uk/uk-quantum-hackathon-2025/).  
