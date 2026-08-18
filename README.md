# USPTO Inventor–Patent–CPC ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline for processing USPTO PatentsView Granted Patent Disambiguated Data.

The objective is to transform large-scale USPTO patent datasets into an inventor-level dataset containing:

1. Inventor name
2. List of patents associated with the inventor
3. List of CPC (Cooperative Patent Classification) classes associated with those patents

The project was developed as a data analysis and research exercise involving large-scale relational data processing.

---

## Problem Statement

The USPTO bulk patent datasets contain information distributed across multiple relational tables. Information about inventors, patents, and CPC classifications must therefore be integrated using appropriate identifiers.

The required output has three columns:

| Column | Description |
|---|---|
| Inventor Name | Name of the inventor |
| Patent List | List of patents associated with the inventor |
| CPC Classes | CPC classifications associated with the inventor's patents |

The main challenge is to efficiently integrate the relevant USPTO datasets and aggregate millions of patent-level records into an inventor-level representation.

---

## Data Source

The project uses the USPTO PatentsView Granted Patent Disambiguated Data available through the USPTO Bulk Data Directory.

The relevant datasets used in the processing pipeline are:

- `g_patent.tsv`
- `g_inventor_disambiguated.tsv`
- `g_persistent_inventor.tsv`
- `g_cpc_at_issue.tsv`

The datasets cover granted patents and associated inventor and classification information.

The raw USPTO datasets are intentionally **not included in this repository** because of their very large size.

---

## ETL Pipeline

The overall processing workflow is:

```text
USPTO Bulk Data
       |
       v
Data Extraction
       |
       v
Dataset Inspection
       |
       v
Inventor–Patent Relationship
       |
       v
Patent Information
       |
       v
CPC Classification Information
       |
       v
Relational Joins Using Patent IDs
       |
       v
Data Transformation
       |
       v
Aggregation by Inventor
       |
       v
Final Inventor-Level Dataset
```

1. Extract

The required USPTO TSV datasets are obtained from the official USPTO bulk data source.

The pipeline processes the data programmatically rather than relying on spreadsheet software, allowing the workflow to scale to millions of records.

2. Transform

The relevant inventor, patent, and CPC classification information is integrated using patent identifiers.

The transformation process includes:

Reading the required USPTO datasets
Inspecting dataset schemas and columns
Establishing inventor–patent relationships
Connecting patents with their CPC classifications
Joining the relational datasets using patent IDs
Aggregating patents associated with each inventor
Aggregating CPC classes associated with those patents
Producing an inventor-level representation
3. Load

The transformed data is written to the final output dataset.

Each row represents an inventor and contains the corresponding patent list and CPC classification list.

Final Output

The complete processing run produced approximately 4.16 million inventor records.

The final dataset contains three primary columns:

```file Column	Description
Inventor Name	Disambiguated inventor name
Patent List	Associated patent identifiers
CPC Classes	CPC classifications associated with the inventor's patents
```

A compressed version of the complete output was generated separately because of its large size.

The complete output is not stored directly in this GitHub repository.

```file Repository Structure
USPTO/
│
├── .gitignore
├── README.md
├── check_columns.py
├── etl.py
├── pipeline.py
├── test.py
└── LICENSE
File Descriptions
check_columns.py
```
Utility script used to inspect the structure, columns, and schema of the USPTO datasets before processing.

etl.py

Contains ETL-related data processing operations used to extract, transform, and integrate the relevant patent data.

pipeline.py

Main pipeline implementation responsible for processing the datasets and generating the inventor-level output.

test.py

Contains testing and validation code used during development to verify the processing workflow and output.

.gitignore

Prevents large USPTO datasets, generated outputs, Python cache files, and other non-source artifacts from being committed to the repository.

```file Technologies
Python
Pandas
USPTO PatentsView Bulk Data
ETL
Data Integration
Relational Data Processing
Large-Scale Data Processing
Reproducibility
```
The raw USPTO datasets are not included in this repository because of their large file sizes.

To reproduce the analysis:

Step 1 — Obtain the USPTO datasets

Download the required USPTO PatentsView Granted Patent Disambiguated Data files:

g_patent.tsv
g_inventor_disambiguated.tsv
g_persistent_inventor.tsv
g_cpc_at_issue.tsv
Step 2 — Prepare the local data directory

Place the extracted USPTO TSV files in the appropriate local data directory expected by the pipeline.

Step 3 — Install dependencies

Install the required Python dependencies:

pip install -r requirements.txt
Step 4 — Inspect the datasets

Run:

python check_columns.py

This can be used to inspect the available fields and verify the input data structure.

Step 5 — Run the ETL pipeline

Run the main processing script:

python pipeline.py

The pipeline processes the USPTO data and generates the inventor-level output.

Data Processing Considerations

The USPTO datasets are large-scale relational datasets. Loading and processing the complete data therefore requires substantially more resources than a typical tabular data analysis project.

The pipeline is designed to process the data programmatically and avoid manual spreadsheet-based processing.

The raw datasets and complete generated output are excluded from version control to keep the repository lightweight and reproducible.

Validation

Validation was performed during development to ensure that:

The expected dataset columns were available.
Inventor and patent relationships could be established.
Patent identifiers could be used to connect patent and CPC information.
The transformation pipeline generated inventor-level records.
The final output contained the requested inventor, patent, and CPC information.
Project Outcome

The completed pipeline successfully processed the USPTO bulk patent datasets and generated an inventor-level dataset containing approximately 4.16 million inventor records.

The resulting dataset provides a structured representation of the relationship between:

Inventor
   |
   +---- Patent 1 ---- CPC Class(es)
   |
   +---- Patent 2 ---- CPC Class(es)
   |
   +---- Patent 3 ---- CPC Class(es)
   |
   +---- ...

This structure can be useful for downstream research involving:

Patent portfolios
Inventor productivity
Technology classification
Innovation research
Inventor networks
Knowledge structures
Technology and innovation analysis
Disclaimer

This repository contains code and documentation for processing publicly available USPTO patent data.

The raw USPTO datasets are not redistributed in this repository because of their size. Users should obtain the source datasets directly from the USPTO and comply with the applicable data-use terms.

Author
Anjnesh Singh Tomar
GitHub: https://github.com/anjnesh111-code
