# 💻 Tools and Environment

INLINE

*Tools and platforms should support efficient, reproducible, and sustainable development, analysis, and delivery.*

**Success Criteria:** Tools and environment are fit for purpose, stable, reproducible, and support best practice.

* **RED:** Tools unsuitable or unstable, preventing good practice
* **AMBER:** Tools adequate but lacking in some key aspects.
* **GREEN:** Tools and environment fully support modern, reproducible development.
* **NA:** Only if project involves no development.

## Good Practice Guidance

| MSC | Good Practice |
| --- | --- |
| MUST | * When setting up a project environment, confirm that it supports:    + **Functional needs** – the concrete features and tools required to build, test, and deliver your model / analysis.   + **Non-functional needs** – the qualities that determine how well the environment works in practice, such as performance, robustness, auditability, and compliance. * Refer to the [checklist](https://nhsd-confluence.digital.nhs.uk/spaces/DAT/pages/1161782786/%F0%9F%92%BB+Tools+and+Environment#id-%F0%9F%92%BBToolsandEnvironment-Checklistfortools%26platformfunctionality) below. |
| MUST | * Members of development team have the required permissions and are able to access and use all platforms / tools that they need. |
| MUST | * Know how to log, track and escalate issues with your development environment. |
| SHOULD | * Plan ahead for the full lifecycle of the project. Anticipate how tooling and platform requirements may evolve over time, from initial exploration through development and into production deployment. Identify any dependencies early and ensure that the necessary capabilities will be in place when needed. * This may involve mapping out a migration path, for example from scratch or prototype environments, to development platforms, and finally to production systems, with appropriate checks and controls at each stage |
| SHOULD | * Identify any dependencies on other teams and the service level agreements (SLAs) governing turnaround times for tool / platform support and/or development. |
| SHOULD | * Utilise platforms that conform to current NHSE / D&A platform and tech strategy (e.g. 'FDP by default') |
| SHOULD | * Prefer tools that are well-supported and commonly used, avoiding reliance on niche skills. |
| SHOULD | * Where incorporating dependencies, prefer use of well-maintained, open-source, and platform-agnostic tools / packages. * Consider platform longevity and whether future migration may be needed. |
| COULD | * Continually review the suitability of your tools and environment through the project lifecycle, optimising where you can and sharing found good practice with other project teams. |

### Checklist for tools & platform functionality

|  |  |
| --- | --- |
| MUST | Tools and platforms must support the following:   * Code development environments that accommodate the tools and languages being adopted. * Delivery of outputs in the required formats and locations. * Connection to required data sources. * Adequate memory, storage, and compute for all stages of the project. * Implementation of agreed coding standards. * Collaborative development, including pair programming, peer review, and shared environments to enable parallel working on the code base. * Testing and debugging without risk of impacting production systems. * Management of packages, dependencies, and environments, ensuring reproducibility and stability across development and production. * Transition from prototyping to production-quality code (e.g. moving from notebooks to tested, version-controlled scripts). * Secure handling of data and credentials. |
| SHOULD | Tools and platforms should support the following:   * Modern code development practices, ideally including tools such as LLM code assistants or copilots. * Automated enforcement of coding standards, using tools such as autocomplete, linters, and integrated testing frameworks. * Reproducibility, transparency, and automation, for example via public or internal Git repositories, RAP (Reproducible Analytical Pipelines) standards, and support for pipelines, scheduled jobs, triggers, and alerts. * Robust testing practices, including unit testing, integration testing, test data management, and automated test execution as part of CI/CD pipelines. * Collaboration features such as code review, version control workflows, and integrated documentation. * Monitoring and observability, including tools to track performance, detect errors, and support ongoing maintenance. |

### Further resources

Further guidance on environment configuration is available in the Government Analysis Function’s ‘Duck Book’:

* [High-level checklist](https://best-practice-and-impact.github.io/qa-of-code-guidance/checklists.html)
* [Detailed configuration guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/configuration.html)