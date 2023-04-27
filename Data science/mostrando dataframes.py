import pandas as pd

#Creando el dataframe del archivo .csv
df_csv = pd.read_csv("StudentsPerformance.csv")

#Imprimiendo las primeras 5 filas del dataframe
print(df_csv.head())

#Impriendo las ultimas 5 filas del dataframe
print(df_csv.tail())

#Puedes tambien pedir que se muestren las primeras x filas que tu quieras y tambien con las ultimas
print(df_csv.head(10))

#Mostrar todo un dataframe
# pd.set_option("display.max_rows", 1000)
# print(df_csv)

#Saber cuantas columnas y filas tiene el dataframe
df_csv.shape