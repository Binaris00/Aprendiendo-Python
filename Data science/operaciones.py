import pandas as pd
import numpy as np

df_csv = pd.read_csv("StudentsPerformance.csv")

#para mostrar el resultado de sumar toda una columna
print(df_csv["math score"].sum())

#El promedio
print(df_csv["math score"].mean())

#El conteo
print(df_csv["math score"].std())

#El valor mas grande de toda la columna
print(df_csv["math score"].max())

#El valor mas pequeno de toda la columna
print(df_csv["math score"].min())

#dar todos los valores de antes
print(df_csv.describe())

#Prueba que hice para ver como se guardaba en una variable y como se muestra 
df_csv_valores = df_csv.describe()
print(df_csv_valores)



#mostrar la suma de todas las columnas en una sola fila y luego mostrar el promedio, el maximo etc, con el mismo metodo
df_csv_valores_suma =(df_csv["math score"] + df_csv ["reading score"] + df_csv['writing score']).describe()
#para redondear los numeros hasta un maximo de 2
df_csv_valores_suma =df_csv_valores_suma.round(2)
print(df_csv_valores_suma)
