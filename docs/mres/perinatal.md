---
title: 'Predicting perinatal depression'
summary: 'A machine learning model of perinatal depression was developed using the Maternity Services Data Set (MSDS) and the Mental Health Services Data Set (MHSDS)'
tags: ['POPULATION HEALTH', 'DISEASES', 'PRIMARY CARE', 'EMERGENCY CARE', 'SECONDARY CARE', 'MACHINE LEARNING', 'CLASSIFICATION', 'FORECASTING', 'MODELLING', 'RESEARCH', 'LINKAGE', 'CLASSIFICATION', 'STRUCTURED DATA', 'TIME SERIES', 'MULTI MODAL', 'PYTHON', 'SQL', 'COMPLETE']
---

*This project was completed by Benedict Wren, Data Engineer, in the Data Engineering Team, as part of the Data Science MRes at the University of Leeds*

Perinatal depression (PND) is a devastating condition that affects a significant proportion of women during pregnancy and following birth. If left undiagnosed and untreated it can have dire consequences for the mother, baby, and family. Presently, there is no national screening programme in the UK. This project aimed to demonstrate the potential for using national linked data sets to predict the condition and form the basis for a screening tool.

I constructed a large-scale prediction model of perinatal depression using pseudonymised linked data from the Maternity Services Data Set (MSDS) and the Mental Health Services Data Set (MHSDS). This included an innovative approach to feature selection which was possibly the largest of type ever constructed and determined many predictors of PND which could prove valuable to other research. Data was used from almost half a million pregnancies between October 2019 and September 2020. A diverse range of around 17,000 sociodemographic, medical and clinical features were modelled and their association with the PND were calculated and compared. 

A final feature set of around 600 were then used to train a logistic regression prediction model. Performance was compared for each of the four trimesters of pregnancy. The model accurately classified the condition, achieving an AUC score of 0.757. I investigated how each of the four trimesters contributed to the performance of the prediction model.

Output|Link
---|---
Code Repository|[Link](https://bitbucket.org/wrenben/pnd_repo/src/develop/)

#