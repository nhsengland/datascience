---
layout: base
title: Investigating Applying and Evaluating a Language Model to Patient Safety Data
permalink: p33_patientsafetylms.html
summary: What's the most suitable models and workflows for representing an NHS text dataset?
tags: ['NATURAL LANGUAGE PROCESSING', 'LLM', 'RESEARCH', 'UNSTRUCTURED DATA', 'TEXT DATA', 'PYTHON', 'COMPLETE', 'EXPERIMENTAL']
---

In collaboration with the NHS England patient safety data team, we present an exploration of a selection of different language model pretraining and finetuning objectives with patient safety incident reports as the domain of interest, followed by a discussion of a number of methods for probing and evaluating these new models, and their respective embedding spaces.

## Results

Results showed that the models trained on the patient safety incident reports using either the Masked Language Model (MLM) objective, or the MLM plus contrastive loss objective, appeared to have a superior performance on the presented pseudo-tasks when compared to their general domain equivalent. Whilst the performance in the frozen setting did not match that of the full fine-tuned setting, we have not performed a thorough investigation, for instance we could look to utilising larger base models. Further there are other examples of promising approaches which can better utilise frozen language models at scale, such as prompt learning and parameter efficient fine-tuning.

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [Github](https://github.com/nhsx/ELM4PSIR) |
| Case Study | Awaiting Sign-Off |
| Technical report | [Here](https://github.com/nhsx/ELM4PSIR/blob/main/reports/ELM4PSIR_NT_v1.1.pdf) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
