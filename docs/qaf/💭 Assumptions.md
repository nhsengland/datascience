# 💭 Assumptions

_Recording and validating assumptions ensures transparency about limitations and dependencies, allowing them to be tested and challenged._

**Success Criteria:** All critical assumptions are recorded, validated, and open to stakeholder challenge.

- **RED:** Assumptions supporting the analysis are not recorded or validated. There is no opportunity for stakeholders to challenge these assumptions.
- **AMBER:** Some assumptions are recorded but critical assumptions are missing or not validated or not made sufficiently visible.
- **GREEN:** All critical assumptions recorded and robustly validated. Stakeholders have sight of these and potential impacts on outputs are well understood.

# Good Practice

| MSC    | Good Practice                                                                                                                                                                                            |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST   | \* Critical assumptions supporting the analysis are recorded - including relating to Data, Methodology, User Requirements, Future Use, Legality/Ethics/Fairness.                                         |
| MUST   | \* Assumptions most likely to impact on outputs / subsequent decision making are prioritised for validation.                                                                                             |
| MUST   | \* The strengths and limitations of the project’s outputs and potential impact of any assumptions are clearly explained and understood by the product owner or any users, as required.                   |
| MUST   | \* There is a culture of calling out assumptions and ensuring they are logged and/or evidenced appropriately - recognising that making assumptions is a necessary part of any modelling / analysis work. |
| MUST   | \* If the project is supporting decision-making, there is an up to date [Assumptions Log](./guidance/Assumptions%20Log%20Guide.md).                                                                      |
| SHOULD | \* There are regular opportunities for stakeholders to challenge whether the assumptions seem appropriate.                                                                                               |

### Supporting guidance:

[Assumptions Log Guide](./guidance/Assumptions%20Log%20Guide.md)

# Learning from experience

The CPAS project used an assumptions log to record assumptions made during the life cycle of the project. This was a test case, and there were lessons learned. The main lessons are:

- **Keep on top of the log**. Any assumption made relating to a project's direction, a choice of technique, data cleansing, feature engineering etc. should be logged as soon as it arises and becomes part of the project fabric.
- **Populate extensively at the start** and update frequently. Many assumptions will be known off the bat. Log them and update them as testing the assumption progresses.
- Assumptions can be made at any stage of a project. **Log them as they arise** and don't assume everything was captured at the start (well, that's one less assumption to log...!).
- Be succinct and precise in stating the assumption. For example; "Any patients without a hospital leaving date were assumed to be still in hospital, for all hospitals" is fine, assuming that there is good reason to believe this. The statement is **clear, precise and specific**.
- The above assumption is a testable assumption- records can be cross referenced, SMEs can be consulted etc. **Document any evidence** to bolster the assumption.
- If an assumption is proven beyond reasonable doubt, **keep it** in the assumption log and document the evidence. When somebody asks later on "why have you done this?" or "this doesn't seem right, did you check it?", you will have the evidence required to support your framework.
- The assumptions log is not a place for verbose evidence. Provide the evidence in confluence, a document, a notebook or similar. **Link** the evidence to the log.
