import pandas as pd

data1 = pd.read_csv("./Data/CIRAD_Sorghum2023_SPIR_all_2.csv",sep=";")
data2 = pd.read_csv("./Data/CIRAD_Sorghum2023_SPIR_all_2 (4).csv",sep=";")

count_id1 = data1["ID"].value_counts().to_dict()
count_id2 = data2["ID"].value_counts().to_dict()

count_id1 = {k: count_id1[k] for k in sorted(count_id1.keys())}
count_id2 = {k: count_id2[k] for k in sorted(count_id2.keys())}

count_id1_keys = set(count_id1.keys())
count_id2_keys = set(count_id2.keys())

missing_in_count_id2 = count_id1_keys - count_id2_keys
missing_in_count_id1 = count_id2_keys - count_id1_keys

print("Keys in count_id1 but not in count_id2:", missing_in_count_id2)
print("Keys in count_id2 but not in count_id1:", missing_in_count_id1)

print(count_id1)
print(count_id2)
print()