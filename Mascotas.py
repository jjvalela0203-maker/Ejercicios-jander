print("BIENVENIDO A LA TIENDA DE MASCOTAS")
print("¿Que mascota posee?")
print("1) Perro")
print("2) Gato")
print("3) Conejo")
print()
animal=int(input("R:"))

while animal >= 4:
    print("Opcion no existente")
    animal=int(input("R:"))

if animal == 1:
    print("Te recomendamos darle Dog show a tu canino")

elif animal == 2:
    print("Te recomendamos Mirringo para tu gatico")

else:
    print("Te recomendamos darle zanahorias a tu conejo")

