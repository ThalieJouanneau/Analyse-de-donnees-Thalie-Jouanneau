#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math
import csv

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding='utf-8') as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def ouvrirUnFichierExcel(nom):
    contenu = pd.read_excel(nom, engine="openpyxl")
    return contenu

def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

def classementPays(ordre1, ordre2):
    classement = []

    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2)):
            for element2 in range(0, len(ordre1)):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1)):
            for element2 in range(0, len(ordre2)):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element1][1]])

    return classement

def analyseRangs(valeurs1, valeurs2):
    serie1 = pd.to_numeric(
        pd.Series(list(valeurs1)), errors="coerce")
    serie2 = pd.to_numeric(
        pd.Series(list(valeurs2)), errors="coerce")
    donnees = pd.DataFrame({
        "valeur1": serie1,
        "valeur2": serie2
    })
    donnees = donnees.dropna()

    resultatSpearman = scipy.stats.spearmanr(donnees["valeur1"], donnees["valeur2"])
    resultatKendall = scipy.stats.kendalltau(donnees["valeur1"], donnees["valeur2"])

    return (
        len(donnees),resultatSpearman[0], resultatSpearman[1], resultatKendall[0], resultatKendall[1])

# Question 2
print("Question 2")
restaurants2023 = ouvrirUnFichier("data/classement-restaurants-paris-2023-par-enseignes.csv")

# Question 3
print("Question 3")

NombreEtablissements = restaurants2023["Nombre d'établissement"].tolist()

# Question 4
print("Question 4")

NombreEtablissements = ordreDecroissant(NombreEtablissements)

print("Nombre d'établissements par enseigne (ordre décroissant) :", NombreEtablissements[:10])

# Question 5
print("Question 5")

rangs = list(range(1, len(NombreEtablissements) + 1))

plt.figure()
plt.figure(figsize=(10, 6))
plt.plot(rangs, NombreEtablissements)

plt.xlabel("Rang de l'enseigne")
plt.ylabel("Nombre d'établissements")
plt.title("Loi rang-taille des enseignes de restaurants à Paris en 2023")

plt.savefig("./img/loi_rang_taille_2023_illisible.png")
plt.close()


# Question 6
print("Question 6")

rangs_log = conversionLog(rangs)
NombreEtablissements_log = conversionLog(NombreEtablissements)

plt.figure(figsize=(10, 6))
plt.plot(rangs_log, NombreEtablissements_log)

plt.xlabel("Logarithme du rang")
plt.ylabel("Logarithme du nombre d'établissements")
plt.title("Loi rang-taille en échelle logarithmique")

plt.savefig("./img/loi_rang_taille_2023_log.png")
plt.close()

# Question 7
print("Question 7")
# Mettre ici votre réponse argumentée

# Un test de corrélation des rangs (Spearman ou Kendall) nécessite
# deux classements comparables portant sur les mêmes individus.
# Ici, nous ne disposons que d'un seul classement des enseignes :
# ces tests ne sont donc pas directement applicables.
# On peut en revanche étudier la relation rang-taille, notamment
# à partir de sa représentation en échelle logarithmique.


# Question 9
print("Question 9")

monde = ouvrirUnFichierExcel("data/Le-Monde-HS-Etats-du-monde-2007-2026.xlsx")

print(monde.head())
print(monde.columns.tolist())
print(monde.shape)

# Question 10
print("Question 10")

monde = monde[
    [
        "État",
        "Pop 2007",
        "Pop 2026",
        "Densité 2007",
        "Densité 2026"
    ]
]

Etats = monde["État"].tolist()
Pop2007 = monde["Pop 2007"].tolist()
Pop2026 = monde["Pop 2026"].tolist()
Densite2007 = monde["Densité 2007"].tolist()
Densite2026 = monde["Densité 2026"].tolist()

print(monde.head())

# Question 11
print("Question 11")

ClassementPop2007 = ordrePopulation(Pop2007, Etats)
ClassementPop2026 = ordrePopulation(Pop2026, Etats)

ClassementDensite2007 = ordrePopulation(Densite2007, Etats)
ClassementDensite2026 = ordrePopulation(Densite2026, Etats)

print("Population 2007 :", ClassementPop2007[:10])
print("Population 2026 :", ClassementPop2026[:10])
print("Densité 2007 :", ClassementDensite2007[:10])
print("Densité 2026 :", ClassementDensite2026[:10])

# Question 12
print("Question 12")

Comparaison2007 = classementPays(ClassementPop2007, ClassementDensite2007)
Comparaison2026 = classementPays(ClassementPop2026, ClassementDensite2026)

Comparaison2007.sort()
Comparaison2026.sort()

print("Comparaison 2007 :", Comparaison2007[:10])
print("Comparaison 2026 :", Comparaison2026[:10])


# Question 13
print("Question 13")

RangsPop2007 = []
RangsDensite2007 = []

for ligne in Comparaison2007:
    RangsPop2007.append(ligne[0])
    RangsDensite2007.append(ligne[1])

RangsPop2026 = []
RangsDensite2026 = []

for ligne in Comparaison2026:
    RangsPop2026.append(ligne[0])
    RangsDensite2026.append(ligne[1])

print("Rangs population 2007 :", RangsPop2007[:10])
print("Rangs densité 2007 :", RangsDensite2007[:10])
print("Rangs population 2026 :", RangsPop2026[:10])
print("Rangs densité 2026 :", RangsDensite2026[:10])

# Question 14
print("Question 14")


Spearman2007 = scipy.stats.spearmanr(
    RangsPop2007,
    RangsDensite2007
)

Kendall2007 = scipy.stats.kendalltau(
    RangsPop2007,
    RangsDensite2007
)

Spearman2026 = scipy.stats.spearmanr(
    RangsPop2026,
    RangsDensite2026
)

Kendall2026 = scipy.stats.kendalltau(
    RangsPop2026,
    RangsDensite2026
)

print("2007")
print("Spearman :", Spearman2007[0], "p-value :", Spearman2007[1])
print("Kendall :", Kendall2007[0], "p-value :", Kendall2007[1])

print("2026")
print("Spearman :", Spearman2026[0], "p-value :", Spearman2026[1])
print("Kendall :", Kendall2026[0], "p-value :", Kendall2026[1])

# Question Bonus
print("Question Bonus")
print("Comparaison classement restaurants entre 2017 et 2023")

restaurants2017Bonus = ouvrirUnFichier("data/classement-restaurants-paris-2017-par-enseignes.csv")
restaurants2023Bonus = ouvrirUnFichier("data/classement-restaurants-paris-2023-par-enseignes.csv")

restaurants2017Bonus = restaurants2017Bonus.dropna(subset=["Enseigne"])
restaurants2023Bonus = restaurants2023Bonus.dropna(subset=["Enseigne"])

RestaurantsCommuns = pd.merge(
    restaurants2017Bonus,
    restaurants2023Bonus,
    on="Enseigne",
    how="inner",
    suffixes=("_2017", "_2023")
)

print("Nombre d'enseignes communes :", len(RestaurantsCommuns))
print(RestaurantsCommuns.head())

nb, rho, pSpearman, tau, pKendall = analyseRangs(
    RestaurantsCommuns["Nombre d'établissement_2017"],
    RestaurantsCommuns["Nombre d'établissement_2023"]
)

print("Nombre d'enseignes comparées :", nb)
print("Coefficient de Spearman :", rho)
print("P-value de Spearman :", pSpearman)
print("Coefficient de Kendall :", tau)
print("P-value de Kendall :", pKendall)

print("Bonus : Population mondiale, 2007-2026")

MondeBonus = ouvrirUnFichierExcel("data/Le-Monde-HS-Etats-du-monde-2007-2026.xlsx")

resultatsAnnuels = []

for annee1 in range(2007, 2026):
    for annee2 in range(annee1 + 1, 2027):

        colonne1 = "Pop " + str(annee1)
        colonne2 = "Pop " + str(annee2)

        nb, rho, pSpearman, tau, pKendall = analyseRangs(
            MondeBonus[colonne1], MondeBonus[colonne2])

        resultatsAnnuels.append([
            annee1,
            annee2,
            nb,
            rho,
            pSpearman,
            tau,
            pKendall
        ])

print("Nombre de comparaisons :", len(resultatsAnnuels))

resultatsPopulation = pd.DataFrame(
    resultatsAnnuels,
    columns=[
        "Année 1",
        "Année 2",
        "États communs",
        "Spearman",
        "P-value Spearman",
        "Kendall",
        "P-value Kendall"
    ]
)

print(resultatsPopulation.head(10))
print(resultatsPopulation[(resultatsPopulation["Année 1"] == 2007) & (resultatsPopulation["Année 2"] == 2026)])

resultatsPopulation.to_csv(
    "./csv/Resultats-concordance-population-2007-2026.csv",
    index=False
)