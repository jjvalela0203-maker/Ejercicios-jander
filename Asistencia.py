respuesta= "si"
while respuesta == "si":
    print("====REGISTRO DE ESTUDIANTES====")

    n=int(input("Cuantos estudiantes desea hacerle seguimiento de asistencia?:"))

    estudiantes= [ ]
    for i in range(0, n, 1):
        nombre=str(input("Ingrese el nombre del estudiante:"))
        asistencia=int(input("Cuantas veces asistio el estudiante en el mes?:"))
        while asistencia < 0:
            print("ERROR: Asistencia no puede ser negativa")
            asistencia=int(input("Por favor ingrese un numero valido:"))
        estudiantes.append(nombre)
        estudiantes.append(asistencia)
    
        match asistencia:
            case n if n < 5:
                estudiantes.append("asistencia baja")
            case n if 5 <= n <= 8:
                estudiantes.append("asistencia media")
            case n if n >= 9:
                estudiantes.append("asistencia alta")
    print("\nResumen de registros:", estudiantes)
    
    
    respuesta = input("\n¿Desea hacer otro registro? (si/no): ").lower().strip()

print("Programa finalizado.")







