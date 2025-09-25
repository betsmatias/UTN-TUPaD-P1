# este programa verifica si un string termina en vocal y añade sgno de exclamacion
frase = input("por favor, ingrese un frase o palabra: ")
vocales = "a", "e", "i", "o", "u"
if frase.lower().endswith(vocales):
    print(frase + "!")
else:
    print(frase)
    