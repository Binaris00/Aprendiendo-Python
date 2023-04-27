import pandas as pd
import statsmodels.api as sm

df_houses = pd.read_csv('Boston House Prices.csv')
print(df_houses.describe())

y = df_houses["Value"]
x = df_houses["Rooms"]

x = sm.add_constant(x)
ln = sm.OLS(y, x).fit
print(ln.predict(x))