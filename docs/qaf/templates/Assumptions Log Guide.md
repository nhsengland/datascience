# Assumptions Log Guide

Template

Just want the Assumptions Log Template? 12733644851273364485DS\_xxx: Assumptions LogClick here to create from template

Assumptions are inherent in any data science project. Indeed you could say that the careful making and evaluation of assumptions is **the major part** of any analytical project.

Sometimes, these assumptions can be verified through further analysis and/or evidence gathering, but it might be necessary to make a **temporary assumption** in order to make headway with a project and not be blocked. In these cases, keeping a log allows the tracking of anything that should be proven later in on a project, or before releasing a product.

In other cases, assumptions must be made precisely because a fact **cannot be known** during the lifecycle of a project. This might be things that we'll only discover later, things that would be prohibitively expensive to prove, or things where there is just an intrinsic uncertainty. We make **simplifying assumptions** - assumptions that are required for us to tackle the problem using available analytical techniques, while acknowledging that the real world is more complex.

In the case of assumptions that are unlikely to be proven during the lifecycle of a project, maintaining a log facilitates the prioritisation of assumptions for further investigation. This will include reviewing potential impact on outputs, and (where possible) bounding the uncertainty through other methods such as examination of proxy measures or drawing on the judgement of subject matter experts. Ultimately, we will refer to our remaining assumptions when we ensure that any **residual sources of uncertainty** are understood and potential impacts on end use case / resulting decision makers are **communicated clearly to our customer**.

Assumptions aren't just about the data or analysis components of a project. We might also make assumptions about how users will interact with the tool, how it will impact or be impacted by changes outside of the product itself, what regulations we will need to comply with, and about what later stages of delivery (such as live deployment and/or integration with other systems) might require.

**In all cases, assumptions must be:**

* Demonstrated to be **correct**; or
* Demonstrated to have **no adverse impact** on outcomes in practice; or
* Understood to **carry a level of uncertainty/risk** -  with either **mitigation** put in place or agreement to **accept** the risk.  Ideally level of uncertainty and its potential impact is quantified.

Maintaining an assumptions log allows teams to:

* Clearly identify assumptions that have been made throughout project delivery
* Have structured discussions about assumptions with the Commissioner, the Analytical Assurer, and other stakeholders
* Solicit advice and correction from subject matter experts
* Build an audit trail of assumptions made through the project lifecycle
* Triage assumptions by potential impact on overall project outputs, and prioritise effort to evidence / refine / challenge those assumptions accordingly.
* Maintain a knowledge base of residual uncertainty that may remain at the end of the project, so that it can be effectively communicated to customers

# AssumptionsLogCreating an assumptions log

Create a log in your project space using the template: 12733644851273364485DS\_xxx: Assumptions LogCreate Assumption Log

An assumptions log could include the following entries:

INLINE

| **ID** | An incremental numeric identifier that allows quick reference. | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Assumption** | A succinct description of the assumption. Try to draft your assumption as a hypothesis - a factual statement of what you are assuming to be true.  Example: *The test dataset is representative of the target population.* | | | | | | |
| **Type** | A label to group assumptions that are similar in nature together. Assumptions of the same type might need to draw on the same subject matter expertise for validation. Use the following types: | | | | | | |
| User Need | What does the user require in order for the product to be usable and deliver business value?  Example assumption: *Users need forecasts at site level covering the next 21 days.* | | | | | |
| Data | Relating to suitability and availability of data for project aims  Example assumption: *Data from January 2022 is available for all trusts.* | | | | | |
| Methodology | Relating to choices of analytical technique  Example assumption: *We have enough data to train a Neural Network.* | | | | | |
| ELSI | Relating to Ethical, Legal and Social Implications (including Information Governance)  Example assumption: *During development phase, this work is covered by the Advanced Analytics Workstation DPIA.* | | | | | |
| Clinical | Relating to assumptions about medical matters (including clinical safety)  Example assumption: *Code List X includes all relevant ICD10 codes to identify condition Y.* | | | | | |
| Deployment | What will be needed to support future deployment and scalability to deliver envisioned business value?  Example assumption: *Team X will be responsible for weekly monitoring for model drift in predictions.* | | | | | |
| **Quality** | GREEN | Reliable assumption, well understood and documented.  For example, confirmed by SME, validated by directly relevant current data or validated by triangulation against several suitable sources of evidence. | | | | | |
| AMBER | Some evidence to support the assumption.  For example, a source with poor methodology or evidence that is a few years old. | | | | | |
| RED | Little evidence to support the assumption.  For example, an opinion or a limited data source with poor methodology. | | | | | |
| UNKNOWN | Not yet determined (there should be an associated follow-up action) | | | | | |
| **Impact** | LOW | Marginal assumption having limited impact on the outputs, confirmed by sensitivity analysis. | | | | | |
| MEDIUM | Assumption with a relevant, but not critical, impact on the outputs. | | | | | |
| HIGH | Core assumption of the analysis; the output would be markedly affected if the assumption changed. | | | | | |
| UNKNOWN | Not yet determined (there should be an associated follow-up action) | | | | | |
| **Status** | ACCEPTED | Assumption has been investigated, drawing on evidence to correctly assess quality and impact.  Where high impact uncertainty remains, mitigation has been put in place (for example, the potential impact is documented and communicated to / accepted by customer). | | | | | |
| INVESTIGATING | Assumption is under investigation - Quality and Impact assessments are subject to change but represent current assessment on limited evidence. | | | | | |
| UNEXPLORED | Assumption has not yet been investigated - Quality and Impact assessments represent pessimistic view. | | | | | |
| REDUNDANT | Assumption no longer required due to change in approach. | | | | | |
| **Evidence** | Very brief summary, and a link to evidence supporting the assumption.  *e.g. link to Confluence page containing analysis comparing test dataset to census data or embedded email from SME with their professional advice.* | | | | | | |
| **Date reviewed** | The date on which this assumption (and its corresponding quality, impact, status and evidence) were reviewed | | | | | | |
| **Follow-up action** | Summary of any actions that were still to be undertaken to support this assumption when it was last reviewed.  *Ideally create a link to an associated Jira ticket so you can track status conveniently.* | | | | | | |