import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

NIRS_INDEXES = [str(i) for i in range(350, 2501)]
NIRS_INDEXES_INT = [i for i in range(350, 2501)]

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

def split_data(df):
    """
    Retourne un dictionnaire de sous-dataframes indexé par (Genotype, Sample).
    Ex: groups[("Btx623", "FreshLeaf")], groups[("Macia", "GrainFlour")], ...
    """
    groups = {}
    for genotype in df["Genotype"].unique():
        for sample in df["Sample"].unique():
            mask = (df["Genotype"] == genotype) & (df["Sample"] == sample)
            groups[(genotype, sample)] = df.loc[mask, :]
    return groups

if __name__ == "__main__":
    data = pd.read_csv("./Data/CIRAD_Sorghum2023_SPIR_all_2 (4).csv",sep=";")

    Control_plantes = data.loc[data["Traitement"]=="RS1",:]
    print(Control_plantes)
    Control_plantes = Control_plantes.drop_duplicates("ID")
    print(Control_plantes)

    print(Control_plantes["ID"].describe())
    print()
