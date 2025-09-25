# Este programa clasifica la magnitud de un terremoto en escala de Richter
magnitud = float(input("por favor, ingrese magnitud del terremoto: "))
if magnitud < 3:
    print("muy leve (imperceptible) ")
elif magnitud >= 3 and magnitud < 4:
    print("leve (ligeramente perceptible) ")
elif magnitud >= 4 and magnitud < 5:
    print("moderado (sentido por personas, no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("fuerte (causa daños en estructuras debiles) ")
elif magnitud >= 6 and magnitud < 7:
    print("muy fuerte(causa daños significativos )")
else: 
    print("extremo (causa daños a gran escala) ")