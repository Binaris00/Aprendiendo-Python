import pandas as pd

#Creando el dataframe del archivo .csv
df_csv = pd.read_csv("StudentsPerformance.csv")

#mostrar una columna en especifico
print(df_csv["gender"])

#mostrar mas de dos columnas
print(df_csv[["gender", "math score", "reading score"]])
