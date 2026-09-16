---
title: 'Predicting GP Staff Turnover'
summary: 'Predicting turnover of general practice staff in England; a machine learning approach. The project aim was to develop a machine learning model which, using currently held data, could at any time predict the number of leavers from the general practice workforce in England over the following 12 months.'
tags: ['WORKFORCE', 'FORECASTING', 'MACHINE LEARNING', 'LINKAGE', 'CLASSIFICATION', 'RESEARCH', 'MODELLING', 'STRUCTURED DATA', 'TIME SERIES', 'PATIENT IDENTIFIABLE DATA', 'PYTHON', 'SQL', 'COMPLETE']
---

*This project was completed by Neil Wilcock, Senior Analyst (Principal Information Analyst), in the Citizen Experience - National Digital Channels Team, as part of the Data Science MRes at the University of Leeds.*

Government manifesto and NHS workforce planning commitments call for increasing numbers of general practice staff. To meet these targets, staff need to be retained. Predicting leaver numbers is useful to policy makers and workforce planners as they track progress towards these commitments and identify areas where recruitment and retention require greatest focus.

With this in mind, the project aim was to develop a machine learning model which, using currently held data, could at any time predict the number of leavers from the general practice workforce in England over the following 12 months.

Person-level data about the general practice workforce from 2016 to 2023, held by NHS England, was combined with information about the practice each individual worked at to feed machine learning models, aimed at predicting whether an individual would leave the workforce. 

In separate experiments, logistic regression, XGBoost and random forest models were trained on single years, all years combined, and using all or selected features, to attempt to predict leavers.

Though there were trends in the characteristics of leavers, no model accurately predicted turnover. All three methods performed best on 2022/23 data. Random forests and XGBoost outperformed logistic regression but each achieved a maximum F1 score of just 0.3.

The conclusion drawn from these experiments and their results was that the information collected about general practice staff in England is not predictive of their likelihood of leaving the workforce within 12 months, using machine learning methods. Personal information is likely to be required, such as job satisfaction, performance levels, salary, marital status and commuting distance.

#