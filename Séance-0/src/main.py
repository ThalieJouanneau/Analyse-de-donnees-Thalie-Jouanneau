import numpy
import pandas as pd
import geopandas as gdp

data = {
    "territoire": ["Bretagne", "Normandie", "Ile de France", "Hauts-de-France", "Grand-est", "Nouvelle Aquitaine"],
    "population": [3400000, 3300000, 12400000, 6000000, 5600000, 6100000],
    "surface": [27200, 29900, 12000, 31800, 57400, 84000]
}

df = pd.DataFrame(data)
df["densite"] = df["population"] / df["surface"]

print(df)

print(df["densite"])

print(df.loc[df["densite"].idxmax()])

print(df.loc[df["densite"].idxmin()])

print(df["densite"].mean())

selection=df[df["densite"] > 150]
print(selection)
