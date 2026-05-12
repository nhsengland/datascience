---
title: 'Predicting Winter Pressures on Emergency Admissions in England Using Machine Learning'
summary: 'A 4-year national study across all NHS Trusts in England using Daily Emergency Care Data Set (ECDS) linked with UK Met Office weather data to predict winter pressures on Emergency admissions using Machine Learning to improve planning and response in the Emergency Department.'
tags: ['SECONDARY CARE', 'EMERGENCY CARE', 'PUBLIC/POPULATION HEALTH', 'MACHINE LEARNING', 'RESEARCH', 'LINKAGE', 'MODELLING', 'STRUCTURED DATA', 'TIME SERIES', 'PYTHON', 'SQL', 'COMPLETE']
---
*This project was completed by Joby Jose, Senior Analytics Developer, in the Enterprise Data Visualisation Team, as part of the Data Science MRes at the University of Leeds.*

Winter pressures present a continued challenge to the National Health Service (NHS) in England, as cold weather causes an increase in Emergency Department (ED) admissions. This study investigates the relationship between winter weather conditions and ED admissions across all NHS trusts in England. It aims to quantify the influence of temperature, rainfall, and snowfall on ED admissions and assess the predictive value of weather features using machine learning.

Daily Emergency Care Data Set (ECDS) records were linked with UK Met Office weather data, assigning mean daily temperature, rainfall, and snowfall to each trust. Feature engineering included lagged weather variables, calendar effects, and public holidays. An Extreme Gradient Boosting model was trained and optimised using GridSearchCV with time-series cross-validation and interpreted using SHapley Additive exPlanations (SHAP).

The model achieved an RMSE of 18.78 and MAE of 10.6 admissions per trust per day. SHAP analysis showed that temperature, and its lagged values were the strongest predictors, with colder weather linked to higher admissions. Subgroup analysis showed diagnosis-specific temperature effects. Circulatory admissions increased 4-6 days after temperatures of 2-12°C; infectious diseases and injuries responded to shorter lags; and respiratory admissions peaked 7 days after temperatures below -2°C. Rainfall had a moderate influence and snowfall had a marginal influence. These findings support the integration of weather-based forecasting into NHS planning tools.

Output|Link
---|---
Code available on the GitHub: | MRes_Project/Predicting_Winter_Pressures.ipynb at main jobyjose6/MRes_Project 

#