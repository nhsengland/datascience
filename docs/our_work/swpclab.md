---
title: "South West Primary Care Lab: Artificial Data Generation"
summary: "Creating an artificial longitudinal patient dataset for use in the South West Primary Care Lab for GPs to trial new technologies in an artificial GP environment."
origin: ""
tags: ["GENERATION", "SYNTHETIC DATA", "PYTHON", "PRIMARY CARE"]
---

![An AI generated image of a GP sat in a clinic, with a high number of computer screens showing data on them.](../images/swpclab_visualabstract.png){: style="height:450px;width:700px"}

Often the problem in the NHS is adoption not innovation, something that the South West Primary Care Lab is trying to combat. The South West Primary Care Lab will be an artificial GP surgery currently being built at a university, for GPs to attend to test out how innovative technology (from hypertension management algorithms to ambient voice technology) could impact their every day life to test out the benefits with no real patients or real clinical outcomes to convince them to implement them in their surgeries, or test whether it's even worth pushing to implement them. This project is being run by the South West Trusts Innovation Team, however, in order for it to be possible they need artificial, high fidelity patient data, which is where we come in!

This project is in very early development, and currently we are working on one specific use case: hypertension. We are creating a hypertension focused, clinical data driven dataset that represents a population of patients with hypertension. We are using the [NICE guidelines](https://www.nice.org.uk/guidance/NG136) of hypertension management to inform the processes, as well as working together with clinicians involved in the project. 

To begin, we used the code made by our clinician that used [Faker](https://faker.readthedocs.io/en/master/) to create low fidelity, but realistic-looking data. We then improved upon this with a range of techniques, and are now looking at adapting [Synthea](https://github.com/synthetichealth/synthea) to take in the patient cohort we have created and create longitudinal data, changing its hypertension and hypertension medications modules to be more UK centric and follow the NICE guidelines better. 

## Outputs
As this project is very early in development, we have no public outputs to share yet, but will update this section as they get published. 

| Output                             | Link                                                                 |
| ---------------------------------- | -------------------------------------------------------------------- |
|        |    |


[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
