# este programa verifica longitud de una contraseña entre 8 y 14 caracteres
contraseña = input("por favor ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("ha ingresado una contraseña correcta.")
else:
    print("por favor, una contraseña de entre 8 y 14 caracteres. ")