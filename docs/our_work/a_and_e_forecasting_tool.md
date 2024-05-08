---
title: 'Accident and Emergency (A&E) Forecasting Tool'
summary: 'A probabilistic model which gives a three-week forecast for A&E departments, predicting their expected admissions loads'
origin: ''
tags: ['MODELLING', 'HOSPITAL', 'MONTE CARLO', 'MCMC', 'URGENT CARE', 'ACCIDENT AND EMERGENCY']
---

The A&E forecasting tool takes historical data from A&E departments, and uses this as a basis for modelling what admissions levels are likely to look like over the coming days and weeks. This is a probabilistic model, which provides a forecasted window within which a given location's admissions numbers are likely to fall, for each day over a three week period starting on the day of the forecast.

Having this information can help departments, trusts, and ICS' plan and prepare for the demand placed on their services. Breakdowns are provided at the Country, Region, ICS, Trust, and Site level. Weekly trends are provided. 

![text](../images/a_and_e_forecasting/weekly_trends.png)

Forecasts are created at the chosen level of granularity (site, region, and so on); and these show expected admissions numbers for the following three weeks. These forecasts come with different levels of specificity, and differing levels of confidence. Users can view different forecasts in this way. For example, the 95% confidence interval forecast makes a less specific prediction than the 50% CI forecast, but as such the predictions made here are more likely to be correct. 
![text](../images/a_and_e_forecasting/forecast.png)

If looking at a higher level of granularity, such as region, a breakdown of constituent locations is shown comparing their forecast admission rates[^1].
![text](../images/a_and_e_forecasting/comparative_forecast.png)


[^1]: Here the different lines correspond to different ICBs within a region. We have intentionally omitted the legend from this example, since the we are aiming to illustrate the functionality of the tool, and not to provide information about particular forecasts at particular site. 

The forecasts themselves are produced using a Hierarchical Linear Bayesian Forecast, based on Monte Carlo Markov Chain modelling techniques. We link to some useful explanatory tools below. 

### Links

Note that the following links are hosted on the Future NHS website, which requires an account and is not open to the general public.

Links|
---|
[User Guide](https://future.nhs.uk/nationaldataplatformfoundry/view?objectID=121110405)|
[Product](https://nhs.sharepoint.com/:w:/r/sites/datasciencerepository/Shared%20Documents/General/03%20Doing%20the%20work/06%20Other/FDP%20Transition/Product%20Documentation%20A%26E%20Admissions%20Forecasting%20Tool.docx?d=w38397884e8a94be89e45bcc338458b99&csf=1&web=1&e=LCbt5S)|
[Prophet Forecasting Repo](https://github.com/facebook/prophet)|
[Accessible lecture on MCMC modelling methods](https://www.youtube.com/watch?v=rZk2FqX2XnY&ab_channel=RichardMcElreath)|


[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)