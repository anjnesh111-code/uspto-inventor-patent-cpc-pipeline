with open("output/inventor_patents_cpc.csv", "r", encoding="utf-8") as f:
    print(sum(1 for _ in f) - 1)