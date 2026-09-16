---
title: 'Impact of midwife-led continuity of carer on birth outcomes'
summary: 'To assess whether women receiving midwife-led continuity of carer in pregnancy in England have better birth outcomes.'
tags: ['MACHINE LEARNING', 'MODELLING', 'RESEARCH', 'POPULATION HEALTH', 'STRUCTURED DATA', PATIENT IDENTIFIABLE DATA, 'PYTHON', 'SQL', 'R', 'COMPLETE']
---

*This project was completed by Chris Roebuck, Deputy Director for Clinical Outcomes and Indicators, in the Clinical Outcomes and Indicators Team, as part of the Data Science MRes at the University of Leeds*

Designed project to use rich record level dataset to answer clinically relevant policy question with data science techniques. In looking to balance these three objectives, the most compromise was on the third of them with the logistic regression model performing better than random forest etc.

## Design
A national secondary uses database of clinical and operational data.

## Population
Just under 1 million women who conceived between October 2020 and August 2022 and gave birth, either as a live birth or stillbirth, to singletons in England after 24 weeks.

## Methods
We created cohorts of women from the data who were and were not on the full midwife led continuity of carer pathway at 24 weeks, along with a separate cohort of women with no antenatal appointment by 24 weeks. We used machine learning models including logistic regression to standardise and compare adjusted outcomes between cohorts.

## Main outcome measures
Stillbirth rate, preterm birth rate and rate of first feed of breast milk.

## Results 
Women on the full continuity of carer pathway at 24 weeks had higher rates of first feed of breast milk (observed/expected 1.03 95% CI 1.03-1.04) and under some models they had lower rates of preterm birth (obs/exp 0.97 95% CI 0.96-0.99). Black women on this pathway had lower than expected rates of stillbirth under some models than (obs/exp 0.74 95% CI 0.53-0.995). More data from the ongoing rollout are needed to validate the stillbirth and preterm birth findings, as model and methodology choice affected significance. Women with no antenatal appointment by 24 weeks had nearly twice the expected stillbirth rate (obs/exp 1.93 95% CI 1.65-2.23).

## Conclusion
Women whose first antenatal appointment is recorded as being over 24 weeks have significantly worse pregnancy outcomes and the reasons driving this should be investigated and outreach policies developed. Midwife-led continuity of carer has a beneficial impact on babies receiving a first feed of breast milk and there is some evidence it reduces stillbirth rate among black women and preterm birth rate among all women and the most deprived group.

Output|Link
---|---
Published Paper | [Nature](https://www.nature.com/articles/s43856-025-01025-z)

#