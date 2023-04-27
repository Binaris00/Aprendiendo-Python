import pandas as pd
import numpy as np

df_csv = pd.read_csv("StudentsPerformance.csv")
df_csv["english score"] = 70
english_score =np.arange(0, 1000)
df_csv["english score"] = english_score
print(df_csv)

english_core = np.random.randint(1, 101, size=1000)
df_csv["english score"] = english_score
print(df_csv)