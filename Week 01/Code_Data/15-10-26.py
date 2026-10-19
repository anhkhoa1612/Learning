import pandas as pd

df = pd.read_csv("baidautien.csv")

df["Population"] = pd.to_numeric(df["Population"], errors="coerce")
df["Area KM2"] = pd.to_numeric(df["Area KM2"], errors="coerce")
df = df.dropna(subset=["Country", "Population", "Area KM2"])

a  = 0
km = {}
pp = {}

for _, row in df.iterrows():
    i = row["Country"]
    pp[i] = pp.get(i, 0) + row["Population"]
    km[i] = km.get(i, 0) + row["Area KM2"]
km = sorted(km.items(), key = lambda x: x[1], reverse = True)
pp = sorted(pp.items(), key = lambda x: x[1], reverse = True)

for i, j in km[:20]:
    for k, v in pp[:20]:
        if k == i:
            print(i)
top_pp = {i for i, j in pp[:20]}
top_km = {i for i, j in km[:20]}

#in ra các quốc gia trong top 20 cả về diện tích lẫn dân số








