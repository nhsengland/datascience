# 👨‍💻 Coding Quality

INLINE

*High-quality, maintainable code is essential for reproducibility, efficiency, and collaboration. Coding standards, version control, documentation, and testing ensure robust analytical outputs.*

**Success Criteria**: Code is maintainable, efficient, well-documented, version-controlled, and subject to appropriate testing.

* **RED:** Little to no coding standards in place, minimal or no version control usage, lack of peer code reviews or testing. The codebase is unstructured and undocumented making it hard to maintain, reproduce or review.
* **AMBER:** Some coding practices are applied, but documentation, testing, or review processes are partially implemented or inconsistent. Version control might be used, but not systematically, and there is limited collaboration.
* **GREEN:** An agreed coding style is consistently used. Effective version control, automated tests, peer reviews on all critical code.
* **NA:** Only where project involves no coding.

## Good Practice Guidance

| MSC | Good Practice |
| --- | --- |
| MUST | * Review: [Peer review](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/workflow/code-review/) critical code to identify bugs early and ensure consistency. |
| SHOULD | * Use a consistent coding style: Adhere to agreed-upon conventions (e.g PEP8, [style guide for Pyspark](https://nhsdigital.github.io/rap-community-of-practice/training_resources/pyspark/pyspark-style-guide/), [Coding Standards (FDP) - Data Science](https://nhsd-confluence.digital.nhs.uk/pages/viewpage.action?pageId=917487909)), naming standards, and file structures. |
| SHOULD | * Code is version controlled (see [Git basics](https://nhsdigital.github.io/rap-community-of-practice/training_resources/git/introduction-to-git/) and [using Git collaboratively](https://nhsdigital.github.io/rap-community-of-practice/training_resources/git/using-git-collaboratively/) guides).   + Commit changes frequently and use branches for new features.   + Document major changes or releases so users can track updates over time. |
| SHOULD | * Write tests and automate: Include unit, integration, and (where relevant) performance tests.   Particularly important where code will execute unsupervised (e.g. as part of a scheduled pipeline) and/or on a platform where environmental conditions or dependencies may change outside the control of the project team. |
| SHOULD | * Document thoroughly: Maintain clear code comments, [docstrings](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/python-functions/#documentation), README files, and usage instructions so others can understand and reproduce your work.    + Provide environment details (e.g., requirements.txt, environment.yml) so work can be easily replicated.   + Specify a standard directory layout—this makes navigation easier and improves consistency across multiple projects. |
| SHOULD | * Integrate logging or checkpointing to detect issues early and confirm outputs are as expected. |
| SHOULD | * Reuse and collaborate: Encourage looking for existing libraries or code from internal/external teams to enhance efficiency and avoid redundant development efforts. |
| SHOULD | * Open publication: Where feasible, [publish code](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/publishing_code/how-to-publish-your-code-in-the-open/) in the open (e.g., GitHub) and link from associated outputs or publications. |
| COULD | * Take steps to make your code discoverable by others:   + Consider packaging any newly developed functions as reusable libraries (or contributing them to existing ones).   + Apply helpful metadata (e.g., GitHub Topics) |
| COULD | * Optimize and scale: Keep performance in mind when processing large datasets; consider memory and runtime efficiency. |
| COULD | * Configure pipelines to run automatically based on schedules or events (e.g., new data arrival). |
| COULD | * Reusability in mind: Automate data ingestion and output generation wherever possible to reduce human error. |
| COULD | * Convert frequently used scripts into installable packages or libraries for consistent deployment. |
| COULD | * Configure pipelines to run automatically based on schedules or events (e.g., new data arrival). |