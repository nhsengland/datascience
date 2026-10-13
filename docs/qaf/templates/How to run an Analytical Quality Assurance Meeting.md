# How to run an Analytical Quality Assurance Meeting

Holding regular AQA meetings is an essential part of delivering a [quality data science](../DS%20Quality%20Framework.md) project.

You might think that an AQA meeting ***sounds*** intimidating.  They absolutely should not be - they are safe spaces for analyst-to-analyst technical discussion of the assumptions and uncertainties that are intrinsic to any analytical project.

AQA reviewers will always be expecting to discuss work-in-progress not finished article. For senior staff they are an important opportunity to maintain understanding of what's going on in projects at a level of technical detail - and to draw on their experience to offer advice and direction. For Lead Analysts they are a mechanism for flagging risks and issues to the senior staff who are ultimately accountable for the quality of our team's outputs and for ensuring that customers understand residual risks in work we deliver.

## When to hold them

There will normally be several Analytical Quality Assurance (AQA) review meetings during the project lifecycle.  These should be:

1. Early on in the project - to validate expressed user requirement, roadmap, methodological approach are ways of working.  e.g. at end of sprint 1 or 2.
2. Late in the project - to validate approach taken through project, assure final outputs, ensure all follow-up actions have been or will be completed.  e.g. 1-2 sprints before project closure.
3. At any point during the project that would be useful - and **at least once in every BPC**.  For example, when emerging findings are available or when a change in approach is being considered.

For business critical models, or work which will inform subsequent decision making, a formal AQA sign-off should be completed by both Analytical Assurer and the Commissioner.

An important topic to discuss with your Analytical Assurer at AQA meetings is agreeing what is the [Proportionate level of QA](../%F0%9F%AA%9C%20Proportionate%20QA.md) for your project.  Not all projects are the same, and not all projects require the same level of scrutiny. Propose what you think is sensible, and get input from your Analytical Assurer.

## Attendees

* Analytical Assurer
* Lead analyst
* Other members of analyst team as required or interested - attendance encouraged!

Commissioner / customer will not generally join AQA meetings, which are intentionally technical.

(See [Role Descriptions Guide](./Role%20Descriptions%20Guide.md))

## Key documents

* Quality Framework Log - to record status, evidence and activities against the key elements of the quality review. This is the key document that will form the agenda for the meeting.
* User Requirements / Project Initiation Document - to record overall objectives of the project, including setting out what is in and out of scope.
* Assumptions Log - to record key assumptions made through the project, record any evidence supporting those assumptions, and highlight areas of risk / uncertainty
* Risk Log - to record current status and any mitigations
* Other confluence documentation - covering methodology, project planning, data processing and IG.

NB - these documents should be maintained routinely throughout project delivery by the analyst team - NOT prepared retrospectively just for AQA review.  Making them live documents and a central part of project delivery is the best way of ensuring that quality is addressed throughout, and that key assumptions and areas of risk are identified and dealt with at the right time.  There are templates for most of these documents - use them!

## In advance of meeting

* Lead analyst convenes meeting and ensures that key documents are up to date and shared in advance.
* Lead analyst highlights any areas in need of more detailed review / decisions to be taken (if any).
* Analytical assurer reviews paperwork ahead of meeting, flagging any items for detailed review during meeting.

Remember it is for the Lead Analyst to schedule AQA meetings - don't wait to be chased...

## Typical meeting

* Lead analyst provides a high level overview of project goals, approach and current situation.
* Detailed review of any elements of methodology / decisions flagged ahead of meeting.
* By exception review of the Quality Framework Log
* By exception review of Assumptions log
* By exception review of Risks / Issues / Dependencies
* Logs and registers updated during meeting
* Lead analyst captures any actions / outstanding queries for follow up.
* Analytical assurer summarises, and records high level outcome from meeting on the QF Log confluence page
* Agree timeframe for next meeting.

Generally allow 60-90 minutes for an AQA meeting.

## Final AQA meeting

* Lead analyst summarises final state of project, including reviewing deliverables against agreed scope.
* Line by line review of QF Log
* Line by line review of Assumptions Log
* Line by line review of Risks / Issues / Dependencies
* Any Risks / Issues to be handed over to customer identified and approach agreed.
* Analytical assurer and Lead Analyst discuss recommendation to customer - including summarising any sources of uncertainty they need to be aware of, and advice to be given on fitness for purpose / scope of application of work.
* AQA reviewer completes ‘Final QA sign-off’ on QF log

## After final AQA meeting

* AQA reviewer provides written statement to customer, and seeks their confirmation of acceptance of any recommendations.