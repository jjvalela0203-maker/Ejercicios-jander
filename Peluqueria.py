print("====WELCOME====")
hora=int(input("Ingrese su hora de llegada en formato 24h:"))

if hora <= 5 or hora >= 23:
    print("Fuera de horario")

elif hora >= 6 and hora <= 11:
    print("Horario de la mañana")

elif hora >= 12 and hora <= 17:
    print("Horario de la tarde")

elif hora >= 18 and hora <= 22:
    print("Horario de la noche")