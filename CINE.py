print("BIENVENIDO AL CINE")
edad=int(input("¿Que edad tiene?:"))

if edad <= 12:
    print("Tu entrada vale 8000")

elif edad > 12 and edad < 59:
    print("Tu entrada vale 12000")

else:
    print("Tu entrada vale 9000")
