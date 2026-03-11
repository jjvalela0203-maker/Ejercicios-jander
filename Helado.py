#Helado
fresa=0
vainilla=0
choco=0

for i in range(0,5):
    ice=str(input("Que sabor de helado desea?:")).strip().lower()
    
    if ice == "fresa":
        fresa += 1
    elif ice == "chocolate":
        choco += 1
    else:
        vainilla += 1

print("Veces que se pidio cada sabor:" )
print("Chocolate:", choco)
print("Fresa:", fresa)
print("Vainilla:", vainilla)





