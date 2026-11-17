# DS*xxx: Roadmap*

# Project Roadmap

A roadmap is a realistic, flexible, up-to-date and agreed plan that gives structure for delivery and aligns with stakeholder requirements. It communicates clear, measurable goals and the likely flow of deliverables.

**Keep it high level** — use Jira for task-level management. This page is for stakeholder alignment, the big picture, and Business Planning Cycle discussions.

The roadmap should establish an initial set of expectations, and be maintained to reflect the most current plan we are confident of delivering. Use the version log to keep track of major changes.

Developing and maintaining a Roadmap and tracking delivery of high level objectives is an [essential part](../%F0%9F%97%BA%EF%B8%8F%20Roadmap.md) of delivering a [quality data science](../DS%20Quality%20Framework.md) project.

Roadmap Guidance

## Table explainer

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quarter          | Usually we will plan out roadmaps at a quarterly granularity aligned to the Business Planning Cycle. Content for more distant quarters might be incomplete, tentative or not yet agreed in which case mark them '_indicative_'.                                                                                                                                                                                                                                                                                                                                      |
| TRL (end of Qtr) | What overall Technical Readiness Level+Guide) are you aiming to reach at the end of the Quarter?                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Workstreams      | Optional - create a column for each distinct workstream if this adds helpful organisation to your roadmap.  Workstreams might align to Epics used in Jira. Examples: Data Access & Familiarisation; Model Build; Customer Engagement; Front End. Smaller projects might just have one workstream. Within each cell: a short goal line plus 2–4 key deliverables / milestones. Goals can convey overall ambition (e.g. 'improve model performance'). Deliverables should be specific and concrete (e.g. 'develop XGBoost model and produce a report on performance'). |

This table always reflects the **current agreed roadmap.**

Title it with a version number and the date confirmed - as per the Version History table below.

**Roadmap Version:**1.0

**Confirmed Date:**

| Quarter                             | TRL (end of Qtr) | Workstream A: [name]                              | Workstream B: [name] |
| ----------------------------------- | ---------------- | ------------------------------------------------- | -------------------- |
| **YY/YY Q1** (Apr–Jun)              |                  | Goal: xxx - [ ] Deliverable 1 - [x] Deliverable 2 |                      |
| **YY/YY Q2** (Jul–Sep) _Indicative_ |                  |                                                   |                      |

# Change Log

Every **rebaseline** is recorded here — a material change to scope, dated deliverables, or quarter goals.

Minor in-quarter updates are not tracked (Confluence page history covers those). A rebaseline bumps the version (v1.0 → v2.0 → v3.0).

Rebaselined roadmaps should be confirmed with senior stakeholders.

Change Log Guidance

## Table explainer

|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Version        | Give each **major** rebaselining a new version number.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Date           | When new roadmap was **confirmed.**                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| What Changed   | Keep this super brief - confluence page history is available if really needed.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Why / trigger  | What prompted need for a rebaselining. Rebaselining could be necessary as part of a 'route to green' plan for a project that has gone off track or because things have moved quicker than expected. It could be that the project has been impacted by delays in dependencies, by risks materialising, by new priorities emerging, or by change in resource profile available on the delivery team.                                                                                       |
| Confirmed with | With what senior stakeholder or at what forum or meeting have you confirmed the change of scope.  Note 'Confirmed' not 'Agreed'. The over-riding requirement of a roadmap is that it is **realistic**. Senior stakeholders need to be aware of roadmap changes and have input to those decisions (they might guide you on trade-offs, for instance) but ultimately, as project lead, you need to sign off on a roadmap that you consider is deliverable given what you know at the time. |
| Audit trail    | Link to a meeting record / provide a copy of an email or Teams message where the new roadmap was confirmed.                                                                                                                                                                                                                                                                                                                                                                              |

| Version | Date | What changed                               | Why / trigger                                  | Confirmed with | Audit trail |
| ------- | ---- | ------------------------------------------ | ---------------------------------------------- | -------------- | ----------- |
| v1.0    |      | Initial baseline                           | Project start                                  | [forum]        |             |
| v2.0    |      | [e.g. Q3 forecast deliverable moved to Q4] | [e.g. IG sign-off delayed — see dependency D2] | [forum]        |             |

# Dependencies Log

A Dependency is a relationship between conditions, events, tasks, projects etc. such that one cannot begin or complete an activity/activities until such conditions, events, tasks or projects etc. have occurred, begun or completed.

Dependencies may impact overall objectives of a project, even if they do not impinge on delivery of internal tasks within the project (for example, the ability of end users to take advantage of a delivered product).

Working with dependencies should be planned into the project roadmap. If there is a likelihood that dependencies will not materialise, this should be tracked as a Risk.

Dependencies may involve additional stakeholders, requiring specific management.

Dependencies Guidance

## Table explainer

|                   |                                                                                                                                                                                                   |                                                                                                                                                                                                                |     |     |     |     |     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
| **Description**   | \* _In order to complete X we require Y_ or \* _If Y does not occur, then Z_                                                                                                                      |                                                                                                                                                                                                                |     |     |     |     |     |
| **Importance**    | VERY LOW → VERY HIGH                                                                                                                                                                              | Assess the relative importance of the of the dependency to delivery of project objectives. Use a scale appropriate to your project's context - the purpose is to support prioritisation so use the full range. |     |     |     |     |     |
| COMPLETE          | Dependency has now been removed (e.g. through delivery of required component / completion of required action). Do not mark COMPLETE if there is (for example) an ongoing maintenance requirement. |                                                                                                                                                                                                                |     |     |     |     |
| UNKNOWN           | Not yet determined (there should be an associated follow-up action to understand impact)                                                                                                          |                                                                                                                                                                                                                |     |     |     |     |
| **Source**        | What system / team / organisation / person / event?                                                                                                                                               |                                                                                                                                                                                                                |     |     |     |     |     |
| **Action(s)**     | Associated actions, if any. Ideally a link to a Jira ticket to complete or monitor completion of the associated task. Might include periodic monitoring of dependency progress.                   |                                                                                                                                                                                                                |     |     |     |     |     |
| **Date Reviewed** | Date on which dependency was last reviewed.                                                                                                                                                       |                                                                                                                                                                                                                |     |     |     |     |     |
| **Comments**      | If helpful to briefly note how a dependency has evolved (remember you also have version history on this page).                                                                                    |                                                                                                                                                                                                                |     |     |     |     |     |

|     | Description | Importance | Source | Action(s) | Date Reviewed | Comments |
| --- | ----------- | ---------- | ------ | --------- | ------------- | -------- |
| 1   |             |            |        |           |               |          |
| 2   |             |            |        |           |               |          |
