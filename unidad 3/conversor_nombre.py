# conversor de nombre a mayuscula, minusculas o con la primer letra en mayuscula segun la opcion elegida 
nombre = input("por favor, ingrese su nombre: ")
opcion = input("elija una opcion (1, 2 o 3): ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2": 
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("opcion no valida")
    