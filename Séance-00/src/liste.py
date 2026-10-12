aliments = ["chocolat", "sucre", "riz", "boeuf", "jambon"]
print(aliments[2])

aliments.append("yaourt")
len(aliments)
print(len(aliments))

aliments[0]="cacao"
print(aliments[0])

bretagne = {
    "population" : 3400000,
    "surface" : 27250,
    "capitale" : "rennes"
}

print(bretagne["population"])

densite = 115

if densite < 50:
    print("très faible")
elif 50 <= densite < 100:
    print("faible")
elif 100 <= densite < 200:
    print("Moyenne")
elif densite >= 200:
    print("Grande")

temperatures = [18, 21, 24, 27, 31, 29, 22]
for temp in temperatures:
    if temp >= 25:
        print(temp, "chaud")

populations = [500000, 2000000, 800000, 7000000]

for population in populations:
    if population > 1000000:
        print(population)


def catégoriser_densite(x):
    if densite < 50:
        print("très faible")
    elif 50 <= densite < 100:
        print("faible")
    elif 100 <= densite < 200:
        print("Moyenne")
    elif densite >= 200:
        print("Grande")
    return 