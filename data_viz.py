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
