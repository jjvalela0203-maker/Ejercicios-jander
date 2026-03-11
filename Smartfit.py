
print("======= SMARTFIT =======")
edad=int(input("Ingrese su edad:"))
if edad < 13:
    print("No puedes entrar")
elif edad >= 13 and edad <= 17:
    print ("Plan juvenil")
elif edad >=18 and edad <= 59:
    print("Plan general")
else:
    print("Plan senior")