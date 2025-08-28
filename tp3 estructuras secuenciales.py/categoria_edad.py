#este programa clasifica al usuario en una categoria sun la edad
edad = int(input("ingresa tu edad. "))
if edad < 12:
    print("niño/a. ")
elif edad >= 12 and edad < 18:
    print("adolescente. ")
elif edad >= 18 and edad < 30:
    print("adulto/a joven. ")
else:
    print("adulto/a. ")
    