#listas 
#EJERCICIO 1:
#notas_estudiantes.py

# Crear una lista con las notas de 10 estudiantes.
notas = [7, 8, 4, 10, 6, 9, 7, 8, 5, 9]

# Mostrar la lista completa.
print("--- Notas de los estudiantes ---")
for nota in notas:
    print(nota, end=" ") # end=" " para mostrarlas en una línea
print("\n") # Salto de línea para separar las secciones

# Calcular y mostrar el promedio.
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio}")

# Indicar la nota más alta y la más baja.
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print(f"La nota más alta fue: {nota_mas_alta}")
print(f"La nota más baja fue: {nota_mas_baja}")


#-------------------------------------------------------#-------------------------------------------------


#EJERCICO: 2 
#producto_supermercado.py

# Pedir al usuario que cargue 5 productos en una lista.
productos = []
print("--- Carga de Productos ---")
for i in range(5):
    producto = input(f"Ingrese el producto N°{i + 1}: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente.
# sorted() devuelve una nueva lista ordenada sin modificar la original.
print("\n--- Lista de productos ordenada ---")
for producto in sorted(productos):
    print(producto)

# Preguntar al usuario qué producto desea eliminar y actualizar la lista.
producto_a_eliminar = input("\n¿Qué producto desea eliminar de la lista?: ")

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"'{producto_a_eliminar}' ha sido eliminado.")
else:
    print(f"El producto '{producto_a_eliminar}' no se encuentra en la lista.")

# Mostramos la lista final
print("\n--- Lista de productos actualizada ---")
for producto in productos:
    print(producto)


#------------------------------------------------------------#----------------------------------------------------------------

#EJERCICIO: 3

#numeros_azar.py

import random

# Generar una lista con 15 números enteros al azar entre 1 y 100.
numeros_azar = []
for _ in range(15):
    numeros_azar.append(random.randint(1, 100))

print("--- Lista de números generados ---")
for numero in numeros_azar:
    print(numero, end=" ")
print("\n")

# Crear una lista con los pares y otra con los impares.
pares = []
impares = []

for numero in numeros_azar:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrar cuántos números tiene cada lista.
print(f"Se encontraron {len(pares)} números pares.")
print(f"Se encontraron {len(impares)} números impares.")

#-------------------------------------------------------#-------------------------------------------------------------------

#EJERCICIO: 4
#valores_repetidos.py

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

print("--- Lista original ---")
for dato in datos:
    print(dato, end=" ")
print("\n")

# Crear una nueva lista sin elementos repetidos.
for numero in datos:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)

# Mostrar el resultado.
print("--- Lista sin elementos repetidos ---")
for numero in sin_repetidos:
    print(numero, end=" ")
print("\n")

#----------------------------------------------------------#--------------------------------------------------

#EJERCICIO: 5 

#lista_asistencia_clase.py

presentes = ["Ana", "Luis", "Maria", "Juan", "Elena", "Pedro", "Sofia", "Carlos"]

print("--- Lista de asistencia inicial ---")
for estudiante in presentes:
    print(estudiante)

#  Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
accion = input("\n¿Desea 'agregar' un estudiante o 'eliminar' uno existente?: ").lower()

if accion == "agregar":
    nuevo_nombre = input("Ingrese el nombre del nuevo estudiante: ")
    presentes.append(nuevo_nombre)
    print(f"¡{nuevo_nombre} ha sido agregado a la lista!")
elif accion == "eliminar":
    nombre_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre_a_eliminar in presentes:
        presentes.remove(nombre_a_eliminar)
        print(f"¡{nombre_a_eliminar} ha sido eliminado de la lista!")
    else:
        print("Ese estudiante no se encuentra en la lista.")
else:
    print("Acción no reconocida.")

# Mostrar la lista final actualizada.
print("\n--- Lista de asistencia final ---")
for estudiante in presentes:
    print(estudiante)


#---------------------------------------------------#--------------------------------------------------------

#EJERCICIO: 6
#rotar_elementos_lista.py

# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha.
numeros = [10, 20, 30, 40, 50, 60, 70]

print("--- Lista Original ---")
for n in numeros:
    print(n, end=" ")
print("\n")

# El método pop() sin argumento elimina y devuelve el último elemento.
ultimo_elemento = numeros.pop()
# El método insert(índice, elemento) agrega un elemento en una posición específica.
numeros.insert(0, ultimo_elemento)

print("--- Lista Rotada a la Derecha ---")
for n in numeros:
    print(n, end=" ")
print("\n")

#--------------------------------------------------#-------------------------------------------------------

#EJERCICIO: 7

#lista_temperatura.py

# matriz (lista anidadada) de 7x2 (días x [min, max]).
semana = [
    [10, 19], # Día 1 (Lunes)
    [14, 24], # Día 2
    [15, 25], # Día 3
    [11, 21], # Día 4
    [10, 20], # Día 5
    [13, 26], # Día 6
    [15, 25]  # Día 7 (Domingo)
]

# Calcular el promedio de las mínimas y el de las máximas.
suma_minimas = 0
suma_maximas = 0
for dia in semana:
    suma_minimas += dia[0] # El índice 0 es la mínima
    suma_maximas += dia[1] # El índice 1 es la máxima

promedio_minimas = suma_minimas / len(semana)
promedio_maximas = suma_maximas / len(semana)

print(f"Promedio de temperaturas mínimas: {promedio_minimas:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}°C")

# Mostrar en qué día se registró la mayor amplitud térmica.
mayor_amplitud = -1
dia_mayor_amplitud = -1

for i, dia in enumerate(semana):
    amplitud = dia[1] - dia[0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1

print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C y se registró en el día {dia_mayor_amplitud}.")

#-------------------------------------------------#-------------------------------------------------------------

#EJERCICIO: 8
#notas_materias.py

# Matriz con notas de 5 estudiantes en 3 materias.
# Filas: Estudiantes, Columnas: Materias (Matemática, Lengua, Historia)
notas_curso = [
    [8, 7, 9],  # Estudiante 1
    [5, 6, 7],  # Estudiante 2
    [10, 9, 9], # Estudiante 3
    [7, 7, 8],  # Estudiante 4
    [6, 8, 7]   # Estudiante 5
]

#  Mostrar el promedio de cada estudiante.
print("--- Promedio por Estudiante ---")
for i, notas_estudiante in enumerate(notas_curso):
    promedio = sum(notas_estudiante) / len(notas_estudiante)
    print(f"Estudiante {i + 1}: Promedio {promedio:.2f}")

# Mostrar el promedio de cada materia.
print("\n--- Promedio por Materia ---")
num_materias = len(notas_curso[0])
for j in range(num_materias): # j es el índice de la materia (columna)
    suma_materia = 0
    for notas_estudiante in notas_curso: # Recorremos cada fila
        suma_materia += notas_estudiante[j]
    
    promedio_materia = suma_materia / len(notas_curso)
    print(f"Materia {j + 1}: Promedio {promedio_materia:.2f}")

    #----------------------------------------------------------------#-----------------------------------------------------

    #EJERCICIO: 9

    #ta_te_ti.py

    # tablero de Ta-Te-Ti como lista de listas (3x3).

#  Inicializarlo con guiones "-" representando casillas vacías.
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero(tablero_actual):
    print("\n--- TA-TE-TI ---")
    for fila in tablero_actual:
        for casilla in fila:
            print(casilla, end=" ")
        print() # Salto de línea al final de cada fila

# Permitir que dos jugadores ingresen posiciones.
# (Simularemos 4 turnos para el ejemplo)
turno = "X"
for i in range(4):
    mostrar_tablero(tablero)
    print(f"\nTurno del jugador '{turno}'")
    
    # Pedimos al usuario que ingrese la posición (usamos 1,2,3 para facilidad)
    fila = int(input("Elige una fila (1, 2, 3): ")) - 1
    columna = int(input("Elige una columna (1, 2, 3): ")) - 1
    
    # Validamos y actualizamos el tablero
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = turno
        # Cambiamos al otro jugador
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
    else:
        print("¡Esa casilla ya está ocupada! Turno perdido.")

# Mostrar el tablero después de cada jugada (se hace dentro del bucle).
print("\n--- Tablero Final ---")
mostrar_tablero(tablero)

#----------------------------------------------#----------------------------------------------------

#EJERCICIO: 10
#ventas_tienda.py
# Matriz de 4x7 con ventas de 4 productos durante 7 días.
# Filas: Productos, Columnas: Días de la semana
ventas = [
#   L   M   X   J   V   S   D
    [10, 12, 15, 11, 20, 18, 22], # Producto 1
    [8,  9,  10, 13, 15, 14, 16], # Producto 2
    [25, 30, 28, 33, 29, 35, 40], # Producto 3
    [5,  7,  6,  8,  5,  9,  10]  # Producto 4
]

#  Mostrar el total vendido por cada producto.
print("--- Total de Ventas por Producto ---")
total_por_producto = []
for i, ventas_producto in enumerate(ventas):
    total = sum(ventas_producto)
    total_por_producto.append(total)
    print(f"Producto {i + 1}: {total} unidades vendidas.")

#  Mostrar el día con mayores ventas totales.
print("\n--- Análisis de Ventas por Día ---")
total_por_dia = [0] * 7 # [0, 0, 0, 0, 0, 0, 0] para sumar las ventas de cada día
for ventas_producto in ventas:
    for dia_idx, venta_dia in enumerate(ventas_producto):
        total_por_dia[dia_idx] += venta_dia

max_ventas_dia = max(total_por_dia)
dia_con_max_ventas = total_por_dia.index(max_ventas_dia) + 1
print(f"El día con mayores ventas fue el día {dia_con_max_ventas} con {max_ventas_dia} unidades vendidas.")

#  Indicar cuál fue el producto más vendido en la semana.
producto_mas_vendido_total = max(total_por_producto)
producto_mas_vendido_idx = total_por_producto.index(producto_mas_vendido_total) + 1
print(f"\nEl producto más vendido de la semana fue el Producto {producto_mas_vendido_idx}.")
