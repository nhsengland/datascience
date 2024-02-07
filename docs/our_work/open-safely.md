---
title: 'Working with a Trusted Research Environment'
summary: 'An exploration of OpenSafely'
category: 'Projects'
origin: 'Skunkworks'
tags: ['EDA']
---

# Project

OpenSAFELY gives trusted researchers restricted levels of access to the server to run analysis on real data and obtain aggregate results, without having sight of the patient level data. Aggregate results are checked to ensure there are no disclosure risks before being released from the server. This highly secure way of working enables researchers to have access to large and sensitive datasets in a safe manner.

This project had two main aims: 

- To understand the reach and coverage of the NHS @Home programme during the pandemic. Specifically looking at: blood pressure monitoring, pulse oximetry and proactive care interventions. 

- To understand how to approach an analysis project using OpenSAFELY, including the amount of time and resource required, and whether this platform would be useful for future analyses. 

# Case Study
This is a backup of the case study published [here]() on the NHS England Transformation Directorate website.

Trusted research environments (TREs) take the form of a secure data environment that allows analysts and researchers to undertake in-depth analysis on rich, joined-up datasets without them seeing any identifiable information. Data is held within a secure server and does not leave that server. Following a recommendation from the [Goldacre review](https://www.gov.uk/government/publications/better-broader-safer-using-health-data-for-research-and-analysis) TREs form a key part of the [Data saves lives: reshaping health and social care with data policy paper](https://www.gov.uk/government/publications/data-saves-lives-reshaping-health-and-social-care-with-data/data-saves-lives-reshaping-health-and-social-care-with-data#empowering-researchers-with-the-data-they-need-to-develop-life-changing-treatments-diagnostics-models-of-care-and-insights). 


**The challenge**  
Using TREs for analytical projects is still a new concept to many analysts. The NHS AI Lab Skunkworks team and NHS England’s Health Inequalities and Evaluation Analytics Team embarked on a partnership project to gain experience of using a TRE to answer key and important questions for a defined project. They used a TRE called [OpenSAFELY](https://www.opensafely.org/), an open-source software platform for analysis of electronic health care records data for COVID-19 related research. 


OpenSAFELY gives trusted researchers restricted levels of access to the server to run analysis on real data and obtain aggregate results, without having sight of the patient level data. Aggregate results are checked to ensure there are no disclosure risks before being released from the server. This highly secure way of working enables researchers to have access to large and sensitive datasets in a safe manner. 

 

This case study outlines the team’s experiences of working through the OpenSAFELY platform to understand the impact of the NHS @Home programme. 

 

### The NHS @Home programme 

During the COVID-19 pandemic there was a necessity to safely deliver high quality care into patients’ homes where appropriate. As part of its response to the pandemic, NHS England brought forward initiatives to help patients better self-manage their health and care at home under the [NHS @Home programme](https://www.england.nhs.uk/nhs-at-home/). NHS @Home is a nationally-led programme of work providing better connected, more [personalised care](https://www.england.nhs.uk/personalisedcare/) in people’s homes, including care homes. 

Now, two years on from the start of the pandemic, the NHS @Home team wanted to understand the reach and coverage of their initiatives to inform future planning. In particular, the team wanted to understand the reach of the following initiatives: 

-   [Blood pressure monitoring](https://www.england.nhs.uk/ourwork/clinical-policy/cvd/home-blood-pressure-monitoring/) 
-   [Covid Oximetry](https://www.england.nhs.uk/nhs-at-home/covid-oximetry-at-home/) 
-   Proactive care 
    

Obtaining this information can be difficult, because access to patient level data within primary care electronic health records is controlled by strict information governance rules due to the importance of patient privacy. This limits the scope of analysis which can be carried out on primary care data. The two main software systems used in primary care in England are operated by the companies [TPP](https://tpp-uk.com/) and [EMIS](https://www.emishealth.com/). 

Therefore, to answer the study questions, the NHS AI Lab Skunkworks Team and NHS England’s Health Inequalities and Evaluation Analytics Team embarked on a partnership project exploring the Uptake of NHS @Home interventions during the COVID-19 pandemic, using the OpenSAFELY platform. OpenSAFELY is a TRE which provides access to patient records in the TPP system, and for certain studies also provides access to patient records in the EMIS system.

### Project aims 

This project had two main aims: 

-   To understand the reach and coverage of the NHS @Home programme during the pandemic. Specifically looking at: blood pressure monitoring, pulse oximetry and proactive care interventions. 
    
-   To understand how to approach an analysis project using OpenSAFELY, including the amount of time and resource required, and whether this platform would be useful for future analyses. 
    

Part of the initial project aims was to look at whether coding of uptake of the interventions of interest varied across TPP and EMIS. Unfortunately, OpenSAFELY were unable to provide access to the EMIS system at the time, so the scope was narrowed to TPP only, which still represents a significant dataset of approximately [24 million patient records](https://wellcomeopenresearch.org/articles/7-191/v1). 

This case study will focus on the second bullet point, the experience of using OpenSAFELY, as the code for the analysis will be published separately and there is ongoing review and further development of the analysis.

### What we did

There are several stages to completing an OpenSAFELY project. These include: 

-   Setting up the project
-   The [co-piloting](https://www.bennett.ox.ac.uk/blog/2021/08/opensafely-co-pilot-programme-assisting-users-on-their-opensafely-journey/) period and project development 
-   Project Wrap up 
    

#### Setting up the project 

The initial step was to complete the study access request and receive approval for the project through OpenSAFELY. This included: 

-   Naming the study sponsor, study lead and team who would need to access the server and work on the analysis   
-   Stating the purpose and scope of the study and the desired outputs 
-   Stating which datasets need to be accessed  
-   Providing additional details, including the relevant experience of the researchers and whether the study is research, a service evaluation, or an audit 
    

Once this was granted, the next step for everyone working on the analysis was to successfully apply to become an [accredited researcher](https://www.ons.gov.uk/aboutus/whatwedo/statistics/requestingstatistics/secureresearchservice/becomeanaccreditedresearcher), recognised by the [Office of National Statistics](https://www.ons.gov.uk/), and to start setting up the technical requirements for OpenSAFELY in parallel. 

The application process to be an accredited researcher will be detailed by OpenSAFELY at the start of the project, [however an outline of the process can be found here](https://uksa.statisticsauthority.gov.uk/wp-content/uploads/2019/07/DEA_Accredited_Researcher_Application_Guidance_v1.0.pdf). Having filled in the application form, it is necessary to attend a virtual training session, which walks through best practices for data publication and data privacy. These sessions must be booked in advance and, due to availability, the whole accreditation process could take a few weeks to complete. Hence, it is worth filling out the application form and booking the training as soon as possible before the start of the co-pilot period. 

For the technical setup, there are two main options for setting up the OpenSAFELY environment:  

-   The first option is to use an online development environment. The online environment recommended by OpenSAFELY is Gitpod, which provides 50 free hours of monthly usage and negates the need for any software other than that required for accessing the TPP server. The Gitpod environment is easy to set up and integrates well with GitHub. 
-   If higher levels of monthly usage are envisaged, which may particularly be the case during the more time intensive co-piloting period, it may be preferrable to have the required software downloaded locally. [The required software is](https://docs.opensafely.org/install-intro/): 
-   Git
-   Docker
-   Coding language and IDE (Integrated development environment, the software which provides the environment for programming - for this project python and Visual Studio code were used)   

For this project the decision was taken to download the required software locally. This software is not part of the standard set up for NHS England laptops, and higher levels of permissions (e.g. a developer account) are required to install it. Obtaining the necessary permissions takes time, so to allow swifter progress the project was instead undertaken on cloud-based virtual machines with a data science set up provided by the NHS Transformation Directorate Analytics Unit. This provided a fast, effective and secure method for working on the code locally. 

Code for all OpenSAFELY projects (regardless of the setup) is stored on GitHub, a website designed for storing and collaborating on code. Instructions for setting up a GitHub account and preparing the necessary computing environment for completion of the project can be found in the OpenSAFELY [Getting Started Guide](https://docs.opensafely.org/getting-started/). 

Another key component to the technical set up (regardless of whether Gitpod or local set up is used) is installing the software required to access the TPP server. This is needed to view the results when the analysis code has been run on real data. This is done by connecting to the TPP VPN. Unfortunately, due to the specific settings for the VPN, it was not possible to connect to the VPN via a cloud-based virtual machine. Connecting to the VPN on NHS England laptops was also not possible at the time. To negate this problem, the OpenSAFELY co-pilots accessed the results and completed all the necessary checks prior to releasing them from the TPP server. 

#### The [co-piloting](https://www.bennett.ox.ac.uk/blog/2021/08/opensafely-co-pilot-programme-assisting-users-on-their-opensafely-journey/) period and project development period 

For the first four weeks of each project OpenSAFELY operate a ‘co-piloting’ period, where an OpenSAFELY ‘co-pilot’ provides an enhanced level of support, with regular meetings, to help researchers to understand and implement OpenSAFELY ways of working. The same co-pilot also continues to provide support beyond the co-piloting period. This was found to be a hugely beneficial system, however ongoing technical difficulties slowed progress during the co-piloting period, as obtaining the correct set-up for completing the project, and installing the necessary software, proved challenging. 

The project team also met for regular review meetings with a small group of collaborators and stakeholders in NHS England in an agile way of working. This group included members with relevant expertise, including analysts, subject experts and data scientists, who inputted knowledge and experience as well as providing steers for each stage of the analysis and giving feedback on work already undertaken. 

In addition to gaining an understanding of the NHS @home interventions and working with OpenSAFELY, the collaborative nature of the project also provided benefits for team members involved, in learning from each other’s skills and areas of expertise. Senior team members assisted the development of junior team members’ skills, in particular the development of: 

-    Best practice for coding such as the benefits of dynamic coding, use of functions to prevent duplication of code and reduce code maintenance burden and commenting the code. 
    
-   GitHub workflows including the benefits of raising small pull requests in making code reviews simpler and importance of maintaining good repo structure. 
    

A key part of the process is writing the code for extracting the relevant study cohort and variables for analysis. This code is known as the study definition. In addition to allowing time for resolving technology and set up issues, it is also important to be aware that creating the code, particularly for the study definition, is an iterative process. It is beneficial to clearly define the study population and the variables of interest at the start of the project with the co-pilot, as it may take several iterations to correctly code the method for extracting the study cohort. Care should also be taken to ensure that key demographics align with NHS standards and that definitions within the study definition are applied correctly.  

Examples of issues which require careful consideration and clarification include: the correct manner for extracting demographic variables, the appropriate inclusion criteria (i.e. what data needed to be present for a patient to be included in the study), issues relating to redaction of small numbers and rounding principles. Redaction and rounding should be applied within the code. Co-pilots may be able to assist with functions which can apply redacting and rounding automatically, but careful consideration must be given to exactly what redaction and rounding is required in each scenario.  

Many variables are extracted based on a codelist (a collection of clinical codes that classifies patients as having certain conditions or demographic properties – code systems include SNOMED and CTV3). OpenSAFELY provide a web-based tool, [OpenCodelists](https://www.opencodelists.org/), for creating and managing codelists. The website can be searched to see if an appropriate codelist already exists or used to create a new one. The project team are responsible for use of codelists and it is important to ensure that codelists used are appropriate for the purpose. Clinical or other expert input may be required to ensure this.  

Currently, for studies looking at multiple time periods, [separate cohorts are extracted for each of the relevant time periods](https://docs.opensafely.org/measures/#extract-the-data) (e.g. one week or one month). For this project separate cohorts were extracted for each week over the time period from April 2019 to June 2022. This can result in the project taking significant time to run in the server. One way to reduce this workload is to put any variables which do not change significantly over time into a ‘static’ study definition and run this cohort extraction only once. OpenSAFELY provide a function to then join the weekly or monthly and static datasets. 

Whilst working with data at arm’s length has significant benefits for security and information governance, it does bring additional challenges. OpenSAFELY provide the means to create fake data, which can be used to test the code prior to running on real data, however the return expectations for the fake data (what it is expected to look like) must be defined by the researcher and this can lead to a mismatch in the format of the fake data compared to the real data. Consequently, even if the project runs locally, upon running in the server there may be problems. Co-pilots and OpenSAFELY tech support are very willing to help, and can be contacted quickly via OpenSAFELY’s dedicated Slack channel  

(Slack is a messaging app for business, which can also be accessed via a web browser), however trouble-shooting such issues can still be difficult. 

Depending on the size of the dataset being analysed, there is also a risk of exceeding the memory limit within the server. To mitigate this, OpenSAFELY provide suggestions of ways to [improve performance and minimise memory usage,](https://docs.opensafely.org/memory-efficient-working/#remove-or-slim-down-large-objects-from-memory) such as considering the datatype for each column of a dataframe. 

It is beneficial for the co-pilot to check the study definition prior to running on the server. Time should also be allowed for running on the server (due to potential for technical difficulties) and obtaining release of results (which requires a full review by OpenSAFELY to ensure there are no disclosure issues). 

#### Project wrap-up 

Once all the required results have been obtained, the next steps are to analyse the results and share them internally for further validation and analysis. In line with OpenSAFELY’s transparency principles, the GitHub repository containing the project code will be made public. 

#### Lessons learned: 

-   Be prepared: it’s helpful to have the software in place and to map out study aims and requirements prior to beginning the co-piloting period. Safe researcher accreditation should be obtained as early as possible as access to the server is dependent on completion of this step. 
    

-   Use of co-piloting period: OpenSAFELY recommend 50-60% of the researchers’ working time be spent on the project during the co-piloting period. This ensures maximum benefit is obtained from the enhanced level of co-pilot support. Co-pilots can help identify appropriate codelists, ensure correct understanding of OpenSAFELY functions and assist with issues such as redacting and rounding scripts. 
    
-   Technical skills: use of the OpenSAFELY module requires a fair amount of technical skill, including writing code, use of software and GitHub and understanding of Git ways of working. It is beneficial to have at least one member of the team who already has some level of technical skill in these areas, and if not then some basic training before the start of the project may be required. 
    
-   Time investment: undertaking projects with OpenSAFELY is time intensive due to the time needed to learn about OpenSAFELY ways of working, this should be factored into the planning for a project. 
    
-   Limitations of the dataset: clinical coding of healthcare interventions is not always consistent, which may limit the usefulness of the data obtained. 
    
-   Importance of the study definition: correct extraction of cohort and variables within the study definition requires careful planning. Thorough checking of codelists and study definition code, along with good communication and liaison with co-pilot, can help with this. 
    

-   Benefits of collaboration: collaborating across teams is beneficial for exchanging knowledge and expertise and ensuring the project team has a good skills mix.  
    
-   Slack channel: Making good use of the Slack channel can help to progress the project as OpenSAFELY support, including tech support, are very willing to help and generally respond quickly. 
    
-   Server time: consider ways to improve performance and reduce memory usage. Allow time for server downtime and keep in mind dates and times for planned maintenance (speak to co-pilot or check on Slack). 
    
-   Checking codelists and definitions: Dedicate time to ensure codelists meet the requirements of the project and definitions of variables within the study definition are correct. Ensure key demographics align with NHS standards. 
    
-   Good coding practice: good coding practice, such as using functions to prevent duplication of code, is important to reduce the likelihood of errors and reduce code maintenance burden, make code reviews easier and improve readability of the code. 
    

### Summary 

The level of access to a vast amount of primary care data makes this platform worth using for future studies. However, the significant time investment required and the need for a certain level of technical skill within the research team should be factored into the decision to undertake a project through OpenSAFELY. Good planning and preparation, such as having the correct software in place prior to starting the study, are essential to ensure smooth running of the project. The co-piloting scheme is extremely helpful, and it is advisable to make best use of the initial co-piloting period to become familiar with OpenSAFELY ways of working.

Output|Link
---|---
Case Study|TBD

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#