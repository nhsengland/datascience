# Risk Log Guide

TL:DR... So what do I have to do?...

Project leads must create and maintain a risks and issues log: 12733644891273364489DS\_xxx: Risk LogCreate Risk Log from template

Project risk logs will be reviewed on a quarterly basis. Every quarter, Analytical Assurers review the Quality Framework Log of each project. As part of this review they will ask whether your risk log has been reviewed recently by the Portfolio and Compliance Function Team. So, in advance of your Quality Framework review, you should ask Portfolio and Compliance to review your Risk Log.

Here's what we'll be checking for:

* Appropriate use of **risk** vs **issue**
* **Descriptions** of risks are structured as follows: "there is a risk that… which would lead to…"
* **Impact** and **likelihood** are scored: low/medium/high or 1/2/3/4/5
* Risks have an appropriate **strategy** (resolve/reduce/accept/transfer)
* **Actions** each have a related Jira ticket

Outcomes of the review could be:

* Does the risk need to be escalated? (based on the impact and likelihood scores)
* Does the risk align to a risk from another project, or a risk already on the Data Science Programme risk register?

Here are some ideas to get you started on populating your project's risks and issues page.

There are two categories of risk described here.   
Firstly you should consider, if your project were delivered successfully, would it be introducing risk to the wider organisation?  
Then you should consider risks that could prevent you from delivering your project successfully.

# **Risks to the wider organisation**

There are several categories of risk to consider. (copied from [Risk management process.pdf](https://nhs.sharepoint.com/:b:/r/sites/PPRteam/FormServerTemplates/Risk%20management%20process.pdf?csf=1&web=1&e=gVp4Dp)).   
Your project is unlikely to have many of these. But in a Data Science project, you'll probably be handling data! So as a minimum you should log a risk about Information Governance/Data Security, explaining the precautions you'll take when you handle data.

| Source | Description |
| --- | --- |
| Financial | Arising from not managing finances in accordance with requirements, and financial constraints. |
| Strategy | Arising from identifying and pursuing a strategy which is poorly defined, is based on flawed data or fails to deliver. |
| Quality of care | Arising from non-compliance with quality policies / standards, and healthcare inequalities. |
| Cyber security and technology | Arising from unauthorised and/or inappropriate access, and loss or misuse of data. |
| Workforce | Arising from suboptimal culture and/or unavailability of capacity and capability. |
| Infrastructure | Arising from infrastructure deficiencies and/or ineffective safety management. |
| Commercial | Arising from commercial partnerships, supply chains and contractual requirements. |
| Operational resilience | Arising from disruption to the systems and processes for which NHSE has responsibility. |
| Data sharing and governance | Arising from poorly defined roles, responsibilities and processes for data accessibility and sharing. |
| Reputational | Arising from external events including ethical violations, repeated failures and poor quality. |
| System oversight | Arising from ineffective oversight of system performance. |
| Legal, compliance and regulatory | Arising from a claim being made, liability or loss and/or failure to meet regulatory requirements |

 

Business Critical Models

Data Science models that are business critical should be subject to thorough quality assurance, which itself includes quantification and logging of the risks associated with deploying the model.

These considerations are currently out of scope for this guidance page.

[Model Quality Assurance and Business Critical Models](./Model%20Quality%20Assurance%20and%20Business%20Critical%20Models.md)Data Hazards

Data Hazards could be considered a category of risk. So you should consider some of these as potential risks for your project.

It is yet to be decided where to include Data Hazards in the Quality Framework, you could consider them as part of the risk log, or as a stand-alone exercise.

[Data Hazards - How to run an assessment](./Data%20Hazards%20-%20How%20to%20run%20an%20assessment.md)

# **Risks to your project**

More locally, you should consider types of risk which could impact the successful delivery of your project. The majority of your risk log are likely to be of this type.

For a technical project, these are likely to include:

|  |  |
| --- | --- |
| **Risk type** | **Mitigations** |
| Uncertainty in estimations | * Elaboration of tasks * Requirements discovery: e.g. tech spikes * Communicate uncertainty to stakeholders * Record [assumptions](../%F0%9F%92%AD%20Assumptions.md) |
| Uncertainty of scope | * Obtain early sign-off on requirements * Agile methodology / Frequent releases * Frequent stakeholder engagement to refine scope |
| Lack of stakeholder support | * Stakeholder matrix and engagement plan * Ownership and responsibilities of each stakeholder made explicit from the outset * Decisions documented and signed off |
| External dependences | * Early identification of external dependencies * Ownership of dependencies agreed * If an external resource is required, their commitment should be allocated and agreed |
| Inadequate tools / data | * Identification of software tools required and associated support * Identification of data access required * Early exploration of data sources to assess quality |
| Poor quality code | * Coding standards framework * Code reviews * Code testing * The open code publication checklist should be followed to ensure no publication of personal data, etc. |
| Poor productivity | * Planning for absence: leave etc * Planning with other projects competing for same resource * Planning for downtime while waiting on external dependencies |

# **Guidance for the risk log**

| Risk/Issue ID | Risk or Issue | Description | Impact | Likelihood | Strategy | Action | Owner | Date Reviewed | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Risk | There is a risk that...  Which would result in... | Very Low / Low / Medium / High / Very High | Very Low / Low / Medium / High / Very High | Resolve / Reduce / Accept / Transfer | Action to take to achieve the strategy.  Ideally with a Jira link. |  | Should be reviewed at least quarterly. | Further detail if needed. |
| 2 | Issue | X has occured / will occur  Resulting in... | Very Low / Low / Medium / High / Very High | N/A | Reduce / Accept | Action to mitigate (reduce) impact of the issue (if any).  Ideally with a Jira link. |  | Should be reviewed at least quarterly. | Further detail if needed. |

Remember that you have version history on the risk log page - so keep the details on the table concise and up to date with the latest situation only.

## **Risk or Issue**

A **Risk** is something that might happen but has not yet happened.

An **Issue** is something that has happened (or is certain to happen) and now has to be dealt with.

(A risk can become an issue if it is not addressed, or sometimes even if it was addressed)

## **Description**

Describe risks in this form: "**T****here is a risk that... which would result in...**". This will help clarify exactly what the risk is.

For example:

Draft 1: **"*New team members are not familiar with the modelling technique needed for the project"***

    There's no uncertainty in this statement. It has happened already. So it's an issue, not a risk.

Draft 2: ***"There is a risk that new team members allocated to the project are not familiar with the modelling technique needed for the project"***

    That's better. But so what?

Draft 3: ***"There is a risk that new team members allocated to the project are not familiar with the modelling technique needed for the project, which would result in them having to upskill and would delay our progress."***

    That's a well articulated risk. Now we know what could happen, and what the impact would be.

## **Impact/Likelihood**

You just need a score here, use **very low / low / medium / high / very high**

So for the example above:

* how **likely** is it that new team members are not familiar with the modelling technique?very low / low / medium / high / very high
* how bad an **impact** would the resulting delay have to the project? very low / low / medium / high / very high

Official scoring thresholds can be found on pages 20-26 of this guidance: [Risk management process.pdf](https://nhs.sharepoint.com/:b:/r/sites/PPRteam/FormServerTemplates/Risk%20management%20process.pdf?csf=1&web=1&e=gVp4Dp). But these are applicable to wider organisational risks.   
For the purpose of scoring risks within your project, you can just define your own scoring criteria, relative to the other risks in your project.

## **Strategy**

This is where we choose what to do about the risk. The most common options would be **resolve**/**reduce**/**accept**.   
Another option is **transfer**, i.e. where a stakeholder outside the project agrees to take responsibility for the risk.

Finally, the "last resort" option is **terminate**, which means stop the project!.. as the risk is too great.

It is very important to name the choice of strategy. A big list of risks can feel overwhelming if we assume that the aim is to **resolve** or **reduce** them all. Choosing to **accept** or **transfer** some risks (with the agreement of stakeholders / quality assurers) focuses our efforts onto which risks to work on.

## **Action**

Each risk and issue should have a corresponding action, and ideally, there should be a link to a JIRA ticket representing the action. Actions can then be added to project JIRA boards and tracked through to resolution via the usual stand ups and retrospectives.

The purpose of the action may be to **resolve** the risk/issue, or **reduce** the **Impact** or **Likelihood** of it to the point where it can be **accept**ed.  
This can be tracked with **post-mitigation scores**. For example, the likelihood of a risk may initially be high, so we take an action to reduce the likelihood. When we come to review that risk again the post-mitigation likelihood may now be low due to the action we have taken, and we can change the strategy to accept.

If the strategy is **accept**, then there will not be an associated action.

If the strategy is **transfer**, then instead of an action you could have evidence (such as an email chain) that another stakeholder has taken on the risk.