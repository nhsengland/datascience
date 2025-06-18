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
```