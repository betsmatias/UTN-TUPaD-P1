
# EJERCICIO 1: IMP_HOLA_MUNDO

# Definición de la función
def imprimir_hola_mundo():
  
  #Esta función imprime el mensaje "Hola Mundo!" en la pantalla.
  
  print("Hola Mundo!")

# Llamada a la función desde el programa principal
imprimir_hola_mundo()

#-----------------------------------------------------------------#----------------------------------------------------------------------


#EJERCICIO 2: SALUDAR_USUARIO

# Definicion de la funcion que recibe un parametro
def saludar_usuario(nombre):

   #recibe un nombre como parametro y devuelve un saludo personalizado
   
   saludo = (f"¡hola {nombre}!")
   return saludo

# Programa principal
# Solicitar el nombre al usuario
nombre_ingresado = input("por favor ingrese su nombre: ")


# Llamar a la función con el nombre ingresado
mensaje_personalizado = saludar_usuario(nombre_ingresado)

# Imprimir el resultado que devolvió la funcion
print(mensaje_personalizado)



#-----------------------------------------------------#-----------------------------------------------------------------------------------


 # EJERCICIO 3: INFORMACION_PERSONAL



# Definición de la función con cuatro parametros
def informacion_personal(nombre, apellido, edad, residencia):
  
  #Recibe nombre, apellido, edad y residencia, y muestra una frasecon esta informacion. 

  
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
print("Por favor, completa tu información personal.")

# Pedir cada dato al usuario y guardarlo en una variable
nombre_usuario = input("Nombre: ")
apellido_usuario = input("Apellido: ")
edad_usuario = input("Edad: ")
residencia_usuario = input("Lugar de residencia: ")

print("---") 

# Llamar a la función y pasarle los datos ingresados como argumentos
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)



#-------------------------------------------------------------------------#---------------------------------------------------------------------------



# EJERCICIO 4: AREA_CIRCULO


import math

#  Definicion de Funciones 

def calcular_area_circulo(radio):
  
  #Calcula el área de un círculo dado su radio.
  # Fórmula: Área = π * radio²
  
  area = math.pi * (radio ** 2)
  return area

def calcular_perimetro_circulo(radio):
  
  # Calcula el perímetro (circunferencia) de un círculo dado su radio.
  # Fórmula: Perímetro = 2 * π * radio
  
  perimetro = 2 * math.pi * radio
  return perimetro

#  Programa Principal 

# Solicitar el radio al usuario y convertirlo a número decimal (float)
radio_usuario = float(input("Ingresa el radio del círculo: "))

# Llamar a las funciones con el radio ingresado
area_calculada = calcular_area_circulo(radio_usuario)
perimetro_calculado = calcular_perimetro_circulo(radio_usuario)

# Mostrar los resultados formateados a dos decimales
print("--- Resultados ---")
print(f"El área del círculo es: {area_calculada:.2f}")
print(f"El perímetro del círculo es: {perimetro_calculado:.2f}")


#---------------------------------------------------------------#-------------------------------------------------------------------------


# EJERCICIO 5: CONVERSION_HORAS


# 1.Definicion de la funcion para convertir segundos a horas
def segundos_a_horas(segundos):
  
  # Recibe una cantidad de segundos y la convierte a horas.
  # Hay 3600 segundos en una hora (60 segundos/minuto * 60 minutos/hora).
  
  horas = segundos / 3600
  return horas

# Programa Principal 

# Solicitar los segundos al usuario y convertirlos a nUmero entero
total_segundos = int(input("Ingresa la cantidad de segundos a convertir: "))

# Llamar a la funcion para realizar el cálculo
cantidad_horas = segundos_a_horas(total_segundos)

# Mostrar el resultado final
print(f"{total_segundos} segundos equivalen a {cantidad_horas:.2f} horas.")



#---------------------------------------------------------------------------#--------------------------------------------------------------------------------

# EJERCICIO 6: TABLA_MULTIPLICAR

# 1. Definición de la función
def tabla_multiplicar(numero):
  
  # Recibe un número e imprime su tabla de multiplicar del 1 al 10.
  
  print(f"--- Tabla de Multiplicar del {numero} ---")
  
  # Usamos un bucle 'for' para recorrer los números del 1 al 10
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Programa Principal 

# Solicitar un numero al usuario y convertirlo a entero
numero_usuario = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Llamar a la funcion con el numero del usuario
tabla_multiplicar(numero_usuario)



#--------------------------------------------------------------------#---------------------------------------------------------------


# EJERCICIO 7 : OPERACIONES_BASICAS
 

# 1. Definicion de la funcion
def operaciones_basicas(a, b):
  
  # Recibe dos numeros y devuelve una tupla con su suma, resta, 
  # multiplicacion y division.
  
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  
  # Manejar el caso de division por cero
  if b != 0:
    division = a / b
  else:
    division = "No se puede dividir por cero"
    
  return (suma, resta, multiplicacion, division)

# Programa Principal 

# Solicitar dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Llamar a la funcion y desempaquetar la tupla de resultados
# en cuatro variables distintas.
resultado_suma, resultado_resta, resultado_mult, resultado_div = operaciones_basicas(num1, num2)

# Mostrar los resultados de forma clara
print("\n--- Resultados de las Operaciones ---")
print(f"Suma: {num1} + {num2} = {resultado_suma}")
print(f"Resta: {num1} - {num2} = {resultado_resta}")
print(f"Multiplicación: {num1} * {num2} = {resultado_mult}")
print(f"División: {num1} / {num2} = {resultado_div}")



#----------------------------------------------------------------------#------------------------------------------------------------------


# EJERCICIO 8: CALCULAR_IMC


# 1. Definición de la funcion para calcular el IMC
def calcular_imc(peso, altura):
  
  # Recibe el peso en kg y la altura en metros, y devuelve el IMC.
  # Formula: IMC = peso / (altura²)
  
  # Evitar la division por cero si la altura es 0
  if altura == 0:
    return 0
  
  imc = peso / (altura ** 2)
  return imc

# Programa Principal 

# Solicitar los datos al usuario
peso_usuario = float(input("Ingresa tu peso en kilogramos (kg): "))
altura_usuario = float(input("Ingresa tu altura en metros (m): "))

# Llamar a la funcion con los datos del usuario
imc_calculado = calcular_imc(peso_usuario, altura_usuario)

# Mostrar el resultado formateado a dos decimales
print(f"\nTu Índice de Masa Corporal (IMC) es: {imc_calculado:.2f}")



#--------------------------------------------------------------------------#-----------------------------------------------------------



# EJERCICIO 9: CONVERSION_TEMPERATURAS


# 1. Definición de la función de conversión
def celsius_a_fahrenheit(celsius):
  
  # Recibe una temperatura en Celsius y la convierte a Fahrenheit.
  # FOrmula: F = (C * 9/5) + 32
  
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Programa Principal 

# Solicitar la temperatura al usuario
grados_celsius = float(input("Ingresa la temperatura en grados Celsius (°C): "))

# Llamar a la función para hacer la conversión
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)

# Mostrar el resultado de la conversión
print(f"{grados_celsius}°C equivale a {grados_fahrenheit:.1f}°F.")


#----------------------------------------------------------------#----------------------------------------------------------------------


# EJERCICIO 10: CALCULAR_PROMEDIO


# 1. Definicion de la función para calcular el promedio
def calcular_promedio(a, b, c):
  
  # Recibe tres números y devuelve su promedio.
  # Formula: Promedio = (a + b + c) / 3
  
  suma = a + b + c
  promedio = suma / 3
  return promedio

# Programa Principal 

print("Calculadora de Promedio de Tres Números")

# Solicitar los tres números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Llamar a la funcion con los numeros ingresados
resultado_promedio = calcular_promedio(num1, num2, num3)

# Mostrar el resultado final formateado a dos decimales
print(f"\nEl promedio de los números ingresados es: {resultado_promedio:.2f}")