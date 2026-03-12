print("=====BIENVENIDO=====")
productos_caros= [ ]
for i in range(6):
    nombreproduc= str(input("Cual es el producto?:"))
    valorproduc=int(input("Cual es el valor de ese producto?:"))
    if valorproduc >= 100000:
        productos_caros.append(nombreproduc)
        productos_caros.append(valorproduc)

print("PRODUCTOS COSTOSOS")
print(productos_caros)
