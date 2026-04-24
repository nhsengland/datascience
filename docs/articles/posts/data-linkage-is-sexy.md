---
title: "Data linkage: the quiet science holding everything together"
authors: [GiuliaMantovani]
date: 2026-04-24
categories:
    - linkage
    - architecture
    - governance
slug: data-linkage-is-sexy
description: >
    It doesn’t usually involve flashy dashboards, cutting‑edge models, or neat Kaggle-style problems. It sits behind the scenes, often unnoticed, quietly doing its job. And yet, without data linkage, much of the data we rely on across NHS England, whether for analysis, planning, research, or direct care, would simply fall apart.
---

Data linkage is complex, foundational work. It requires statistical rigour, technical depth, and strong governance, and it underpins how the rest of the organisation uses and trusts data.

---

## What does a data linker actually do?

Being a data linker is not a single, neatly defined role. It sits at the intersection of many disciplines:

- **Data science**, for probabilistic matching, bias assessment, quality metrics, and uncertainty  
- **Data engineering**, for scalable pipelines, performance, and reproducibility  
- **Data architecture**, for designing consistent, reusable, and interoperable services  
- **Information governance and assurance**, for ensuring lawful, ethical, and transparent use of data  
- **Technology and solution design**, often working closely with solution architects on complex, distributed systems  

A data linker is rarely only one of these things. At the same time, they are not fully any one of them either. The role exists at the edges, bridging disciplines that don’t always naturally meet.

---

## The invisible foundation

Most analysts, clinicians, and patients never “see” data linkage directly.

They see:

- A longitudinal patient record  
- A coherent dataset spanning multiple services  
- A dashboard where figures line up and make sense  
- Analytical outputs that can be trusted and reproduced  

What they don’t see is the work needed to reconcile slightly inconsistent identifiers, different naming conventions, missing values, changing structures, or historical system quirks. Data linkage quietly absorbs that complexity so others don’t have to.

Because it works best when it’s invisible, it’s also easy to underestimate.

---

## What if we unplugged data linkage?

A useful thought experiment is to imagine what would happen if we turned data linkage off tomorrow.

Suddenly:

- Datasets that were previously joined no longer align  
- Trends break because entities cannot be followed over time  
- Population-level analyses fragment into partial views  
- Local and national reporting drift out of sync  
- Trust in analytical outputs erodes  

This isn’t to say that other technologies are not equally critical, many would produce similarly dramatic effects if removed. But the exercise helps frame just how foundational data linkage really is, despite often sitting at the fringes of established professions.

---

## A day in the life of a data linker

On any given day, the role might look something like this.

It starts with checking in with the team, understanding what moved, what broke, and what improved overnight.

Then a conversation with data engineers:

> “Oh really, the pipeline now runs in under ten minutes for half a million records? That’s fantastic. And thanks for salting the gender variable.”

A chat with an assurer:

> “That test record should definitely have returned a non‑match. Let’s walk through what happened there.”

Working alongside data scientists:

> “If we introduce this alternative phonetic encoding, we could reduce bias against naming conventions that don’t follow standard English patterns.”

Pushing forward a DPIA with IG colleagues:

> “Thank you for raising that concern, we’ll make sure it is explicitly reflected in our governance when reconciling and integrating these sources.”

A discussion with a solution architect:

> “So if we expose a connector from this platform to that system, we could provide a consistent service to all local trusts? That’s exactly what we need.”

And occasionally, a conversation with academic partners:

> “That’s a great idea, we can explore adding improved quality metrics to the linked outputs so downstream analyses are easier to trust.”

None of these conversations sit neatly within a single discipline. All of them are essential.

---

## Why this matters

Data linkage may not always get the spotlight, but it enables nearly everything that follows: analysis, insight, planning, research, and ultimately better decision‑making.

It demands technical skill, statistical thinking, architectural awareness, and a deep respect for governance and ethics. It requires people who are comfortable operating in the spaces between roles, translating across communities, and holding complexity so others don’t have to.

And that’s exactly why data linkage is sexy.

<img width="1024" height="1024" alt="Image" src="https://github.com/user-attachments/assets/1acb09f6-9848-4e83-9415-40afae7f9688" />
