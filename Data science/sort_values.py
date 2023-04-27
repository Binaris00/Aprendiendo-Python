import pandas as pd


#Creando el dataframe del archivo .csv
df_csv = pd.read_csv("StudentsPerformance.csv")

#Esto no lo dice en el video
#Si uso esta forma lo que va a hacer es solo devolverme la columna organizada pero sin todo el dataframe
print(df_csv["math score"].sort_values())

#En cambio si uso esta forma me devolvera todo el dataframe original organizando solo la columna math score
print(df_csv.sort_values("math score"))

#Ahora se organiza de forma descendiente
print(df_csv.sort_values("math score", ascending=False))

#Usar el metodo con mas de dos columnas y descendiente
print(df_csv.sort_values(["math score", "reading score"], ascending=False))

#Reemplazar el archivo original
print(df_csv.sort_values("math score", inplace=True))

#para organizar cadenas de texto
print(df_csv.sort_values("race/ethnicity", ascending=True))