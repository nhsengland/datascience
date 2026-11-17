# SLA guidance

This guidance is for writing a Service Level Agreement (SLA) for your project as it moves beyond the initial 'delivery' stage, to set realistic expectations about ongoing engagements with outside teams.

## When an SLA might be needed

A SLA is useful when there is ongoing interaction between teams where expectations, responsibilities and timelines need to be clearly defined. Therefore if your project is moving into a BAU stage that involves engaging with another team, either regularly through recurring deliverables or ad hoc via bug fixes, you should draw up an SLA.

The SLA could be more formally written up such as via a Word doc (as in the example below), or more informally documented in a Confluence page. Choose the medium that best suits your project and teams.

## Service tiers and response times

When considering response times, consider:

- What is practically possible from the DS team
- The service level of the host team

NHSE digital services generally have Bronze/Silver/Gold/Platinum classifications. Bronze and Silver are supported 8-6 Mon-Fri ex. bank holidays, while Silver Plus, Gold and Platinum are supported 24hrs, Mon-Sun, every day of the year.

See the National Service Desk confluence section on SLAs for more info.

## Sections to include in an SLA

### Generally useful

These sections are likely to be useful, no matter what the exact ongoing nature of the project.

- Agreement overview
  - Specify who the agreement is between
  - Outline the document
- Project background
  - Explain any necessary context for the project
  - Why were DS team brought in and what did we do?
- Definitions, conventions, acronyms and abbreviations
  - List of terms with descriptions
  - Can define here the SLA effective date and review date, for clarity
- Purpose and scope
  - Define what the SLA covers and what it does not
  - Specify the DS outputs/models/products included (e.g. dashboard, models, reports)
- Duration and renewal
  - Make clear the start and end date for the SLA
  - Specify renewal process (e.g. automatic, upon yearly agreement)
- Decomissioning criteria
  - Define criteria for when renewal may not happen/the project should be decomissioned
  - This could be because the project no longer provides value, or technology becomes obsolete, or a fixed timebox comes to an end
- Roles and responsibilities
  - Outline, for each team involved, the actions they are committing to
  - Might include expected timelines for bug fixes, any regular reporting, performance monitoring
  - An SLA is designed so all teams are held accountable - don't think you just have to list DS responsibilities here!
- Communication schedule and methods
  - Explain how and how often the teams will keep in touch, both between and during engagements
  - List any key contacts
  - Any specific escalation processes can be detailed separately
- Escalation path / Support process
  - Common escalation paths, e.g. if a bug is identified what process should each team follow to trigger SLA/action?
  - Flow diagram could be helpful here, or a table with numbered steps
  - Can help to clarify things like communication routes and expected timelines
- Confidentiality
  - Clarify all parties agree to maintain the confidentiality of all data and information exchanged as part of the SLA
  - Data will be handled in accordance with NHS data protection policies and relevant laws
- Compliance
  - Specify the compliance of any tools/products with NHS guidelines, including patient privacy, data protection and ethical standards
- Signatures
  - You need everyone to sign off on the document and agree!
  - You will need the Name, Title and Data of Signature from a representative of each team involved

### Deep-dive sections

You might want to consider deeper-dive sections on several project specifics, if:

- There is a handover of code, process etc. away from the DS team:
  - Define what work the DS team has completed and and who it is being handed over to
  - Specify what handover documentation (guides, demos, etc.) will be supplied by DS team and link out to these
  - Validation and sign-off expectations
  - Ownership transition point
- The DS team are expected to provide ongoing support and maintenance:
  - What clarifies as a bug/error vs a new request?
  - How should DS team be contacted? (also see communication)
  - Expected response times - could be broke down by severity of bug or incident
  - Define what happens if the root cause is unclear or shared/out of DS control
- The DS team are anticipating specific recurring engagements, e.g. evaluation schedule or retraining:
  - Specify the frequency or trigger, and scope of these engagements
  - Define inputs required from the product team
  - Clarify what success looks like. Is the engagement output-driven? Performance-driven?
  - Is monitoring required between engagements? Who owns this?
- There are fallbacks available, in the case of the DS solution being unavailable:
  - Define the fallback - is a previous process or model still an option?
  - When should the fallback be applied? e.g. model drift reaches certain unacceptable limits, or a platform issue disrupts daily model runs
  - How quickly will the fallback be applied, if the DS solution starts to fail? Is downtime accepted?
