# Introduction to Quality Assurance

## Why do we need Quality Assurance?

From [“The Aqua Book”](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/416478/aqua_book_final_web.pdf):

> Analysis is vital to the success of policy development and the delivery of programmes, projects, and operational services. Analysis helps to shape and appraise options, provides insight into how complex systems work and behave, measures system performance and improves efficiency.
>
> However, if analysis and any supporting models, data and assumptions are not fit-for-purpose then the consequences can be severe ranging from financial loss through to reputational damage and legal challenge. In the most severe of consequences, lives and livelihoods can be affected.

Quality Assurance can help you and your team:

- Overcome blockers.
- Have a clear route of escalation.
- Gain analytical authority to release.
- Ensure that your documentation is good enough and understandable.
- Ensure that your analysis is done with RIGOUR (Repeatable, Independent, Grounded, Objective, Uncertainty-managed, Robust).

## Who is involved in Quality Assurance?

All your team should be involved in Quality Assurance, with its practices embedded consistently across all team members of all the squads.

However, there are some key players in Quality Assurance that you should be aware of:

- **Commissioner** –Works with the Analyst to define the problem, criticality, scope, and deliverables and assist with Resource allocation, including SMEs, whilst ensuring sufficient time and resources for the required level of assurance.
- **Analytical Assurer** –Usually, a senior analyst or analytical project manager who is not one of the analysts delivering the analysis. Ensures evidence of appropriate analytical quality assurance activities throughout the life cycle of the analysis.
- **Lead Analyst** – Works with the Commissioner to define the problem, criticality, scope, and deliverables and assist with Resource allocation. Validates the problem statement and user requirements. Questions if the analysis is done with RIGOUR.
- **Dimension Lead** – Rotating position among the analysts delivering the analysis. Acts as a guide and advocate of quality processes, helping to ensure that the analysis being carried out meets the Quality Framework.

See more details about the [QA roles here.](./Role%20Descriptions%20Guide.md)

## What is involved in Quality Assurance?

### Proportionality of response

The extent of the analytical quality assurance effort should be proportionate in response to the risks associated with the intended use of the analysis. These risks include financial, legal, operational, and reputational impacts. In addition, analysis that is frequently used to support a decision-making process may require a more comprehensive analytical quality assurance response.

The figure below provides a good demonstration of how the proportionality of response can scale with the complexity and risk of a project:

### Assurance throughout development

Quality assurance considerations should be considered throughout the life cycle of the analysis and not just at the end. Effective communication is crucial when understanding the problem, designing the analytical approach, conducting the analysis, and relaying the outputs.

### Verification and validation

Analytical quality assurance is more than checking that the analysis is error-free and satisfies its specification (verification). It must also include checks that the analysis is appropriate, i.e., fit for the purpose for which it is being used (validation).

### Analysis with RIGOUR

Quality analysis needs to be **repeatable**, **independent**, **grounded**, **objective**, have understood and managed **uncertainty**, and the results should address the initial question **robustly**.

It is important to accept that uncertainty is inherent within the inputs and outputs of any piece of analysis. It is important to establish how much we can rely upon the analysis for a given problem.

### The Quality Framework

The Quality Framework for Data Science projects and services is an assessment tool to help us deliver high-quality, assured products that meet user needs.  It reflects the principles of the AQuA book and other quality frameworks and should be reviewed periodically during the project lifecycle.

It is not intended as a checklist but as a flexible guidance to be adapted based on the complexity and risks associated with the model or analysis and the time and resources available.

The Quality Framework is included in all project templates.

## When should Quality Assurance be done?

As mentioned above, Quality Assurance should be done throughout the life cycle of a project. This can be assisted by:

- The Lead Analyst (or a delegate) arranges timely review meetings with the Analytical Assurer
- The Dimension Lead at the time checks in with the analytical team on a regular basis, reviewing a single or handful of the dimensions at a time.

However, there are stages of the project where some parts of Quality Assurance will focus on:

- Customer engagement phase:
  - Challenging and testing the understanding of the problem.
  - Challenging the requirements, boundaries and scope and assessing whether sufficient views have been considered.
- Design and conduct of analysis phase:
  - Ensuring the level of quality checking of the analysis is appropriate for the decision being supported.
- Delivery of the analysis phase:
  - Ensuring a suitable audit trail is in place that clarifies the level of validation, scope, and risks associated with the analysis.

## How to run a QA meeting

### How to run an Analytical Quality Assurance Meeting

Holding regular AQA meetings is an essential part of delivering a quality data science project.

You might think that an AQA meeting sounds intimidating. They absolutely should not be - they are safe spaces for analyst-to-analyst technical discussion of the assumptions and uncertainties that are intrinsic to any analytical project.

AQA reviewers will always be expecting to discuss work-in-progress not finished article. For senior staff they are an important opportunity to maintain understanding of what's going on in projects at a level of technical detail - and to draw on their experience to offer advice and direction. For Lead Analysts they are a mechanism for flagging risks and issues to the senior staff who are ultimately accountable for the quality of our team's outputs and for ensuring that customers understand residual risks in work we deliver.

### When to hold them

There will normally be several Analytical Quality Assurance (AQA) review meetings during the project lifecycle. These should be:

Early on in the project - to validate expressed user requirement, roadmap, methodological approach are ways of working. e.g. at end of sprint 1 or 2.
Late in the project - to validate approach taken through project, assure final outputs, ensure all follow-up actions have been or will be completed. e.g. 1-2 sprints before project closure.
At any point during the project that would be useful - and at least once in every BPC. For example, when emerging findings are available or when a change in approach is being considered.
For business critical models, or work which will inform subsequent decision making, a formal AQA sign-off should be completed by both Analytical Assurer and the Commissioner.

An important topic to discuss with your Analytical Assurer at AQA meetings is agreeing what is the Proportionate level of QA for your project. Not all projects are the same, and not all projects require the same level of scrutiny. Propose what you think is sensible, and get input from your Analytical Assurer.

### Attendees

Analytical Assurer
Lead analyst
Other members of analyst team as required or interested - attendance encouraged!
Commissioner / customer will not generally join AQA meetings, which are intentionally technical.

(See Role Descriptions Guide)

### Key documents

Quality Framework Log - to record status, evidence and activities against the key elements of the quality review. This is the key document that will form the agenda for the meeting.
User Requirements / Project Initiation Document - to record overall objectives of the project, including setting out what is in and out of scope.
Assumptions Log - to record key assumptions made through the project, record any evidence supporting those assumptions, and highlight areas of risk / uncertainty
Risk Log - to record current status and any mitigations
Other confluence documentation - covering methodology, project planning, data processing and IG.
NB - these documents should be maintained routinely throughout project delivery by the analyst team - NOT prepared retrospectively just for AQA review. Making them live documents and a central part of project delivery is the best way of ensuring that quality is addressed throughout, and that key assumptions and areas of risk are identified and dealt with at the right time. There are templates for most of these documents - use them!

### In advance of meeting

Lead analyst convenes meeting and ensures that key documents are up to date and shared in advance.
Lead analyst highlights any areas in need of more detailed review / decisions to be taken (if any).
Analytical assurer reviews paperwork ahead of meeting, flagging any items for detailed review during meeting.
Remember it is for the Lead Analyst to schedule AQA meetings - don't wait to be chased...

### Typical meeting

Lead analyst provides a high level overview of project goals, approach and current situation.
Detailed review of any elements of methodology / decisions flagged ahead of meeting.
By exception review of the Quality Framework Log
By exception review of Assumptions log
By exception review of Risks / Issues / Dependencies
Logs and registers updated during meeting
Lead analyst captures any actions / outstanding queries for follow up.
Analytical assurer summarises, and records high level outcome from meeting on the QF Log confluence page
Agree timeframe for next meeting.
Generally allow 60-90 minutes for an AQA meeting.

### Final AQA meeting

Lead analyst summarises final state of project, including reviewing deliverables against agreed scope.
Line by line review of QF Log
Line by line review of Assumptions Log
Line by line review of Risks / Issues / Dependencies
Any Risks / Issues to be handed over to customer identified and approach agreed.
Analytical assurer and Lead Analyst discuss recommendation to customer - including summarising any sources of uncertainty they need to be aware of, and advice to be given on fitness for purpose / scope of application of work.
AQA reviewer completes ‘Final QA sign-off’ on QF log

### After final AQA meeting

AQA reviewer provides written statement to customer, and seeks their confirmation of acceptance of any recommendations.
