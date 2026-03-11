print("BIENVENIDO A CAT CAFE")
print("¿Que bebida desea ordenar?")
print("1) Cafe: 4000")
print("2) Te: 3500")
print("3) Jugo: 5000")

elecc= int(input("Seleccione una opcion (1-3):"))

while elecc >= 4:
    print("No existe esa opcion")
    elecc= int(input("Seleccione una opcion (1-3):"))

if elecc == 1:
    elecc= 5000

elif elecc == 2:
    elecc= 3500

else:
    elecc= 5000

cant=int(input("Cuanta/os quiere?:"))

total= elecc*cant

print("TOTAL A PAGAR")
print(total)