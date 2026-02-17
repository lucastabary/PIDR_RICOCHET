import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./Data/CIRAD_Sorghum2023_SPIR_all_2 (4).csv",sep=";")

#### premier jeu de visualisation des spectres des plantes de controle en ne prenant pas en comtpe les doublons de mesure
Control_plantes = data.loc[data["Traitement"]=="C",:]

Control_plantes = Control_plantes.drop_duplicates("ID")

print(Control_plantes["ID"].describe())


## graphique de superpositon en plt pour observer l'évolution de l'absorption

wavelength = [i for i in range(350,2501)]
x_data_control= Control_plantes.loc[:,"350":"2500"].to_numpy()


plt.figure(figsize=(12,6))
plt.xlabel("Wavelength")
plt.ylabel("Absorption")
fill = plt.subplot()
for k in x_data_control: 
    fill.plot(wavelength,k,color='Red')


#############################################################

##recherche impact chaleur sur spectre  
SS1_plantes = data.loc[data["Traitement"]=="SS1",:]
SS1_plantes = SS1_plantes.drop_duplicates("ID")

x_data_SS1 = SS1_plantes.loc[:,"350":"2500"].to_numpy()

# plt.figure(figsize=(12,6))
# plt.xlabel("Wavelength")
# plt.ylabel("Absorption")
plot = plt.subplot()
for k in x_data_SS1: 
    fill.plot(wavelength,k,color='Blue',alpha = 0.3)
# plt.show()

###
#####SS2

SS2_plantes = data.loc[data["Traitement"]=="SS2",:]
SS2_plantes = SS2_plantes.drop_duplicates("ID")

x_data_SS2 = SS2_plantes.loc[:,"350":"2500"].to_numpy()

for k in x_data_SS2: 
    fill.plot(wavelength,k,color='Green',alpha = 0.3)
# plt.show()

#####

###RS1
RS1_plantes = data.loc[data["Traitement"]=="RS1",:]
RS1_plantes = RS1_plantes.drop_duplicates("ID")

x_data_RS1 = RS1_plantes.loc[:,"350":"2500"].to_numpy()

for k in x_data_RS1: 
    fill.plot(wavelength,k,color='yellow',alpha = 0.5)
# plt.show()
###
###RS2

RS2_plantes = data.loc[data["Traitement"]=="RS2",:]
RS2_plantes = RS2_plantes.drop_duplicates("ID")

x_data_RS2 = RS2_plantes.loc[:,"350":"2500"].to_numpy()

for k in x_data_RS2: 
    fill.plot(wavelength,k,color='Black',alpha = 0.3)

plt.show()

# -----------------------------------------------------------------------------
# Bloc ajouté : tracer UNE courbe moyenne par jeu (± 1σ) — n'écrase pas le code ci‑dessous
# -----------------------------------------------------------------------------
import numpy as np

def _matrix_from_xdata(x):
    """Retourne une matrice float (NaN si conversion impossible) à partir de x_data (numpy array ou similaire)."""
    import pandas as _pd
    if x is None:
        return None
    mat = _pd.DataFrame(x).apply(_pd.to_numeric, errors='coerce').to_numpy(dtype=float)
    return mat if mat.size else None


def _mean_std(x):
    mat = _matrix_from_xdata(x)
    if mat is None:
        return None, None
    return np.nanmean(mat, axis=0), np.nanstd(mat, axis=0)

# calculs
m_control, s_control = _mean_std(x_data_control)
m_ss1, s_ss1 = _mean_std(x_data_SS1)
m_ss2, s_ss2 = _mean_std(x_data_SS2)
m_rs1, s_rs1 = _mean_std(x_data_RS1)
m_rs2, s_rs2 = _mean_std(x_data_RS2)

# tracé propre des moyennes (+ bandes ±1σ)
plt.figure(figsize=(12, 6))
ax = plt.gca()

if m_control is not None:
    ax.plot(wavelength, m_control, color='red', label='Moyenne C', linewidth=2)
    ax.fill_between(wavelength, m_control - s_control, m_control + s_control, color='red', alpha=0.08)

if m_ss1 is not None:
    ax.plot(wavelength, m_ss1, color='blue', label='Moyenne SS1', linewidth=2)
    ax.fill_between(wavelength, m_ss1 - s_ss1, m_ss1 + s_ss1, color='blue', alpha=0.06)

if m_ss2 is not None:
    ax.plot(wavelength, m_ss2, color='green', label='Moyenne SS2', linewidth=2)
    ax.fill_between(wavelength, m_ss2 - s_ss2, m_ss2 + s_ss2, color='green', alpha=0.06)

if m_rs1 is not None:
    ax.plot(wavelength, m_rs1, color='orange', label='Moyenne RS1', linewidth=2)
    ax.fill_between(wavelength, m_rs1 - s_rs1, m_rs1 + s_rs1, color='orange', alpha=0.04)

if m_rs2 is not None:
    ax.plot(wavelength, m_rs2, color='black', label='Moyenne RS2', linewidth=2)
    ax.fill_between(wavelength, m_rs2 - s_rs2, m_rs2 + s_rs2, color='black', alpha=0.04)

ax.set_xlabel('Wavelength')
ax.set_ylabel('Absorption')
ax.set_title('Spectre moyen par traitement (± 1σ)')
ax.grid(alpha=0.3)
ax.legend() 

# effectifs utilisés pour chaque moyenne
try:
    print(f"N (après drop_duplicates) — C: {x_data_control.shape[0]}, SS1: {x_data_SS1.shape[0]}, SS2: {x_data_SS2.shape[0]}, RS1: {x_data_RS1.shape[0]}, RS2: {x_data_RS2.shape[0]}")
except Exception:
    pass

plt.show()

