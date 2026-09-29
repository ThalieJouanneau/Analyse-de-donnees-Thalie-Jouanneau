age : int = 10
name : str = "Thalie"

print ("name:", name, "age:", str(age))
print (f'name: {name}, age: {age}')

def add(a: float, b: float) -> float:
    print (f'Adding {a} and {b}')
    return a + b

print(add(10.2, 7.2))

annee = 2026
print("Nous sommes en", annee)

population = 68000000
surface = 551695

densite = population / surface

print(f'La densité de population en {annee} est de {densite:.2f} habitants par km².')
print(type(population))
print(type(surface)) 