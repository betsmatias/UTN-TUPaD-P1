# -----------hola mundo--------


print("hola mundo")

#----------- altura_peso....................................

# pedir altura y peso al usuario 
altura = float(input(" Por favor, introduce tu altura en metros(por ejemplo: 1.70): "))
peso = float(input("ingresar tu peso en kilogramos (ejemplo 70.5): "))
# calculamos el indice de masa corporal (IMC)
#la formula es 
imc = peso / (altura * altura)
imc = peso / (altura ** 2)
#imprimimos el resultado con dos decimilas
print(f"tu IMC es:  {imc: .2f}")

# --------area_perimetro_circulo------------------------------------------

# este programa calcula el area y el perimetro de un circulo
# se importa el modulo math para usar el valor pi
import math
radio = float(input("Por favor, ingresar el radio del circulo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio 
print(f"el area del circulo es: {area:.2f}")
print(f"el perimetro del circulo es: {perimetro:.2f}")

# ------conversion_temeperatura-----------

#pedimos al usuario introducir la temperatura en grados Celsious
celcius = float(input(" Por favor, introducir la temeperatura en grados Celsius: "))
#calculamos la temeperatura en grados fahrenheit
#la formula es:
Fahrenheit = (9/5) * celcius + 32 
fahrenheit = (9/5) * celcius + 32
#imprimimos el resultado
print(f"la temperatura de {celcius} °C ES EQUIVALENTE A {fahrenheit} °F")

#-------------conversor_sgundos_horas-------------

# Este programa convierte segundos en cantidad de horas
#Solicitar al usuario ingrese cantidad de segundos
segundos_totales = int(input("Por foavor, ingresar cantidad de sugundos: ")) 
# realizar el calculo de la conversion
horas = segundos_totales / 3600
# imprimir el resultado
print(f"{segundos_totales} segundos equivalentes a {horas:.2f} horas. ")

#----------------datos_personales-----------------

# Pedir al usuario ingresar datos personales
# Luego imprima una horacion con los datos ingresados
nombre = input("Por favor, ingresar su nombre ")
apellido = input("Por favor, ingresar su apellido ")
edad = input("Por favor, ingresar su edad ") 
residencia = input("Por favor, ingresar su lugar de residencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y  resido en {residencia} ")

#------------------operaciones aritmeticas---------------------------


# pidir al usuario dos numeros enteros distintos de 0
# ingresar los numeros enteros distintos de 0
#  # ingrese los dos numeros enteros
num1 = int(input("por favor ingresar el primer numero entero distinto de 0 : "))
 
while num1 == 0:
    num1  = int(input("el numero debe ser distinto de cero. intenta de nuevo: "))
num2 = int(input("por favor ingresar el segundo numero entero distinto de 0 : "))
while num2 == 0:
    num2 = int(input("el numero debe ser distinto de 0. intenta de nuevo: "))
    # realizar operaciones 
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
divicion = num1 / num2
print("\n---resultados de las operaciones---")
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"divicion: {divicion} ")

#-----------------promedios_numeros----------------

# pedimos al usuario ingresar los tres numeros
numero1 = float(input("por favor, ingrese el primer numero: "))
numero2 = float(input("por favor, ingrese el segundo numero:"))
numero3 = float(input("por favor, ingrese el tercer numero: "))
# calculamos el promedio
# la suma de los tres numeros se divide por 3
promedio = (numero1 + numero2 + numero3) / 3
# imprimimos el resultado 
print(f"el promedio de los tres numeros es:{promedio}")


#----------------------saludo---------------------

# pedir al usuario el nombre  
nonbre = input("¡cual es tu nombre? ")
# imprimir el saludo
print(f"hola {nonbre} ! ")


#--------------------tabla de multiplicar----------------



# este programa pide al usuario un numero e imprime la tabla de multiplicar del numero
# pedir al usuario el numero
numero = int(input("por favor, ingrese un numero " ))
# imprimir la tabla de multiplicar 
print(f"tabla de multiplicar de {numero}: ")
for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")


        