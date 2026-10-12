
import pandas as pd
import matplotlib.pyplot as plt

# 1. Créer les données issues du codage des entretiens
donnees = {
    "Plat": [
        "Carbonade / bœuf à la bière",
        "Potjevleesch",
        "Welsh",
        "Poulet au maroilles",
        "Frites",
        "Coq à la bière",
        "Tripes à la mode de Caen",
        "Waterzoï",
        "Tarte au maroilles",
        "Flamiche",
        "Endives au jambon",
        "Gratin d'endives",
        "Croquettes de crevettes",
        "Quiche flamande",
        "Fricadelle",
        "Pâté de foie régional",
        "Poulet au citron"
    ],
    "Nombre d'entretiens": [
        7, 6, 5, 2, 2,
        1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1
    ]
}

df = pd.DataFrame(donnees)

# 2. Classer les plats du plus cité au moins cité
df = df.sort_values(
    "Nombre d'entretiens",
    ascending=True
)

# 3. Construire le diagramme en barres horizontales
plt.figure(figsize=(10, 8))

plt.barh(
    df["Plat"],
    df["Nombre d'entretiens"],
    color="#455747"
)

# 4. Ajouter les nombres au bout des barres
for i, valeur in enumerate(df["Nombre d'entretiens"]):
    plt.text(
        valeur + 0.08,
        i,
        str(valeur),
        va="center"
    )

# 5. Ajouter le titre et les axes
plt.title(
    "Plats mentionnés dans les huit entretiens",
    fontsize=15,
    pad=15
)
plt.xlabel("Nombre d'entretiens mentionnant le plat")
plt.ylabel("Plat")

# Les fréquences sont des nombres entiers
plt.xticks(range(0, 9))
plt.xlim(0, 8)

# Simplifier la présentation
plt.grid(axis="x", alpha=0.25)
plt.gca().set_axisbelow(True)
plt.tight_layout()

# 6. Enregistrer le graphique en haute résolution
plt.savefig(
    "./img/" + "diagramme_des_plats_flamands" + ".png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


