---
title: 'Study Relationship Between Continuity of Midwife Care, Deprivation, Ethnicity, and Stillbirth Outcomes'
summary: 'To investigate the association between a data-driven measure of care continuity, socioeconomic deprivation, ethnicity, and other key factors with the risk of stillbirth, using the Maternity Services Dataset maintained by NHS England.'
tags: ['SECONDARY CARE', 'MACHINE LEARNING', 'CLASSIFICATION', 'EXPLAINABILITY', 'RESEARCH', 'STRUCTURED DATA', 'PYTHON', 'COMPLETE']
---
*This project was completed by Ketankumar Italiya, Senior Data Architect, in the Metadata, Data Quality & Standards Team, as part of the Data Science MRes at the University of Leeds.*

In my capacity as a Data Engineer, my previous experience working with the NHS Maternity Services Data Set (MSDS) and the research conducted by Chris Roebuck inspired me to pursue further investigation into this domain. I was further encouraged by the collaboration and sponsorship of two relevant senior staff. Their support provided the necessary confidence to move forward with this strategic initiative.

The analysis was conducted on a filtered cohort of 773,786 pregnancies (including 2,233 stillbirths) where the number of unique care activities was greater than two, ensuring a sufficient basis for continuity analysis.

We found a mix-trend relationship between the care continuity cohorts and the stillbirth rate. The stillbirth rate was lowest (0.186%) with 'Fragmented Care' (care from >6 midwives), rising to 0.339% with 'Good Continuity' (≤3 midwives) and peaking at 0.416% with 'Low Continuity' (≤6 midwives). The analysis by subgroups revealed that the impact of ethnicity, deprivation, and maternal age on stillbirth risk varied significantly across these continuity cohorts. For example, after multivariable adjustment, the odds ratio for stillbirth among Black women (compared to White women) was highest in the 'Low Continuity' cohort (OR 1.806). Predictive models achieved high accuracy (0.9972) but Area Under the Curve (AUC) is 0.500, indicating no predictive power is not helpful.

Output|Link
---|---
Published paper on the Impact of midwife continuity of carer on stillbirth rate and first feed in England
|[Link](https://www.nature.com/articles/s43856-025-01025-z)

#
