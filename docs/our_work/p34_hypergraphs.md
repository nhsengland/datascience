---
layout: base
title: Transforming Healthcare Data With Graph-Based Techniques
permalink: p34_hypergraphs.html
summary: Application of directed hypergraphs for SAIL data bank to investigate disease progression
tags: ['GRAPHS', 'CHARLSON INDEX', 'SAIL DATABANK', 'MULTIMORBIDITY']
---
![Figure 1 form https://www.medrxiv.org/content/10.1101/2023.08.31.23294903v1.full.pdf: Four different types of unweighted, fully connected graph models with 3 nodes. (A) undirected graph, (B) undirected hypergraph, (C) directed graph, (D) directed hypergraph of B-hyperarcs, the only type of hyperarc considered in this work. Dotted lines here represent nodes as part of the tail set in each hyperarc. Edges have been colour coded to help identify children from their parents — looking top-down, we can observe how the directed edges (children) are generated from their corresponding undirected edges (parents). Note also the existence of self-edges in the directed representations.](images/hypergraphs.png)

In this project we explored (directed) hypergraphs as a novel tool for assessing the temporal relationships between coincident diseases, addressing the need for a more accurate representation of multimorbidity. Directed hypergraphs offer a high-order analytical framework that goes beyond the limitations of directed graphs in representing complex relationships. After exploring novel weighting schemes which can capture different aspects of the underlying data, we then turn our attention at the power of these higher-order models through the use of PageRank centrality to detect and classify the temporal nature of conditions. 

## Results
See the associated publication and report for detailed learning around applying these techniques to Charlson indexed data to explore disease progression.  This work then seeded two further PhD Internships exploring the addition of temporal information and alternative graph representations. 

| Output | Link |
| ---- | ---- |
| Open Source Code & Documentation | [github](https://github.com/nhsx/hypergraph-mm) |
| Case Study | Awaiting Sign-Off |
| Technical report | [Report](https://github.com/nhsx/hypergraph-mm/blob/main/reports/Hypergraph_mm_report_JB.pdf) |
| Publication | [Representing Multimordbid Disease Progressions Using Directed Hypergraphs](https://www.medrxiv.org/content/10.1101/2023.08.31.23294903v1) |

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
