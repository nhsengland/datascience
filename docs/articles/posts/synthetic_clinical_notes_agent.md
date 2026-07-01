---
title: From synthetic clinical notes to a simple agent, in a few hours
authors: [ChaeyoonKimNHSE]
date: 2026-06-28
categories:
    - Synthetic Data
    - LLM
    - Generative AI
    - Python
links:
    - NHS guidance for redaction: https://www.england.nhs.uk/long-read/redacting-information-for-online-record-access/
    - Claude written Codes to pull down synthetic clinical notes: https://github.com/chaeyoonyunakim/noteguard-agent/blob/main/src/fetch_dataset.py
    - Claude written Codes for an agent graph: https://github.com/chaeyoonyunakim/noteguard-agent/blob/main/agent/graph.py
slug: synthetic_clinical_notes_agent
description: >
    This article introduces an application of the [team's synthetic clinical notes dataset](https://huggingface.co/datasets/NHSEDataScience/synthetic_clinical_notes), published on Hugging Face. It is a very small agent example, built on purpose to demonstrate the open-source LangGraph framework and to show how little it takes to get started.
---

> This article introduces an application of the [team's synthetic clinical notes dataset](https://huggingface.co/datasets/NHSEDataScience/synthetic_clinical_notes), published on Hugging Face. It is a very small agent example, built on purpose to demonstrate the open-source LangGraph framework and to show how little it takes to get started.

<!-- more -->

The motivation was the team's synthetic data publication.

> Check out information in the [previous post](https://nhsengland.github.io/datascience/articles/2026/04/09/synthetic_clinical_notes/).

I'd thought it might be helpful to introduce how I went from synthetic clinical notes to a simple agent, in a few hours.


### The agent
![Image](../images/blogs_images/synthetic_clinical_notes_agent/9c01aafc-4a11-4564-b816-18b630b1208f.png)


The example I built is deliberately small.

A single straightforward workflow. No branching nodes. No loops.


It only gets to grips with the open-source [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) framework along the way.

```{python}
g = StateGraph(State)
    g.add_node("deidentify_in", deidentify_in)
    g.add_node("agent", run_agent)
    g.add_node("reidentify_out", reidentify_out)
    g.add_node("compute_trust", compute_trust)
    g.add_edge(START, "deidentify_in")
    g.add_edge("deidentify_in", "agent")
    g.add_edge("agent", "reidentify_out")
    g.add_edge("reidentify_out", "compute_trust")
    g.add_edge("compute_trust", END)
    return g.compile()
```

`deidentify_in` redacts PII*, using `[TYPE]` tags like `[NAME]` or `[NHS number]`.

`agent` drafts the summary.

`reidentify_out` restores the PII at the end.

`compute_trust` sits in to evaluate the records what was removed.

*Please be reassured that Personally Identifiable Information (PII) are taken only from the [team's synthetic clinical notes dataset](https://huggingface.co/datasets/NHSEDataScience/synthetic_clinical_notes) in this example.




The de-identification is ordinary.

No patient data leaves NHS. Rules strictly applies to ML/AI Engineering too.

In this example, I've chosen redaction (see [details](https://www.england.nhs.uk/long-read/redacting-information-for-online-record-access/)) for de-identifying the information what can then feed to Gen AI and LLMs.

My go-to model `gemini-2.0-flash` drafts compact eDischarge card based on NICE/NHS guidance that are pulled via Tavily.

This is a LangGraph ReAct agent (Gemini + Tavily) wrapped so the model and tools only ever see de-identified text, therefore real identifiers are restored only in the final clinician-facing answer.


```
messy NHS note  ──►  NoteGuard de-id  ──►  de-identified text
(synthetic)           (NHS-aware rules       + identifiers removed count
                       + vault from CSV)     + residual leakage %
                                │
                  Tavily (NICE/NHS guidance) ──►│
                                                ▼
                                         Gemini drafts
                                         compact eDischarge card
                                         (sees ONLY de-identified text)
                                                │
                         NoteGuard re-id  ◄─────┘
                         (surrogates → real names, clinician only)
                                │
                         Trust panel:
                         leakage % · identifiers removed
                         leaked tokens · faithfulness · sources
```

A practical tip if you try it: decide what travels between nodes first. Almost every bug I hit was a state-shape disagreement, not a logic error.

For a prototype, I designed the structure of the graph can carry a guarantee that a script only carries by convention. The `deidentify_in` is the only door into the rest of the graph as shown in the sample. It is, however, on the limitation as a few hours job that de-identification is not perfectly done. So there is some leaks downstream runs and later node has receive some identifier; which should be addressed in future developments in case someone found it interested in.


### Why I'm sharing it?
Vibe coding was not taking long enough for me to learn. But I found that spending a few focused hours vibe on an open dataset with a framework is genuinely giving much foods for thoughts. If you have heard about agents but not yet tried building your own, the synthetic notes are ready and risk-free place to start experimenting tools on top. My code for today's experiments is public, open to all feedback.
