import polars as pl

inventor = (
    pl.scan_csv(
        "data/g_inventor_disambiguated.tsv",
        separator="\t",
        infer_schema_length=0,
        quote_char='"'
    )
    .with_columns(
        pl.col("patent_id").cast(pl.Utf8)
    )
    .select([
        "patent_id",
        "inventor_id",
        "disambig_inventor_name_first",
        "disambig_inventor_name_last"
    ])
)

cpc = (
    pl.scan_csv(
        "data/g_cpc_at_issue.tsv",
        separator="\t",
        infer_schema_length=0,
        quote_char='"'
    )
    .with_columns([
        pl.col("patent_id").cast(pl.Utf8),

pl.col("cpc_subclass").alias("cpc_code")
    ])
    .select([
        "patent_id",
        "cpc_code"
    ]))

print("Schemas loaded successfully!")
joined = inventor.join(
    cpc,
    on="patent_id",
    how="left"
)

print("Join created!")

# Aggregate

result = (
    joined
    .with_columns(
        (
            pl.col("disambig_inventor_name_first").fill_null("") +
            pl.lit(" ") +
            pl.col("disambig_inventor_name_last").fill_null("")
        ).str.strip_chars().alias("inventor_name")
    )
    .group_by([
    "inventor_name"
])
    .agg([
        pl.col("patent_id").unique().sort().alias("patents"),
        pl.col("cpc_code").drop_nulls().unique().sort().alias("cpc_classes")
    ])
)

# output

print(result.explain())

print("Collecting results...")

final = result.collect(engine="streaming")

print(final.head())

# Convert list columns to string columns
final = final.with_columns([
    pl.col("patents").list.join("; ").alias("patents"),
    pl.col("cpc_classes").list.join("; ").alias("cpc_classes"),
])

# Rename columns
final = final.rename({
    "inventor_name": "Inventor Name",
    "patents": "Patent IDs",
    "cpc_classes": "CPC Classes"
})
print(final.schema)   # <-- Check datatypes

from pathlib import Path
Path("output").mkdir(exist_ok=True)

final.write_csv("output/inventor_patents_cpc.csv")

print("Done!")