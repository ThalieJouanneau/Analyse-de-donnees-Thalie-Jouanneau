import pandas as pd

donnees = {
    "region": ["Bretagne", "Normandie", "Occitanie", "Île-de-France"],
    "population": [3400000, 3300000, 6100000, 12400000],
    "surface": [27208, 29907, 72724, 12012]
}

df = pd.DataFrame(donnees)
print(df)