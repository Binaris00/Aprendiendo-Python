import pandas as pd

#Creando el dataframe del archivo .csv
df_csv = pd.read_csv("StudentsPerformance.csv")

#Una prueba que quise hacer
# print((df_csv["gender"] + df_csv["parental level of education"] + df_csv["lunch"]).value_counts())

#Mostrar cuantas female y male tiene la columna
print(df_csv["gender"].value_counts())

#Mostrar un tipo de porcentaje
#tambien luego se puede usar round() para limitar los decimales
print(df_csv["gender"].value_counts(normalize=True))
