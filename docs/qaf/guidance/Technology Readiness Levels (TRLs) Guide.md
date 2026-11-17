# Technology Readiness Levels (TRLs) Guide

We accept that work at different stages takes different ways of working and that not all projects need to progress all the way through the TRL levels and thus it is important to capture learning and outputs at each stage.

---

# **Scan**

---

# Findings Review

Research and innovative ideas begin to be translated into applied research and development. Scientific findings are reviewed and assessed as a foundation for characterising new technologies. The main aim is to end up with a clear way of describing why there is interest in this area or a need to be aware of the technique

***For Example:** Beliefs for the opportunity of Homomorphic Encryption in healthcare*

**Envisaged Output:** Green Paper

# Research Idea

The main focus is on the problem itself and on generating research ideas, Hypothesises are formed and preliminary studies are set to define parameters and to identify candidate concepts.  
  
***For example:** review of state of the art and technical thinking around how to assess privacy attacks on a language model*

**Envisaged Output:** White Paper | Proposals (New work requests)

# Proof Of Concept

At this step in the maturation process, active research and development (R&D) is initiated. This may include both healthcare and non-healthcare demonstrations. These studies and experiments should constitute “proof-of-concept” validation of the applications/concepts formulated at TRL 2.

***For example:** Code on github with associated technical report for process mining.*

**Envisaged Output:** Published Code and Report

# Ugly-Prototype

Basic technological elements must be integrated to establish that the “pieces” will work together alongside our data and in our infrastructure to achieve concept-enabling levels of performance.  The validation is developed in Dev but with Prod in mind.  
  
***For example:** Geospatial application built in one of our platforms working on synthetic data.*

***Envisaged Output:** Functional Requirements*

---

**Pause -** Learning needs to be collated, documented and a wider group of stakeholders and disciplines should be consulted at this stage.   The business model needs to be considered to understand longevity, value and responsibilities. 

***Envisaged Output:*** [Project Specification (Quality Framework)](../DS%20Quality%20Framework.md)| Business Model | Engagement Plan | QA Plan | Ethics Plan | Exit Plan 

---

---

# **Pilot**

---

# *Pre-Prototype*

*The Technology has now been demonstrated.  However, at this point the development takes over and usually starts from scratch using the learnings from the demonstration to build a simpler and robust product with longevity and maintenance in mind.  Clear specifications for functionality and success are now definable.  
  
**For example:** A forecast model re-written with time spent on creating a full feature store rather than producing features on the fly.*

***Envisaged Output:** Non-Functional Requirements | Production Resource Request*

# *Prototype*

*TRL 6 is achieved when the prototype product is tested successfully in a relevant environment.  At this point the maturation step is driven more by assuring management confidence than by R&D requirements.  
   
**For example:** Named entity recognition tool demonstrated in SDE platform for a subset of real data*

***Envisaged Output:** Performance Report*

---

# **Scale**

---

# *Full fidelity*

*The same as TRL 6 but working at the scale, speed, concurrency as the live system would need.    
   
**For example:** Live data quality reporting of large dataset working on a full cut of the data*

***Envisaged Output:** User Documentation | Developer Documentation*

# *TME (Testing, Monitoring & Evaluation)*

*Once approval to proceed is given, then the testing, monitoring and evaluation aspects are built into the deployment system.  Associated user and developer documentation ready.  
  
**For Example:** Scheduling algorithm built in final environment with associated monitoring dashboard and automated reports*

***Envisaged Output:** Testing Report*

# *Live Deployment*

*A fully deployed product with feedback mechanism.  Appropriate standards have been worked through and met.  User testing and patient voice have been reviewed and implemented.*

***Envisaged Output:** Lessons Learnt | KERs | Product*

**Note - Whilst appearing linear this process will end up being very iterative and make use of the dashed line loops.   This can be considered through the triple8 lens.**

---

# Examples

**Self generated 1-4**(28 weeks)

Pre-BPC: Anna reads about variational auto encoders and thinks this would be a good technique for the team to use to create synthetic data

She puts in a proposal to New Work Requests and continues her reading resulting in the creation of a Green Papers.    
Anna presents the green paper and proposal to one of the SMT resulting in a "Go" decision which means the project gets put into the next BPC.

BPC1: Anna and Bob put forwards a preference to work on this proposal and get it allocated.   They are told to aim for TRL 3 in the next quarter.

Anna focusses on creating a White Papers whilst Bob starts to explore open code repos that implement VAEs for SDG.    
A reduced form of the confluence documentation is created.   
The white paper is presented to the project Analytical Assurer at the half way review alongside some specific proposals for benchmarking VAE vs GANs and exploring privacy metrics  
During the second half of the quarter a series of codebooks are released on github highlighting implementation and exploration.

BPC2: During the next BPC Anna is reallocated to the work and asked to progress the work to TRL 4 and to form the business model.

Anna takes the learning from TRL 2 & 3 to put together a Functional Requirements document outlining the specifications for a larger scale project.  This doesn't include the solution or project timelines but instead focusses on what success would look like and defining the specific components that need to be built for an MVP and full solution.    
During this quarter she also starts to work on the Business Model.  Initially she starts with the people layer defining who the stakeholders/users are but quickly moves to the value layer defining the as is and to be states.  She sets out the solution and timeline for the work considering input from engineers and architects around the distribution layer.  Finally she gets input from SMT on the finance layer and defined ethics, QA and CDE plans for the work to consider.   
The confluence documentation is filled out alongside this thinking.

**Stakeholder general request 1-4**(24 weeks)

Pre-BPC: The one voice team has asked what can be done to identify the mood of the responses they are getting from their regular survey.

Through discussions with Jonathan Hope the data science team have agreed to explore this and have put the work through the book of work.   This is now planned for the next BPC.

BPC1: Carl and Diageo have been allocated the work and asked to take this from TRL 2 through to TRL 4+.

They start off with an exploration of methods and ask around the team to find out what knowledge currently exists.     
Unfortunately, the team appear to be lacking in experience in this area and there are no clear examples of papers on the topic of sentiment analysis.     
Carl and Diageo therefore embark upon creating a White Papers through a literature review.    
They create a series of proof of concepts for different sentiment libraries and look at a few available frameworks for assessing the quality of the sentiment recovered.     
This iterative process covers TRL 2 and 3 at the same time and the white paper end up being a literature review pointing towards a few different code demonstrations showcasing different approaches.

BPC2: Carl and Diageo have continued to be allocated the work but told to make a go/no-go decision by the midpoint

Diageo focusses on creating the Functional Requirements document putting together their learning into a single problem statement.   
Carl however, has identified a potential bias in their preferred approach an so has continued to investigate proof of concepts around dealing with this bias in the project.     
In the end Carl decides that whilst this is an issue that needs to be highlighted there wouldn't be time to develop this work within this project.    
Instead he puts this into a New Work Requests form and writes up his thoughts into a Green Papers.     
As the ask was a bit more vague there isn't a defined set of stakeholders for the work and the Business Model is proving difficult to put together.    
The work therefore pauses and a request goes back to SMT that the requesting team push forwards the thinking around need and priority before the work continues.  However, the  solution is now well specified and learning is captured for similar requests in the future.

**Stakeholder specific request 1-4** (6 weeks)

Pre-BPC: The elective recovery team have presented a work request to the D&A book of work to link two datasets and create a waiting list prediction tool.

This has been allocated to the data science team and is incorporated as a project in the next BPC.

BPC1: Eddie is allocated to the work with support from Francis and George and asked to progress the work from TRL 2 through to TRL 6 over the next two quarters.

A single sprint of 2 weeks is defined for scoping and project setup.     
Eddie starts by using the DS\_xxx template to align the project to the assurance checklist and sets up a Jira board ready for project management.     
Meanwhile Francis is focussed upon the data looking into the metadata, access, quality and IG.     
George is tasked with looking into the methods, ethics, evaluation and previous examples of similar projects.     
By the end of the first sprint it has become apparent that that datasets are well established, there is a previous example of the method and the knowledge is known about within the team.    
TRL 2 is covered in the methodology section of the project documentation whilst previous examples are identified which cover TRL 3.     
Data and cloud resource requests are made at this point as well as the tickets being created in Jira and documentation created in confluence over the next 2 week sprint.     
Whilst waiting for the requests to come through the team embark on creating an ugly prototype using available data.    
The focus is on the end to end run and identifying each component in the pipeline.     
During this time the TRL 4 Functional Requirements document is forming; much of this links to confluence documentation.     
As the team know this project is already commissioned they can start to put together the Business Model whilst the requirements are being reviewed.     
This means that by the half way point of the quarter they managed to be ready to start the development in earnest dependent on the data and resource requests.     
They have documentation in place and already have ELSI, QA and CDE considerations in their minds.     
The team SMT can also start to think through the longer term home and resourcing for this work.  