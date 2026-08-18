from pathlib import Path
import pandas as pd

DATA = Path("data")

print("Loading Patent...")
patent = pd.read_csv(
    DATA / "g_patent.tsv",
    sep="\t",
    low_memory=False
)

print("Loading Inventor...")
inventor = pd.read_csv(
    DATA / "g_inventor_disambiguated.tsv",
    sep="\t",
    low_memory=False
)

print("Loading Persistent Inventor...")
persistent = pd.read_csv(
    DATA / "g_persistent_inventor.tsv",
    sep="\t",
    low_memory=False
)

print("Loading CPC...")
cpc = pd.read_csv(
    DATA / "g_cpc_at_issue.tsv",
    sep="\t",
    low_memory=False
)

print("Done!")

print(patent.shape)
print(inventor.shape)
print(persistent.shape)
print(cpc.shape)