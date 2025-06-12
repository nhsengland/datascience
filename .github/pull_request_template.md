<!-- 
- Pull request title follows this format "SH NV-1234 Solves this problem":
    - Initials of author
    - associated Jira ticket number
    - brief description
- Choose appropriate labels
- Use the "development" sidebar option to indicate if this closes any open issues, etc.
-->
# Description
<!-- 
In the body of the pull request, provide a description following the "What, Why, How" approach. 

You could also add a gif using the "gifs for GitHub" Chrome extension: https://chrome.google.com/webstore/detail/gifs-for-github/dkgjnpbipbdaoaadbdhpiokaemhlphep/related?hl=en
-->

❓**What**:

🧠**Why?**:

👨‍💻**How?**:

# Checklist:
Have checked for the following:
- [ ] The website still builds correctly, and you can view it using `mkdocs serve`.
- [ ] There are no new "warnings" from mkdocs (see [here](#existing-warnings) for existing warnings you can safely ignore)
- [ ] Does your page follow the [page template](https://nhsdigital.github.io/rap-community-of-practice/example_RAP_CoP_page/) (or [here in Markdown](https://github.com/NHSDigital/rap-community-of-practice/blob/main/docs/example_RAP_CoP_page.md))? (**need to make a new one specific to NHSE Data Science**)
- [ ] Spelling errors
- [ ] Consistent capitalization
- [ ] Consistent numbers
- [ ] Material features incorrectly implemented: search for code blocks and markers (e.g. !!!).
- [ ] Code snippets don't work
- [ ] Images not working
- [ ] Links not working

## Where it was tested
<!-- 
Please describe the test configuration - below is an example.
-->
- Github Codespaces - 2-core, 4GB RAM, 32GB hard drive
- devcontainer.json describes further settings

# Existing Warnings
The following are errors that are already existing in the mkdocs build and that you can safely ignore when creating a PR:
```
INFO    -  The following pages exist in the docs directory, but are not included in the "nav" configuration:
             - what_is_data_science/index.md
             - what_is_data_science/Benefits of Data Science in the NHS.md
             - what_is_data_science/How you can learn Data Science.md
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:primary-care', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:secondary-care', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:social-care', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:emergency-care', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:diseases', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:population-health', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:workforce', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:prescribing', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:financial', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:forecasting', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:classification', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:computer-vision', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:deep-learning', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:llm', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:machine-learning', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:neural-networks', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:nlp', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:linkage', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:simulation', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:best-practice', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:data-validation', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:documentation', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:ethics', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:explainability', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:generation', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:modelling', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:rap', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:research', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:structured-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:unstructured-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:multi-modal', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:audio-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:genomics-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:visual-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:text-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:time-series', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:pii', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:synthetic-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:open-data', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:pseudonymised', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:python', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:sql', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:r', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:webdev', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:wip', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:complete', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:paused', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:in-development', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:retired', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:deployed', but there is no such anchor on this page.
INFO    -  Doc file 'our_work/tags.md' contains a link '#tag:experimental', but there is no such anchor on this page.
```