import pandas as pd
import numpy as np

####OPCION 1
#Creando un array
array_data = np.array([[1, 5], [9, 6], [7,2]])

#Creando un dataframe
df = pd.DataFrame(array_data, index=["Row 1", "Row 2", "Row 3"], columns=["col1", "col2"])
print(df)




######OPCION 2
data = [[1, 5], [9, 6], [7,2]]
df = pd.DataFrame(array_data, index=["Row 1", "Row 2", "Row 3"], columns=["col1", "col2"])
print(df)


#####OPCION CON DICCIONARIOS
states = ["California", "Texas", "Florida", "New York"]
population = [1, 5, 7, 8]
dict_states = {"States":states, "Population":population}

df_diccionario = pd.DataFrame(dict_states)
print(df_diccionario)


######OPCION CON ARCHIVO CSV (EXCEL)
df_csv = pd.read_csv("StudentsPerformance.csv")
print(df_csv)