print("====BIENVENIDO====")
time=int(input("Cuantas horas estuvo parqueado?:"))

while time <= 0:
    print("VALOR NO VALIDO")
    time=int(input("Cuantas horas estuvo parqueado?:"))

if time == 1:
    print("Total a pagar: 5000")
else:
    total=5000+(3000*(time-1))
    print("Total a pagar:", total)