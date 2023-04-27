import pandas as pd

df_csv = pd.read_csv("StudentsPerformance.csv")

print(df_csv.index)

print(df_csv.columns)

print(df_csv.dtypes)

#Metodos
print(df_csv.info())

print(df_csv.describe())

#redondear valores decimales
round(df_csv, 2)