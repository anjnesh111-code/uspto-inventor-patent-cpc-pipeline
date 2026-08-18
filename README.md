# USPTO Inventor–Patent–CPC ETL Pipeline

## Overview

This project implements an ETL pipeline for processing USPTO Granted Patent Disambiguated Data.

The objective is to create an inventor-level dataset containing:

1. Inventor name
2. List of associated patents
3. List of CPC classes associated with those patents

The project was developed as a data analysis/research exercise using USPTO bulk patent datasets.

## Data Sources

The pipeline uses the following USPTO bulk datasets:

- `g_patent.tsv`
- `g_inventor_disambiguated.tsv`
- `g_persistent_inventor.tsv`
- `g_cpc_at_issue.tsv`

The raw USPTO datasets are intentionally excluded from this repository because of their large size.

## ETL Pipeline

```text
USPTO Bulk Datasets
        │
        ▼
Data Loading
        │
        ▼
Patent–Inventor Relationships
        │
        ▼
Patent Information
        │
        ▼
CPC Classification
        │
        ▼
Relational Joins using Patent IDs
        │
        ▼
Aggregation by Inventor
        │
        ▼
Inventor-Level Output
