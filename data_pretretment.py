import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./Data/CIRAD_Sorghum2023_SPIR_all_2 (4).csv",sep=";")

Control_plantes = data.loc[data["Traitement"]=="RS1",:]
print(Control_plantes)
Control_plantes = Control_plantes.drop_duplicates("ID")
print(Control_plantes)

print(Control_plantes["ID"].describe())

