# este programa determina la estacion del año basandose en el hemisferio, mes dia
hemisferio = input("¿en que hemisferio se encuentra? (N/S): ").upper()
mes = input("¿que (mes del año es? ").lower
dia = int(input("¿que dia es?: "))

if hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Invierno")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Primavera")
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Verano")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Otoño")
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio no válido. Por favor, ingrese 'N' o 'S'.")