#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding = "utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1
print("Question 1")

donnees = ouvrirUnFichier("./data/Produits-alimentaires-vs-autres-2024.csv")


colonnes = [
    "Année",
    "Code-ISO",
    "Total-export-alimentaire-USD",
    "Total-import-alimentaire-USD",
    "Total-export-autres-USD",
    "Total-import-autres-USD",
    "Total-export-USD",
    "Total-import-USD"
]

donnees = donnees[colonnes]

# "Année" : Année, ici 2024
# "Code-ISO" : code ISO du territoire
# "Total-export-alimentaire-USD" : total des exportations concernant les produits alimentaires
# "Total-import-alimentaire-USD" : total des importations concernant les produits alimentaires
# "Total-export-autres-USD" : total des exportations concernant les produits non alimentaires
# "Total-import-autres-USD" : total des importations concernant les produits non alimentaires
# "Total-export-USD" : total des exportations
# "Total-import-USD" : total des importations

# Question 2
print("Question 2")

# Sélection des variables
x1 = donnees["Total-export-alimentaire-USD"]
y1 = donnees["Total-import-alimentaire-USD"]

x2 = donnees["Total-export-autres-USD"]
y2 = donnees["Total-import-autres-USD"]

x3 = donnees["Total-export-USD"]
y3 = donnees["Total-import-USD"]


# Calcul de la régression linéaire pour la méthode des moindres carrés 1
regression1 = scipy.stats.linregress(x1, y1)

# Calcul de la droite de régression 1
a1 = regression1.slope
b1 = regression1.intercept
droite1 = a1 * x1 + b1


# Calcul de la régression linéaire pour la méthode des moindres carrés 2
regression2 = scipy.stats.linregress(x2, y2)

# Calcul de la droite de régression 2
a2 = regression2.slope
b2 = regression2.intercept
droite2 = a2 * x2 + b2


# Calcul de la régression linéaire pour la méthode des moindres carrés 3
regression3 = scipy.stats.linregress(x3, y3)

# Calcul de la droite de régression 3
a3 = regression3.slope
b3 = regression3.intercept
droite3 = a3 * x3 + b3

regression_inverse = scipy.stats.linregress(y1, x1)

print("Régression alimentaire :", a1, "x +", b1)
print("Régression non alimentaire :", a2, "x +", b2)
print("Régression totale :", a3, "x +", b3)

print("Pente inverse :", regression_inverse.slope)
print("Ordonnée à l'origine inverse :", regression_inverse.intercept)

# Question 3
print("Question 3")
# Calcul du coefficient de corrélation 1

correlation1 = scipy.stats.pearsonr(x1, y1)
r1 = correlation1[0]

# Calcul du coefficient de corrélation 2

r2 = scipy.stats.pearsonr(x2, y2)[0]

# Calcul du coefficient de corrélation 3

r3 = scipy.stats.pearsonr(x3, y3)[0]

print("Corrélation alimentaire :", r1)
print("Corrélation non alimentaire :", r2)
print("Corrélation totale :", r3)

# Question 4
print("Question 4")
# Calcul du graphique 1

x_graphique = np.linspace(x1.min(), x1.max(), 100)
y_graphique = a1 * x_graphique + b1

plt.figure()
plt.scatter(x1, y1, label="Territoires")
plt.plot(x_graphique, y_graphique, color="red", label="Régression linéaire")

plt.title("Importations et exportations alimentaires")
plt.xlabel("Exportations alimentaires (USD)")
plt.ylabel("Importations alimentaires (USD)")
plt.legend()

plt.savefig("./img/regression_lineaire_alimentaire.png")
plt.close()

# Calcul du graphique 2

x_graphique = np.linspace(x2.min(), x2.max(), 100)
y_graphique = a2 * x_graphique + b2

plt.figure()
plt.scatter(x2, y2, label="Territoires")
plt.plot(x_graphique, y_graphique, color="red", label="Régression linéaire")

plt.title("Importations et exportations non alimentaires")
plt.xlabel("Exportations non alimentaires (USD)")
plt.ylabel("Importations non alimentaires (USD)")
plt.legend()

plt.savefig("./img/regression_lineaire_non_alimentaire.png")
plt.close()

# Calcul du graphique 3

x_graphique = np.linspace(x3.min(), x3.max(), 100)
y_graphique = a3 * x_graphique + b3

plt.figure()
plt.scatter(x3, y3, label="Territoires")
plt.plot(x_graphique, y_graphique, color="red", label="Régression linéaire")

plt.title("Importations et exportations totales")
plt.xlabel("Exportations totales (USD)")
plt.ylabel("Importations totales (USD)")
plt.legend()

plt.savefig("./img/regression_lineaire_flux_totaux.png")
plt.close()