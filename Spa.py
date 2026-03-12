
print("===WELCOME TO THE SPA===")
servicio=input("¿Que servicio desea?:").strip().lower()

while servicio == "":
    print ("Error: entrada vacio")
    servicio=input("¿Que servicio desea?:").strip().lower()

match servicio:
    case "facial"| "masaje"|"manicure":
        print("Servicio disponible")
    case _:
        print("Servicio no disponible")