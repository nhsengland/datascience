---
layout: base
title: TxtRayAlign
permalink: p22_txtrayalign.html
summary: Generating descriptive text from X-Ray images using contrastive learning on multi-modal data
tags: ['NLP', 'MULTI-MODAL', 'RETRIEVAL', 'DEEP LEARNING', 'PYTHON']
---

![](../images/p22fig1.png)
<p align="left">
    <em>Figure 1: A contrastive retrieval mechanism.   A query image is encoded and compared with the embeddings of a corpus of reference reports.  The report with the greatest cosine similarity in the shared embedding space is returned as the output.</em>
</p>

TxtRayAlign exploits contrastive training to learn similarities between text and images, allowing a retrieval-based mechanism to find reports that are “similar” to an image.

## Results

We observe that even the best performing model (ResNet50-DeCLUTR) only retrieves anything of relevance for 62% of queries. The retrieved sentences tend to contain findings that are not relevant for the query, as indicated by the relatively poor precision. Further, the query image contains findings that are only poorly covered by the retrieved sentences, as indicated by the low recall.

The results of our investigation indicate that this approach can help generate reasonably grammatical and clinically meaningful sentences, yet falls short in achieving this with sufficient accuracy. While improvements to the model could be made, our findings are corroborated by others in literature. Besides improving
performance, future work could develop other applications of TxtRayAlign for other downstream tasks, such as image-to-image or text-to-image retrieval.

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [Github](https://github.com/nhsx/txt-ray-align) |
| Case Study | Awaiting Sign-Off |
| Technical report | [Here](https://github.com/nhsx/txt-ray-align/blob/main/report/TxtRayAlign_Report_DZ.pdf) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
