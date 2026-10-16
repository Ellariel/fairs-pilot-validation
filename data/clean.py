import os
import glob
import numpy as np
import pandas as pd


base_dir = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(base_dir, "..", "data"))


def q(s, data):
    ret = []
    if isinstance(s, list):
        for i in s:
            j = q(i, data)
            if pd.notna(j):
                ret += [j]
        return ret
    for i in data.columns:
        if i.startswith(s):
            return i
    return s


results = glob.glob(os.path.join(data_dir, "*.csv"))
data = pd.DataFrame()
for r in results:
    if "cleaned" not in r and "filtered" not in r:
        data = pd.concat([data, pd.read_csv(r)])
data.columns = [f"q{idx + 1:0>2}-{i[:200]}" for idx, i in enumerate(data.columns)]
data.reset_index(drop=True, inplace=True)
print(f"Number of rows in raw data: {len(data)}")

min_filter = q(list(set(["q14", "q15", "q17", "q18"])), data)
data = data.dropna(subset=min_filter, how="all")

qs = ["q19", "q22", "q23"]
qq = q(qs, data)
f1 = (data[qq] >= 3).astype(int).sum(1) > 0
qs = ["q14", "q15"]
qq = q(qs, data)
f2 = (
    data[qq]
    .map(
        lambda x: (
            np.nan if x == "Less than 5" or x == "Master's" or x == "Bachelor's" else x
        )
    )
    .map(pd.notna)
    .astype(int)
    .sum(1)
    > 0
)
qs = ["q17", "q18"]
qq = q(qs, data)
f3 = (
    data[qq]
    .apply(lambda x: x.fillna("").str.startswith("Extensive"), axis=1)
    .astype(int)
    .sum(1)
    > 0
)
filtered_data = data[(f1 | f2) & f3].copy()
filtered_data.to_csv(os.path.join(data_dir, "filtered_data.csv"), index=False)
print(f"Number of rows in filtered data: {len(filtered_data)}")

cleaned = q(
    list(
        set(
            ["q09", "q10", "q11", "q12", "q13"]
            + ["q14", "q15", "q16"]
            + ["q17", "q18"]
            + ["q19", "q20", "q21", "q22", "q23"]
            + ["q44", "q45", "q52", "q55"]
            + ["q63", "q64", "q65"]
            + ["q56", "q57", "q58"]
            + ["q68", "q69", "q70", "q71", "q72"]
            + ["q27", "q28"]
            + ["q29", "q30", "q31", "q32", "q33", "q34", "q35", "q36"]
        )
    ),
    data,
)

df1 = filtered_data[cleaned].copy()
df1["----Selected_expert"] = 1
df2 = data[cleaned].copy()
df2 = df2[~df2.index.isin(df1.index)]
df2 = df2[pd.notna(df2[q("q19", data)])].copy()
df2["----Selected_expert"] = 0
print(f"Selected experts: {len(df1)}, Non-selected experts: {len(df2)}")
df = pd.concat([df1, df2], ignore_index=True)
df.columns = [i[4:] for i in df.columns]
df = df[sorted(df.columns)]
df = df.sort_values("Selected_expert", ascending=False)

df.columns = [
    i.replace("\xa0", " ")
    .replace("\n", " ")
    .replace("  ", " ")
    .replace("  ", " ")
    .strip()
    for i in df.columns
]

df.to_csv(os.path.join(data_dir, "cleaned_data.csv"), index=False)
