print("BIENVENIDO A LA TIENDA DE MASCOTAS")
print("¿Que mascota posee?")
print("-perro")
print("-gato")
print("-conejo")
print()
animal=str(input("R:")).strip().lower()

while animal == "":
    print("Opcion no existente")
    animal=int(input("R:"))

if animal == "perro":
    print("Te recomendamos darle Dog show a tu canino")

elif animal == "gato":
    print("Te recomendamos Mirringo para tu gatico")

elif animal == "conejo":
    print("Te recomendamos zanahorias para tu conejo")

else:
    print("No conocemos a ese animal")

