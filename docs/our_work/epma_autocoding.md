---
title: 'ePMA Auto-Coding'
summary: 'A rule-base data processing pipeline to map free text medication descriptions to SNOMED codes using the dm+d standard.'
origin: ''
tags: ['PYTHON','SECONDARY CARE','PRESCRIBING','TEXT DATA']
---
## The Problem
The ePMA (electronic prescribing and medicine administration) data collection is a person-level data asset containing information on what medication is prescribed and administered in secondary care settings. The ePMA data that hospitals submit contain a number of free text fields including: medication name, dosage, route and frequency. This creates some challenges when aiming to collect and eventually disseminate this data:

1. Free text can potenitally contain PID (patient identifiable data) which is not permitted
2. Free text descriptions of medication makes analysis hard because the same medication could be described in multiple ways 

## Our Solution
The ePMA auto-coding pipeline was created which maps the free text descriptions of medications to valid SNOMED codes using dm+d (dictionary of medicines and devices). The pipeline has a series of deterministic steps as follows (high level view only):

1. Filter submissions - records that have been mapped before or deemed to be unmappable are not run through the pipeline again
2. Preprocessing - convert to lowercase, replace words and punctuation
3. Read data - the input ePMA data with dm+d reference data from VTM (chemical), VMP (product), AMP (branded product)
4. Exact matching - does the input exactly match any of the dm+d reference data?
5. Entity matching - split the medication description into moiety, unit, strength and dose form and attempt to match to dm+d reference data
6. Fuzzy matching* - compare the input against the dm+d reference data using fuzzy logic

*Fuzzy logic is a technique using various distance metrics to find out how different two texts are from one another. In it's simplest form it can compare word to word by how many characters need removing, adding or changing (e.g. the fuzzy matching score between "internationalization" and "internationalisation" is 95.00 because one character needs changing. A score of 100 means the words are identical), this technique helps to pick up spelling mistakes and spelling differences. More complex versions of fuzzy matching allow for sentences to be compared, with options to ignore the order of words, duplicated words and partial matches within a sentence.

![A sankey diagram showing the logical flow of submissions through the pipeline](../images/epma_autocoding/logic_sankey_epma.png)

## Results

A review of the most common prescriptions and adminstrations found:

- 93% correct
- 4% wrong granularity - meaning extra information such as dose and form were provided but autocoding only mapped to the parent level
- 3% incorrect

Granularity:

| Level | Proportion |
|-----|------------|
| Virtual Theraputic Moiety (VTM) | 49.1% |
| Virtual Medicinal Product (VMP) | 42.6% |
| Actual Medicinal Product (AMP) | 8.3% |

General:

- Richer data more useful for analysis and other downstream applications
- Pipeline capable of processing many thousands of records at a time
- Rules are able to be modified when new supplier systems of ePMA data are submitting

Incorrect matches:

Sometimes the autocoding will make a small number of incorrect matches and work is ongoing to improve methodology and minimise these. Where known incorrect matches are discovered, these are excluded from future mappings and will be published as known issues for analysts to be aware of.


## Outputs

| Output                             | Link                                                                 |
| ---------------------------------- | -------------------------------------------------------------------- |
| Published repo | [Github Repo](https://github.com/NHSDigital/medicines-text-mining-tool)|


[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
