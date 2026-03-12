print("REGISTRO DE GIMNASIO")

bajo= 0
medio= 0
alto= 0

for i in range(1,6,1):
    print(f"Persona {i}")
    nombre=input("Nombre:")
    dias=int(input("Dias asitidos por semana:"))
    while dias < 0:
        print("Dias negativos invalidos")
        dias=int(input("Dias asitidos por semana:"))
    minutos= float(input("Promedio de minutos por dia:"))
    while minutos < 0:
        print("Minutos negativos no validos")
        minutos= float(input("Promedio de minutos por dia:"))
    if dias < 3:
        print("Estado: Compromiso bajo")
        bajo += 1
    elif 3 <= dias <= 4:
        print("Estado: Compromiso medio")
        medio += 1
    else:
        print("Estado: Compromiso alto")
        alto += 1

print("\n"+ "="*30)
print("RESUMEN DE CATEGORIAS")
print("="*30)
print(f"Bajo compromiso:{bajo}")
print(f"Compromiso medio:{medio}")
print(f"Compromiso alto:{alto}")
