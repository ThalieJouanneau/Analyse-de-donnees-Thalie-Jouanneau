#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats
import matplotlib.pyplot as plt

# C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
# Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
# Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

# Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom, header="infer"):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier, header=header)
    return contenu

# Question 1 : Théorie de l'échantillonnage (intervalles de fluctuation)
# L'échantillonnage se base sur la répétitivité.
print("Question 1")
print("Résultat sur le calcul d'un intervalle de fluctuation")

echantillons = ouvrirUnFichier("data/Echantillonnage-100-Echantillons.csv")
population = ouvrirUnFichier("data/Echantillonnage-Population-reelle.csv", header=None)

moyennes = echantillons.mean()

moyennes_arrondies = []

for valeur in moyennes:
    moyennes_arrondies.append(round(valeur))

print("Moyennes arrondies :", moyennes_arrondies)

total_moyennes = sum(moyennes_arrondies)

frequences_echantillons = []

for valeur in moyennes_arrondies:
    frequence = valeur / total_moyennes
    frequences_echantillons.append(round(frequence, 2))

print("Fréquences des échantillons :", frequences_echantillons)

effectifs_population = population.iloc[:, 0].tolist()

total_population = sum(effectifs_population)

frequences_population = []

for valeur in effectifs_population:
    frequence = valeur / total_population
    frequences_population.append(frequence)

print("Effectifs de la population :", effectifs_population)
print("Fréquences de la population :",
      [round(p, 2) for p in frequences_population])


taille_echantillon = 1000
zC = 1.96

intervalles_fluctuation = []

for p in frequences_population:
    marge = zC * math.sqrt(p * (1 - p) / taille_echantillon)
    borne_inferieure = p - marge
    borne_superieure = p + marge

    intervalles_fluctuation.append(
        (round(borne_inferieure, 3), round(borne_superieure, 3))
    )

print("Intervalles de fluctuation :", intervalles_fluctuation)

# Question 2 : Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Question 2")
print("Résultat sur le calcul d'un intervalle de confiance")

echantillon = list(echantillons.iloc[0])
total_echantillon = sum(echantillon)

print("Premier échantillon :", echantillon)
print("Effectif total de l'échantillon :", total_echantillon)

frequences_echantillon = []

for valeur in echantillon:
    frequence = valeur / total_echantillon
    frequences_echantillon.append(frequence)

print("Fréquences du premier échantillon :",
      [round(p, 3) for p in frequences_echantillon])

zC = 1.96

intervalles_confiance = []

for p in frequences_echantillon:
    marge = zC * math.sqrt(p * (1 - p) / total_echantillon)

    borne_inferieure = p - marge
    borne_superieure = p + marge

    intervalles_confiance.append(
        (round(borne_inferieure, 3), round(borne_superieure, 3))
    )

print("Intervalles de confiance :", intervalles_confiance)


# Question 3 : Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
# Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Question 3")
print("Théorie de la décision")

loi1 = ouvrirUnFichier("data/Loi-normale-Test-1.csv")
loi2 = ouvrirUnFichier("data/Loi-normale-Test-2.csv")

valeurs1 = loi1["Test"].dropna()
valeurs2 = loi2["Test"].dropna()

resultat1 = scipy.stats.shapiro(valeurs1)
resultat2 = scipy.stats.shapiro(valeurs2)

print("Test de Shapiro-Wilk, série 1 :", resultat1)
print("Test de Shapiro-Wilk, série 2 :", resultat2)
print("Selon les résultats du test de Shapiro-Wilk, seule la série 1 suit une loi normale, car sa statistique est très proche de 1.")

# Question bonus
print("Question bonus")

plt.figure()
plt.hist(valeurs1, bins=30)
plt.title("Distribution de la série 1")
plt.xlabel("Valeurs")
plt.ylabel("Effectifs")
plt.savefig("./img/distribution_series_1.png")
plt.close()

plt.figure()
plt.hist(valeurs2, bins=30)
plt.title("Distribution de la série 2")
plt.xlabel("Valeurs")
plt.ylabel("Effectifs")
plt.savefig("./img/distribution_series_2.png")
plt.close()