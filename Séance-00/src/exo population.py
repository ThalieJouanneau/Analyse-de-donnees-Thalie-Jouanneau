population = 500000
surface = 25_000
region = "Bretagne"

densite = population / surface
print(f'La densité de population en 2026 est de {densite:.2f} habitants par km².')

population *= 1.005
print(population)

population = 1256249.9999999998
print(densite)

surface = population / densite
densite = 100.0

print(surface)

pays = "France"
region = "Bretagne"
print(f'La {region} compte {population:.0f} habitants sur une surface de {surface:.0f} km².')

if population > 5000000:
    print("Très grande")
elif population > 1000000:
    print("Grande")
elif population > 500000:
    print("Moyenne")
else : 
    print("Petite")