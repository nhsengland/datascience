---
title: "Developing Artificial Priamry Care Records"
summary: "Creating an artificial longitudinal patient dataset for GPs to trial new technologies in an artificial GP environment."
category: "Playbook"
origin: ""
tags: ["GENERATION","SYNTHETIC DATA","PYTHON","PRIMARY CARE"]
---

Primary care records are crucial for understanding healthcare interactions at both the population and individual levels. However, these records are difficult to obtain and integrate with other services, hindering innovation due to data unavailability and privacy concerns.

Our project aims to address this by developing a code base to generate primary care electronic health records. We start by creating a synthetic population that mirrors a region in England, and then adapt the US-based tool [Synthea](https://github.com/synthetichealth/synthea) for the English NHS context.

![](../images/swpc_simple.png)
<p align="left">
    <em>Figure 1: High-level schematic of the different components of the project. Population level relationships are derived from the raw data and feed through a simple synthetic data generator to create a population. Clinical knowledge is captured as a clinical reference pathway (CRP) and fed into the engine. This engine takes the syntehtic population and processes them through the CRPs. This results in records being created and adapted for the syntehtic individuals which can then be viewed at a patient (EHR), service (GP system) or System (regional) levels.</em>
</p>


Project Overview Task 1: Creating a Synthetic Population with Faker We begin by generating a table of fake but realistic individuals using the [Faker](https://faker.readthedocs.io/en/master/) library, based on demographic profiles and disease prevalence probabilities. These records are validated against the OneDevon dataset to ensure accuracy and privacy.

Task 2: Digitizing Clinical Pathways To simulate real-world patient interactions, we translate clinical knowledge into digital formats. Using Synthea's graphical interface, we create JSON files representing clinical pathways, starting with the Hypertension module. This involves adapting US modules to match English drug names, values, and logic starting by aligning to the [NICE guidelines](https://www.nice.org.uk/guidance/NG136).

Task 3: Customizing Synthea for the English NHS Whilst the adaption of [synthea for international](https://github.com/synthetichealth/synthea-international) contexts is well established in their site, this results in records which still have many US elements. Adapting Synthea for the English NHS involves removing obsolete US elements like insurance logic and updating regional specifics such as town names and vaccination schedules. We are progressively modifying demographic, geographic, and societal health determinants to fit the English context.

<details class="nhsuk-details nhsuk-expander">
    <summary class="nhsuk-details__summary">
      <span class="nhsuk-details__summary-text">
        Details of Synthea Adaption
      </span>
    </summary>
    <div class="nhsuk-details__text">
      <p>Stage 1: Removing non-English NHS functions and simplifying the Java to a MVP</p>
        <ul>
            <li>Functions relating to Flexporter (functionality which could be brought back later)</li>
            <li>Functions relating to Payers and related managers</li>
            <li>Functions relating to Insurance plans</li>
            <li>Functions relating to Claims (mostly for medications)</li>
            <li>Functions relating to income, healthcare expenses and coverage</li>
            <li>Functions relating to Cost</li>
            <li>Functions relating to exporting as DSTU2 or STU3</li>
            <li>Functions relating to the Cardiovascular diseease module (as this is an US-based calculator)</li>
            <li>Functions relating to the ASCVD, Framingam and C19 Immunizations (as these are all US-based and not applicable)</li>
            <li>Functions relating to the CMSStateCodeMapper</li>
        </ul>
      <p>These funtions have all been commented using a `UKAdp` tag to keep an audit trail.   These adaptions results in 113 sections of code commented out across 16 files (all within then `src/main/java/org/mitre/synthea/`).</p>
    </div>
    <div class="nhsuk-details__text">
      <p>Stage 2: Adapting Resource files for UK South West Region context</p>
        <ul>
            <li>Replace demographics.csv with South West towns</li>
            <li>Replace fipscodes.csv with ??</li>
            <li>Update social determinants of health (sdoh.csv) file with ??</li>
            <li>Replace timezones.csv with GMT</li>
            <li>Replace zipcodes.csv with uk based postcodes</li>
            <li>Keep birthweights.csv as US version (for the moment)</li>
            <li>Keep bmi_correlations.json as US version (for the moment)</li>
            <li>Keep cdc_growth_charts.json as US version (for the moment)</li>
            <li>Keep gbd_disability_weigths.csv as US version (for the moment)</li>
            <li>Update immunization_scheldule.json to ??</li>
            <li>Update synthea.properties to remove unused exporter and payer functionality and ammend inputs for South West Region.   In addition reduce the care settings down to hospitals, priamry_care and urgent_care.</li>
        </ul>
      <p>There are still many US-based nuances that need to be dealt with such as payer columns still appearing in the outputs.</p>
    </div>
        <div class="nhsuk-details__text">
      <p>Stage 3: Nunances</p>
        <ul>
            Coming
        </ul>
      <p>At the end of this stage we aim for a fully UK-base version.</p>
    </div>
</details>

Next Steps Our work is ongoing, with updates available on our GitHub repository. Future plans are outlined in Figure 2, showcasing various potential directions for this project.

Stay tuned for progress updates and check out our code development on GitHub.

![](../images/swpc_complex.png)
<p align="left">
    <em>Figure 2: Potential to expand the tooling in a vairety of ways to increase fidelity of the generated records and include additional modalitieis.</em>
</p>


Output|Link
---|---
Open Source Code & Documentation|[Github](https://github.com/nhsengland/swpc_synthea) - WIP
Case Study| Awaiting Sign-off

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
