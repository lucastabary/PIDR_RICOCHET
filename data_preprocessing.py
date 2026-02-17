import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def standardize_dates(df):
    df["Date_Floraison"] = pd.to_datetime(df["Date_Floraison"], format="%d/%m/%Y")

    df['Date_SPIR'] = df['Date_SPIR'].str.replace('juin', '06', case=False)
    df['Date_SPIR'] = df['Date_SPIR'].str.replace('mai', '05', case=False)
    df['Date_SPIR'] = df['Date_SPIR'].str.replace('nov', '11', case=False)
    df["Date_SPIR"] = pd.to_datetime(df["Date_SPIR"], format="%d-%m-%y")
    return df

def add_days_to_floraison(df):
    df["Dates_Delta"] = (df["Date_SPIR"] - df["Date_Floraison"]).dt.days
    return df

data = pd.read_csv("./Data/CIRAD_Sorghum2023_SPIR_all_2 (4).csv",sep=";")

Control_plantes = data.loc[data["Traitement"]=="RS1",:]
print(Control_plantes)
Control_plantes = Control_plantes.drop_duplicates("ID")
print(Control_plantes)

print(Control_plantes["ID"].describe())
print()
