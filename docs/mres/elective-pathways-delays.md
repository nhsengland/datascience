---
title: 'Understanding delays in elective pathways'
summary: 'A case study of lithotripsy using NHS England data and process mining and machine learning techniques'
tags: ['SECONDARY CARE', 'FORECASTING', 'PROCESS MINING', 'MODELLING', 'STRUCTURED DATA', 'PYTHON', 'PYSPARK', 'COMPLETE']
---
*This project was completed by Evelyn Koon, Analyst, in the Elective Analysis Team, as part of the Data Science MRes at the University of Leeds.*

## Background
The UK’s National Health Service (NHS) provides publicly funded healthcare free at the point of use. In 2025, NHS England introduced the 'Reforming Elective Care for Patients' (NHS England and Department of Health and Social Care, 2025) initiative, aimed at enhancing the delivery of elective services and reducing waiting times. Urology was one of the first five specialties chosen for reform due to its large and growing waiting list (NHS England and Department of Health and Social Care, 2025). Using national data, this project examines patient pathways for Extracorporeal Shock Wave Lithotripsy (ESWL) within Urology, aiming to understand why some patients remained on the waiting list for over 18 weeks.

## Methods

NHS England has introduced a new dataset, the Elective Patient Pathway (EPP), designed to capture activities within the elective care journey. This project applied process mining techniques to the national dataset, extending the scope beyond a single site. Directly Follows Graphs (DFGs) were used with input from NHS experts, new variables were derived and further examined using machine learning techniques to evaluate the association of these new variables on elective waiting times. Additionally, conformance analysis was used to compare individual hospitals with the longest and shortest durations on the elective waiting list, highlighting variations in care processes.

## Results 

Incorporating four of the additional activity types, which were non-lithotripsy appointments and assigning sequential identifiers to lithotripsy treatments (e.g., ESWL_1  or lit_1 for the first session), enabling the discovery of more meaningful care pathways. The machine learning models identified two of these as the most predictive features when they were tested. These were the other last appointment, which occurred last out of all non-lithotripsy appointments, and the first other outpatient routine appointment.
Patients who waited less than 18 weeks generally followed similar sequences to those who waited longer, though extended delays were concentrated in the early stages of the pathway, particularly after being added to the waiting list. Conformance analysis across hospitals revealed that more complex pathways, with more activity, took longer to complete. Much of this extended activity occurred after patients left the waiting list, indicating the potential impacts of more complicated pathways on service provision.

## Conclusions

By combining national data with clinical expertise, this study uncovered variation in patient pathways, particularly for those with complex needs navigating the lithotripsy pathway. Process mining and machine learning revealed disparities in waiting list durations and activities that influence time a patient waited for their treatment, while conformance analysis highlighted variations in patient pathways. Grounding the dataset in real-world clinical practice ensured operational relevance to improve NHS performance. These insights can support frontline decision-making and offer promising applications in the NHS, especially with the development of new pathway datasets.

Output|Link
---|---
Code and Documentation - private while under development|[Link](https://github.com/nhsengland/PM4_elective_care.git)

#
