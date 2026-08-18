import pandas as pd

files = [
    "g_patent.tsv",
    "g_inventor_disambiguated.tsv",
    "g_persistent_inventor.tsv",
    "g_cpc_at_issue.tsv"
]

for file in files:
    print("\n" + "=" * 60)
    print(file)

    df = pd.read_csv(
        f"data/{file}",
        sep="\t",
        nrows=5,
        low_memory=False
    )

    print(df.columns.tolist())